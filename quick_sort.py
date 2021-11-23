def quickSort(array):
   quickSortHelper(array,0,len(array)-1)

def quickSortHelper(array,first,last):
   if first<last:
       splitpoint = partition(array,first,last)
       quickSortHelper(array,first,splitpoint-1)
       quickSortHelper(array,splitpoint+1,last)


def partition(array,first,last):
   pivotvalue = array[first]
   left = first+1
   right = last

   while True:
       while left <= right and array[left] <= pivotvalue:
           left += 1
       while right >= left and array[right] >= pivotvalue:
           right -= 1
       if right < left:
           break
       else:
           array[left],array[right] = array[right],array[left]

   array[first],array[right] = array[right],array[first]
   return right



arrayToSort = [26,81,54,1,93,65,58,74,36,18,9,95,75,58,61,42]
quickSort(arrayToSort)
print(arrayToSort)