# 🎬 Catálogo de Filmes e Séries

Sistema desenvolvido em **Python** para gerenciamento de um catálogo de filmes e séries, permitindo ao usuário cadastrar mídias, criar listas personalizadas, avaliar conteúdos e gerar relatórios de consumo.  
Projeto baseado no **Tema 10 — Catálogo de Filmes e Séries**, da disciplina de **Programação Orientada a Objetos (UFCA)**.

---

## 🧱 Estrutura do Sistema

O sistema é orientado a objetos e estruturado com base no **diagrama UML** a seguir, que representa as classes principais e seus relacionamentos de herança, agregação e composição:

<img width="1294" height="935" alt="image" src="https://github.com/user-attachments/assets/8f086bac-ab81-4661-81a5-025923b4bc7e" />

### 🧩 Descrição das Classes

- **Midia** → Classe base para `Filme` e `Serie`.  
  Contém informações comuns como título, gênero, ano, duração, elenco, classificação indicativa, status e notas.
- **Filme** → Herda de `Midia`, representando um filme individual.
- **Serie** → Herda de `Midia`, agregando várias `Temporada` e calculando automaticamente sua nota média.
- **Temporada** → Representa uma temporada de uma série, composta por vários episódios.
- **Episodio** → Contém número, título, duração, data de lançamento, status e nota opcional.
- **Usuario** → Armazena dados do usuário, suas listas personalizadas e histórico de mídias assistidas.
- **ListaPersonalizada** → Coleção de mídias criada pelo usuário (ex: “Favoritos”, “Assistir depois”).
- **Historico** → Registra as mídias assistidas, progresso, notas e gera relatórios estatísticos.
- **Configuracao** → Gerencia parâmetros globais do sistema definidos em `settings.json`.


---

## ⚙️ Funcionalidades Principais

- Cadastro e gerenciamento de filmes e séries (CRUD completo).  
- Criação de listas personalizadas de mídias.  
- Registro de progresso e notas de visualização.  
- Cálculo automático de notas médias para séries e temporadas.  
- Relatórios estatísticos:
  - Média de notas por gênero;
  - Tempo total assistido por tipo;
  - Top 10 mídias assistidas;
  - Série mais assistida.

---

## 🧩 Tecnologias Utilizadas

- **Linguagem:** Python 3.12+
- **Paradigma:** Programação Orientada a Objetos (POO)
- **Bibliotecas padrão:**
  - `json` → persistência de dados e configurações  
  - `datetime` → manipulação de datas  
  - `enum` → definição de status e tipos  
  - `typing` → uso de listas e tipagem genérica  
- **Formato de persistência:** arquivos `.json` (ex: `midias.json`, `usuarios.json`, `settings.json`)

---

## 🧠 Organização do Projeto
A estrutura de diretórios do projeto segue o padrão modular da Programação Orientada a Objetos, facilitando a manutenção e o reuso de código.

catalogo-de-filmes-e-series/
│
├── main.py # Arquivo principal para execução do sistema
│
├── models/ # Pacote contendo as classes do sistema
│ ├── midia.py
│ ├── filme.py
│ ├── serie.py
│ ├── temporada.py
│ ├── episodio.py
│ ├── usuario.py
│ ├── lista_personalizada.py
│ ├── historico.py
│ └── configuracao.py
│
├── data/ # Armazena arquivos de dados e configurações
│ ├── midias.json
│ ├── usuarios.json
│ └── settings.json
│
├── docs/ # Documentação do projeto
│ └── uml_catalogo_midias.png
│
└── README.md # Documentação geral do projeto

