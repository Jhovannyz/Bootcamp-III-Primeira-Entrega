"""Módulo de análise estatística e métricas de produtividade do TaskAnalyzer."""

from datetime import datetime
import logging
from typing import Any, Dict, List, Optional

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class InvalidTaskDataError(Exception):
    """Exceção disparada quando os dados de uma tarefa são inconsistentes ou inválidos."""
    pass


class TaskAnalyzer:
    """Analisador determinístico de produtividade e métricas de tarefas."""

    @staticmethod
    def _parse_datetime(dt_val: Any) -> Optional[datetime]:
        """Converte strings ISO-8601 ou objetos datetime para datetime."""
        if dt_val is None:
            return None
        if isinstance(dt_val, datetime):
            return dt_val
        if isinstance(dt_val, str):
            try:
                return datetime.fromisoformat(dt_val)
            except ValueError as exc:
                raise InvalidTaskDataError(f"Formato de data inválido: {dt_val}") from exc
        raise InvalidTaskDataError(f"Tipo de data não suportado: {type(dt_val)}")

    @classmethod
    def analyze(cls, tasks: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Processa uma coleção de tarefas e calcula métricas de produtividade.

        Args:
            tasks: Lista de dicionários representando as tarefas.

        Returns:
            Dicionário com métricas agregadas gerais e por prioridade.

        Raises:
            InvalidTaskDataError: Se alguma tarefa contiver inconsistência temporal ou campos inválidos.
        """
        logging.info("Iniciando análise de %d tarefas.", len(tasks))

        total_geral = len(tasks)
        concluidas = []
        pendentes_count = 0

        prioridades_validas = {"baixa", "media", "alta"}
        prioridade_stats = {
            p: {"total": 0, "concluidas": 0, "tempo_total_horas": 0.0, "atrasadas": 0}
            for p in prioridades_validas
        }

        for task in tasks:
            prioridade = task.get("prioridade")
            if prioridade not in prioridades_validas:
                raise InvalidTaskDataError(f"Prioridade inválida '{prioridade}'. Deve ser baixa, media ou alta.")

            status = task.get("status")
            if status not in {"pendente", "concluida"}:
                raise InvalidTaskDataError(f"Status inválido '{status}'. Deve ser pendente ou concluida.")

            prioridade_stats[prioridade]["total"] += 1

            if status == "pendente":
                pendentes_count += 1
                continue

            # Processa tarefa concluída
            dt_criacao = cls._parse_datetime(task.get("data_criacao"))
            dt_prazo = cls._parse_datetime(task.get("prazo_limite"))
            dt_conclusao = cls._parse_datetime(task.get("data_conclusao"))

            if not dt_criacao or not dt_prazo or not dt_conclusao:
                raise InvalidTaskDataError("Tarefas concluídas devem possuir data_criacao, prazo_limite e data_conclusao.")

            if dt_conclusao < dt_criacao:
                raise InvalidTaskDataError(
                    f"Inconsistência temporal na tarefa '{task.get('id')}': "
                    f"data_conclusao ({dt_conclusao}) é anterior à data_criacao ({dt_criacao})."
                )

            # Cálculo de duração em horas
            duracao_horas = (dt_conclusao - dt_criacao).total_seconds() / 3600.0
            em_atraso = dt_conclusao > dt_prazo

            concluidas.append({"duracao_horas": duracao_horas, "atrasada": em_atraso})

            stats_p = prioridade_stats[prioridade]
            stats_p["concluidas"] += 1
            stats_p["tempo_total_horas"] += duracao_horas
            if em_atraso:
                stats_p["atrasadas"] += 1

        total_concluidas = len(concluidas)

        # Prevenção de divisão por zero nas métricas gerais
        if total_concluidas > 0:
            tempo_medio_geral = round(sum(t["duracao_horas"] for t in concluidas) / total_concluidas, 2)
            atrasadas_total = sum(1 for t in concluidas if t["atrasada"])
            taxa_atraso_geral = round((atrasadas_total / total_concluidas) * 100.0, 2)
        else:
            tempo_medio_geral = 0.0
            taxa_atraso_geral = 0.0

        # Monta métricas por prioridade
        metricas_por_prioridade = {}
        for p, data in prioridade_stats.items():
            qtd_conc = data["concluidas"]
            if qtd_conc > 0:
                t_medio = round(data["tempo_total_horas"] / qtd_conc, 2)
                t_atraso = round((data["atrasadas"] / qtd_conc) * 100.0, 2)
            else:
                t_medio = 0.0
                t_atraso = 0.0

            metricas_por_prioridade[p] = {
                "total": data["total"],
                "concluidas": qtd_conc,
                "tempo_medio_conclusao_horas": t_medio,
                "taxa_atraso_percentual": t_atraso,
            }

        logging.info("Análise concluída com sucesso.")

        return {
            "total_geral": total_geral,
            "total_concluidas": total_concluidas,
            "total_pendentes": pendentes_count,
            "tempo_medio_conclusao_horas": tempo_medio_geral,
            "taxa_atraso_percentual": taxa_atraso_geral,
            "metricas_por_prioridade": metricas_por_prioridade,
        }

# Homologação de código
