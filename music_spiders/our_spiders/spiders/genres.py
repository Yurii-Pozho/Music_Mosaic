import scrapy

class GenreSpider(scrapy.Spider):
    name = 'genrespider'
    start_urls = ['https://www.everynoise.com/everynoise1d.html']

    def parse(self, response):
        for row in response.css('tr'):

            genre_name = row.css('td:nth-child(3) a::text').get(default='N/A') 

            playlist_url = row.css('td:nth-child(2) a::attr(href)').get()  

            if playlist_url is not None:
                yield {
                    'name': genre_name,
                    'url': response.urljoin(playlist_url)  
                }
