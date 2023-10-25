from bs4 import BeautifulSoup
import requests

def webScrape():
    # website = 'https://subslikescript.com/movie/Titanic-120338'
    root = 'https://subslikescript.com'
    website = f'{root}/movies_letter-A'
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    #print(soup.prettify())

    #pagination
    pagination = soup.find('ul', class_='pagination')
    pages = pagination.find_all('li', class_='page-item')
    last_page = pages[-2].text

    links = []
    for page in range(1, int(last_page)+1)[:2]:

        result = requests.get(f'{website}?page={page}')
        content = result.text
        soup = BeautifulSoup(content, 'lxml')

        box = soup.find('article', class_='main-article')


        for link in box.find_all('a', href=True):
            links.append(link['href'])

        print(links)

        for link in links:
            try:
                result = requests.get(f'{root}/{link}')
                content = result.text
                soup = BeautifulSoup(content, 'lxml')

                box = soup.find('article', class_='main-article')

                title = box.find('h1').get_text()
                # print(title)

                transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
                # print(transcript)
                with open(f'{title}.txt', 'w', encoding='utf-8') as file:
                    file.write(transcript)
            except:
                #if one link is not working go to the next link
                print("----------Link not working-----------")
                print(link)
                pass



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    webScrape()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
