# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/04/26 19:40'
from  bs4 import  BeautifulSoup
import requests
import pymongo
import time
from multiprocessing import Pool
from area import area_string
from getIPProxy import IP_LIST,get_random_ip,cip,Random_header,Headers

client = pymongo.MongoClient('localhost',27017)
youxin = client.youxin
url_list = youxin.url_list
detail_info = youxin.detail_info
none_url_list = youxin.none_url_list
error_area_list = youxin.error_area_list
none_detail_info = youxin.none_detail_info
except_detail_info = youxin.except_detail_info
# url_item = youxin.url_item
def extract_url(url):
    try:
        proxy = get_random_ip(IP_LIST)
        while (not cip(proxy)):
            proxy = get_random_ip(IP_LIST)

        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',

        }
        header['User-Agent'] = Random_header(Headers)
        requests.adapters.DEFAULT_RETRIES = 4

        wb_data = requests.get(url,headers = header, proxies=proxy)
        requests.session().close()
        # wb_data = requests.get(url)
        if wb_data.status_code ==404:
            print "没有内容"
            return "null"

        soup = BeautifulSoup(wb_data.text,'lxml')
        # print repr(soup.prettify()).decode("unicode–escape")
        if soup.find("p","search-nodata-txt"):
            return "null"
        item_urls = soup.select("#search_container > div._list-con.list-con.clearfix.ab_carlist > ul > li > div.across > a")
        # prices = soup.select("#search_container > div._list-con.list-con.clearfix.ab_carlist > ul > li > div.across > div > p > em")
        area = url.split('/')[3]

        for item_url in item_urls:
            # title = item_url.get("title")
            detail_url = item_url.get("href")
            url_list.insert_one({"url":detail_url[2:],"area":area})
            print detail_url[2:]
            # price = prices.get_text
        return "complate"
    except:
        none_url_list.insert_one({"url":url,"area":area})
        print "error"

def area_url(area):
    try:
        for i in range(1,200):
            result = extract_url("https://www.xin.com/{}/i{}/".format(area,i))
            print "https://www.xin.com/{}/i{}/".format(area,i)
            if result =="null":
                break
    except:
        error_area_list.insert_one({"area":area})
        print "areaerror"

def get_detail_info(url):
    try:
        proxy = get_random_ip(IP_LIST)
        while (not cip(proxy)):
            proxy = get_random_ip(IP_LIST)

        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',

        }
        header['User-Agent'] = Random_header(Headers)
        requests.adapters.DEFAULT_RETRIES = 4

        wb_data = requests.get(url, headers=header, proxies=proxy)
        # wb_data = requests.get(url)
        requests.session().close()
        # wb_data = requests.get(url)
        if wb_data.status_code == 404:
            print "没有内容"
            none_detail_info.indert_one({"url":url})
            return "null"

        soup = BeautifulSoup(wb_data.text, 'lxml')
        # print repr(soup.prettify()).decode("unicode–escape")
        if soup.find("p", "search-nodata-txt"):
            none_detail_info.indert_one({"url": url})
            return "null"
        city = soup.select("#current_city_id") if soup.select("#current_city_id").__len__()>0 else None

        car_name = soup.select("body > div.cd_m > div.cd_m_info.cd_m_info_zjf > div.cd_m_info_it2 > div.cd_m_h.cd_m_h_zjf > span") if soup.select("body > div.cd_m > div.cd_m_info.cd_m_info_zjf > div.cd_m_info_it2 > div.cd_m_h.cd_m_h_zjf > span").__len__()>0 else None
        # print repr(car_name).decode("unicode–escape")
        cost_money = soup.select("body > div.cd_m > div.cd_m_info.cd_m_info_zjf > div.cd_m_info_it2 > p > span.cd_m_info_jg > b") if soup.select("body > div.cd_m > div.cd_m_info.cd_m_info_zjf > div.cd_m_info_it2 > p > span.cd_m_info_jg > b").__len__()>0 else None

        original_cost = soup.select("span.cd_m_cursor > b")[0].get_text() if soup.select("span.cd_m_cursor > b").__len__()>0 else None
        # print repr( original_cost).decode("unicode–escape")
        use_time  = soup.select("body > div.cd_m > div.cd_m_info.cd_m_info_zjf > div.cd_m_info_it2 > ul > li:nth-of-type(1) > span.cd_m_desc_val")[0].get_text() if soup.select("body > div.cd_m > div.cd_m_info.cd_m_info_zjf > div.cd_m_info_it2 > ul > li:nth-of-type(1) > span.cd_m_desc_val").__len__()>0 else None
        # print repr( use_time).decode("unicode–escape")
        register_time = soup.select("body > div.cd_m > div.cd_m_info.cd_m_info_zjf > div.cd_m_info_it2 > ul > li:nth-of-type(1) > span.cd_m_desc_key")[0].get_text() if soup.select("body > div.cd_m > div.cd_m_info.cd_m_info_zjf > div.cd_m_info_it2 > ul > li:nth-of-type(1) > span.cd_m_desc_key").__len__()>0 else None
        # print repr(register_time).decode("unicode–escape")
        km = soup.select("body > div.cd_m > div.cd_m_info.cd_m_info_zjf > div.cd_m_info_it2 > ul > li:nth-of-type(2) > a")[0].get_text() if soup.select("body > div.cd_m > div.cd_m_info.cd_m_info_zjf > div.cd_m_info_it2 > ul > li:nth-of-type(2) > a").__len__()>0 else None
        # print repr(km).decode("unicode–escape")
        emission_standard = soup.select("body > div.cd_m > div.cd_m_info.cd_m_info_zjf > div.cd_m_info_it2 > ul > li:nth-of-type(3) > span.cd_m_desc_val.cd_m_desc_cursor")[0].get_text() if soup.select("body > div.cd_m > div.cd_m_info.cd_m_info_zjf > div.cd_m_info_it2 > ul > li:nth-of-type(3) > span.cd_m_desc_val.cd_m_desc_cursor").__len__()>0 else None
        # print repr(emission_standard).decode("unicode–escape")
        displacement = soup.select("body > div.cd_m > div.cd_m_info.cd_m_info_zjf > div.cd_m_info_it2 > ul > li:nth-of-type(4) > span.cd_m_desc_val")[0].get_text() if soup.select("body > div.cd_m > div.cd_m_info.cd_m_info_zjf > div.cd_m_info_it2 > ul > li:nth-of-type(4) > span.cd_m_desc_val").__len__()>0 else None
        # print repr(displacement).decode("unicode–escape")
        buy_time = soup.select("body > div.cd_m > div.cd_m_info.cd_m_info_zjf > div.cd_m_info_it2 > ul > li:nth-of-type(5) > span.cd_m_desc_val")[0].get_text() if soup.select("body > div.cd_m > div.cd_m_info.cd_m_info_zjf > div.cd_m_info_it2 > ul > li:nth-of-type(5) > span.cd_m_desc_val").__len__()>0 else None
        # print repr(buy_time).decode("unicode–escape")
        # prices = soup.select("#search_container > div._list-con.list-con.clearfix.ab_carlist > ul > li > div.across > div > p > em")
        detail_info.insert_one({"car_name":car_name[0].get_text().strip(),
                                "cost_momey":cost_money[0].get_text(),
                                "original_cost":original_cost,
                                "use_time":use_time,
                                "register_time": register_time,
                                "km":km.strip(),
                                "emission_standard":emission_standard,
                                "displacement":displacement,
                                "buy_timeOrLocation":buy_time,
                                "city":city[0].get_text()})


        return "complate"
    except:
        print "detail_error"
        except_detail_info.insert_one({"url":url})
        return "detail_error"



# get_detail_info("https://www.xin.com/8qk7jmpkm2/che66251497.html")
if __name__=="__main__":

    pool = Pool()
    # # pool.map(area_url,area_string.split())
    urllist = []
    for url in url_list.find():
        urllist.append("https://"+url["url"])
    pool.map(get_detail_info, urllist)
# print extract_url("https://www.xin.com/guigang/i7/")
# for area in area_string.split():
#     area_url(area)
