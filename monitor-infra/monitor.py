import json
import subprocess
import logging
from pathlib import Path
import time
from datetime import datetime
##import requests

url_webhook = ""

pasta_logs = Path("logs")
pasta_logs.mkdir(exist_ok=True)
arquivo_log = pasta_logs / "monitor.log"
logging.basicConfig(
    filename=arquivo_log,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

with open("config.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

hosts = dados["hosts"]
tentativas = dados["tentativas"]
online = 0
offline = 0
tempo_total = 0
resultados = []
for host in hosts:
    logging.info(f"Iniciando monitoramento do host{host}")
    inicio = time.time()
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    resultado =subprocess.run(
        ["ping","-n",str(tentativas), host],
        capture_output= True,
        text= True
    )
    fim = time.time()
    tempo = fim - inicio
    tempo_ms = tempo * 1000
    print(f"Tempo total: {tempo_ms:.2f} ms")
    if resultado.returncode == 0:
        online += 1
        tempo_total += round(tempo_ms,2)
        logging.info(f"Host {host} está acessível!")
        resultados.append({
            "host": host,
            "status": "online",
            "tempo_ms": round(tempo_ms,2),
            "data_hora": data_hora
        })
    else:
        offline += 1
        logging.info(f"Host {host} está inacessível!")
        resultados.append(
            {
                "host": host,
                "status": "offline",
                "data_hora": data_hora
            }
        )
        dados = {
            "content": f"🚨 ALERTA!\n\nHost: {host}\nStatus: OFFLINE\nData: {data_hora}"
        }
        ##requests.post(url_webhook, json=dados)

total = online + offline
disponibilidade = (online/total) * 100
tempo_medio = tempo_total / online
pasta_resultados = Path("resultados")
pasta_resultados.mkdir(exist_ok=True)
arquivo_resultado = pasta_resultados / "resultado.json"

with open(arquivo_resultado,"w", encoding="utf-8") as arquivo:
    json.dump(resultados, arquivo, indent=4, ensure_ascii=False)


print("\n========================================")
print("       RELATÓRIO DE MONITORAMENTO")
print("========================================")

print(f"\nHosts monitorados: {total}")
print(f"Hosts online:      {online}")
print(f"Hosts offline:     {offline}")
print(f"Disponibilidade:   {disponibilidade:.2f}%")
print(f"Tempo médio:       {tempo_medio:.2f} ms")

print("\n========================================")