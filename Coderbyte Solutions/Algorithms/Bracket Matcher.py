def BracketMatcher(str):

  # code goes here
  counter = 0
  for char in str:
    if(char == '('):
      counter += 1
    elif(char == ')'):
      if(counter == 0):
        return (0)
      counter -= 1
  if(counter > 0):
    return (0)
  return (1)

# keep this function call here 
print(BracketMatcher(input()))