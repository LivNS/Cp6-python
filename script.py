'''
Integrantes:
- Debora da Silva Amaral RM 550412
- Levy Nascimento Junior RM 98655
- Lívia Namba Seraphim RM 97819
- Mateus Iago Sousa Conceição RM 550270
- Sarah Ribeiro da Silva RM 97747
'''

import os

class Estoque:
    def __init__(self):
        self.estoque = {}

    def entrada(self, item, quantidade):
        if item in self.estoque:
            self.estoque[item] += quantidade
        else:
            self.estoque[item] = quantidade

    def saida(self, item, quantidade):
        if item in self.estoque and self.estoque[item] >= quantidade:
            self.estoque[item] -= quantidade
        else:
            print("Produto não disponível em estoque.")

    def mostrar_estoque(self):
        for item, quantidade in self.estoque.items():
            print(f"{item}: {quantidade} unidades")

def gerar_relatorio_estoque(estoque):
    nome_arquivo = "relatorio_estoque.txt"  
    diretorio_atual = os.getcwd()
    caminho_absoluto = os.path.join(diretorio_atual, nome_arquivo)

    with open(nome_arquivo, "w") as arquivo: 
        arquivo.write("** Relatório de Estoque **\n")
        for item, quantidade in estoque.estoque.items():
            arquivo.write(f"{item}: {quantidade} unidades\n")
    print(f"Relatório de estoque gerado em {nome_arquivo}")

def main():
    estoque = Estoque()

    while True:
        print("1 - Registrar entrada")
        print("2 - Registrar saída")
        print("3 - Mostrar estoque")
        print("4 - Gerar relatório de estoque")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            item = input("Digite o item: ")
            quantidade = int(input("Digite a quantidade: "))
            estoque.entrada(item, quantidade)
        elif escolha == "2":
            item = input("Digite o item: ")
            quantidade = int(input("Digite a quantidade: "))
            estoque.saida(item, quantidade)
        elif escolha == "3":
            estoque.mostrar_estoque()
        elif escolha == "4":
            gerar_relatorio_estoque(estoque)
        elif escolha == "0":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
