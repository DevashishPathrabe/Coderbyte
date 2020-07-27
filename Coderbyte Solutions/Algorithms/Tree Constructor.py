def TreeConstructor(strArr):

  # code goes here
    arrLen = len(strArr)
    i1 = dict()
    i2 = []
    for i in range(arrLen):
      pair = strArr[i]
      child, parent = integer(pair)
      if (parent in i1):
        if (i1[parent] == 2):
          return ("false")
        else:
          i1[parent] += 1
      else:
        i1[parent] = 1
      if (child in i2):
        return ("false")
      else:
        i2.append(child)
    return ("true")

def integer(pair):
  pairSplit = pair.split(",")
  child = int(pairSplit[0][1 : ])
  parent = int(pairSplit[1][ : -1])
  return (child, parent)

# keep this function call here 
print(TreeConstructor(input()))