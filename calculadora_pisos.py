def selecionar_porcelanato(especificacoes):
    print("Selecione o tipo de porcelanato:")
    for i, tipo in enumerate(especificacoes.keys(), 1):
        print(f"{i}. {tipo}")

    opcao = int(input("Digite o número correspondente à sua escolha: "))
    tipo_selecionado = list(especificacoes.keys())[opcao - 1]

    return tipo_selecionado, especificacoes[tipo_selecionado]

def calcular_quantitativos():
    # Entradas do usuário
    largura_area = float(input("Digite a largura da área em metros: "))
    comprimento_area = float(input("Digite o comprimento da área em metros: "))
    percentual_perda = float(input("Digite o percentual de perda (%): "))

    # Seleção do tipo de porcelanato
    tipo, especificacao = selecionar_porcelanato(especificacoes)  # Passando 'especificacoes' como argumento

    # O restante do seu código...

# Executar a calculadora
calcular_quantitativos()

