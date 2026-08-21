def main():
    """
    Verificar si un número es múltiplo de 3 y 5
    """

    numero = int(input("Ingrese un número:"))

    print(numero % 3 == 0 and numero % 5 == 0)

if __name__=='__main__':
    main()
