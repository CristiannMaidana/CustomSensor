import requests
import json

from src.sensor_custom.domain.medicion_sensor import MedicionSensor
from src.sensor_custom.domain.medicion_sensor_dto import to_json


class ApiClient:
    #Inicializo la api con la url, un tiempo y una llave de autorizacion(Agregar)
    def __init__(self, base_url, timeout=5):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        #self.session.headers.update({"Authorization": f"Bearer {api_key}"})

    # Obtener los datos del sensor y entregarlos en tipo json
    def get_sensor(self, sensor_id):
        url = f"{self.base_url}/api/sensores/{sensor_id}"
        resp = self.session.get(url, timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()

    # Envia la medida obtenida del sensor al backend
    def post_medicion_sensor(self, medicion_sensor):
        url = f"{self.base_url}/api/medicion_sensores/"
        if isinstance(medicion_sensor, MedicionSensor):
            payload = json.loads(to_json(medicion_sensor))
        elif isinstance(medicion_sensor, str):
            payload = json.loads(medicion_sensor)
        else:
            payload = medicion_sensor
        resp = self.session.post(url, json=payload, timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()