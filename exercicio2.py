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