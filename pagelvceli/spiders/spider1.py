from scrapy import Spider
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from scrapy.selector import HtmlXPathSelector

from pagelvceli.items import PagelvceliItem
 
class Spider1(Spider):
    name = 'stack'
    start_urls = ['http://www.lvceli.lv/cms/login.php']
 
    def parse(self, response):
        return FormRequest.from_response(response,
                                         formdata={'login': 'demo',
                                                   'password': 'demo',
                                                   'Submit': 'ieiet'},
                                         callback=self.scrape_pages)
 
    def scrape_pages(self, response):
        item = PagelvceliItem()
        item['station_name'] = response.css('#LV41 a *::text').get()
        item['time'] = response.css('#LV41 > td:nth-child(2) *::text').extract()
        item['air_temperature'] = response.css('#LV41 > td:nth-child(3) *::text').extract()
        item['air_temperature_trend'] = response.css('#LV41 > td:nth-child(4) *::text').extract()
        item['air_humidity'] = response.css('#LV41 > td:nth-child(5) *::text').extract()
        item['dew_point'] = response.css('#LV41 > td:nth-child(6) *::text').extract()
        item['precipitation'] = response.css('#LV41 > td:nth-child(7) *::text').extract()
        item['intensity'] = response.css('#LV41 > td:nth-child(8) *::text').extract()
        item['visibility'] = response.css('#LV41 > td:nth-child(9) *::text').extract()
        item['road_temperature1'] = response.css('#LV41 > td:nth-child(10) *::text').extract()
        item['road_temperature1_trend'] = response.css('#LV41 > td:nth-child(11) *::text').extract()
        item['road_condition1'] = response.css('#LV41 > td:nth-child(12) *::text').extract()
        item['road_warning1'] = response.css('#LV41 > td:nth-child(13) *::text').extract()
        item['freezing_point1'] = response.css('#LV41 > td:nth-child(14) *::text').extract()
        item['road_temperature2'] = response.css('#LV41 > td:nth-child(15) *::text').extract()
        item['road_temperature2_trend'] = response.css('#LV41 > td:nth-child(16) *::text').extract()
        item['road_condition2'] = response.css('#LV41 > td:nth-child(17) *::text').extract()
        item['road_warning2'] = response.css('#LV41 > td:nth-child(18) *::text').extract()
        item['freezing_point2'] = response.css('#LV41 > td:nth-child(19) *::text').extract()
       
        #LV41 > td:nth-child(2)

        return item

        #print response.css('#LV01 a *::text').get()
        #print response.css('#LV41 *::text').extract()

        #print response.css('#LV41 a *::text').get()

        #print response.css('#LV41 td *::text').extract()
        
        #print response.xpath('//tr/td[contains(text(), "Stac")]').get()

        #print response.xpath('//*[@id="LV01"]/td[1]/a[2]').get()

        #print response.xpath('//*[@id="LV41"]/td[3]').extract()

        #print response.css('#LV41 *::text').extract()

        #print response.css('td.norm > a::attr(href)').extract()

        #print response.css('td:nth-child(1) > a.norm::attr(href)').extract()

        #print response.css('title').extract()
        #print response.css('body > table > tbody > tr:nth-child(3) > td:nth-child(2) > table > tbody > tr:nth-child(1) > td:nth-child(2)').get()



        

