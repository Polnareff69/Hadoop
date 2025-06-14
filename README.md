#  Proyecto MapReduce con Hadoop — TRM Mensual + API

##  Descripción

Este proyecto implementa un flujo de procesamiento distribuido usando **Hadoop** y **MapReduce** para calcular el **promedio mensual de la Tasa Representativa del Mercado (TRM)** a partir de datos abiertos de la **Superintendencia Financiera de Colombia**.  
El resultado final se expone a través de una **API REST desarrollada con FastAPI**.

---

##  Herramientas utilizadas

- ️ **Hadoop 3.3.1** (modo pseudo distribuido)
-  **HDFS** para almacenamiento de archivos
-  **MapReduce** con `mrjob` en Python
-  **Python 3.10** + `mrjob`, `fastapi`, `uvicorn`, `chardet`
-  **FastAPI** para exponer resultados por API REST

---

##  Estructura del proyecto

```
.
├── datos/
│   └── TRM_20250531.csv              # Archivo original descargado
├── scripts/
│   └── trm_promedio_mensual.py      # Script MapReduce con mrjob
│   └── convertir_txt_a_csv.py       # Convierte salida.txt a CSV
├── resultado.txt                        # Salida cruda del MapReduce
├── resultado.csv                        # Resultado procesado como CSV
├── main.py                           # API FastAPI
└── README.md                         # Documentación del proyecto
```

---

##  Flujo de trabajo

### 1. **Carga del archivo en HDFS**
```bash
hdfs dfs -mkdir /datos
hdfs dfs -put TRM_20250531.csv /datos/
```

### 2. **Ejecución del trabajo MapReduce en local o Hadoop**
```bash
python trm_promedio_mensual.py TRM_20250531.csv > resultado.txt
```


### 3. **Inicio de la API**
```bash
uvicorn main:app --reload
```

Accede a los resultados en:

-  JSON: [http://localhost:8000/trm](http://localhost:8000/trm)
-  Documentación Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)

---

##  Resultado esperado (ejemplo)

```json
[
  { "mes": "1991-12", "promedio_trm": 630.12 },
  { "mes": "1992-01", "promedio_trm": 644.60 },
  ...
]
```

---

##  Requisitos para ejecutar

- Python 3.10
- Hadoop 3.3.x
- Dependencias:
  ```bash
  pip install mrjob fastapi uvicorn chardet
  ```
Video sustentacion:
https://teams.microsoft.com/l/meetingrecap?driveId=b%21SYqh4IsjcE6RyGXMoGW5flIO2SNlhWFAg8iO4bSq0wwqLPYhJBgeRaSLlXSFTQQa&driveItemId=01JRIBNJMG5MGQBNMORZFYJSFTVFQWERYW&sitePath=https%3A%2F%2Feafit-my.sharepoint.com%2F%3Av%3A%2Fg%2Fpersonal%2Fjjmunozg_eafit_edu_co%2FEYbrDQC1jo5LhMizqWFiRxYBQlUzPaJPGNHIKbwl1TlhBw&fileUrl=https%3A%2F%2Feafit-my.sharepoint.com%2Fpersonal%2Fjjmunozg_eafit_edu_co%2FDocuments%2FGrabaciones%2FHola-20250602_053344-Grabaci%25C3%25B3n%2520de%2520la%2520reuni%25C3%25B3n.mp4%3Fweb%3D1&iCalUid=040000008200e00074c5b7101a82e00800000000863032c5a8d3db010000000000000000100000003069600847ddaf40bed788703556972e&threadId=19%3Ameeting_YzA4NTUxNzItNjMzNS00YTFmLWE5ZTEtODM0OTllYzI2ZGZk%40thread.v2&organizerId=57068c87-48fb-4155-99ed-c923d7a3abd7&tenantId=99f7b55e-9cbe-467b-8143-919782918afb&callId=b44092e7-5d6a-4ebe-b151-7525dfb03e19&threadType=Meeting&meetingType=Scheduled&subType=RecapSharingLink_RecapCore

- **Nombre:** Juan Muñoz
- **Curso:** Topico. Telematica
- **Fecha:** Mayo de 2025
