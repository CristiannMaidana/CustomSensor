# CustomSensor (simulador)

Simulador en Python que:
1) Obtiene metadatos de sensores desde un backend Django (GET /api/sensores/{id})
2) Genera mediciones de volumen llenado
3) Envía mediciones al backend (POST /api/medicion_sensores/)
4) Puede correr múltiples sensores en paralelo (threads) y sincronizar turnos (semaforos)

## Requisitos
- Python 3.12 (recomendado)
- Backend Django corriendo (por defecto http://127.0.0.1:8000)

## Instalación (Windows PowerShell)
Desde la raíz del repo:

py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
python -m pip install -r requirements.txt

## Configuración
Copiar plantilla:

Copy-Item .env.example .env

Editar .env con tus valores reales.

Variables principales:
- BASE_URL
- SENSORES
- INTERVAL_SECONDS
- TIMEOUT_SECONDS

## Ejecución
.\scripts\run_windows.ps1

