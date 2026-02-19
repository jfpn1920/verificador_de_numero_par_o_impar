print("#----------------------------------#")
print("#--| verificar si es par o impar|--#")
print("#----------------------------------#")
numero = input("ingrese un numero entero: ")
if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print("el numero", numero, "es par")
    else:
        print("el numero", numero, "es impar")
else:
    print("entrada no valida, debe ingresar un numero entero.")