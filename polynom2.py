def polyEval(poly, x):
    result =  0
    n = len(poly)
    for i in range (n):
        result = result + poly[i] * x ** i
    return result

def polySum(poly1, poly2):
    poly3 = []
    if len(poly1) > len(poly2):
        while len(poly1) != len(poly2):
            poly2.append(0)
        for n in range(len(poly1)):
            poly3.append(poly1[n] + poly2[n]) 
        while poly3[-1] == 0:
            poly3.pop()
    else:
        while len(poly1) != len(poly2):
            poly1.append(0)
        for n in range(len(poly2)):
            poly3.append(poly1[n] + poly2[n]) 
        while poly3[-1] == 0:
            poly3.pop()
    return poly3; 
      
def polyMultiply(poly1, poly2):
    poly3 = [0] * (len(poly1) + len(poly2) - 1)
    for n in range(len(poly1)):
        for m in range(len(poly2)):
            poly3[n + m] += poly1[n] * poly2[m]
    return poly3;  

poly = [1, 2.5, 3.5, 0, 5.4]
print(polySum([1, 2, 5], [2, 0, 1, -7]))
