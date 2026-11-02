Python 3.10 o superior instalado.

Creación de entorno virtual: 
    python -m venv .lab03

source .lab03/bin/activate      # En Windows: .lab03\Scripts\activate

Dependencias de Python (pip install -r requirements.txt):
    - locust>=2.20.0
    - requests>=2.31.0
    - pydantic>=2.5.0

laboratorio_semana3_locust/
|__ config/
|   |__ settings.py
|__ models/
|   |__ post_model.py
|__ locustfiles/
|   |__ level1_basic.py
|   |__ level2_intermediate_serial.py
|   |__ level3_intermediate_parallel.py
|   |__ level4_advanced_heavy_payload.py
|__ requirements.txt
|__ README.md

Ejecutar Pruebas con Interfaz Web de Locust:
- Nivel 1 (Básico): locust -f locustfiles/level1_basic.py
- Nivel 2 (Intermedio Serie): locust -f locustfiles/level2_intermediate_serial.py
- Nivel 3 (Intermedio Paralelo): locust -f locustfiles/level3_intermediate_parallel.py
- Nivel 4 (Avanzado Heavy Payload): locust -f locustfiles/level4_advanced_heavy_payload.py

Acceder a la Interfaz Gráfica:

Abrir en el navegador web: http://localhost:8089 o http://TU_IP:8089

## Autores
| <sub>ESCOBEDO PUMACAYO, PIER JONATHAN</sub> | <sub>HUAMÁN MORIANO, ERICK OLIVER</sub> | <sub>JOSÉ HUGO SARAVIA CHÁVEZ</sub> |
| :---: | :---: | :---: |
