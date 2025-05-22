# web_search.py

import requests
from bs4 import BeautifulSoup


def buscar_na_web(pergunta):
	try:
		query = pergunta.replace(" ", "+")
		url = f"https://www.google.com/search?q={query}"
		headers = {"User-Agent": "Mozilla/5.0"}
		
		response = requests.get(url, headers=headers)
		soup = BeautifulSoup(response.text, "html.parser")
		
		resposta = soup.find("div", class_="BNeawe").text
		return resposta if resposta else "Não encontrei nada relevante na web."
	except Exception as e:
		return "Não consegui buscar na web no momento."
