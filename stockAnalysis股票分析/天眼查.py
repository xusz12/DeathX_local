from selenium import webdriver as wd
import pandas as pd
import time
import requests
import re
from bs4 import BeautifulSoup
import xlwt
import xlrd
#------------------------------------------------------------有效区域----------------------------------------------
url = 'https://www.tianyancha.com/search?key='
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Cookie': 'aliyungf_tc=AQAAAGp8/GSg4gEAfcrveHzLUhIFEWCw; csrfToken=hl4PDgctN1NTUK-UMT1kOqC4; TYCID=b280f870711511eaa56247e3f8680851; undefined=b280f870711511eaa56247e3f8680851; ssuid=5660732920; RTYCID=1e2619d0b847407ba4f1955fb056dd3b; CT_TYCID=7f2cebb022fe4815b2e499e142ada891; _ga=GA1.2.1844157902.1585414862; tyc-user-phone=%255B%252213928044041%2522%255D; bannerFlag=true; jsid=SEM-BAIDU-PZ2003-VI-000001; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1585414861,1585462459; _gid=GA1.2.861519966.1585586174; _gat_gtag_UA_123487620_1=1; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522vipToMonth%2522%253A%2522false%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522integrity%2522%253A%252210%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522schoolGid%2522%253A%2522%2522%252C%2522bidSubscribe%2522%253A%2522-1%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzkyODA0NDA0MSIsImlhdCI6MTU4NTU4NjE5OCwiZXhwIjoxNjE3MTIyMTk4fQ.zn75Qsx-MivA0qmqIBlmSuP50tSv3ego5eaG4gnixPrRRF8eUYSk3djN-maPa-9B-if5InGClvTqMVml-IMPkA%2522%252C%2522schoolAuthStatus%2522%253A%25222%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522companyAuthStatus%2522%253A%25222%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E5%25A5%25A5%25E4%25BC%25A6%25E5%25A8%259C%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522companyGid%2522%253A%2522%2522%252C%2522mobile%2522%253A%252213928044041%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzkyODA0NDA0MSIsImlhdCI6MTU4NTU4NjE5OCwiZXhwIjoxNjE3MTIyMTk4fQ.zn75Qsx-MivA0qmqIBlmSuP50tSv3ego5eaG4gnixPrRRF8eUYSk3djN-maPa-9B-if5InGClvTqMVml-IMPkA; token=1accc1d5e143433c9bdbe5c172c7a64f; _utm=9b8731038fa84232934cfecb13a202de; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1585586204; cloud_token=538e543f9ea74f37a68c9fab24ffd60b; cloud_utm=92fa6f06b5a141ec9a880f200cdf9291'
}
nameCsv = pd.read_csv('高剩.csv')
companyNames = nameCsv['name']
nameCsv['checkName'] = None
nameCsv['ID'] = None
a = 0
b=0
#------------------------------------------------------------有效区域----------------------------------------------
# companyNamesCheck=[]
# taxpayersID=[]
# browser=wd.Chrome()
# browser.get(url)
# time.sleep(1)
# for companyName in companyNames:
#     inputBox = browser.find_element_by_id('header-company-search')
#     inputBox.clear()
#     inputBox.send_keys(companyName)
#     butten = browser.find_element_by_class_name('input-group-btn')
#     butten.click()
#     firstTag = browser.find_element_by_class_name('select-none')
#     firstTagUrl = firstTag.get_attribute('href')
#     # firstTag.click()
#     # time.sleep(5)
#     # companyName=browser.find_element_by_class_name('header').find_element_by_class_name('name').text
#     # print(companyName)
#
#     request=requests.get(firstTagUrl,headers=headers)
#     # # soup=BeautifulSoup(request.text,'lxml')
#     # # print(soup.find('table',class_='table -striped-col -border-top-none -breakall'))
#     # ###
#     # # '<div class="header"><h1 class="name">珠海康泰明输变电工程有限公司</h1><span class="button -h28 button-claim company-header-claim-btn" onclick="claimCompanySelect(1475560339)" tyc-event-click="" tyc-event-ch="CompangyDetail.Head.Renzheng"><i class="tic tic-claim button-icon"></i><span class="btn-inner">我要认证</span><div class="warp -normal"><div class="triangle"></div><div class="desc-left"><div class="title">完成高级及以上认证</div><div class="desc">可以获得专属认证标识、自主管理产品信息、查看访问用户、优惠券等10余项特权。更为企业树立权威性，让客户更信赖！</div></div><img class="desc-right lazy-img -image" data-src="https://cdn.tianyancha.com/web-require-js/public/images/claim/company-header-desc.png" src="https://cdn.tianyancha.com/web-require-js/public/images/claim/company-header-desc.png"></div></span><div class="float-right btns-right-container"><!--信用报告--><div class="button -normal -sm" tyc-event-click="" tyc-event-ch="CompangyDetail.xiazaiaogao" onclick="downloadReport314(0)"><span class="tic tic-download-report button-icon"></span><span class="btn-inner">下载报告</span></div><input type="hidden" is-monitor="" value="false"><div id="" style="min-width: 90px;" class="button -sm -active watch-btn" watch-btn="" tyc-event-click="" tyc-event-ch="CompangyDetail.Monitor" onclick="toogleWatch()"><i class="tic tic-monitor button-icon"></i><span class="btn-inner">风险监控</span><div class="warp -normal"><div class="triangle"></div><img class="desc-left lazy-img -image" data-src="https://cdn.tianyancha.com/web-require-js/public/images/watch-intro-img.png" src="https://cdn.tianyancha.com/web-require-js/public/images/watch-intro-img.png"><div class="desc-right">实时监控100家公司/老板/投资机构的工商、司法诉讼、经营风险等信息变更，每日9点推送监控日报，不再错过任何一个重要情报。</div></div><div class="watch-people-num">180人已监控</div></div></div></div>'
#     print(re.search('统一社会信用代码</td><td width="308px">(.*?)</td>', request.text).group(1))
#     print(re.search('<div class="header"><h1 class="name">(.*?)</h1>', request.text).group(1))
#     taxpayerID = re.search('统一社会信用代码</td><td width="308px">(.*?)</td>', request.text).group(1)
#     companyNameCheck = re.search('<div class="header"><h1 class="name">(.*?)</h1>', request.text).group(1)
#
#     nameCsv.iloc[a, 2] = companyNameCheck
#     nameCsv.iloc[a, 3] = taxpayerID
#     a+=1
#     time.sleep(0.5)
# nameCsv.to_csv('查询公司纳税人识别号.csv')
# browser.close()
#------------------------------------------------------------有效区域----------------------------------------------
#只使用requests，re，bs4完成爬虫，此爬虫重点在于需要登入账号才能获取信息，不然爬去到的都是垃圾信息，登入账号可以用selenium，淡过于麻烦，这里使用headers中的cookie登入
for companyName in companyNames:
    if b<9:
        request = requests.get(url + companyName, headers=headers)
        soup = BeautifulSoup(request.text, 'lxml')

        try:
            firstTagUrl = soup.find('a', class_='name').get('href')
            requestUrl = requests.get(firstTagUrl, headers=headers)
            taxpayerID = re.search('统一社会信用代码</td><td width="308px">(.*?)</td>', requestUrl.text).group(1)
            companyNameCheck = re.search('<div class="header"><h1 class="name">(.*?)</h1>', requestUrl.text).group(1)
        except:
            print('ip被封maybe#####################################################',companyName,a)
            a+=1
            b+=1
        else:
            print(taxpayerID, companyNameCheck,a)
            nameCsv.iloc[a, 1] = companyNameCheck
            nameCsv.iloc[a, 2] = taxpayerID
            a += 1
            b=0
            time.sleep(0.5)
            nameCsv.to_excel('高剩1.xlsx')
    else:
        a += 1
        b = 0
        for i in range(20):
            print(20 - i)
            time.sleep(1)
nameCsv.to_excel('/Users/x/Desktop/高剩1.xlsx')
# nameCsv.to_csv('剩下1.csv')
#------------------------------------------------------------有效区域----------------------------------------------
# idcheck=pd.read_csv('查询公司纳税人识别号.csv')
# idcheck['check'] = idcheck.name == idcheck.checkName
# idcheck.to_csv('查询公司纳税人识别号2.csv')
# print(idcheck)
#----------------------------------------------------------------------------------------------------------
checkclsx=pd.read_excel('高宁宁2.xlsx')
checkclsx['check']=checkclsx.name==checkclsx.checkName
checkclsx.to_excel('高宁宁.xlsx')
