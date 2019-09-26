from scrapy import Spider
from scrapy.selector import Selector
from scraperideo.items import ScraperideoItem

class MySpider(Spider):
    name = "ideo"
    allowed_domains = ["challenges.openideo.com"]
    start_urls = ["https://challenges.openideo.com/challenge/"]
    def parse(self,response):
        hxs = Selector(response)
        baseurl="https://challenges.openideo.com"
        items = []
        completed_project_list = hxs.xpath("//div[@class='details-box distance-padding-top distance-padding-bottom col-8']//h2[@class='challenge-title sub-headline-text']/a")
        for projects in completed_project_list:
            item = ScraperideoItem()
            item["project_title"] = projects.xpath("text()").extract()[0].encode('utf-8').strip()
            item["project_url"] = projects.xpath("@href").extract()[0].encode('utf-8').strip()
            items.append(item)
        return items 

    def parse_stage(self,response): 
        hxs = Selector(response)
        phase_name = hxs.xpath("//a[@class='phase-name indent-text']")
        phase_caption = hxs.xpath("//span[@class='phase-caption indent-text']")
        proj_brief_url = hxs.xpath("//p[@class='distance-margin-bottom']/a/@href").extract()[0].strip()
        csv_contribution=""
       
        for i in range(0,len(phase_name)):
            phase= str(phase_name[i].xpath("text()").extract()[0])
            phase=str((phase).strip())
            dict_obj[proj_name][phase] = {}
            item["contributions_count"] = str(phase_caption[i].xpath("text()").extract()[0]).strip()
            item["phase_link"]= str(phase_name[i].xpath("@href").extract()[0]).strip()
            dict_obj[proj_name][phase] = dict(item)
            csv_contribution += phase+": "+item["contributions_count"]+" "
            if phase == "Research" or phase == "Inspiration":
                stage_count = 1;
            else:
               stage_count = 0;
            yield Request(url= (baseurl+item["phase_link"]),meta={'item':item,'dict_obj':dict_obj,'phase':phase,'proj_name':proj_name,'csv':c,'proj_csv':proj_csv,'network_csv':network_csv,'stage_count':stage_count}, callback = self.parse_url)
        yield Request(url= (baseurl+proj_brief_url),meta={'item':item,'dict_obj':dict_obj,'phase':phase,'proj_name':proj_name,'csv':c,
                 
 def run(self):
        for project in range(53):
            # Retrieving the data
            data = self.parse(project)
            self.parse_stage(data)

            # Parsing it
            self.parse_stores(data)
            print('scraped the page' + str(page))

        self.save_data()