# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/04/21 13:45'
from bs4 import BeautifulSoup
import requests
import random

def cip(ip):
    try:
        if ip.keys()[0]=="http":
            requests.get('https://www.xin.com/',proxies={'http':ip["http"]},timeout=3)
        else:
            requests.get('https://www.xin.com/', proxies={'https': ip["https"]}, timeout=3)
    except:
        # print("failure")
        return False
    else:
        print(ip)
        return  True
def cip2(ip):
    try:

        if ip[0:5]=="HTTPS":
            requests.get('https://www.xin.com/', proxies={'https': ip}, timeout=3)
        else:
            requests.get('https://www.xin.com/', proxies={'http': ip}, timeout=3)

    except:
        # print("failure")
        return False
    else:
        print(ip)
        return  True



def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[5].text+'://'+tds[1].text + ':' + tds[2].text)

    return ip_list



# if __name__ == '__main__':
#     url = 'http://www.xicidaili.com/nn/'
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
#     }
#     ip_list = get_ip_list(url, headers=headers)
#     for ip in ip_list:
#         cip(ip)
    # proxies = get_random_ip(ip_list)
    # print(proxies)

IP_LIST ='''
    HTTPS://183.159.83.241:18118
    HTTPS://223.241.79.225:18118
    HTTPS://14.215.224.254:3128
    HTTPS://125.118.78.165:6666
    HTTPS://218.72.67.3:18118
    HTTPS://223.241.116.50:18118
    HTTPS://117.68.194.77:18118
    HTTPS://223.241.117.49:8010
    HTTPS://114.232.106.142:29838
    HTTPS://27.154.182.160:29017
    HTTPS://60.182.238.236:29770
    HTTPS://183.159.86.231:18118
    HTTPS://223.241.116.137:18118
    HTTPS://113.87.194.70:61234
    HTTPS://183.159.85.155:18118
    HTTPS://218.72.66.98:18118
    HTTPS://182.34.23.138:808
    HTTPS://218.72.109.195:18118
    HTTPS://223.241.117.222:8010
    HTTPS://112.80.119.66:8118
    HTTPS://114.215.107.94:60443
    HTTPS://183.159.92.87:18118
    HTTPS://218.72.108.240:18118
    HTTPS://183.128.34.13:18118
    HTTPS://49.85.4.34:44553
    HTTPS://121.226.186.92:45300
    HTTPS://223.241.118.129:8010
    HTTPS://183.159.88.192:18118
    HTTPS://183.159.95.38:18118
    HTTPS://183.159.91.4:18118
    HTTPS://223.241.116.36:8010
    HTTPS://49.79.193.223:61234
    HTTPS://14.120.183.144:61234
    HTTPS://223.241.116.254:18118
    HTTPS://27.217.155.8:8118
    HTTPS://183.159.90.99:18118
    HTTPS://183.128.33.139:18118
    HTTPS://223.241.117.114:8010
    HTTPS://42.7.26.21:60443
    HTTPS://183.159.91.10:18118
    HTTPS://59.42.41.169:808
    HTTPS://183.159.86.114:18118
    HTTPS://223.241.118.104:8010
    HTTPS://183.159.90.171:18118
    HTTPS://218.72.64.36:18118
    HTTPS://218.72.65.208:18118
    HTTPS://223.241.78.217:18118
    HTTPS://60.168.81.219:18118
    HTTPS://1.196.62.22:61234
    HTTPS://218.72.67.9:18118
    HTTPS://60.168.80.208:18118
    HTTPS://183.128.35.243:18118
    HTTPS://218.72.67.68:18118
    HTTPS://218.72.67.149:18118
    HTTPS://183.159.95.214:18118
    HTTPS://183.159.91.219:18118
    HTTPS://223.241.78.20:18118
    HTTPS://223.241.79.96:18118
    HTTPS://183.159.95.91:18118
    HTTPS://111.170.82.89:61234
    HTTPS://60.177.227.204:18118
    HTTPS://115.46.73.180:8123
    HTTPS://115.58.131.229:8118
    HTTP://183.159.86.138:18118
    HTTP://183.159.84.179:18118
    HTTP://183.159.82.39:18118
    HTTP://27.40.132.41:61234
    HTTP://111.155.116.215:8123
    HTTP://14.120.182.7:61234
    HTTP://122.4.29.213:61234
    HTTP://218.72.110.205:18118
    HTTP://60.177.227.179:18118
    HTTP://223.241.118.204:8010
    HTTP://60.177.226.170:18118
    HTTP://60.177.225.226:18118
    HTTP://119.180.196.170:61234
    HTTP://111.170.81.144:61234
    HTTP://218.72.109.221:18118
    HTTP://183.159.94.97:18118
    HTTP://112.248.17.110:61234
    HTTP://223.241.117.133:18118
    HTTP://223.241.118.92:8010
    HTTP://223.241.78.16:8010
    HTTP://182.202.222.94:61234
    HTTP://183.159.91.177:18118
    HTTP://49.79.193.181:61234
    HTTP://49.79.194.84:61234
    HTTP://183.159.82.133:18118
    HTTP://114.239.123.97:61234
    HTTPS://183.159.85.155:18118
    HTTP://223.241.116.118:8010
    HTTP://223.241.78.155:808
    HTTP://101.27.20.27:61234
    HTTPS://49.79.193.223:61234
    HTTP://171.115.238.140:61234
    HTTP://60.177.231.146:18118
    HTTP://223.241.78.240:18118
    HTTP://223.241.78.125:8010
    HTTPS://60.168.81.219:18118
    HTTP://180.110.249.210:8118
    HTTP://111.183.230.42:61234
    HTTP://110.73.53.211:8123
    HTTP://110.73.15.238:8123
    HTTPS://183.159.86.135:18118
    HTTP://14.120.182.84:61234
    HTTP://183.159.86.182:18118
    HTTP://60.177.224.205:18118
    HTTP://49.79.194.215:61234
    HTTP://125.104.241.164:26431
    HTTP://220.161.242.245:23250
    HTTP://117.64.225.79:18118
    HTTP://121.225.24.177:3128
    HTTP://223.241.79.179:8010
    HTTP://111.155.116.217:8123
    HTTP://218.72.65.187:18118
    HTTP://111.155.116.207:8123
    HTTP://119.179.209.43:61234
    HTTP://223.241.117.10:8010
    HTTP://60.177.225.221:18118
    HTTP://60.177.225.108:18118
    HTTP://114.99.25.98:18118
    HTTP://101.27.22.23:61234
    HTTP://223.241.78.101:18118
    HTTP://121.31.177.218:8123
    HTTP://183.159.93.220:18118
    HTTP://115.198.36.124:6666
    HTTP://183.159.83.223:18118
    HTTP://183.159.90.143:18118
    HTTP://183.159.89.89:18118
    HTTP://123.53.118.167:61234
    HTTP://183.159.95.221:18118
    HTTP://111.183.228.20:61234
    HTTP://183.159.80.59:18118
    HTTP://60.177.225.218:18118
    HTTP://183.159.94.231:18118
    HTTP://223.241.119.141:8010
    HTTP://60.177.230.192:18118
    HTTP://106.41.84.222:8118
    HTTP://49.81.33.200:32770
    HTTP://110.73.29.56:8123
'''
# HTTP://112.86.153.61:8118
# HTTP://110.73.28.200:8123
# HTTPS: // 60.177.227.96:18118
#HTTPS://183.159.95.174:18118
# HTTPS://60.177.231.253:18118
# HTTP://124.161.100.70:8118
# HTTP://123.53.119.69:61234
#HTTP://171.115.237.247:61234
def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list.split():
        proxy_list.append( ip)
    proxy_ip = random.choice(proxy_list)
    if proxy_ip[4] == "S":
        proxies = {'https': proxy_ip}
    else:
        proxies = {'http': proxy_ip}

    return proxies

Headers='''
    Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13:
    Mozilla/5.0 (iPhone; U; CPU like Mac OS X) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/4A93 Safari/419.3:
    Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1: 
    Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3: 
    Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12 
'''
def Random_header(Headers):
    header_list = []
    for header in Headers.split(':'):
        header_list.append(header.strip())
    proxy_header = random.choice(header_list)

    return proxy_header
# cip("//119.115.235.131:8118/")
# headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
#     }
# for ip in get_ip_list('http://www.xicidaili.com/nn/3',headers=headers):
#     print(ip)
# for i in range(1,20):
#     get_random_ip(IP_LIST)
# print Random_header(Headers)

# for url in temp.split():
#     cip2(url)