import re
from datetime import datetime

def so_digitos(texto):
    """
    Retorna uma string contendo apenas os dígitos do texto fornecido.

    Parâmetros:
    texto (str): A string de entrada da qual os dígitos serão extraídos.

    Retorna:
    str: Uma string contendo apenas os dígitos encontrados no texto.
    """
    return re.sub(r"\D", "", texto)

def normaliza_nome(nome):
    """
    Normaliza um nome, removendo espaços extras e convertendo para título.

    Parâmetros:
    nome (str): O nome a ser normalizado.

    Retorna:
    str: O nome normalizado.
    """
    return ' '.join(nome.split()).title()

def converte_data(texto):
    """
    Converte uma data no formato 'dd/mm/aaaa' para o formato 'aaaa-mm-dd'.

    Parâmetros:
    data_str (str): A string de data no formato 'dd/mm/aaaa'.
    
    Retorna:
    str: A data convertida para o formato 'aaaa-mm-dd'.
    """
    return datetime.strptime(texto, "%d/%m/%Y").strftime("%Y-%m-%d")


if __name__ == "__main__":
    print(so_digitos("(48) 991055515"))       
    print(normaliza_nome("  ana   SOUZA ")) 
    print(converte_data("15/08/2023"))  