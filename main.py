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

def SumaNnumerosNa(n):
    if n ==0:
        return 1
    else:
        return n*SumaNnumerosNa(n-1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def contarLetra(palabra,letra):
    if len(palabra)==0:
        return 0
    elif palabra[0]==letra:
        return 1+contarLetra(palabra[1:],letra)
    else:
        return contarLetra(palabra[1:],letra)

def invertir(cadena):
    if len(cadena)==0:
        return ""
    else:
        return invertir(cadena[1:]+cadena[0])

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
                n=int(input("\nIngrese un numero: "))
                print(f"la suma de los primeros numeros naturales es: {SumaNnumerosNa(n)}")

            elif opcion == 3:
                n=int(input("\nIngrese un numero: "))
                print(f"el resultado de la secuancia es: {fibonacci(n)}")

            elif opcion == 4:
                palabra=input("\nIngrese una palabra: ")
                letra=input("\nIngrese una letra para buscar: ")
                print(f"la letra {letra} aparece {contarLetra(palabra,letra)} en la palabra {palabra}")
            elif opcion == 5:
                texto=input("\nIngrese un texto: ")
                cadenaInvertida = invertir(texto)
                print(f"la cadena de texto es: {cadenaInvertida}")
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