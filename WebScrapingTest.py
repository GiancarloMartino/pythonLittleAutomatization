# this program takes img avatar from github profiles
# app just learn some functions 



import requests, webbrowser
from bs4 import BeautifulSoup

github_user = input('Input Github user: ')
url = 'https://github.com/' + github_user

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
profile_image = soup.find('img', {'alt': 'Avatar'})['src']
webbrowser.open(profile_image)
