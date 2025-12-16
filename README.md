# 🔥🎬 ForgeFlix

> Sistema de gerenciamento de catálogo de filmes e séries com persistência de dados, perfis de usuário e relatórios estatísticos.

O **ForgeFlix** é uma aplicação em Python (CLI) desenvolvida como Trabalho da disciplina de **Programação Orientada a Objetos (POO)**. O sistema simula o backend de um serviço de streaming, permitindo o gerenciamento completo de mídias (incluindo controle detalhado de episódios de séries), criação de listas personalizadas e geração de relatórios de consumo.

---

## ⚙️ Funcionalidades e Decisões de Implementação

### 🏛️ Arquitetura Orientada a Objetos
O sistema foi projetado para maximizar o reaproveitamento de código e representar fielmente as relações do mundo real:
- **Herança e Abstração:** A classe abstrata `Midia` define o contrato base (ID, Título, Ano). `Filme` e `Série` herdam dessa base, especializando comportamentos.
- **Composição Forte:** Em vez de listas simples, adotou-se uma estrutura de composição para Séries: `Série` contém objetos `Temporada`, que contêm objetos `Episódio`. Isso permite controle granular de status e notas por episódio individual.
- **Polimorfismo:** Métodos como o cálculo de duração e média de notas comportam-se de forma distinta: para filmes é um valor fixo/direto; para séries, é o resultado de uma iteração recursiva sobre seus episódios.

### 🛡️ Integridade e Encapsulamento (Regras de Negócio)
- **Validação via Setters:** Todos os dados de entrada passam por *Setters* rigorosos. O sistema rejeita ativamente estados inválidos (ex: notas fora do intervalo 0-10, anos negativos ou strings vazias), garantindo que apenas dados "limpos" cheguem à camada de persistência.
- **Máquina de Estados de Status:** O status de uma Série (*Não Assistido, Assistindo, Assistido*) não é arbitrário. Ele é calculado dinamicamente com base na proporção de episódios concluídos, impedindo inconsistências lógicas.

### 💾 Estratégia de Persistência e Otimização
- **Banco de Dados em JSON:** O sistema utiliza arquivos JSON para persistência, simulando um banco NoSQL documental.
- **Normalização de Dados:** Para evitar redundância e circularidade, o arquivo `usuarios.json` armazena apenas as **referências** (títulos) das mídias no histórico e nas listas, e não os objetos inteiros.
- **Reconstrução de Objetos (Linkagem):** Durante a inicialização (`boot`), o sistema realiza uma varredura para reconectar os históricos dos usuários aos objetos reais do catálogo carregados na memória, garantindo acesso imediato a propriedades atualizadas das mídias.

### 📊 Inteligência de Dados (Relatórios)
O módulo de relatórios utiliza manipulação de datas e algoritmos de ordenação para gerar *insights*:
1.  **Tempo de Tela (Time-Window):** Filtra o histórico com base em objetos `datetime`, permitindo saber exatamente quantos minutos foram consumidos em um intervalo de datas específico.
2.  **Ranking e Comparativos:** Utiliza ordenação de listas via métodos mágicos (`__lt__`) para gerar rankings de qualidade e preferência de formato (Filmes vs. Séries).
3.  **Singleton de Configuração:** As regras globais (como limites de listas) são geridas por uma classe Singleton, centralizando a parametrização do sistema.
---

## 🧱 Estrutura do Projeto

O código foi organizado seguindo os princípios de modularidade e responsabilidade única.

```text
catalogo-de-filmes-e-series/
│
├── main.py                    # Ponto de entrada (Entry Point)
├── dados.py                   # Camada de Persistência (JSON ETL)
│
├── classes/                   # Classes de Domínio e Lógica
│   ├── interface_CLI.py       # Controller/View (Menu Principal)
│   ├── midia.py               # Classe Abstrata Base
│   ├── filme.py               # Herança de Midia
│   ├── serie.py               # Herança de Midia (Lógica de Status)
│   ├── temporada.py           # Composição de Série
│   ├── episodio.py            # Agregação em Temporada
│   ├── usuario.py             # Gestão de usuário e listas
│   ├── lista_personalizada.py # Agregação de Mídias
│   ├── historico.py           # Motor de registros
│   ├── registro_visualizacao.py # DTO do histórico
│   ├── configuracao.py        # Gestão de settings
│   └── relatorios.py          # Lógica estatística
│
└── data/                      # Banco de Dados (Gerados automaticamente)
    ├── midias.json
    ├── usuarios.json
    └── settings.json
└── tests/                      # Testes parciais e oficais automatizado (Pytest)
    ├── test_midia.py
    ├── test_serie.py
    └── testes_oficiais.py
```
## 🏗️ Diagrama de Classes
```text
classDiagram
    class Midia {
        <<Abstract>>
        +id: int
        +titulo: str
        +ano: int
        +genero: str
        +status: str
        +notas: list
        +avaliar()
    }
    class Filme {
        +duracao_minutos: int
        +tempo_assistido: float
        +avaliar_filme()
    }
    class Serie {
        +temporadas: List
        +verificar_status_automatico()
    }
    class Temporada {
        +numero: int
        +episodios: List
        +nota_media: float
    }
    class Episodio {
        +numero: int
        +titulo: str
        +duracao: int
        +avaliar_episodio()
    }
    class Usuario {
        +nome: str
        +email: str
        +criar_lista()
    }
    class Historico {
        +registros: List
        +registrar_conclusao()
        +calcular_tempo_assistido()
    }
    class ListaPersonalizada {
        +nome: str
        +adicionar_midia()
        +remover_midia()
    }
    class Configuracao {
        +nota_recomendada: float
        +limite_listas: int
    }

    Midia <|-- Filme
    Midia <|-- Serie
    Serie *-- Temporada
    Temporada *-- Episodio
    Usuario *-- Historico
    Usuario o-- ListaPersonalizada
    ListaPersonalizada o-- Midia
    Historico --> Midia : Referencia
```
### 🚀 Como Executar
**Pré-requisitos**
Python 3.10 ou superior.

**Passo a Passo**
1. **Clone o repositório:**
- git clone https://github.com/lfariazzz/Catalogo-de-filmes-e-series
- cd ForgeFlix
2. **Execute o sistema:**
- python main.py
3. **Primeiro Acesso:**
- O sistema identificará a ausência de dados e criará um usuário Admin padrão.
- Os arquivos JSON serão criados automaticamente na pasta data/ na primeira execução.

### 💻 Exemplos de Uso
**1. Adicionando um Filme**
```text
O que deseja fazer? 2
------------------------------ Este é modo de adição ------------------------------
Digite o título da mídia: Matrix
Digite o ano da mídia: 1999
Deseja criar um (1) filme ou uma (2) série? 1
Digite o gênero da mídia: Ficção Científica
Digite a duração (em minutos): 136
Digite a classificação indicativa: 14
Deseja adicionar o elenco? (1) Sim (2) Não: 2
Mídia adicionada ao catálogo!
```
**2. Gerando Relatório de Tempo de Tela**
```text
O que deseja fazer? 6
========================================
      📊 RELATÓRIOS DO CATÁLOGO      
========================================
1 - ⏱️  CÁLCULO DE TEMPO DE TELA
...
Qual relatório deseja exibir? 1
----------------------------------------
   ⏱️  RELATÓRIO DE TEMPO DE TELA
----------------------------------------
Digite as datas no formato dia/mês/ano
Data Inicial: 01/01/2024
Data Final:   31/12/2024

✅ Resultados:
   Total assistido: 2500 minutos
   Equivalente a:   41h 40min
```

### 🧪 Roteiro de Testes Manuais
Como o projeto é baseado em CLI, recomenda-se seguir o seguinte fluxo para validar as funcionalidades principais:

**1. Teste de Cadastro:**
**- Adicione um filme com ano inválido (ex: 1800) -> O sistema deve barrar.
- Adicione uma série sem temporadas e verifique se ela aparece no catálogo.

**2. Teste de Avaliação:**
- Avalie uma mídia com nota 11 -> O sistema deve exibir erro.
- Avalie com nota 8.5 -> A média da mídia deve ser atualizada.

**3. Teste de Hierarquia (Séries):**
- Adicione uma Série -> Adicione Temporada 1 -> Adicione Episódio 1.
- Marque o Episódio 1 como "ASSISTIDO".
- Verifique se o status da Série mudou para "ASSISTINDO" ou "ASSISTIDO" (dependendo da quantidade de episódios).

**4. Teste de Persistência:**
- Cadastre dados, encerre o programa com a opção 0 e abra novamente.
- Verifique se os dados continuam lá.

### 🤖 Testes Automatizados (Pytest)
Foram implementados **20 testes unitários** cobrindo validações de setters, cálculo de médias e lógica de status de séries.

Para executar:
1. Instale o framework de testes:
   ```bash
   pip install pytest
2. Rode a bateria de testes:
    ```bash
   python -m pytest tests/test_forgeflix.py -v
### 👨‍💻 Autor
**Desenvolvido por Levi Farias 🎓 Engenharia de Software - Universidade Federal do Cariri (UFCA)**
