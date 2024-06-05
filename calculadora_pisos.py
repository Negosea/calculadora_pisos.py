def selecionar_porcelanato(especificacoes):
    print("Selecione o tipo de porcelanato:")
    for i, tipo in enumerate(especificacoes.keys(), 1):
        print(f"{i}. {tipo}")

    opcao = int(input("Digite o número correspondente à sua escolha: "))
    tipo_selecionado = list(especificacoes.keys())[opcao - 1]

    return tipo_selecionado, especificacoes[tipo_selecionado]

def calcular_quantitativos(especificacoes):
    # Entradas do usuário
    largura_area = float(input("Digite a largura da área em metros: "))
    comprimento_area = float(input("Digite o comprimento da área em metros: "))
    percentual_perda = float(input("Digite o percentual de perda (%): "))

    # Seleção do tipo de porcelanato
    tipo, especificacao = selecionar_porcelanato(especificacoes)

    # Cálculo dos quantitativos
    area_total = largura_area * comprimento_area
    area_por_caixa = especificacao["area_por_caixa"]
    pecas_por_caixa = especificacao["pecas_por_caixa"]
    consumo_argamassa = especificacao["consumo_argamassa"]
    consumo_rejunte = especificacao["consumo_rejunte"]
    argamassa_por_saco = especificacao.get("argamassa_por_saco", None)  # Adicionado para obter argamassa por saco

    quant_caixas = (area_total * (1 + percentual_perda / 100)) / area_por_caixa
    quant_pecas = quant_caixas * pecas_por_caixa
    argamassa_total = consumo_argamassa * area_total
    rejunte_total = consumo_rejunte * area_total

    if argamassa_por_saco is not None:
        sacos_argamassa = argamassa_total / argamassa_por_saco
        print(f"\nQuantidade de sacos de argamassa necessários: {sacos_argamassa:.2f}")
    else:
        print("\nNão foi possível calcular a quantidade de argamassa necessária. Especificação não encontrada.")

    # Exibindo os resultados
    print(f"Quantidade de caixas necessárias: {quant_caixas:.2f}")
    print(f"Quantidade de peças necessárias: {quant_pecas:.2f}")
    print(f"Quantidade de argamassa necessária: {argamassa_total:.2f} kg")
    print(f"Quantidade de rejunte necessária: {rejunte_total:.2f} kg")

# Defina o dicionário 'especificacoes' com mais opções de fabricantes
especificacoes = {
    "Portobello 60x60": {
        "fabricante": "Portobello",
        "dimensoes": (60, 60),  # em cm
        "pecas_por_caixa": 4,
        "area_por_caixa": 1.44,  # em m²
        "consumo_argamassa": 4,  # em kg/m²
        "consumo_rejunte": 0.5,  # em kg/m²
        "argamassa_por_saco": 25,  # em m² por saco
        "uso": "Residencial",
        "resistencia": "Alta"
    },
    "Portobello 80x80": {
        "fabricante": "Portobello",
        "dimensoes": (80, 80),
        "pecas_por_caixa": 3,
        "area_por_caixa": 1.92,
        "consumo_argamassa": 4,
        "consumo_rejunte": 0.5,
        "argamassa_por_saco": 25,  # em m² por saco
        "uso": "Residencial",
        "resistencia": "Alta"
    },
    "Eliane 60x60": {
        "fabricante": "Eliane",
        "dimensoes": (60, 60),
        "pecas_por_caixa": 4,
        "area_por_caixa": 1.44,
        "consumo_argamassa": 4,
        "consumo_rejunte": 0.5,
        "argamassa_por_saco": 30,  # em m² por saco
        "uso": "Comercial",
        "resistencia": "Média"
    },
    "Eliane 90x90": {
        "fabricante": "Eliane",
        "dimensoes": (90, 90),
        "pecas_por_caixa": 3,
        "area_por_caixa": 2.43,
        "consumo_argamassa": 4,
        "consumo_rejunte": 0.5,
        "argamassa_por_saco": 30,  # em m² por saco
        "uso": "Comercial",
        "resistencia": "Média"
    },
    "Ceusa 60x60": {
        "fabricante": "Ceusa",
        "dimensoes": (60, 60),
        "pecas_por_caixa": 4,
        "area_por_caixa": 1.44,
        "consumo_argamassa": 4,
        "consumo_rejunte": 0.5,
        "argamassa_por_saco": 28,  # em m² por saco
        "uso": "Residencial",
        "resistencia": "Alta"
    },
    "Ceusa 80x80": {
        "fabricante": "Ceusa",
        "dimensoes": (80, 80),
        "pecas_por_caixa": 3,
        "area_por_caixa": 1.92,
        "consumo_argamassa": 4,
        "consumo_rejunte": 0.5,
        "argamassa_por_saco": 28,  # em m² por saco
        "uso": "Residencial",
        "resistencia": "Alta"
    }
    # Adicione mais especificações de diferentes fabricantes e dimensões conforme necessário
}

# Executar a calculadora
calcular_quantitativos(especificacoes)


