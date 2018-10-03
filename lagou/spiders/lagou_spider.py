import scrapy
from lagou.items import LagouItem
import json

class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = 'lagou.com'
    custom_settings = {  
            'DEFAULT_REQUEST_HEADERS' : {  
            'Accept': 'application/json, text/javascript, */*; q=0.01',  
            'Accept-Encoding': 'gzip, deflate, br',  
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
            'Host':'www.lagou.com',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
              
            'Origin': 'https://www.lagou.com',  
            'Referer': 'https://www.lagou.com/jobs/list_python?',  
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',  
            'X-Anit-Forge-Code': '0',  
            'X-Anit-Forge-Token': 'None',  
            'X-Requested-With': 'XMLHttpRequest'  
        },
'ITEM_PIPELINES' : {'lagou.pipelines.LagouPipeline': 300}
}

    def start_requests(self):
        url = "https://www.lagou.com/jobs/positionAjax.json?"
        requests=[]
        for i in range(1,31):
            formdata = {'first':'false','pn':str(i),'kd':'python'}
            request = scrapy.FormRequest(url,callback = self.parse,formdata = formdata)
            requests.append(request)
            print(request)
        return requests




    def parse(self,response):
        jsonBody =json.loads(response.body.decode())  
        results = jsonBody['content']['positionResult']['result']
        
        items = []

        for result in results:
            item = LagouItem()
            item['job'] = result['positionName']
            item['address'] = result['city']
            item['money'] = result['salary']
            item['req'] = result['education']+'/'+result['workYear']
            item['company'] = result['companyFullName']
            item['qua'] = result['industryField']+'/'+result['financeStage']
            item['des'] = ','.join(result['companyLabelList'])

            items.append(item)
        return items

    
