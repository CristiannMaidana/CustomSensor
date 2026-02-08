class MedicionSensor:
    def __init__(self, volumen_medido, sensor):
        self.volumen_medido = volumen_medido
        self.id_sensor = sensor.id_sensor
        self.id_contenedor = sensor.id_contenedor