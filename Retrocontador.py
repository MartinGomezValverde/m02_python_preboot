def retrocontador(e):
    print("{},".format(e), end = "")
    
    if e > 0:
        retrocontador(e-1) # Recursividad, usando una función que se llama asímisma. Da problemas.
        
retrocontador(10)

def sumatorio(n):
    if n > 0:
        return n + sumatorio(n-1)
    
    else:
        return 0
    
print(sumatorio(5))