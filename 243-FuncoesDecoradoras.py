# Esta função estará fazendo o papel de um decorador para Classes;
# Por isso ele recebe como parâmetro 'cls', para que ele possa alterar a classe em sí.
# Dito isso, na função interna, ele recebe self como forma de manipulação dos atributos internos da classe.

def add_repr(cls):
    def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'({class_name} {class_dict})'
        return class_repr
    cls.__rerpr__ = meu_repr
    return cls

# Neste segundo exemplo; É criado uma função 'decoradora' que vai receber um método de uma classe dentro de sí;
# Em sua função interna ele recebe os parâmetros do método 'self, *args, **kwargs' podendo agora ter acesso ao resultado
# da alteração e podendo manipular a saída do método da classe.

def meu_planeta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)

        if resultado == 'Terra':
            return 'Você está em casa.'
        return resultado
    return interno


# Aplicando o decorador de Classe: 
@add_repr
class Time():
    def __init__(self, nome):
        self.nome = nome



@add_repr
class Planeta():
    def __init__(self, nome):
        self.nome = nome
        
# Aplicando o decorador de métodos: 
    @meu_planeta
    def falar_nome(self):
        return f'O planeta é {self.nome}'
