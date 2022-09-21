from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def collect_data(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(url)
    return driver.page_source

def parse_data(data):
    soup = BeautifulSoup(data, 'lxml')
    content = soup.find('div', id='contenido')
    ps = content.findAll('p', {'style': ' text-align: center;'})
    blocks = []
    for p in ps:
        block = []
        block.append(p.find('strong').text)
        block.append(p.findNext('div'))
        blocks.append(block)

    grades = []

    for item in blocks:
        tds = item[1].findAll('td')
        for td in tds:
            grade = {}
            grade['dir'] = item[0]
            grade['name'] = td.find('strong').text.replace('\n', '')
            grade['href'] = td.find('strong').findParent().get('href')
            grade['center'] = td.text.split('\n')[1]
            grades.append(grade)


    return grades


url1 = "https://www.upm.es/Estudiantes/Estudios_Titulaciones/EstudiosOficialesGrado"

data = collect_data(url1)

grades = parse_data(data)

for grade in grades:
    print(grade['name'])
    print(grade['href'])
