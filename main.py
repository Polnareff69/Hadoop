from fastapi import FastAPI
import chardet

app = FastAPI()

@app.get("/trm")
def leer_trm():
    resultados = []
    try:
        with open("resultado.txt", "rb") as f:
            raw = f.read()
            deteccion = chardet.detect(raw)
            codificacion = deteccion["encoding"]

        texto = raw.decode(codificacion)

        for linea in texto.strip().splitlines():
            if "\x00" in linea or not linea.strip():
                continue
            partes = linea.strip().split("\t")
            if len(partes) == 2:
                mes = partes[0].replace('"', '').strip()
                trm = float(partes[1])
                resultados.append({
                    "mes": mes,
                    "promedio_trm": trm
                })

    except Exception as e:
        return {"error": str(e)}

    return resultados
