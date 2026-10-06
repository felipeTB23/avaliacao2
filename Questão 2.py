# 2° Questao

class Produto:
    def __init__(self, nome, preco, descricao, quantidade):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.quantidade = quantidade

    def get_nome(self):
        return self.nome

    def get_preco(self):
        if self.preco >= 0:
            return self.preco
            return 0.0

    def get_descricao(self):
        return self.descricao

    def get_quantidade(self):
        if self.quantidade >= 0:
            return self.quantidade
        return 0

class Carrinho_de_Compras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print(f"Produto {produto.get_nome()} adicionado ao carrinho!")

    def remover_produto(self, nome_produto):
        achou = False
        for produto in self.produtos:
            if produto.get_nome() == nome_produto:
                self.produtos.remove(produto)
                print(f"Produto {nome_produto} removido com sucesso!")
                achou = True
                break
        if not achou:
            print(f"Produto {nome_produto} nao encontrado no carrinho!")

    def calcular_total(self):
         total = 0.0
         for produto in self.produtos:
             total += produto.get_preco() * produto.get_quantidade()
         return total

    def exibir_carrinho(self):
        if not self.produtos:
          print("Carrinho esta vazio.")
          return

        print("---ITENS NO CARRINHO---")
        subtotal = 0.0
        for produto in self.produtos:
            print(f"Nome: {produto.get_nome()}")
            print(f"Preco: R$ {produto.get_preco():.2f}")
            print(f"Descricao: {produto.get_descricao()}")
            print(f"Quantidade: {produto.get_quantidade()}")
            item_total = produto.get_preco() * produto.get_quantidade()
            subtotal += item_total
            print(f"Subtotal deste item: R$ {item_total:.2f}")
            print("-" * 24)
        print(f"TOTAL DO CARRINHO: R$ {self.calcular_total():.2f}\n")


#Menu
carrinho = Carrinho_de_Compras()

opcao = ""
while opcao != "0":
  print("=== MENU CARRINHO ===")
  print("1 - Adicionar produto")
  print("2 - Remover produto")
  print("3 - Exibir carrinho")
  print("4 - Ver total da compra")
  print("0 - Sair")
  opcao = input("Escolha uma opcao: ")

  if opcao == "1":
      nome = input("Digite o nome do produto: ")
      preco = float(input("Digite o preco do produto: "))
      descricao = input("Digite a descricao do produto: ")
      quantidade = int(input("Digite a quantidade do produto: "))
      produto = Produto(nome, preco, descricao, quantidade)
      carrinho.adicionar_produto(produto)

  elif opcao =="2":
      nome_remover = input("Digite o nome do produto que deseja remover: ")
      carrinho.remover_produto(nome_remover)

  elif opcao =="3":
      carrinho.exibir_carrinho()

  elif opcao =="4":
      total = carrinho.calcular_total()
      print(f"Total da compra: R$ {total:.2f}")

  elif opcao =="0":
      print("Saindo...")

  else:
      print("Opcao invalida, tente novamente.")
