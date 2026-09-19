# 🚚 GlobalMove Logística — Sistema de Gestão de Frotas & Distribuição de Cargas

> Plataforma corporativa para controle de frotas, alocação inteligente de cargas, travas de segurança contra sobrecarga e estimativa automatizada de custos operacionais.

---

## 📌 Sobre o Projeto

A **GlobalMove Logística** opera diariamente com múltiplos tipos de veículos (furgões, caminhões leves e carretas) para o transporte de mercadorias. Para eliminar gargalos operacionais como sobrecarga de eixos, alocação duplicada de veículos e falta de previsibilidade nos custos de combustível, este sistema foi projetado para centralizar e automatizar a tomada de decisão da equipe de pátio.

O projeto foi arquitetado em etapas:
1. **Fase 1 (Atual):** Núcleo de regras de negócio em Python (CLI), utilizando dicionários e validações estritas para cadastros, travas operacionais e cálculos de rota.
2. **Fase 2 (Em Desenvolvimento):** Persistência de dados e API RESTful.
3. **Fase 3 (Planejada):** Dashboard Web interativo (HTML5/CSS3/JS) com identidade visual própria e visualização em tempo real para a diretoria.

---

## 🎯 Funcionalidades e Regras de Negócio

* **Gestão Cadastral da Frota:**
  * Mapeamento único por **Placa** do veículo.
  * Suporte a categorias operacionais: *Furgão*, *Caminhão Leve* e *Carreta*.
  * Monitoramento de estado em tempo real: `Disponível`, `Em Rota` ou `Manutenção`.

* **Trava Operacional Antierro (Alocação Inteligente):**
  * **Validação de Capacidade:** Impede o carregamento de peso excedentário à capacidade máxima em kg do veículo.
  * **Validação de Disponibilidade:** Bloqueia a alocação de veículos ocupados ou sob manutenção.

* **Calculadora Financeira de Viagem:**
  * Estimativa automatizada de combustível cruzando a distância ($\text{km}$), o consumo médio ($\text{km/l}$) do veículo e o preço do combustível no dia.

---

## 📁 Estrutura do Repositório

A arquitetura do projeto adota o padrão **Modular em Camadas**, garantindo fácil manutenção e escalabilidade sem necessidade de refatorar regras de negócio ao integrar novas tecnologias:

```text
globalmove-logistica/
│
├── README.md               # Documentação executiva do sistema
├── .gitignore              # Configuração de arquivos ignorados pelo Git
├── requirements.txt         # Dependências e bibliotecas do projeto
│
├── docs/                    # Ativos de Marca e Documentação de Design
│   ├── branding/            # Identidade visual (Logótipos, Paleta de Cores, Tipografia)
│   │   ├── logo.svg
│   │   └── color_palette.png
│   └── architecture/        # Diagramas de fluxo e arquitetura de software
│       └── fluxo_operacional.png
│
├── frontend/                # Interface Web (HTML5 / CSS3 / JavaScript)
│   ├── index.html           # Painel de Controle / Dashboard operacional
│   ├── css/
│   │   ├── style.css        # Estilos gerais e componentes responsivos
│   │   └── variables.css    # Guia de estilo (Design Tokens e Cores da Marca)
│   ├── js/
│   │   ├── main.js          # Manipulação do DOM e eventos do usuário
│   │   └── api.js           # Integração assíncrona com o backend
│   └── assets/              # Mídias e ícones da aplicação
│
├── tests/                   # Suíte de Testes Automatizados
│   └── test_alocacao.py    # Testes unitários para validação de peso e custos
│
└── src/                     # Backend & Regras de Negócio em Python
    ├── __init__.py
    ├── main.py              # Ponto de entrada (Interface via Terminal / CLI)
    ├── core/                # Módulos de Regras de Negócio Puras
    │   ├── __init__.py
    │   ├── frota.py          # Gerenciamento do dicionário de veículos
    │   ├── validacoes.py     # Travas operacionais de peso e disponibilidade
    │   └── calculos.py       # Funções matemáticas de custo e consumo
    ├── database/            # Camada de Persistência (JSON / SQL)
    │   └── __init__.py
    └── api/                 # Camada de Exposição para API Web (FastAPI)
        └── __init__.py
````
