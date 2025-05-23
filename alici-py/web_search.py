from duckduckgo_search import DDGS


def buscar_na_web(pergunta):
	try:
		print("Pesquisando no DuckDuckGo...")
		with DDGS() as ddgs:
			resultados = ddgs.text(
				pergunta,
				region="br-pt",
				safesearch="Moderate",
				timelimit="d",
				max_results=3
			)
			
			for resultado in resultados:
				titulo = resultado.get("title", "").strip()
				descricao = resultado.get("body", "").strip()
				link = resultado.get("href", "").strip()
				
				if descricao:
					resposta = f"{descricao}"
					if link:
						resposta += f"\n(Fonte: {link})"
					return resposta
		
		return "Desculpe, não encontrei nada relevante na web."
	
	except Exception as e:
		print("Erro na busca na web:", e)
		return "Desculpe, não consegui buscar na web no momento."
