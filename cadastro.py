def obter_nome_produto():
    return input("Digite o nome do produto: ")

def obter_preco_produto():
    return float(input("Digite o preço: "))

def main():
    nome = obter_nome_produto()
    preco = obter_preco_produto()
    print(f"Produto: {nome} - Preço: R$ {preco:.2f}")

if __name__ == "__main__":
    main()
