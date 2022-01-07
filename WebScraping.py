import requests
from bs4 import BeautifulSoup

# Usando URL do site para encontrar a versao mais recente
URL = "https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

result = soup.find(id="parent-fieldname-text")
elements = result.find_all("a", class_="alert-link internal-link")

# Procurando o link do pdf
URL_new = elements[0].attrs["href"]
page_new = requests.get(URL_new)
soup_new = BeautifulSoup(page_new.content, "html.parser")

result_new = soup_new.find(id="parent-fieldname-text")
elements_new = result_new.find_all("a", class_="btn btn-primary btn-sm center-block internal-link")

# Baixando pdf pela URL
URL_pdf = elements_new[0].attrs["href"]
page_pdf = requests.get(URL_pdf, allow_redirects=True)

open('padrao.pdf', 'wb').write(page_pdf.content)