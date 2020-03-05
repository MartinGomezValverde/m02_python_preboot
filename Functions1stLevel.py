def normal(x):
    return x

def elevated(y):
    return y * y

def cube(x):
    return x**3

def addAll(limitTo, f):
    result = 0
    for i in range(limitTo+1):
        result += f(i)
        
    return result

if __name__ == '__main__': #Para que cuando lo importe no se me haga todo el programa, sinó sólo lo que importo.
    
    print(addAll(100, normal))
    print(addAll(3, elevated))
    
else:
    print(__name__)