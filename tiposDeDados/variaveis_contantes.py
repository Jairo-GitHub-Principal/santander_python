nome = "jairo"

idade = 20


class GeneroMasculino: # uma forma de tornar uma nome imutavel 
   

    def __init__(self):
         self._GENERO = "masculino"

    @property
    def genero(self):
         return self._GENERO
    
# o retorno do .genero sera imutavel, porem a constante GENERO ainada  pode ser alterada
GENERO = GeneroMasculino().genero  # o nome em maiúsculo é uma constante, porem ele apenas informa oa programador que não pode ser mudado,
                     # mais o python não impede a mudança como em outras linguagens, caso os programador tente muda-lo


print(f"nome: {nome} idade: {idade} genero: {GENERO}")  