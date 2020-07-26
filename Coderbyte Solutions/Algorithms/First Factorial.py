def FirstFactorial(num):

  # code goes here
  i=1
  if(num==0):
    return "1"
  for i in range(1,num):
    num = num*i
  return (num)

# keep this function call here 
print(FirstFactorial(input()))