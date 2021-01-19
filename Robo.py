
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


print("Configurando navegador")
option = Options()
option.headless = True
fp = webdriver.FirefoxProfile()
driver = webdriver.Firefox(firefox_profile=fp, options=option)
print("Executando...")
driver.close()