import pyautogui as py
from time import sleep
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pyperclip as pc

contatos = 'Johnny Vivo'

# TEXTO DO DIA
url = 'https://wol.jw.org/pt/wol/h/r5/lp-t'

option = Options()
option.headless = True
#driver = webdriver.Chrome(options=option)   # NAVEGADOR OFF
driver = webdriver.Chrome(r'C:\Program Files\chromedriver\chromedriver.exe')                  # NAVEGADOR ON
driver.get(url)

textocompl = driver.find_element_by_xpath('//*[@id="dailyText"]/div[2]').text[0:300] 
#textocompl = driver.find_element_by_xpath('//*[@id="dailyText"]/div[2]').text[0:300]
driver.quit()


# ABRIR NAVEGADOR
#py.click(152,746)           # PC Trabalho
py.click(384, 1062)          # PC HOME
sleep(3)

# DIGITAR WEB.WHATSAPP 
#py.click(319,64)            # PC WORK
py.click(201,51)            # PC HOME 
sleep(3) 
py.typewrite('https://web.whatsapp.com\n') 
sleep(35)

# COPIAR TEXTO E COLAR
pc.copy(textocompl)
#py.click(80,274)
py.click(365,293)
py.typewrite(contatos,interval=0.3)
py.press('enter') 
sleep(3) 
py.typewrite('>>> *_TEXTO DO DIA_* <<<\n', interval=0.3)
sleep(2)
py.hotkey('ctrl','v')
sleep(2)
py.typewrite(' (...)', interval=0.3)
py.press('enter')
sleep(2)
py.typewrite('_Para continuar, clique abaixo e leia diretamente no site_ https://wol.jw.org/pt/wol/h/r5/lp-t\n', interval=0.3)
sleep(2)
# FECHAR NAVEGADOR
#py.click(1340,8)
py.click(1896,10)
sleep(2)
py.press('enter')