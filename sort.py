
def sortNumbers(data, condition):
 list1 = [];
 i = 0;
 l = 0;
 if condition == "ASC":   
  for n in range(len(data)):   
     for q in range(len(data) - 1):
      if i <= data[q]:
        i = data[q];
      else: continue
      for q in range(len(data) - 1):
          if i > data[q]:
            i = data[q] 
          elif i < data[q]:
           continue
          data.remove(i);
          list1.append(i); 
 elif condition == "DESC":
        pass
 return list1;




def sortData(weights, data, condition):
    pass


data = [4,2,3, 5, 6, 7];
print(sortNumbers(data, 'ASC'))