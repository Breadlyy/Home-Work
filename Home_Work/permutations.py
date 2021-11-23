def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]
def permutations(array):
    myarray = []
    if len(array) <= 1:
        return array
    else: 
     for i in range(len(array)):
         for q in range(len(array)):
             pass
            
array = [2,7,5] 
for q in range(len(array)):
   x = array[q]   
   for i in range(len(array)):
    array[x], array[i] = array[i], array[x]
    print(array)


  
