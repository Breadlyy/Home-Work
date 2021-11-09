
def sortNumbers(data, condition):
 if condition == "ASC":
  for last in range(len(data)-1):
    for i in range(len(data)-1):
      if data[i]>data[i+1]:
        data[i],data[i+1]=data[i+1],data[i]
  return data
 if condition == "DESC":
   for last in range(len(data)-1):
    for i in range(last):
      if data[i] < data[i+1]:
        data[i],data[i+1]=data[i+1],data[i]
   return data

def sortData(data, weights, condition):
  if len(data) == len(weights):
   if condition == "ASC":
     for last in range(len(data)-1):
      for i in range(len(data)-1):
        if data[i] > data[i+1]:
          data[i],data[i+1]=data[i+1],data[i]
          weights[i],weights[i+1]=weights[i+1],weights[i]
     return weights
   if condition == "DESC":
     for last in range(len(data)-1):
      for i in range(len(data)-1):
        if data[i] < data[i+1]:
          data[i],data[i+1]=data[i+1],data[i]
          weights[i],weights[i+1]=weights[i+1],weights[i]
     return weights
  else:
        raise ValueError('Invalid input data')

data = [4,2,8, 5, 6,7,0,234,34,56,23,78,990,765];
manufactures = ['Ford','BMW','Audi'];
weights = [2,5,6];
print(sortNumbers(data, "ASC"))
print(sortData(weights, manufactures, "DESC"))
