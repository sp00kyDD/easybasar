from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

# Parameter
path = r"C:\ProgramData\chocolatey\lib\chromedriver\tools\chromedriver-win32\chromedriver.exe"
url = [
    'https://www.easybasar.de/einloggen',
    'https://www.easybasar.de/artikel-erfassen'
]
myuser = "test@test.de"
mypass = "test"
mycsv = "test_basar_2024.csv"
# Important! File ANSI coded and without special chars

# Service
cservice = webdriver.ChromeService(path)
cdriver = webdriver.Chrome(service=cservice)
cdriver.get(url[0])
time.sleep(5)
print(cdriver.title)

# Login
alert = cdriver.find_element(by=By.XPATH, value='/html/body/div[5]/div/a[1]')
alert.click()

username = cdriver.find_element(by=By.ID, value='username')
password = cdriver.find_element(by=By.ID, value='password')
login = cdriver.find_element(by=By.XPATH, value='//*[@id="tm-content"]/div[2]/form/fieldset/div[4]/div/button')
username.send_keys(myuser)
password.send_keys(mypass)
login.click()

# Items
cdriver.get(url[1])
time.sleep(5)
print(cdriver.title)

print(cdriver.find_element(by=By.ID, value='basar_name').text)
print(cdriver.find_element(by=By.ID, value='basar_owner').text)
print(cdriver.find_element(by=By.ID, value='seller_chiffre').text)
print(cdriver.find_element(by=By.ID, value='seller_name').text)

size = cdriver.find_element(by=By.ID, value='Größe')
color = cdriver.find_element(by=By.ID, value='Farbe')
brand = cdriver.find_element(by=By.ID, value='Marke')
desc = cdriver.find_element(by=By.ID, value='Beschreibung')
price = cdriver.find_element(by=By.ID, value='price')
submit = cdriver.find_element(by=By.ID, value='article_submit')

# Test
#size.clear()
#size.send_keys('80')
#color.clear()
#color.send_keys('beige')
#brand.clear()
#brand.send_keys('Coolclub')
#desc.clear()
#desc.send_keys('Latzhose')
#price.clear()
#price.send_keys('1,5')
#time.sleep(1)
#submit.click()

# CSV
with open(mycsv) as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE)

    for row in csvreader:
        print(row)
        size.clear()
        size.send_keys(row['Groesse'])
        color.clear()
        color.send_keys(row['Farbe'])
        brand.clear()
        brand.send_keys(row['Marke'])
        desc.clear()
        desc.send_keys(row['Beschreibung'])
        price.clear()
        price.send_keys(row['Preis'])
        time.sleep(1)
        submit.click()
        time.sleep(2)

# Logout
cdriver.close()
