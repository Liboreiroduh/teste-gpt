# teste-gpt

Projeto de exemplo para experimentos com GPT. Agora inclui uma estrutura
inicial para um aplicativo de controle de painel de LED com banco de dados.

## Estrutura

- `calculadora.py` - funcoes utilitarias de calculo usadas em exemplos e testes.
- `ledpanel/` - modulo principal do painel de LED.
- `database/` - camada simples de persistencia utilizando SQLite.
- `cli.py` - ponto de entrada de linha de comando.
- `docs/TAREFAS.md` - documento com divisao de tarefas para evolucao do projeto.

## Execucao

Para executar comandos do painel de LED, instale as dependencias (apenas
biblioteca padrao) e execute:

```bash
python cli.py ligar
python cli.py mensagem --texto "Ola" 
```

Os testes podem ser executados com:

```bash
pytest -q
```
