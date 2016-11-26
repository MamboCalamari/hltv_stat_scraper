import scrapy


class HLTVSpider(scrapy.Spider):
    #must give spider name, run with scrapy crawl <name>
    name = "hltv"
    #team page min 29 maps, last 3 months
    start_urls = ['http://www.hltv.org/?pageid=182&statsfilter=5']
    base_url = "http://www.hltv.org"

    def parse(self, response):
        team_link = self.base_url + response.xpath('//a[@href="/?pageid=179&teamid=6773&statsfilter=5"]/@href').extract_first()

        yield scrapy.Request(team_link, callback=self.parseTeam)

    def parseTeam(self, response):
        print "Yay!"