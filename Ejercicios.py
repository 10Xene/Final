# 1. Crea una función de nombre enviarMensaje, que se le pasa por parámetro
#    un nombre, y al ser llamada, imprime un mensaje con el nombre de la persona

def enviarMensaje(nombre):
    print(f"Hola, {nombre}")
    
'''
OUTPUT:
Hola, Fulano
'''



# 2. Dada la siguiente lista de números, imprime línea a línea cada número
numeros = [4, 3, 2, 5, 6]

def imprimirNumeros(lista):
    for numero in lista:
        print(numero)
imprimirNumeros(numeros)



'''
OUTPUT:
4
3
2
5
6
'''



# 3. Genera un bucle while que se rompe cuando el valor es un número negativo. Inicialmente,
#    el valor empieza en 5 y va reduciendo
numero = 5

def reducirNumero():
    global numero
    while numero >= 0:
        print(f"El número ahora es {numero}")
        numero -= 1


'''
OUTPUT:
El número ahora es 5
El número ahora es 4
El número ahora es 3
El número ahora es 2
El número ahora es 1
'''



# 4. Generar una función que se le pasa dos números, el usuario indica por consola cada número,
#    y una vez indicados se llama a la función pasando los números que el usuario ha escrito.
#    La función sumará los números y devolverá el resultado

def solicitarNumero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, ingresa un número válido.")  
numero1 = solicitarNumero("Introduce el primer número: ")
numero2 = solicitarNumero("Introduce el segundo número: ")
def sumar(numero1, numero2):
    return numero1 + numero2
print(f"SUMA: {sumar(numero1, numero2)}")




# 5. Crea una función para que, cuando se le pase una lista cualquiera, imprima sus valores en orden inverso


def imprimirListaInversa(lista):
    for elemento in reversed(lista):
        print(f"- {elemento}")
nombres = ["Mengano", "Fulano", "Zutano", "Perantano"]
imprimirListaInversa(nombres)



'''
OUTPUT:
- Perantano
- Zutano
- Fulano
- Mengano
'''


# 6. Crear una función que busque una palabra en una lista, se le pasa la lista y la palabra a buscar
#    Si la palabra existe, devuelve True, de lo contrario False


def buscarPalabra(lista, palabra):
    return palabra in lista
print(buscarPalabra(["Fulano", "Mengano", "Zutano"], "Mengano")) # OUTPUT: True






# 7. Crea un diccionario que contenga como clave tu nombre y como valor la cantidad de letras de la clave,
#    lo mismo con el primer y segundo apellido, quedando un diccionario de tamaño 3. Luego, utiliza un bucle
#    para imprimir el contenido


def crearDiccionario(nombre, apellido1, apellido2):
    diccionario = {
        nombre: len(nombre),
        apellido1: len(apellido1),
        apellido2: len(apellido2)
    }
    return diccionario
nombre = "Nombre"
apellido1 = "Apellido1"

'''
OUTPUT:
Nombre
Apellido1
Apellido2
'''