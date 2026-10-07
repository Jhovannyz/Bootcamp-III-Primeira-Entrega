<h1 align="center">SDD TaskAnalyzer</h1>

Módulo avançado de métricas e produtividade desenvolvido com **Spec-Driven Development (SDD)**, governança de IA e Test Harness automatizado para a disciplina de **Bootcamp III (UniCEUB)**.

---

## Sobre o Projeto

O **TaskAnalyzer** é um motor determinístico em Python desenvolvido para analisar coleções de tarefas operacionais, calcular tempos médios de conclusão, computar taxas de atraso e segmentar indicadores por prioridade (`baixa`, `media`, `alta`).

Sua arquitetura segue o paradigma **Spec-Driven Development (SDD)**, utilizando o contrato executável em `specs/task_analyzer_spec.md` e as regras em `CONTEXT_RULES.md`[cite: 23].

>  **Contrato Principal:** `TaskAnalyzer.analyze(tasks: list[dict]) -> dict`  
> - **Filtro Estrito:** Processa apenas tarefas concluídas (`status == "concluida"`).
> - **Resiliência:** Retorna `0.0` em coleções sem conclusões (evita divisão por zero).
> - **Validação:** Lança `InvalidTaskDataError` caso `data_conclusao < data_criacao`.

---

## Tecnologias

- **Python 3.11+**
- **Pytest** (Test Harness)
- **Git / GitHub** (Git Flow)

---

## Estrutura do Repositório

```text
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
```

---

## Como Executar

1. **Instalar as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Executar o Test Harness (Pytest):**
   ```bash
   py -m pytest -v
   ```

---

## Autor

- **Nome:** Giovani Silva Rodrigues
- **Curso:** Análise e Desenvolvimento de Sistemas — UniCEUB
- **E-mail:** giovani.rodrigues@sempreceub.br
