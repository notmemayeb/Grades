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
# Starts chrome driver in headless mode

def get_data(url, univers_name):
    print(f'Getting data from {univers_name}...')
    driver.get(url)
    # Driver goes to *url*
    print('Done!')
    return driver.page_source

def create_json(univers_name, data, parse_data_func):
    print(f'Parsing {univers_name} data...')
    grades = parse_data_func(data)
    print(f'Creating {univers_name}.json...')
    json_grades = json.dumps(grades)
    with open(f'{univers_name}.json', 'w', encoding="utf-8") as file:
        file.write(json_grades)
    print(f'Done! Look for {univers_name}.json')
    # Dumps data to json and saves it in $university_name.json



def main():
    create_json('upm', get_data(url_upm, 'upm'), parse_upm)

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(exc)