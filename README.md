# BotDiscord - Jogo de Adivinhação de Campeão do League of Legends

Este projeto é um bot para Discord que permite aos usuários jogarem um divertido jogo de adivinhação de campeões do League of Legends. Os jogadores entram em uma partida e tentam adivinhar qual campeão está sendo pensado pelo bot.

## Funcionalidades

- Inicialização de partidas por servidor
- Participação de múltiplos jogadores
- Comandos interativos para jogar e receber dicas
- Registro de jogadores por servidor

## Comandos Principais

- `R!init` — Inicia uma nova partida no servidor
- `R!play` — Entra na partida atual
- `R!hello` — Mensagem de saudação

## Como rodar o projeto

1. **Clone o repositório**
2. **Instale as dependências com Poetry**
   ```sh
   poetry install
   ```
3. **Configure o arquivo `.env`**
   - Crie um arquivo em `resources/.env` com:
     ```
     DISCORD_TOKEN=seu_token_aqui
     ```
4. **Inicie o bot**
   ```sh
   poetry run python src/bot.py
   ```

## Estrutura do Projeto

```
BotDiscord/
├── src/
│   └── bot.py
├── models/
│   └── Game.py
├── resources/
│   └── .env
├── README.md
├── pyproject.toml
```

## Requisitos

- Python 3.12+
- [discord.py](https://discordpy.readthedocs.io/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
