def CodelandUsernameValidation(str):

  # code goes here
  if (not str[0].isalpha()) or (len(str)>25) or (len(str) < 4) or (str[-1] == "_"):
    return "false"
  
  for i in range(len(str)-2):
      if str[i+1].isalpha() or str[i+1].isdigit() or str[i+1] == "_":
        pass
      else:
        return "false"
  
  return "true"

# keep this function call here 
print(CodelandUsernameValidation(input()))