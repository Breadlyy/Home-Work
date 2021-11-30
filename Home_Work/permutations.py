def permutations(array):
 result = []
 if len(array) <= 1:
    return [array[:]]
 for i in range(len(array)):
    n = array.pop(0)
    perms = permutations(array)
    for perm in perms:
       perm.append(n)
    result.extend(perms)
    array.append(n)
 return result

print(permutations(array=[1,9,3]))

  
