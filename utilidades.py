import datetime
import re
from datetime import datetime


def validar_data_padrao_br(text: str) -> bool:
    """
    :param text: Texto que será avaliado para o padrão dd/mm/aaaa
    :return: True caso o texto esteja no padrão, False caso não esteja no padrão
    """
    # Expressão regular para o formato "dd/mm/aaaa"
    pattern = r'^\d{0,2}(/)?\d{0,2}(/)?\d{0,4}$'
    if re.match(pattern, text):
        return True
    return False

def get_data_extenso(data: str) -> str:
    """
    Converte uma data no formato 'dd/mm/aaaa' para o formato por extenso, como 'vinte e sete de outubro de dois mil e vinte e quatro'.
    :param data (str): Data no formato 'dd/mm/aaaa'.
    :return: Data por extenso.
    """
    dias = {
        '1': 'um', '2': 'dois', '3': 'três', '4': 'quatro', '5': 'cinco',
        '6': 'seis', '7': 'sete', '8': 'oito', '9': 'nove', '10': 'dez',
        '11': 'onze', '12': 'doze', '13': 'treze', '14': 'quatorze', '15': 'quinze',
        '16': 'dezesseis', '17': 'dezessete', '18': 'dezoito', '19': 'dezenove', '20': 'vinte',
        '21': 'vinte e um', '22': 'vinte e dois', '23': 'vinte e três', '24': 'vinte e quatro',
        '25': 'vinte e cinco', '26': 'vinte e seis', '27': 'vinte e sete', '28': 'vinte e oito',
        '29': 'vinte e nove', '30': 'trinta', '31': 'trinta e um'
    }

    meses = {
        '01': 'janeiro', '02': 'fevereiro', '03': 'março', '04': 'abril',
        '05': 'maio', '06': 'junho', '07': 'julho', '08': 'agosto',
        '09': 'setembro', '10': 'outubro', '11': 'novembro', '12': 'dezembro'
    }

    def ano_por_extenso(ano: int) -> str:
        """Converte o ano para o formato por extenso."""
        unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
        dezenas = ["", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
        centenas = ["", "cem", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos",
                    "oitocentos", "novecentos"]
        ano_str = str(ano)

        ano_extenso = "dois mil" + (f" {centenas[int(ano_str[1])]}" if ano_str[1] != "0" else "") \
                      + (f" e {dezenas[int(ano_str[2])]}" if ano_str[2] != "0" else "") \
                      + (f" e {unidades[int(ano_str[3])]}" if ano_str[3] != "0" else "")

        return ano_extenso.strip()

    try:
        data_obj = datetime.strptime(data, "%d/%m/%Y")
    except ValueError:
        raise ValueError("Formato de data inválido. Use 'dd/mm/aaaa'.")

    dia = dias[str(data_obj.day)]
    mes = meses[data_obj.strftime('%m')]
    ano = ano_por_extenso(data_obj.year)

    return f"{dia} de {mes} de {ano}"


# Função para converter a data
def get_data_semi_extenso(data_str: str) ->str :
    """
    Função que recebe 28/10/2024 e retorna 28 de setembro de 2024 para fechos de ofícios
    :param data_str: Data no formato 28/10/2024
    :return: 28 de dezembro de 2024
    """
    # Converter a string de data para um objeto datetime
    data = datetime.strptime(data_str, '%d/%m/%Y')
    # Formatando a data no formato desejado
    data_formatada = data.strftime('%d de %B de %Y')
    return data_formatada
