def obter_nome_produto():
    return input("Digite o nome do produto: ")

def main():
    nome = obter_nome_produto()
    print(f"Produto cadastrado: {nome}")

if __name__ == "__main__":
    main()
