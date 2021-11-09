def heapSort(array):
  for start in range((len(array)-2)//2, -1, -1):
    movedown(array, start, len(array)-1)

  print(array)

  for end in range(len(array)-1, 0, -1):
    array[end], array[0] = array[0], array[end]
    movedown(array, 0, end - 1)


def movedown(array, start, end):
  root = start
  while True:
    child = root * 2 + 1
    if child > end: break
    if child + 1 <= end and array[child] < array[child + 1]:
      child += 1
    if array[root] < array[child]:
      array[root], array[child] = array[child], array[root]
      root = child
    else:
      break

arrayToSort = [26,81,54,1,93,65,58,74,36,18,9,95,75,58,61,42]
heapSort(arrayToSort)
print(arrayToSort)

