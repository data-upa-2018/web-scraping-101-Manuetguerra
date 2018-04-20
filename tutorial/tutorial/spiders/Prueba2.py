import scrapy
import json

class Prueba2 (scrapy.Spider):
    name = "presidente"

    def start_requests(self):
        url = 'https://www.presidencia.gov.py/tmpl/grillas/nomina.php'

        for page in range(24):
               yield scrapy.FormRequest(url=url, method='POST', formdata={"rows": "16", "page": str(page + 1)}, callback=self.parse)

    def parse(self,response):
        rows = json.loads(response.body)['rows']
        for row in rows:
            yield {
                'Nro': row['cell'][0],
                'Nombre y Apellido': row['cell'][1],
                'Cargo': row['cell'][2],
                'Total': row['cell'][3],
                'Sueldo': row['cell'][4],
                'G.Representante': row['cell'][5],
                'Bonificacion': row['cell'][6],
                'Tipo': row['cell'][7]
            }
