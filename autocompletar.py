# Crear una lista con los cuadrados de los n primeros números naturales 
def cuadrados_recursivos(n):
    if n == 0:
        return [0]
    else:
        return [n**2] + cuadrados_recursivos(n-1)

print(cuadrados_recursivos(5))

# Crear una lista con los cubos de los n primeros números naturales
def cubos_recursivos(n):
    if n == 0:
        return [0]
    else:
        return [n**3] + cubos_recursivos(n-1)   

        