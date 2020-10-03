import scrapy

# titulo = //h1/a/text()
# citas = //span[@class="text" and @itemprop="text"]/text()
# top_ten_tags = //div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
    ]
    # analizar un archivo para extraer informacion
    # valiosa a partir de el

    def parse(self, response):
        title = response.xpath('//h1/a/text()').get()
        print(f'Titulo: {title}')

        qoutes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        print('Citas: ')
        for quote in qoutes:
            print(f'-{quote}')

        top_ten_tags = response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()
        print('Top Ten Tags: ')
        for tag in top_ten_tags:
            print(f'-{tag}')
