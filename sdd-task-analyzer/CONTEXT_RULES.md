# CONTEXT RULES - Governança e Regras de IA

## Diretrizes Arquiteturais (Obrigatórias)
1. Compatibilidade estrita com Python 3.11+.
2. Uso integral de type hints em argumentos e retornos de classes/funções.
3. Aderência irrestrita às convenções PEP 8 e princípio da responsabilidade única (SRP).
4. Documentação via Google Style Docstrings em todos os módulos, classes e funções.
5. Rastreabilidade via biblioteca padrão `logging` estruturada (níveis INFO/WARNING/ERROR).
6. Exceções customizadas herdadas de `Exception` para cada caso de falha de validação.

## Proibições Explícitas (Regras Restritivas)
1. Não adicionar bibliotecas externas fora do `requirements.txt` básico (pytest).
2. Proibida a persistência de dados em arquivos locais (JSON, TXT, SQLite) ou bancos de dados externos.
3. Proibido alterar contratos de interface: nomes de métodos e parâmetros públicos são imutáveis.
4. Proibido alterar, comentar ou enfraquecer asserções dentro de `test_harness.py`.
5. Proibida a suposição de campos ou regras não documentadas na especificação SDD.