import scrapy

"""
A class that scrapes exporters info from 
the fruits attraction exhibition site
http://appcatalogo.ifema.es/waCatalogoWeb/ \
index.html?feria=FA17&idioma=es#LACTIVIDAD&p=1&i=en&t=TODO&e=20&b=&a=3
"""
class FruitAttractionSpider(scrapy.Spider):
    name = 'fruit_attraction'
    # allowed_domains = ['']
    def start_requests(self):
        urls = [
            'http://appcatalogo.ifema.es/waCatalogoWeb/index.html?feria=FA17&idioma=es#LACTIVIDAD&p=1&i=en&t=TODO&e=20&b=&a=3'

        ]
        for url in urls:
            yield scrapy.Request(
                url=url,callback=self.parse
            )
    
    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = 'fruits-{}.html'.format(page)
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file {}'.format(filename))
