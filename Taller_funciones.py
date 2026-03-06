"""
#1. Crea una función llamada "edad" que le pide al usuario que ingrese su edad y le muestra un mensaje en la consola que dice "Tu edad es: XX años", donde XX es la edad ingresada por el usuario.
def edad():
    edad=input("ingrese su edad: ")
    return edad
edad=edad()
print("Tu edad es:",edad, "años")

#2. Crea una función llamada "suma" que le pide al usuario que ingrese dos números y muestra en la consola la suma de ambos.
a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))
def suma():
    resultado=a+b
    return resultado
resultado=suma()
print("La suma da: ", resultado)

#3. Crea una función llamada "num_aleatorio" que genera un número aleatorio entre 1 y 100 y le pide al usuario que adivine el número. La función debe decirle al usuario si el número que ingresó es mayor o menor que el número aleatorio generado. Si el usuario adivina el número, la función debe imprimir "¡Felicitaciones, adivinaste el número!".
def num_aleatorio():
    import random
    numero=random.randint(1,100)
    return numero
numero=num_aleatorio()
usuario_numero=int(input("Ingrese un numero del 1 al 100: "))
if usuario_numero==numero:
    print("¡Felicidades! Has adivinado el número.")
else:
    print("Lo siento, el número no es correcto")

#4 Crea una función llamada "contador_vocales" que le pide al usuario que ingrese una cadena y cuenta el número de vocales que tiene la cadena. La función debe devolver el número de vocales.
def contador_vocales():
    cadena=input("Ingrese una cadena: ")
    vocales="aeiouAEIOU"
    contador=0
    for letra in cadena:
        if letra in vocales:
            contador+=1
    return contador
vocales=contador_vocales()
print("El número de vocales en la cadena es: ", vocales)

#5 Crea una función llamada "palindromo" que toma un parámetro "palabra" y devuelve True si la palabra es un palíndromo (es decir, se lee igual de adelante hacia atrás que de atrás hacia adelante), y False de lo contrario.
def Palidromo():
    palabra=input("Ingrese una palabra: ")
    if palabra==palabra[::-1]:
        return True
    else:
        return False
palidromo=Palidromo()
print(palidromo)

#6 Crea una función llamada "calcular_potencia" que toma dos parámetros "base" y "exponente" y calcula la potencia de la base elevada al exponente. La función debe imprimir el resultado en la consola.
def calcular_potencia():
    base=int(input("Ingrese la base: "))
    exponente=int(input("Ingrese el exponente: "))
    resultado=base**exponente
    return resultado
potencia=calcular_potencia()
print("El resultado de la potencia es: ", potencia)

#7 Crea una función llamada "calcular_media" que toma un parámetro "lista" y calcula la media de los elementos de la lista. La función debe imprimir el resultado en la consola.
def calcular_media():
    lista=[]
    n=int(input("Ingrese la cantidad de números: "))
    for i in range(n):
        numero=int(input("Ingrese un número: "))
        lista.append(numero)
    media=sum(lista)/len(lista)
    return media
media=calcular_media()
print("La media de los números es: ", media)

#8 Crea una función llamada "invertir_cadena" que toma un parámetro "cadena" y devuelve la cadena invertida.
def invertir_cadena():
    cadena=input("Ingrese una cadena: ")
    cadena_invertida=cadena[::-1]
    return cadena_invertida
cadena_invertida=invertir_cadena()
print("La cadena invertida es: ", cadena_invertida)

#9 Crea una función llamada "mayor_de_tres_numeros" que toma tres parámetros "numero1", "numero2" y "numero3" y devuelve el número mayor.
def mayor_de_tres_numeros():
    numero1=int(input("Ingrese el primer número: "))
    numero2=int(input("Ingrese el segundo número: "))
    numero3=int(input("Ingrese el tercer número: "))
    if numero1>=numero2 and numero1>=numero3:
        mayor=numero1
    elif numero2>=numero1 and numero2>=numero3:
        mayor=numero2
    else:
        mayor=numero3
    return mayor
mayor=mayor_de_tres_numeros()
print("El número mayor es: ", mayor)

# 10 Crea una función llamada "calcular_area" que toma dos parámetros "radio" y "altura" y calcula el área del cilindro (2 * pi * radio * altura + 2 * pi * radio^2). La funcion debe devolver el resultado.
def calcular_area():
    radio=float(input("Ingrese el radio del cilindro: "))
    altura=float(input("Ingrese la altura del cilindro: "))
    area=2*3.1416*radio*altura+2*3.1416*radio**2
    return area
area=calcular_area()
print("El área del cilindro es: ", area)

# 11 Crea una función llamada "buscar_palabra" que toma dos parámetros "cadena" y "palabra" y devuelve True si la palabra está en la cadena, y False de lo contrario.
def buscar_palabra():
    cadena=input("Ingrese una cadena: ")
    palabra=input("Ingrese una palabra a buscar: ")
    if palabra in cadena:
        return True
    else:
        return False
buscar=buscar_palabra()
print(buscar)
#12 Crea una función llamada "promedio" que toma un número variable de parametros y devuelve el promedio de todos ellos.
def promedio():
    numeros=[]
    n=int(input("Ingrese la cantidad de números: "))
    for i in range(n):
        numero=float(input("Ingrese un número: "))
        numeros.append(numero)
    promedio=sum(numeros)/len(numeros)
    return promedio
promedio=promedio()
print("El promedio de los números es: ", promedio)
"""
#13 Crea una función llamada "multiplicar_lista" que toma dos parámetros "lista" y "numero" y devuelve una lista donde cada elemento de la lista original es multiplicado por el número.
def multiplicar_lista():
    lista=[]
    n=int(input("Ingrese la cantidad de elementos en la lista: "))
    for i in range(n):
        elemento=float(input("Ingrese un elemento: "))
        lista.append(elemento)
    numero=float(input("Ingrese el número por el cual multiplicar los elementos de la lista: "))
    lista_multiplicada=[elemento*numero for elemento in lista]
    return lista_multiplicada
lista_multiplicada=multiplicar_lista()
print("La lista multiplicada es: ", lista_multiplicada)

# 14 Crea una función llamada "mayor_de_varios_numeros" que toma un número variable de parámetros y devuelve el número mayor.
def mayor_de_varios_numeros():
    numeros=[]
    n=int(input("Ingrese la cantidad de números: "))
    for i in range(n):
        numero=float(input("Ingrese un número: "))
        numeros.append(numero)
    mayor=max(numeros)
    return mayor
mayor=mayor_de_varios_numeros()
print("El numero mayor es: ", mayor)

#15 Crea una función llamada "calcular_mediana" que toma un número variable de parámetros y devuelve la mediana de los números. La mediana es el número que se encuentra en el medio de la lista ordenada. Si la lista tiene un número par de elementos, la mediana es el promedio de los dos números del medio.
def calcular_mediana():
    numeros=[]
    n=int(input("Ingrese la cantidad de números: "))
    for i in range(n):
        numero=float(input("Ingrese un número: "))
        numeros.append(numero)
    numeros.sort()
    if len(numeros)%2==1:
        mediana=numeros[len(numeros)//2]
    else:
        mediana=(numeros[len(numeros)//2-1]+numeros[len(numeros)//2])/2
    return mediana
mediana=calcular_mediana()
print("La mediana es: ", mediana)

#16 Crea una función llamada "contar_ocurrencias" que toma dos parámetros "cadena" y "palabra" y devuelve el número de veces que la palabra aparece en la cadena.
def contar_ocurrencias():
    cadena=input("Ingrese una cadena: ")
    palabra=input("Ingrese una palabra a contar: ")
    ocurrencias=cadena.count(palabra)
    return ocurrencias
ocurrencias=contar_ocurrencias()
print("La palabra aparece ", ocurrencias, " veces en la cadena.")
