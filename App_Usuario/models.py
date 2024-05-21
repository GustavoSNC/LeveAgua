#Bibliotecas
from django.db import models


# Criando classe generalizada (Usuário)
class Modelo_Usuario(models.Model):
    Nome = models.CharField(max_length=50)
    Sobrenome = models.CharField(max_length=100)
    Email = models.EmailField(max_length=200)
    Senha = models.CharField()
    CPF = models.IntegerField(14)
    Data_De_Nascimento = models.DateField()

    class Meta:
        abstract = True  # Define o modelo como abstrato para evitar criação de tabela no banco de dados

# Criando classe filho (Cliente)
class Modelo_Cliente(Modelo_Usuario):
    ID = models.AutoField(primary_key=True)
    Endereco = models.OneToOneField("Modelo_Endereco", on_delete=models.CASCADE)

# Criando classe filho (Administrador)
class Modelo_Administrador(Modelo_Usuario):
    ID = models.AutoField(primary_key=True)

# Criando classe Endereço | Diretemente ligada com o cliente (indica sua propriedade)
class Modelo_Endereco(models.Model):
    ID = models.AutoField(primary_key=True)
    
    # Definição de Municipio (choices)
    Guanambi = "Guanambi"
    Escolha_Municipio = {
        Guanambi: "Guanambi"
    }
    Municipio = models.CharField(max_length=50, choices=Escolha_Municipio, default="Guanambi")

    # Definição de Distrito (choices)
    if(Municipio == "Guanambi"):
        Ceraima = "Ceraima"
        Escolha_Distrito = {
            Ceraima: "Ceraima"
        }
    Distrito = models.CharField(max_length=50, choices=Escolha_Distrito, default="Ceraima")

    # Definição de CEP
    if(Distrito == "Ceraima"):
        CEP = "46430-000" #CEP de Ceraima

    Nome_Da_Propriedade = models.CharField(max_length=100)
    Complemento = models.TextField(max_length=50)
    Imagens = models.ImageField(upload_to='Arquivos_Static/Imagens_ModeloEndereco')
