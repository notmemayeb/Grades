from bs4 import BeautifulSoup

def parse_upm(data):
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






