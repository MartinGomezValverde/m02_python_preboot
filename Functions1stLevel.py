def normal(x):
    return x

def elevated(y):
    return y * y

def addAll(limitTo, f):
    result = 0
    for i in range(limitTo+1):
        result += f(i)
        
    return result

print(addAll(100, normal))