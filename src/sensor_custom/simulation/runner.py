import time

from src.sensor_custom.simulation.generador_llenado import GeneradorLlenado


class Runner:
    def __init__(self, medicion_sensor, semaforo):
        self.ms = medicion_sensor
        self.generador = GeneradorLlenado()
        self.sem1, self.sem2 = semaforo

    def iniciar(self):
        while self.ms.volumen_medido < 1:
            self.sem1.acquire()
            self.ms.volumen_medido += self.generador.get_valor()
            self.sem2.release()
            time.sleep(30)
