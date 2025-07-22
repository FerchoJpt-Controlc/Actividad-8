def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def potenciacion(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base*potenciacion(base, exponente-1)

def Menu():
    opcion = 0

    while opcion != 5:
        print("-_M E N U_-")
        print("1. Calcular el factorial")
        print("2. Suma de los primeros N números naturales")
        print("3. Calcular el n-ésimo número de Fibonacci")
        print("4. Contar cuántas veces aparece una letra en una palabra")
        print("5. Invertir una cadena de texto")
        print("6. Calcular la potencia de un número")
        print("7. SALIR")

        opcion_input = input("\nIngrese su opción: ")
        if opcion_input.isdigit():

            opcion = int(opcion_input)
            if opcion == 1:
                n=int(input("\nIngrese un numero: "))
                fac=factorial(n)
                print(factorial(n))

            elif opcion == 2:
                print("")
            elif opcion == 3:
                print("")
            elif opcion == 4:
                print("")
            elif opcion == 5:
                print("")
            elif opcion == 6:
                base=int(input("\nIngrese la base: "))
                exponente=int(input("\nIngrese el exponente: "))
                print(potenciacion(base, exponente))
            elif opcion == 7:
                print("")
            else:
                print("Opción inválida, vuelva a intentar")
        else:
            print("Error: ingreso de datos no numéricos")
            opcion = 0

        if opcion != 7:
            input("Presione ENTER para continuar...")

Menu()