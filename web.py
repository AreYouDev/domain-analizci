import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from urllib.parse import quote
import os
from selenium.webdriver.chrome.service import Service

option = Options()
option.add_experimental_option("excludeSwitches", ["enable-logging"])
option.add_argument("--profile-directory=Default")
option.add_argument("--user-data-dir=/var/tmp/chrome_user_data")
#option.add_argument("--headless")
option.add_extension('/Users/alpguney/Documents/WebDriver/AdBlock.crx')


chrome_driver_path = '/Users/alpguney/Documents/WebDriver/chromedriver'

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=option)
print("\033[94mChromeDriver yükleniyor...\033[00m")

with open('domains.txt', 'r') as file:
    domains = file.read().splitlines()
    print(f"\033[92m{len(domains)} domain okundu.\033[00m")

results = []

for domain in domains:
    driver.get('https://checkpagerank.net/check-page-rank.php')
    print("\033[93mSayfa yükleniyor...\033[00m")
    #time.sleep(1) 

    input_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/input')  # Bu satırı değiştirin
    print("\033[96mURL giriliyor...\033[00m")
    #time.sleep(1)  
    input_element.send_keys(domain)
    #time.sleep(1) 
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/button').click()
    print(f"\033[95m{domain} analiz ediliyor...\033[00m")
    time.sleep(1)

    da = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[3]/div[7]/div[2]').text
    prdurum = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[3]/div[19]/div[2]').text
    tf = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[3]/div[8]/div[2]').text
    index_sayisi = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[3]/div[27]/div[2]').text
    spam_skoru = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[3]/div[12]/div[4]').text
    
    results.append([domain, da, prdurum, tf, index_sayisi, spam_skoru])
    print(f"\033[91m{domain} analiz edildi. ve rapor için belleğe alındı. Sıradaki domaine geçiliyor...\033[00m")
    time.sleep(32)  

with open('rapor.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Domain', 'DA', 'PR Durumu', 'TF', 'Index Sayısı', 'Spam Skoru'])
    writer.writerows(results)
    print("\033[92mRapor yazıldı.\033[00m")

driver.quit()
