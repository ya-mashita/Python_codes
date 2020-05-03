import requests
from bs4 import BeautifulSoup
import re

r = requests.get('https://www.malaymail.com/')
soup = BeautifulSoup(r.content, "html.parser")
a=soup.find("ul", "prime prime-small").text
print(re.sub(r'\n+','\n',a))

from googletrans import Translator
translator = Translator()
translator.translate(a,dest='ja')
print(translator.translate(re.sub(r'\n+','\n',a),dest='ja').text)

