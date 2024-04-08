# Funções decoradoras e decoradores com classes

def add_repr(cls):
    def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'({class_name} {class_dict})'
        return class_repr
    cls.__rerpr__ = meu_repr
    return cls


def meu_planeta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)

        if resultado == 'Terra':
            return 'Você está em casa.'
        return resultado
    return interno



@add_repr
class Time():
    def __init__(self, nome):
        self.nome = nome



@add_repr
class Planeta():
    def __init__(self, nome):
        self.nome = nome

    @meu_planeta
    def falar_nome(self):
        return f'O planeta é {self.nome}'