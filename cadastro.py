def obter_nome_produto():
    return input("Digite o nome do produto: ")

def obter_preco_produto():
    return float(input("Digite o preço do produto (R$): "))

def obter_quantidade_produto():
    return int(input("Digite a quantidade em estoque: "))

def main():
    nome = obter_nome_produto()
    preco = obter_preco_produto()
    quantidade = obter_quantidade_produto()
    print(f"Produto: {nome} - Preço: R$ {preco:.2f} - Quantidade: {quantidade}")

if __name__ == "__main__":
    main()
