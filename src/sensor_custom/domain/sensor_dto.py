from datetime import date
from pydantic import BaseModel, ConfigDict

from src.sensor_custom.domain.Sensor import Sensor


class SensorDTO(BaseModel):
    model_config = ConfigDict(extra="ignore")  # ignora campos extra del backend

    id_sensor: int
    nombre_sensor: str
    fecha_instalacion_sensor: date | None = None
    numero_serie: str
    id_contenedor: int | None = None

    def to_domain(self) -> Sensor:
        return Sensor(**self.model_dump())
