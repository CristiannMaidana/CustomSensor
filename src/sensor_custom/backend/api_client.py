import requests


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