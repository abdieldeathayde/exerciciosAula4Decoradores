class Empregado:
    def __init__(self, nome, idade, cpf, salario, positivo):
        self._nome = nome
        self._idade = idade
        self._cpf = cpf
        self._salario = salario
        self._positivo = positivo
    
    @property
    def salario(self):
        return self._salario
    
    # @salario.setter
    # def salario(self, novo_salario):
    #     self._salario = novo_salario

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, nova_idade):
        self._idade = nova_idade
    
    @property
    def positivo(self):
        return self._positivo
    
    @positivo
    def salario(self, novo_salario):
        if self._salario > 0:
             @salario.setter
             def salario(self, novo_salario):
                self._salario = novo_salario
        try:
            self._salario = novo_salario
            raise self._salario < 0 
        except self._salario as x:
            print(x)