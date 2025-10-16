"""
Enunciado:
Desenvolva um sistema de monitoramento baseado em sensores.

O sistema deve:
- Ter classes de sensores:
  - SensorTemperatura: retorna valores aleatórios entre 20 °C e 30 °C.
  - SensorPressao: retorna valores aleatórios entre 950 hPa e 1050 hPa.
- Ter a classe SistemaMonitoramento que:
  - Armazena sensores (lista).
  - Permite adicionar novos sensores.
  - Gera um relatório textual (relatorio()) com as leituras e tipos de sensores.

O que será avaliado:
- Uso de composição (sistema contendo sensores).
- Geração dinâmica de relatórios.
- Aleatoriedade controlada (faixas coerentes).
"""
# TODO: implementar classes SensorTemperatura, SensorPressao e SistemaMonitoramento
import random
class Sensor:
    def ler(self):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")
class SensorTemperatura(Sensor):
    def __init__(self):
        self.tipo = "Temperatura"
    def ler(self):
        return round(random.uniform(20.0, 30.0), 2)
class SensorPressao(Sensor):
    def __init__(self):
        self.tipo = "Pressão"
    def ler(self):
        return round(random.uniform(950.0, 1050.0), 2)
class SistemaMonitoramento:
    def __init__(self):
        self.sensores = []
    def adicionar(self, sensor):
        if isinstance(sensor, Sensor):
            self.sensores.append(sensor)
        else:
            raise ValueError("O sensor deve ser uma instância de Sensor.")
    def relatorio(self):
        rel = "Relatório de Monitoramento:\n"
        for sensor in self.sensores:
            leitura = sensor.ler()
            rel += f"- {sensor.tipo}: {leitura}\n"
        return rel