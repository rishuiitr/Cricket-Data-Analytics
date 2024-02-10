from bs4 import BeautifulSoup
import requests
import time
# print(f'hello')

html_text = requests.get('https://www.espncricinfo.com/records/tournament/team-match-results/icc-cricket-world-cup-2023-24-15338')
soup = BeautifulSoup(html_text, 'lxml')

temp = soup.find_all('tbody').text