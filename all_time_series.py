import requests
from bs4 import BeautifulSoup


r = float(input("What's the minimum rate that you're looking for ?"))

url = "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"
response = requests.get(url)

html_content = response.content

soup = BeautifulSoup(html_content,"html.parser")

series = soup.find_all("td",{"class":"titleColumn"})
rates = soup.find_all("td",{"class":"ratingColumn imdbRating"})

for serie,rate in zip(series,rates):
    serie = serie.text
    rate = rate.text

    serie = serie.strip()
    serie = serie.replace("\n","")

    rate = rate.strip()
    rate = rate.replace("\n","")

    if float(rate)>r:
        print(f"Serie:{serie} Rate:{rate}")
  
print("\nIMDB DATA FETCHED SUCCESSFULLY...\n")
    
