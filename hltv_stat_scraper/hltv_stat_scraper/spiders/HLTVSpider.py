
import scrapy
from scrapy.crawler import CrawlerProcess

from TestInput import TestInput


class HLTVSpider(scrapy.Spider):
    #must give spider name, run with scrapy crawl <name>
    name = "hltv"
    #team page min 29 maps, last 3 months
    start_urls = ['http://www.hltv.org/?pageid=182&statsfilter=5']

    def __init__(self):
        self.base_url = "http://www.hltv.org"
        self.team1 = '"Astralis"'
        self.team2 = '"G2"'
        self.parse(self)

    #initial parse method, starts on start_urls
    def parse(self, response):
        #only search links from team data table, or else it will scrape matches, forum posts, etc.
        team_data_xpath = response.xpath('//div[@class="covMainBoxContent"]')

        team_links = []
        self.add_team_link(team_links, self.team1, team_data_xpath)
        self.add_team_link(team_links, self.team2, team_data_xpath)

        filename = 'team_list.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

        #visits each team page
        for link in team_links:
            yield scrapy.Request(link, callback=self.parse_team_page)

    #constructs a link to team's page using xpath
    def add_team_link(self, team_links, team, team_data_xpath):
        team_link_xpath = './/a[contains(.,%s)]/@href' % team
        team_link = self.base_url + team_data_xpath.xpath(team_link_xpath).extract_first()
        team_links.append(team_link)

    def parse_team_page(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)

        print "Yee"

        logo_box_content = response.xpath('//div[@class="covGroupBoxContent"][1]')
        team_logo = logo_box_content.xpath('.//img/@src').extract_first()

        player_box_content = response.xpath('//div[@class="covGroupBoxContent"][2]')
        players = player_box_content.xpath('.//div[@class="covSmallHeadline"]//text()').extract()
        for player in players:
            print player

        print "Yay!"

ti = TestInput()
ti.enter_teams()
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
process.crawl(HLTVSpider)
process.start()