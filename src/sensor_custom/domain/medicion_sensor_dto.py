from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict

from src.sensor_custom.domain.medicion_sensor import MedicionSensor


class MedicionSensorDTO(BaseModel):
    model_config = ConfigDict(extra="ignore")

    #Propiedades para cargar en el backend
    fecha_hora_medicion: datetime
    id_sensor: int
    id_contenedor: int
    volumen_medido: Optional[float] = None

    @classmethod
    def from_domain(cls, ms: MedicionSensor) -> "MedicionSensorDTO":
        return cls(
            fecha_hora_medicion=datetime.now().astimezone(),
            id_sensor=ms.id_sensor,
            id_contenedor=ms.id_contenedor,
            volumen_medido=ms.volumen_medido,
        )


def to_json(ms: MedicionSensor) -> str:
    dto = MedicionSensorDTO.from_domain(ms)
    return dto.model_dump_json(exclude_none=True)
