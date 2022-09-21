from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import json

url1 = "https://www.upm.es/Estudiantes/Estudios_Titulaciones/EstudiosOficialesGrado"


def collect_data(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    # Starts chrome in headless mode
    driver.get(url)
    return driver.page_source
    # Gets data form url


def parse_data(data):
    soup = BeautifulSoup(data, 'lxml')
    content = soup.find('div', id='contenido')
    # Gets blocks of content
    ps = content.findAll('p', {'style': ' text-align: center;'})
    blocks = []
    for p in ps:
        block = []
        block.append(p.find('strong').text)
        block.append(p.findNext('div'))
        blocks.append(block)
        # Creates array of blocks

    grades = []

    for item in blocks:
        tds = item[1].findAll('td')
        # Finds every grade in block
        for td in tds:
            grade = {}
            grade['dir'] = item[0]
            grade['name'] = td.find('strong').text.replace('\n', '')
            grade['href'] = td.find('strong').findParent().get('href')
            grade['center'] = td.text.split('\n')[1]
            # Gets data form grades
            grades.append(grade)
            # Creates array of grades

    return grades


if __name__ == "__main__":
    data = collect_data(url1)
    grades = parse_data(data)
    json_grades = json.dumps(grades)
    with open("upm.json", 'w', encoding="utf-8") as file:
        file.write(json_grades)



