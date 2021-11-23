def mergeSort(array):
    if len(array) < 2:
        return array
    m = len(array) // 2
    return merge(mergeSort(array[:m]), mergeSort(array[m:]))

def merge(leftPart, rightPart):
    result = []
    i = j = 0
    while i < len(leftPart) and j < len(rightPart):
        if leftPart[i] < rightPart[j]:
            result.append(leftPart[i])
            i += 1
        else:
            result.append(rightPart[j])
            j += 1
    result += leftPart[i:]
    result += rightPart[j:]
    return result

arrayToSort = [26,81,54,1,93,65,58,74,36,18,9,95,75,58,61,42]
print(mergeSort(arrayToSort))
