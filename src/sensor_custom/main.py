import threading

from src.sensor_custom.backend.api_client import ApiClient
from src.sensor_custom.domain.medicion_sensor import MedicionSensor
from src.sensor_custom.domain.medicion_sensor_dto import to_json
from src.sensor_custom.domain.sensor_dto import SensorDTO
from src.sensor_custom.simulation.runner import Runner

if __name__ == '__main__':
    # Cargo la base de la url
    api = ApiClient('http://127.0.0.1:8000/')

    # elijo el sensor y valido datos json y convierto en python
    sensor1 = SensorDTO.model_validate(api.get_sensor(1)).to_domain()
    sensor2 = SensorDTO.model_validate(api.get_sensor(2)).to_domain()

    # genero la carga de datos del sensor
    ms1 = MedicionSensor(volumen_medido=0, sensor=sensor1)
    ms2 = MedicionSensor(volumen_medido=0, sensor=sensor2)

    # Par de semáforos por sensor (turnos)
    sem1_1 = threading.Semaphore(1)   # arranca el sensor 1
    sem2_1 = threading.Semaphore(0)

    sem1_2 = threading.Semaphore(0)   # el sensor 2 espera su turno
    sem2_2 = threading.Semaphore(0)


    # genero el runner
    run1 = Runner(medicion_sensor=ms1, semaforo=(sem1_1, sem2_1))
    run2 = Runner(medicion_sensor=ms2, semaforo=(sem1_2, sem2_2))

    #Mando el hilo de runner
    threading.Thread(target=run1.iniciar, daemon=True).start()
    threading.Thread(target=run2.iniciar, daemon=True).start()

    while ms1.volumen_medido < 1 or ms2.volumen_medido < 1:

        if ms1.volumen_medido < 1:
            sem2_1.acquire()
            print(ms1.__dict__)
            api.post_medicion_sensor(to_json(ms1))
            (sem1_2 if ms2.volumen_medido < 1 else sem1_1).release()

        if ms2.volumen_medido < 1:
            sem2_2.acquire()
            print(ms2.__dict__)
            api.post_medicion_sensor(to_json(ms2))
            (sem1_1 if ms1.volumen_medido < 1 else sem1_2).release()
