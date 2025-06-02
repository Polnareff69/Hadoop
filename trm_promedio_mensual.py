from mrjob.job import MRJob
import csv
from datetime import datetime

class MRTRMPromedioMensual(MRJob):

    def mapper(self, _, line):
        try:
            if isinstance(line, bytes):
                line = line.decode("utf-8")


            if "VALOR" in line or not line.strip():
                return

            row = next(csv.reader([line], delimiter=','))

            valor = float(row[0])
            fecha = datetime.strptime(row[1], "%d/%m/%Y")
            clave_mes = fecha.strftime("%Y-%m")

            yield clave_mes, (valor, 1)

        except Exception as e:
            self.stderr.write(f"ERROR: {e} - línea: {line}\n".encode('utf-8'))
            pass

    def reducer(self, mes, valores):
        total_valor = 0
        total_dias = 0
        for valor, conteo in valores:
            total_valor += valor
            total_dias += conteo
        promedio = total_valor / total_dias if total_dias > 0 else 0
        yield mes, round(promedio, 2)

if __name__ == '__main__':
    MRTRMPromedioMensual.run()
