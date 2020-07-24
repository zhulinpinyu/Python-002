import scrapy
from scrapy.selector import Selector
from maoyan.items import MaoyanItem

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    def start_requests(self):
        headers = {'Cookie': '__mta=51272342.1595578571207.1595578603793.1595578669279.5; uuid_n_v=v1; uuid=EDD78390CD8511EA8AF6570E3933DABA25EBEA8014A048379ECCB31D2388E323; _csrf=d5f48b2a2327a8689869e6cc33b1b21a1e0f6db700298abcc678b3245fca551a; _lxsdk_cuid=1737fe4d774c8-0b3f8041caebee-15356650-13c680-1737fe4d774c8; _lxsdk=EDD78390CD8511EA8AF6570E3933DABA25EBEA8014A048379ECCB31D2388E323; mojo-uuid=e2d7239259a9da63d21596b4723989d5; mojo-session-id={"id":"5043b9cca45bdf949ff15a5c6ad0fd22","time":1595578571229}; mojo-trace-id=8; __mta=51272342.1595578571207.1595578669279.1595579224054.6; _lxsdk_s=1737fe4d775-5e2-de8-589%7C%7C14'}

        url = "https://maoyan.com/films?showType=3"
        yield scrapy.Request(url, callback=self.parse, headers=headers)

    def parse(self, response):
        movie_items = Selector(response).xpath('//div[@class="movie-hover-info"]')[0:10]
        for movie_item in movie_items:
            item = MaoyanItem()
            item['name'] = movie_item.xpath('./div[1]/span[1]/text()').extract_first()
            item['tag'] = movie_item.xpath('./div[2]/text()').extract()[1].strip()
            item['plan_date'] = movie_item.xpath('./div[4]/text()').extract()[1].strip()
            yield item
