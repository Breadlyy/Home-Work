a = [234, 654, 678,981, 100, 392]
search_for = 100;

def linear_search(where, what):
     for v in enumerate(where):
         if v[1] == what:
             return v[0]
     return None;

def reverse_string(s):
    chars = list(s)

    for i in range(len(s) // 2):
        temp = chars[i]
        chars[i] = chars[len(s) - i - 1]
        chars[len(s) - i - 1] = temp

    return ''.join(chars)   

def Binary_Search(a, value):
    mid = len(a) // 2
    low = 0
    high = len(a) - 1
    while a[mid] != value and low <= high:
        if value > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    
    if low > high:
        print("No value")
    else:
        print("ID =", mid)

a.sort()
string = "Я мля Джаггернаут"
print(reverse_string(string));