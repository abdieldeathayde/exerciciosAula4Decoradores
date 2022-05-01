class calculadora:
    import time    
    x = 5
    y = ' '    
    while (x != 0):
        x = int(input('Digite o numero da operação \n 0 - Sair \n 1 - Soma \n 2 - Subtração \n 3 - Divisão \n 4 - Multiplicação ')) 
        
        a = int(input('Digite um numero: '))
        b = int(input('Digite outro número: '))
    
        def __init__(self, a , b):
            self._a = a
            self._b = b
            
        
        @property
        def numero1(self):
            return self._a
        
        # @a.setter
        # def numero1(self, novo_numero):
        #     self._a = novo_numero
        
        @property
        def numero2(self):
            return self._b
        
        # @b.setter
        # def numero2(self, numero_novo):
        #     self._b = numero_novo
            
       
        # @tipo_requerido
        def tipo_requerido(a,b):
                if a > 0 and isinstance(a, int) and b > 0 and isinstance(b, int):
                    print('Sim, você está usando um inteiro')
                else:
                    assert "invalido", "Precisa ser inteiro"
                
        
        
        inicio = time.time() 
        
        def soma( a, b):
            return a + b
        
        fim = time.time()
        
        def subtrai(a, b):
            return a - b
        
        def divide(a, b):
            return a / b
        
        def multiplica(a, b):
            return a * b
    
        if x < 0:
            assert y == "negativo", "Digite uma opção valida"
        if x == 1:
            i = soma(a,b)
            print(i)
            print(fim - inicio)
        elif x == 2 : 
            i = subtrai(a,b)
            print(i)
        elif x == 3:
            i = divide(a,b)
            print(i)
        elif x == 4:
            i = multiplica(a,b)
            print(i)
        else:
            assert y == 'invalido', "Digite uma opcao valida"