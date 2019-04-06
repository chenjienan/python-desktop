from scrapy import Request
# 导入Scrapy.spiders中的Spider类
from scrapy.spiders import Spider
# 导入spider.items中我们刚刚定义好的DoubanMovieItem
from spider.items import DoubanMovieItem


# inherit from Spider class
class DoubanMovieTop250Spider(Spider):
    name = 'douban-movie-top250'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield Request(url, headers=self.headers)


    def parse(self, response):
        item = DoubanMovieItem()

        movies = response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            item['ranking'] = movie.xpath('.//div[@class="pic"]/em/text()').extract()[0]
            item['movie_name'] = movie.xpath('.//div[@class="hd"]/a/span[1]/text()').extract()[0]
            item['score'] = movie.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            # item['score_num'] = movie.xpath('.//div[@class="star"]/span/text()').re(ur'(\d+)人评价')[0]
            yield item

        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        print(next_url)
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            print('=============', next_url)
            yield Request(next_url, headers=self.headers)
