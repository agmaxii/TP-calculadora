def suma(a, b):
    """
    Función que calcula la suma de dos números.

    Args:
        a (float): Primer operando.
        b (float): Segundo operando.

    Returns:
        float: Resultado de la suma.
    """
    return a + b

def resta(a, b):
    """
    Función que calcula la resta de dos números.

    Args:
        a (float): Primer operando.
        b (float): Segundo operando.

    Returns:
        float: Resultado de la resta.
    """
    return a - b

def division(a, b):
    """
    Función que calcula la división de dos números.

    Args:
        a (float): Primer operando.
        b (float): Segundo operando.

    Returns:
        float: Resultado de la división.
        str: Mensaje de error si se intenta dividir por cero.
    """
    if b == 0:
        return "No es posible dividir por cero"
    else:
        return a / b

def multiplicacion(a, b):
    """
    Función que calcula la multiplicación de dos números.

    Args:
        a (float): Primer operando.
        b (float): Segundo operando.

    Returns:
        float: Resultado de la multiplicación.
    """
    return a * b

def factorial(n):
    """
    Función que calcula el factorial de un número.

    Args:
        n (int): Número para calcular el factorial.

    Returns:
        int: Resultado del factorial.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

A = None
B = None

while True:
    print("\nCalculadora")
    print("1. Ingresar 1er operando (A={})".format(A if A is not None else "x"))
    print("2. Ingresar 2do operando (B={})".format(B if B is not None else "y"))
    print("3. Calcular todas las operaciones")
    print("4. Informar resultados")
    print("5. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        A = float(input("Ingrese el valor de A: "))
    elif opcion == "2":
        B = float(input("Ingrese el valor de B: "))
    elif opcion == "3":
        suma_result = suma(A, B)
        resta_result = resta(A, B)
        division_result = division(A, B)
        multiplicacion_result = multiplicacion(A, B)
        factorial_a = factorial(int(A))
        factorial_b = factorial(int(B))
    elif opcion == "4":
        print("El resultado de A+B es:", suma_result)
        print("El resultado de A-B es:", resta_result)
        print("El resultado de A/B es:", division_result)
        print("El resultado de A*B es:", multiplicacion_result)
        print("El factorial de A es:", factorial_a, "y El factorial de B es:", factorial_b)
    elif opcion == "5":
        break
    else:
        print("Opción inválida. Intente nuevamente.")