##texto = input("Ingrese el texto que desea analizar").lower()
texto = "HolA Mundo, como estan, como les va en su dìa a dìa, HOY APRENDEREMOS A PROGRAMAR EN PYTHON".lower() ##aseguramos todas las letras a minuscula para poder hacer una mejor bùsqueda màs adelante
letra1 = input("Ingrese la primera letra a analizar ").lower()
letra2 = input("Ingrese la segunda letra a analizar ").lower()
letra3 = input("Ingrese la tercera letra a analizar ").lower()
letras = [letra1,letra2,letra3] ##Unimos las letras en una lista
texto_lista = list(texto.lower())  ##Aseguramos convertirlo a lista

##0.
print("------------------------------------------------------------\nEL ANALIZADOR DE TEXTOS NOS INDICA LO SIGUIENTE\n------------------------------------------------------------")
##1. Cuàntas veces aparecer cada letra ingresada
print("1. Respecto a las letras ingresadas: ")
for a in letras:
    print(f'la letra \'{a}\' aparece {texto_lista.count(a)} veces')

##2. Cuantas palabras hay en total
palabras_lista = texto.split()
print(f'2. El texto ingresado tiene {len(palabras_lista)} palabras')

##3. Primera y ùltima letra
print(f'3. El texto empieza con la letra \'{texto_lista[0]}\' y termina con la letra \'{texto_lista[-1]}\'')

##4. Palabras en orden inverso
palabras_lista.reverse()
palabras_lista_join_reverse = ' '.join(palabras_lista)
print(f'4. El texto invertido es de la siguiente forma: \'{palabras_lista_join_reverse}\'')

##5. El sistema nos dira si la palabra python se encuentra en el texto
control = 'python' in palabras_lista
if control == True:
    print("5. La palabra 'python' sì se encuentra en el texto ingresado")
else:
    print("5. La palabra 'python' no se encuentra en el texto ingresado")

print("---FIN---")



