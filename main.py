from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from upm import parse_upm
import json


url_upm = "https://www.upm.es/Estudiantes/Estudios_Titulaciones/EstudiosOficialesGrado"


chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get(url_upm)
upm_data = driver.page_source



def create_json(univers_name, data, parse_data_func):
    grades = parse_data_func(data)
    json_grades = json.dumps(grades)
    with open(f'{univers_name}.json', 'w', encoding="utf-8") as file:
        file.write(json_grades)

if __name__ == "__main__":
    create_json('upm', upm_data, parse_upm)