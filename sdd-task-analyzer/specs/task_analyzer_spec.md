# Especificação Técnica SDD - TaskAnalyzer

## 1. Propósito
O módulo `TaskAnalyzer` é uma biblioteca para analisar métricas de produtividade em coleções de tarefas, calculando tempo médio de conclusão, taxa de atraso e agrupamentos por prioridade.

## 2. Contrato de Interface
- **Método:** `TaskAnalyzer.analyze(tasks: list[dict]) -> dict`
- **Exceção de Validação:** `InvalidTaskDataError`

## 3. Campos de Entrada (por tarefa)
- `id`: str | int (Obrigatório)
- `titulo`: str (Obrigatório)
- `prioridade`: "baixa" | "media" | "alta" (Obrigatório)
- `data_criacao`: datetime | str ISO-8601 (Obrigatório)
- `prazo_limite`: datetime | str ISO-8601 (Obrigatório)
- `data_conclusao`: datetime | str ISO-8601 | None (Opcional, obrigatório se status == "concluida")
- `status`: "pendente" | "concluida" (Obrigatório)

## 4. Regras de Negócio
- Apenas tarefas com `status == "concluida"` entram nos cálculos de tempo e atraso.
- Se não houver tarefas concluídas, as médias e taxas retornam `0.0` (sem divisão por zero).
- Se `data_conclusao < data_criacao`, o sistema dispara `InvalidTaskDataError`.