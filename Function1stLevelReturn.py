functions = {
    'max': maxi,
    'min': mini,
    'media': mid}

def maxi(*l):
    if len(l) == 0:
        return 0
    
    m = l[0]
    
    for ix in range(1, len(1)):
        if l[ix] > m:
            m = l[ix]
            
    return m

def mini(*l):
    if len(l) == 0:
        return 0
    
    m = l[0]
    
    for ix in range(1, len(1)):
        if l[ix] < m:
            m = l[ix]
            
    return m

def mid(*l):
    if len(l) == 0:
        return 0
    
    suma = 0
    for valor in l:
        suma += valor
        
    return suma / len(l)

def returnF(name):
    name = name.lower()
    if name in functions.keys():
        return functions[name]
    
    return None