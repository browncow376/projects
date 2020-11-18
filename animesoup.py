import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

# request url
url = 'https://www3.animepace.si/'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}

df = pd.DataFrame(columns=('Date', 'Title', 'Time'))

# get response
def check_time():
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    dates = soup.find_all("h4")
    titles = soup.find_all("td", class_="schedule")
    times = soup.find_all("td", class_="schedule-time")

    i=0
    temp=0
    date = iter(dates)
    pdate = next(date)
    for title, time in zip(titles, times):
        if(float(time.get_text().replace(':','')) < temp):
            pdate = next(date)
        df.loc[i] = [pdate, title.get_text(), time.get_text()]
        temp = float(time.get_text().replace(':',''))
        i+=1
   

   
check_time()
print(df)



