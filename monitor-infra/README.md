# Monitor Infra

Projeto de monitoramento de hosts desenvolvido em Python.

O programa lê uma lista de hosts a partir de um arquivo de configuração, realiza testes de conectividade utilizando `ping`, registra os eventos em logs, mede o tempo de resposta, salva os resultados em JSON e envia um alerta para o Discord quando um host está inacessível.

## Funcionalidades

- Monitoramento de múltiplos hosts
- Configuração dos hosts através de arquivo JSON
- Teste de conectividade utilizando `ping`
- Registro de eventos através de logging
- Medição do tempo de resposta
- Registro de data e hora dos testes
- Salvamento dos resultados em formato JSON
- Geração de relatório no terminal
- Alertas via Discord Webhook quando um host fica offline

## Tecnologias utilizadas

- Python 3
- `subprocess`
- `json`
- `logging`
- `pathlib`
- `datetime`
- `requests`
- Discord Webhook
- Git e GitHub

## Estrutura do projeto

```text
monitor-infra/
│
├── monitor.py
├── config.json
├── requirements.txt
├── README.md
│
├── logs/
│   └── monitor.log
│
└── resultados/
    └── resultado.json

## Requisitos

Para executar o projeto, é necessário ter:

### Software

- **Python 3.10 ou superior**
- **pip** para instalação das dependências
- **Git** (opcional, caso o projeto seja clonado do GitHub)
- **Discord** (opcional, apenas para receber os alertas)

### Sistema operacional

O projeto foi desenvolvido e testado no **Windows**, utilizando o comando `ping` do sistema operacional.

> Atualmente, o código utiliza `ping -n`, que é a sintaxe utilizada pelo Windows. Para executar o projeto no Linux, seria necessário adaptar o comando para `ping -c`.

### Dependências Python

O projeto utiliza a biblioteca externa:

- `requests`

As demais bibliotecas utilizadas são nativas do Python:

- `json`
- `subprocess`
- `logging`
- `pathlib`
- `time`
- `datetime`

A dependência externa pode ser instalada através do arquivo `requirements.txt`:

```powershell
pip install -r requirements.txt