import random
print("Python de nuevo?! yep... y mucho mas")

#lambda (funciones anonimas)

#ejemplo de la suma
def sumaNormal (a,b):
    return a+b

print(sumaNormal(5,5))
#var = lambda parametros: expresion
sumaLambda = lambda a,b: a+b
sayHi = lambda name: f"Hi {name}"
#f"Hi {name}" ---> texto preformateado, equivalente al `Hi ${name}` de js
print(sumaLambda(7,7)) 
print(sayHi('Pepe'))
#en cuantas lineas lo puedes hacer?

#tipo de dato list
#[] --> list / array 
#{} --> set, no permite duplicados
#() --> tuple, no es mutable

# objeto en js --> diccionario

dic = {
    "llave":"valor"
}

#print(dic.llave) #para objetos, NO para diccionarios
print(dic["llave"])


#map
#map(funcion, iterable)
arr = [1,2,3]
# arr.map(el=>console.log(el))
#quiero todos los numeros multiplicados por 2
mapeado = map(lambda a: a*2, arr) #devuelve un objeto
print(list(mapeado))

names = ['pepe', 'lola', 'maria']

def toUpperCase (name):
    return name.upper()

print(toUpperCase('matia'))

namesMod = map(toUpperCase, names)
print(list(namesMod))

#list comprehension parecido al map
sin_mapear_nombres = [name.upper() for name in names] #devuelve array nuevo
print('sin mapear', sin_mapear_nombres)

randoms = [random.randint(1,99) for x in range(20)]
print(randoms)

multi_por_dos = [x*2 for x in arr]
print(multi_por_dos)

arrb = [5]
#la x es el valor dentro del array, variable de iteracion
funciona = [x*x for x in arrb if x is not None]
#cuando se utiliza --> cuando no sabemos si va a haber informacion
funciona_tambien = [x*x for x in arrb] if arrb else ['no tengo datos']
print(funciona)
print(funciona_tambien)

print(not not arrb) # en vez de "!arrb" es "not arrb"

#filter
#filter(funcion, iterable)

para_filtrar = [1,2,3,4,5,6]

#queremos los pares

pares = filter(lambda x: x%2 == 0, para_filtrar)
print(list(pares)) #[2,4,6]


def get_impares (num):
    return num%2 != 0

impares = filter(get_impares, para_filtrar)
print(list(impares)) 

filtrar_nombres = ['pepe', 'lola', 'matia', 'barbara']

nombres_con_mas_de_cuatro_letras = filter(lambda x: len(x)>4, filtrar_nombres)
print(list(nombres_con_mas_de_cuatro_letras))




pares_v_dos = [x%2==0 for x in para_filtrar] #para filtrar, no nos sirve tanto el list comprehension
print(pares_v_dos) #devuelve en un array todos los elementos diciendo si se cumple o no la condicion


#encadenar filter con map
#js --> filter().map()
# map(func, iterable)
#el iterable me lo va a dar el filter
reuslt = map(lambda x: x*2, filter(lambda x: x%2 == 0, para_filtrar))
print(list(reuslt))

#para un array de 100 elementos
#si quieres aplicar algo a unos elementos dentro de un array y a otros no, primero limpiamos el array -> 150 iteracion
#si quieres filtrar el resultado del map, primero map despues filter -> 200 iteraciones