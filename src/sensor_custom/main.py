import threading

from src.sensor_custom.backend.api_client import ApiClient
from src.sensor_custom.domain.medicion_sensor import MedicionSensor
from src.sensor_custom.domain.medicion_sensor_dto import to_json
from src.sensor_custom.domain.sensor_dto import SensorDTO
from src.sensor_custom.simulation.runner import Runner

if __name__ == '__main__':
    # Cargo la base de la url
    api = ApiClient('http://127.0.0.1:8000/')

    # elijo el sensor
    sensor_data = api.get_sensor(2)

    # Valido los datos json del sensor a python
    dto = SensorDTO.model_validate(sensor_data)  # validación + parseo

    # Sensor ya en python
    sensor = dto.to_domain()  # dominio

    # genero la carga de datos del sensor
    ms = MedicionSensor(volumen_medido=0, sensor=sensor)

    sem1 = threading.Semaphore(1)
    sem2 = threading.Semaphore(0)

    # genero el runner
    run = Runner(medicion_sensor=ms, semaforo=(sem1, sem2))  # semaforo 1 + semaforo 2

    hilo_runner = threading.Thread(target=run.iniciar, daemon=True)
    hilo_runner.start()

    while ms.volumen_medido < 1:
        # se consume semaforo 2
        sem2.acquire()

        print(ms.__dict__)
        api.post_medicion_sensor(to_json(ms))

        # activa el semaforo 1
        sem1.release()
