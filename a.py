while True:
    valorCapital = int(input("Digite o valor do seu captal:\n"))
    print("Vamos considerar uma selic de 13,25 por cento e ver quanto renderá seu captal")
    rentabilidadeBruta = valorCapital *1.1325
    print(f"Se você investir seu dinheiro na Selic no fim do ano voce terá: \n{rentabilidadeBruta}")

    faturamento = int(input("Digite o faturamento do seu negócio por um ano: \n"))
    lucroLiquido = faturamento * 0.15

    if lucroLiquido < rentabilidadeBruta-valorCapital :
        print("Você esta perdendo tempo, investe em caixinha do nuBank !")
        print(f"O seu lucro liquido é {lucroLiquido}")
    else:
        print("O negocio vai estourar na Norte !!!")
        print(f"O seu lucro liquido é {lucroLiquido}")
    resposta = input("Deseja refazer ? (s/n)")
    if resposta == "n":
        break
    else:
        print("")
