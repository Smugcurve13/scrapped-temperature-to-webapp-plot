import requests
import selectorlib
import datetime
import time

URL = 'http://programmer100.pythonanywhere.com/'

def get_date_temp():
    def scrape(url):
        response = requests.get(url)
        source = response.text
        return source


    def extract(source):
        extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
        value = extractor.extract(source)['temp']
        return value
    

    def store(extracted):
        now = datetime.datetime.now()
        fnow = now.strftime("%y-%m-%d-%H-%M-%S")
        with open("data.txt",'a') as file:
            file.write(f'\n{fnow},{extracted}')  

    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        store(extracted)
        time.sleep(2)

if __name__ == "__main__":
    print("dont")     
