# 1 questao
class Comodo:
    def __init__(self, nome, area):
        self.nome = nome
        self.area = area

    def get_nome(self):
        return self.nome

    def get_area(self):
        return self.area

class Residencia:
    def __init__(self):
        self.comodos = []

    def adicionar_comodo(self, nome, area):
        comodo = Comodo(nome, area)
        self.comodos.append(comodo)
        print(f"Comodo {nome} adicionado com sucesso!")

    def calcular_area_total(self):
        total = 0.0
        for comodo in self.comodos:
            total += comodo.get_area()
        return total

    def listar_comodos(self):
        if not self.comodos:
            print(f"Nenhum comodo cadastrado nesta residencia!")
            return

        print("\n--- COMODOS DA RESIDENCIA ---")
        for comodo in self.comodos:
            print(f"Nome: {comodo.get_nome()}, Area: {comodo.get_area()} m²")
        print("------------------------\n")


#Menu
residencia = None

opcao = ""
while opcao != "0":
  print("=== MENU RESIDENCIA ===")
  print("1 - Criar nova residencia")
  print("2 - Adicionar comodo")
  print("3 - Visualizar comodo")
  print("4 - Calcular area total")
  print("0 - Sair")
  opcao = input("Escolha uma opcao: ")

  if opcao == "1":
      residencia = Residencia()
      print("Nova residencia criada com sucesso!")

  elif opcao == "2":
      if residencia is None:
          print("Crie uma residencia antes de adicionar um comodo.")
      else:
          nome = input("Digite o nome do comodo: ")
          area = float(input("Digite a area do comodo em m² (apenas numeros): "))
          residencia.adicionar_comodo(nome, area)

  elif opcao =="3":
      if residencia is None:
          print("Crie uma residencia antes de visualizar comodo.")
      else:
          residencia.listar_comodos()

  elif opcao =="4":
      if residencia is None:
         print("Crie uma residencia antes de calcular area total.")
      else:
         total = residencia.calcular_area_total()
         print(f"Area total da residencia: {total:.2f} m²")

  elif opcao =="0":
      print("Saindo...")

  else:
      print("Opcao invalida, tente novamente.")