def imprimir(string):
    if len(string) != 0:
        imprimir(string[1:])
        print(string[0], end='')
        
imprimir('Hola Mundo!'[::-1])
