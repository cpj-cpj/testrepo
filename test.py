#adding a url
!mamba install bs4==4.10.0 -y
!pip install lxml==4.6.4
!mamba install html5lib==1.1 -y

from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page

url = "https://labs.cognitiveclass.ai/v2/tools/jupyterlab?ulid=ulid-ec44233a5e2eba03be46c7f0f3a3a99b836ddc1b'
assignment = BeautifulSoup(url, "html.parser")


print(soup.prettify())
