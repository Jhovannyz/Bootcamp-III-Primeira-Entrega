"""Test Harness para validação determinística do TaskAnalyzer com pytest."""

import pytest
from src.task_analyzer import TaskAnalyzer, InvalidTaskDataError


def test_cenario_1_sucesso_metricas_corretas():
    """Valida cálculo preciso de métricas gerais e por prioridade (Cenário 1)."""
    tasks = [
        {
            "id": 1,
            "titulo": "Tarefa 1",
            "prioridade": "alta",
            "data_criacao": "2026-09-01T08:00:00",
            "prazo_limite": "2026-09-02T18:00:00",
            "data_conclusao": "2026-09-02T12:00:00",
            "status": "concluida",
        },
        {
            "id": 2,
            "titulo": "Tarefa 2",
            "prioridade": "alta",
            "data_criacao": "2026-09-03T09:00:00",
            "prazo_limite": "2026-09-04T12:00:00",
            "data_conclusao": "2026-09-05T12:00:00",
            "status": "concluida",
        },
        {
            "id": 3,
            "titulo": "Tarefa 3",
            "prioridade": "media",
            "data_criacao": "2026-09-01T10:00:00",
            "prazo_limite": "2026-09-03T18:00:00",
            "data_conclusao": "2026-09-02T10:00:00",
            "status": "concluida",
        },
    ]

    resultado = TaskAnalyzer.analyze(tasks)

    assert resultado["total_geral"] == 3
    assert resultado["total_concluidas"] == 3
    assert resultado["taxa_atraso_percentual"] == 33.33
    assert resultado["tempo_medio_conclusao_horas"] == 34.33
    assert resultado["metricas_por_prioridade"]["alta"]["taxa_atraso_percentual"] == 50.0
    assert resultado["metricas_por_prioridade"]["alta"]["tempo_medio_conclusao_horas"] == 39.5


def test_cenario_2_excecao_datas_inconsistentes():
    """Valida disparo de InvalidTaskDataError ao identificar datas inconsistentes (Cenário 2)."""
    tasks = [
        {
            "id": 99,
            "titulo": "Tarefa Corrompida",
            "prioridade": "alta",
            "data_criacao": "2026-09-05T10:00:00",
            "prazo_limite": "2026-09-06T10:00:00",
            "data_conclusao": "2026-09-01T10:00:00",  # Conclusão anterior à criação
            "status": "concluida",
        }
    ]

    with pytest.raises(InvalidTaskDataError):
        TaskAnalyzer.analyze(tasks)


def test_cenario_3_casos_de_borda_sem_concluidas():
    """Valida prevenção de divisão por zero quando não há tarefas concluídas."""
    tasks = [
        {
            "id": 10,
            "titulo": "Tarefa Pendente 1",
            "prioridade": "baixa",
            "data_criacao": "2026-09-01T10:00:00",
            "prazo_limite": "2026-09-10T10:00:00",
            "data_conclusao": None,
            "status": "pendente",
        }
    ]

    resultado = TaskAnalyzer.analyze(tasks)

    assert resultado["total_geral"] == 1
    assert resultado["total_concluidas"] == 0
    assert resultado["total_pendentes"] == 1
    assert resultado["tempo_medio_conclusao_horas"] == 0.0
    assert resultado["taxa_atraso_percentual"] == 0.0
    assert resultado["metricas_por_prioridade"]["baixa"]["tempo_medio_conclusao_horas"] == 0.0