from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome(options=options)
#browser = webdriver.Chrome('C:/chromedriver.exe')



browser.get(
    "https://www.hanseo.ac.kr/boardCnts/list.do?boardID=298&m=040101&s=hs")
time.sleep(2)

def hanseo_home(keyword):

    browser.find_element(By.XPATH,
                         '//*[@id="sub_content"]/div[2]/form/div/section/fieldset/div/input').click()  # 검색창 클릭
    browser.find_element(By.XPATH,
                         '//*[@id="sub_content"]/div[2]/form/div/section/fieldset/div/input').send_keys(keyword)  # 검색어 입력
    
    browser.find_element(By.XPATH,
                         '//*[@id="sub_content"]/div[2]/form/div/section/fieldset/div/button').click()
    time.sleep(2)
  
    result = []
    soup = BeautifulSoup(browser.page_source, "html.parser")

    content = soup.find("table", class_="wb")
    content_1 = content.find('tbody')
    contents = content_1.find_all('tr')

    for con in contents:
        anchor = con.select_one("td a")  
        title = anchor['title']

        num, writer, view, day = con.find_all("td", class_="")

        home_data = {
            'num': num,
            'writer': writer,
            'view': view,
            'day': day,
            'title': title
        }
        print(day)
        result.append(home_data)
    return result





"""
[{'num': < td class= "" >
< img align = "absmiddle/" alt = "HOT아이콘" border = "0" height = "14" src = "/images/comm/board/icon/bullet_03.gif" width = "22"/>
< /td >,
'writer': < td class = "" > 교무처 < /td >,
'view': < td class = "" > 5670 < /td >,
'day': < td class = "" > 2023-02-24 < /td >,
'title': '2023학년도 1학기 9학기 이상 재학생 등록 안내'},
"""
