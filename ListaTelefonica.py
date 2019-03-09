class ListaTelefonica():

   def __init__(self):
       self.listatelefonica = []

   def Adicionar(self,numero):

       self.listatelefonica.append(numero)

   def Remover(self,numero):

       for x in self.listatelefonica:
           if x.numero == numero:
               self.listatelefonica.remove(x)



   def BuscarNome(self,nomeinput):

       achados = 0

       for x in self.listatelefonica:
           if x.nome == nomeinput:
               achados = achados + 1
               x.SelfPrint()
       print("Foram encontrados ",achados,"elementos com esse nome.")

   def SelfPrint(self):

       for x in self.listatelefonica:
           x.SelfPrint()
       return



class Numero():
   def __init__(self,nome,numero):
       self.nome = nome
       self.numero = numero


   def SelfPrint(self):
       print("Nome: ",self.nome,"------ Telefone: ",self.numero,)
       return



class Menu():

   def __init__(self):
       self.lista = ListaTelefonica()

   def MenuControl(self,x):

       self.lista.SelfPrint()

       while x != "5":
           if x == "1":
               self.lista.Adicionar(self.AddElemento())

           elif x == "2":
               self.lista.Remover(self.RemElemento())

           elif x == "3":
               self.lista.BuscarNome(self.BuscarElemento())
           elif x == "4":
               self.lista.SelfPrint()


           x = self.MenuShow()

   def MenuShow(self):
       return input("1 - Adicionar Elemento\n 2- Excluir Elemento\n 3- Buscar Elemento\n 4- Mostrar Elementos\n 5- Sair\n\n")

   def AddElemento(self):
       while True:
           nom = input("Digite o nome do contato: ")
           nume = input("Digite o número de telefone: ")
           elemento = Numero(nom,nume)

           return elemento

   def RemElemento(self):
       while True:

           num = input("Digite o numero do contato para remover: ")

           return num

   def BuscarElemento(self):

       while True:
           nome = input("Digite o nome da pessoa que deve ser encontrada: ")

           return nome




menu = Menu()
menu.MenuControl(menu.MenuShow())




