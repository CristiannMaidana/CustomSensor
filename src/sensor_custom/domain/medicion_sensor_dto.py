from typing import Optional
from pydantic import BaseModel, ConfigDict

from src.sensor_custom.domain.medicion_sensor import MedicionSensor


class MedicionSensorDTO(BaseModel):
    model_config = ConfigDict(extra="ignore")

    #Propiedades para cargar en el backend
    sensor_id: int
    contenedor_id: int
    volumen_medido: Optional[float] = None

    @classmethod
    def from_domain(cls, ms: MedicionSensor) -> "MedicionSensorDTO":
        return cls(
            sensor_id=ms.id_sensor,
            contenedor_id=ms.id_contenedor,
            volumen_medido=ms.volumen_medido,
        )


def to_json(ms: MedicionSensor) -> str:
    dto = MedicionSensorDTO.from_domain(ms)
    return dto.model_dump_json(exclude_none=True)
