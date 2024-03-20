from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.common.action_chains import ActionChains

import os
import time
import shutil
import requests



def procesar_tomo(tomo):
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument("--headless")
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(), options=options)
    driver.set_window_size(1400,1000)
    
    url = 'https://www.onepiecemangayanime.com/mangaonline/manga.php'
    driver.get(url)
    time.sleep(5)
    
    actions = ActionChains(driver)
    
    tomo_id = f"tomo{tomo}efect"
    
    url_capitulo = "https://www.onepiecemangayanime.com/mangaonline/Visualizador/capitulos.php?Capi={id_capitulo}&Modo=1&IDM=0"
    img_src = "https://www.onepiecemangayanime.com/mangaonline/Visualizador/{src}"
    tomos_id_capitulos = dict()
    
    tomos_id_capitulos[tomo] = list()
    print(f"Procesando tomo {tomo}")
    actions.move_to_element(driver.find_element(By.ID, tomo_id)).click()
    actions.perform()
    
    time.sleep(2)
    if len(driver.window_handles) == 2:
        print("Cerrando ventanas emergentes")
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    
    tabla_capitulos = driver.find_element(By.CLASS_NAME, 'lista_de_capitulos')
    data_capisend = tabla_capitulos.find_elements(By.TAG_NAME, 'li')
    
    for capitulo in data_capisend:
        print("ID Capitulo:", capitulo.get_attribute('data-capisend'))
        tomos_id_capitulos[tomo].append(capitulo.get_attribute('data-capisend'))
    
    driver.switch_to.new_window('tab')
    for tomo, ids in tomos_id_capitulos.items():
        if not os.path.exists(f"./images/tomo_{tomo}"): 
            os.makedirs(f"./images/tomo_{tomo}") 
        for cap, id in enumerate(ids):
            if not os.path.exists(f"./images/tomo_{tomo}/capitulo_{cap}"): 
                os.makedirs(f"./images/tomo_{tomo}/capitulo_{cap}") 
            print(f"Tomo: {tomo} || Capitulo: {id}")
            print("URL:", url_capitulo.format(id_capitulo=id))
            
            driver.get(url_capitulo.format(id_capitulo=id))
            time.sleep(2)
            
            div_imgenes = driver.find_elements(By.CLASS_NAME, 'divinterno')
            for page, div in enumerate(div_imgenes):
                img_src = div.find_element(By.TAG_NAME, 'img').get_attribute('src')
                print(img_src)
                response = requests.get(img_src, stream=True)
                with open(f"./images/tomo_{tomo}/capitulo_{cap}/{page}.jpg", 'wb') as f:
                    shutil.copyfileobj(response.raw, f)
    
    
    print("FINISH TOMO:", tomo)
    driver.close()


if __name__ == '__main__':
    procesar_tomo(tomo=1)
