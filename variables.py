
num_entero = 7
num_real = 12.8
tipo_cadena = "ciao mondo"
tipo_bool = True
print (num_entero)
print (num_real)
print (tipo_cadena)
print (tipo_bool)
print (num_entero, num_real, tipo_bool, tipo_cadena)

# Los números enteros representan a los números naturales más el 0 pudiendo ser positivos o negativos, en Python no hay limite de tamaño de estos números. Al contrario de los flotantes cuyo limite es de 53 bits.

#Sumar nùmeros pares
suma = 0
n = 1
while n != 0: 
    n = int(input ("Ingresa un numero: ")) 
    if n  != 0:
        if n % 2 == 0: 
            suma = suma + n
print("la suma de los numeros pares es: ", suma)