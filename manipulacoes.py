import os
import re
from docxtpl import DocxTemplate


def criar_pasta_saida(num_portaria_completo: str) -> str:
    # Usando expressão regular para capturar os números iniciais do num_portaria_completo
    resultado = re.match(r'(\d+)/IPM/CORREG/PMMS/', num_portaria_completo)
    num = 0
    if resultado:
        num =  resultado.group(1)  # Retorna apenas os números capturados

    # Caminho do arquivo main.py
    caminho_principal = os.path.dirname(os.path.abspath(__file__))

    # Nome da nova pasta, num_portaria_completo[-4:] pega o ano 2024 que fica no final de /IPM/CORREG/PMMS/2024
    nome_pasta = "IPM Portaria n " + str(num) + " " + num_portaria_completo[-4:]

    # Caminho completo para a nova pasta
    caminho_pasta = os.path.join(caminho_principal, nome_pasta)

    # Criação da pasta
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)
        print(f"Pasta '{nome_pasta}' criada com sucesso.")
    else:
        print(f"A pasta '{nome_pasta}' já existe.")
    return nome_pasta  # Retorna o nome da pasta independente dela já existir

def processar_capa(obj):
    documento = DocxTemplate("templates/A - Capa.docx")
    dados = {
        "uopm": obj["uopm"],
        "num_portaria": obj["num_portaria"],
        "data_portaria": obj["data_portaria"],
        "posto_encarregado": obj["posto_encarregado"],
        "nome_encarregado": obj["nome_encarregado"],
        "mat_encarregado": obj["mat_encarregado"],
        "postograd_investigado": obj["postograd_investigado"],
        "nome_investigado": obj["nome_investigado"],
        "mat_investigado": obj["mat_investigado"],
        "texto_finalidade": obj["texto_finalidade"]
    }
    documento.render(dados)
    nome_da_pasta = criar_pasta_saida(obj["num_portaria"])
    caminho_saida = nome_da_pasta + r"\A - Capa.docx"
    documento.save(caminho_saida)
    return None

def processar_autuacao(obj):
    # aqui processa cabeçalho, rodapé e texto interno
    documento = DocxTemplate("templates/B - Autuacao.docx")
    dados = {
        "uopm_cidade": obj["uopm_cidade"],
        "uopm_extenso": obj["uopm_extenso"],
        "num_portaria": obj["num_portaria"],
        "data_portaria": obj["data_portaria"],
        "uopm": obj["uopm"],
        "grande_comando": obj["grande_comando"],
        "uopm_extenso": obj["uopm_extenso"],
        "uopm_email": obj["uopm_email"],
        "uopm_telefone": obj["uopm_telefone"],
        "uopm_cidade": obj["uopm_cidade"],
        "uopm_endereco": obj["uopm_endereco"], #dados do cabeçalho e rodapé terminam aqui
        "posto_encarregado": obj["posto_encarregado"],
        "nome_encarregado": obj["nome_encarregado"],
        "mat_encarregado": obj["mat_encarregado"],
        "postograd_escrivao": obj["postograd_escrivao"],
        "nome_escrivao": obj["nome_escrivao"],
        "mat_escrivao": obj["mat_escrivao"],
        "postograd_investigado": obj["postograd_investigado"],
        "nome_investigado": obj["nome_investigado"],
        "mat_investigado": obj["mat_investigado"],
        "data_autuacaoextenso": obj["data_autuacaoextenso"],
    }
    documento.render(dados)
    nome_da_pasta = criar_pasta_saida(obj["num_portaria"])
    caminho_saida = nome_da_pasta + r"\B - Autuação.docx"
    documento.save(caminho_saida)
    return None

def processar_portaria_encarregado(obj):
    # aqui processa cabeçalho, rodapé e texto interno
    documento = DocxTemplate("templates\C - Portaria do encarregado.docx")
    dados = {
        "uopm_cidade": obj["uopm_cidade"],
        "uopm_extenso": obj["uopm_extenso"],
        "num_portaria": obj["num_portaria"],
        "data_portaria": obj["data_portaria"],
        "uopm": obj["uopm"],
        "grande_comando": obj["grande_comando"],
        "uopm_email": obj["uopm_email"],
        "uopm_telefone": obj["uopm_telefone"],
        "uopm_endereco": obj["uopm_endereco"],  # dados do cabeçalho e rodapé terminam aqui
        "posto_autinst": obj["posto_autinst"],
        "nome_autinst": obj["nome_autinst"],
        "func_autinst": obj["func_autinst"],
        "texto_finalidade": obj["texto_finalidade"],
        "data_autuacao": obj["data_autuacao"],
        "nome_encarregado": obj["nome_encarregado"],
        "posto_encarregado": obj["posto_encarregado"],
        "mat_encarregado": obj["mat_encarregado"]
    }

    documento.render(dados)
    nome_da_pasta = criar_pasta_saida(obj["num_portaria"])
    caminho_saida = nome_da_pasta + r"\C - Portaria do encarregado.docx"
    documento.save(caminho_saida)
    return None

def processar_designacao(obj):
    # aqui processa cabeçalho, rodapé e texto interno
    documento = DocxTemplate("templates\D - Designacao escrivao.docx")
    dados = {
        "uopm_cidade": obj["uopm_cidade"],
        "uopm_extenso": obj["uopm_extenso"],
        "num_portaria": obj["num_portaria"],
        "data_portaria": obj["data_portaria"],
        "uopm": obj["uopm"],
        "grande_comando": obj["grande_comando"],
        "uopm_email": obj["uopm_email"],
        "uopm_telefone": obj["uopm_telefone"],
        "uopm_endereco": obj["uopm_endereco"],  # dados do cabeçalho e rodapé terminam aqui
        "postograd_escrivao": obj["postograd_escrivao"],
        "nome_escrivao": obj["nome_escrivao"],
        "mat_escrivao": obj["mat_escrivao"],
        "data_autuacao": obj["data_autuacao"],
        "nome_encarregado": obj["nome_encarregado"],
        "posto_encarregado": obj["posto_encarregado"],
        "mat_encarregado": obj["mat_encarregado"]
    }
    documento.render(dados)
    nome_da_pasta = criar_pasta_saida(obj["num_portaria"])
    caminho_saida = nome_da_pasta + r"\D - Designação escrivao.docx"
    documento.save(caminho_saida)
    return None

def processar_termo_compromisso(obj):
    # aqui processa cabeçalho, rodapé e texto interno
    documento = DocxTemplate("templates\E - Termo de compromisso.docx")
    dados = {
        "uopm_cidade": obj["uopm_cidade"],
        "uopm_extenso": obj["uopm_extenso"],
        "num_portaria": obj["num_portaria"],
        "data_portaria": obj["data_portaria"],
        "uopm": obj["uopm"],
        "grande_comando": obj["grande_comando"],
        "uopm_extenso": obj["uopm_extenso"],
        "uopm_email": obj["uopm_email"],
        "uopm_telefone": obj["uopm_telefone"],
        "uopm_cidade": obj["uopm_cidade"],
        "uopm_endereco": obj["uopm_endereco"],  # dados do cabeçalho e rodapé terminam aqui
        "posto_encarregado": obj["posto_encarregado"],
        "nome_encarregado": obj["nome_encarregado"],
        "mat_encarregado": obj["mat_encarregado"],
        "postograd_escrivao": obj["postograd_escrivao"],
        "nome_escrivao": obj["nome_escrivao"],
        "mat_escrivao": obj["mat_escrivao"],
        "postograd_investigado": obj["postograd_investigado"],
        "nome_investigado": obj["nome_investigado"],
        "mat_investigado": obj["mat_investigado"],
        "data_autuacaoextenso": obj["data_autuacaoextenso"],
    }
    documento.render(dados)
    nome_da_pasta = criar_pasta_saida(obj["num_portaria"])
    caminho_saida = nome_da_pasta + r"\E - Termo de compromisso.docx"
    documento.save(caminho_saida)
    return None

def processar_despacho(obj):
    # aqui processa cabeçalho, rodapé e texto interno
    documento = DocxTemplate("templates\F - Despacho 001.docx")
    dados = {
        "uopm_cidade": obj["uopm_cidade"],
        "uopm_extenso": obj["uopm_extenso"],
        "num_portaria": obj["num_portaria"],
        "data_portaria": obj["data_portaria"],
        "uopm": obj["uopm"],
        "grande_comando": obj["grande_comando"],
        "uopm_extenso": obj["uopm_extenso"],
        "uopm_email": obj["uopm_email"],
        "uopm_telefone": obj["uopm_telefone"],
        "uopm_cidade": obj["uopm_cidade"],
        "uopm_endereco": obj["uopm_endereco"],  # dados do cabeçalho e rodapé terminam aqui
        "func_autinst": obj["func_autinst"],
        "posto_encarregado": obj["posto_encarregado"],
        "nome_encarregado": obj["nome_encarregado"],
        "mat_encarregado": obj["mat_encarregado"],
        "data_autuacao": obj["data_autuacao"],
    }
    documento.render(dados)
    nome_da_pasta = criar_pasta_saida(obj["num_portaria"])
    caminho_saida = nome_da_pasta + r"\F - Despacho 001.docx"
    documento.save(caminho_saida)
    return None

def processar_recebimento(obj):
    # aqui processa cabeçalho, rodapé e texto interno
    return None

def processar_oficio_001(obj):
    # aqui processa cabeçalho, rodapé e texto interno
    return None

def processar_oitiva_investigado(obj):
    # aqui processa cabeçalho, rodapé e texto interno
    return None

def processar_conclusao(obj):
    # aqui processa cabeçalho, rodapé e texto interno
    return None

def processar_relatorio(obj):
    # aqui processa cabeçalho, rodapé e texto interno
    return None

def processar_termo_remessa(obj):
    # aqui processa cabeçalho, rodapé e texto interno
    return None

def processar_oficio_remessa(obj):
    # aqui processa cabeçalho, rodapé e texto interno
    return None
