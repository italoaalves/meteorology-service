# Serviço de previsão do tempo
Este sistema captura informações do weather.com e envia boletins diários sobre os dias seguintes em que a temperatura e possibilidade de chuva atingem certos limites.

## Configuração
Configure seu ambiente .env na raiz do repositório, através da amostra disponível.
```bash
cp .env-sample .env
```
### Variaveis disponíveis
Modifique os valores de acordo com a sua necessidade.
#### Filtros
- `MIN_TEMP` a temperatura mínima
- `MAX_TEMP` a temperatura máxima
- `PRECIPITATION` a porcentagem de possibilidade de chuva desejada

#### Agendamento das tarefas
- `WEEK_INTERVAL` intervalo de dias da semana (ex.: mon-fri)
- `HOUR` hora do dia em que o job será executado (ex.: 14)
- `MINUTE` minutos da hora em que será executado (ex.: 16)
- `TIMEZONE` fuso horário para calibrar o scheduler (ex.: America/Fortaleza)
- `DB_UPDATE_INTERVAL` a cada quantas horas o scrapper irá rodar para atualizar o BD

#### Mailer
- `SENDER_EMAIL` endereço de email configurado para smtp
- `RECEIVER_EMAIL` destinatário
- `SMTP_PASSWORD` senha de app disponibilizada pelo provedor de email do `SENDER_EMAIL`

## Como executar
Tenha em sua máquina `Docker` e `Docker Compose`.

Clone este repositório:
```bash
git clone https://github.com/italoaalves/meteorology-service
```
Suba o cluster:
```bash
docker-compose up -d --build
```
Pronto, seu serviço já está rodando.
