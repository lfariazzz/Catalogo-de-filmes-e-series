# 🔥🎬 ForgeFlix

> Sistema de gerenciamento de catálogo de filmes e séries com persistência de dados, perfis de usuário e relatórios estatísticos.

O **ForgeFlix** é uma aplicação em Python (CLI) desenvolvida como Trabalho da disciplina de **Programação Orientada a Objetos (POO)**. O sistema simula o backend de um serviço de streaming, permitindo o gerenciamento completo de mídias (incluindo controle detalhado de episódios de séries), criação de listas personalizadas e geração de relatórios de consumo.

---

## ⚙️ Funcionalidades

### 🎞️ Gestão de Catálogo (CRUD)
- **Filmes:** Cadastro completo com validação de gênero, ano e notas (0-10).
- **Séries:** Estrutura hierárquica robusta (`Série` → `Temporadas` → `Episódios`).
- **Polimorfismo:** O cálculo de duração e média de notas comporta-se de maneira diferente para Filmes (direto) e Séries (agregado dos episódios).

### 🧠 Regras de Negócio (Encapsulamento)
- **Status Automático:** O sistema impede inconsistências. Uma série só é marcada como "ASSISTIDO" se todos os seus episódios estiverem concluídos.
- **Proteção de Dados:** Uso de *Properties* e *Setters* para garantir que não entrem dados inválidos (ex: notas negativas, strings vazias ou datas futuras).

### 👤 Perfil do Usuário
- **Listas Personalizadas:** Criação de listas temáticas (ex: "Maratona de Terror") com adição/remoção dinâmica de mídias do catálogo.
- **Histórico Inteligente:** Ao finalizar uma mídia, o sistema grava automaticamente a data, a nota atribuída e o status.
- **Configurações:** Singleton que carrega parâmetros globais (como limites do sistema) via `settings.json`.

### 📊 Relatórios (Business Intelligence)
O módulo de relatórios cruza dados do histórico e do catálogo para gerar:
1.  **Tempo de Tela:** Total de horas/minutos assistidos em um período.
2.  **Preferência de Formato:** Gráfico comparativo entre Filmes vs. Séries.
3.  **Ranking:** Top 10 mídias melhor avaliadas e Top 3 séries mais maratonadas.

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

### 💾 Persistência de Dados
O sistema utiliza arquivos JSON para manter o estado entre execuções:

Relacionamentos: O sistema reconstrói as ligações entre objetos (ex: Histórico → Mídia) através de buscas por título durante o carregamento, garantindo integridade referencial na memória sem duplicar dados pesados nos arquivos de usuário.

### 👨‍💻 Autor
**Desenvolvido por Levi Farias 🎓 Engenharia de Software - Universidade Federal do Cariri (UFCA)**
