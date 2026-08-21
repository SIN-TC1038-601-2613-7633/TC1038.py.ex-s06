def main():
    """
    Comparar edades de tres personas para verificar si la primer persona es la más joven
    """

    edad1 = int(input("Edad de la primer persona:"))
    edad2 = int(input("Edad de la segunda persona:"))
    edad3 = int(input("Edad de la tercer persona:"))
        
    print(edad1 < edad2 and edad1 < edad3)

if __name__=='__main__':
    main()
