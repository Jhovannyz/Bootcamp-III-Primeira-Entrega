# SDD TaskAnalyzer

Módulo avançado de métricas e produtividade desenvolvido com **Spec-Driven Development (SDD)**, governança de IA e Test Harness automatizado para a disciplina de **Bootcamp III (UniCEUB)**.

---

## 🛠️ Tecnologias

- **Python 3.11+**
- **Pytest** (Test Harness)
- **Git / GitHub** (Git Flow)

---

## Estrutura do Repositório

sdd-task-analyzer/
├── README.md                  # Documentação do projeto
├── CONTEXT_RULES.md           # Regras de governança para a IA
├── requirements.txt           # Dependências (pytest)
├── .gitignore                 # Ficheiros ignorados
├── specs/
│   └── task_analyzer_spec.md  # Especificação técnica SDD
├── tests/
│   └── test_harness.py        # Suíte de testes (pytest)
└── src/
    ├── __init__.py
    └── task_analyzer.py       # Código-fonte principal

---

## Como Executar

1. Instalar as dependências:
   pip install -r requirements.txt

2. Executar o Test Harness (Pytest):
   pytest -v

---

## Contrato de Interface (Resumo)

- **Método Principal:** TaskAnalyzer.analyze(tasks: list[dict]) -> dict
- **Regras de Negócio:**
  - Métricas calculadas apenas para tarefas com status == "concluida".
  - Retorna 0.0 para médias/taxas se não houver tarefas concluídas (previne divisão por zero).
  - Lança a exceção InvalidTaskDataError caso data_conclusao < data_criacao.

---

## Autor

- **Nome:** Giovani Silva Rodrigues
- **Curso:** Análise e Desenvolvimento de Sistemas — UniCEUB
- **E-mail:** giovani.rodrigues@sempreceub.br