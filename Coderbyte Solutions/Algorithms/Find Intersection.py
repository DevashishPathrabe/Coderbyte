def FindIntersection(strArr):

  # code goes here
  firstList = set(map(int, strArr[0].split(', ')))
  secondList = set(map(int, strArr[1].split(', ')))
  sortedList = sorted(list(firstList&secondList))
  if len(sortedList) ==0:
    return ('false')
  strArr = """"""
  for i in range(len(sortedList)):
      strArr += str(sortedList[i])
      if i<len(sortedList)-1:
          strArr+= ","
  return strArr

# keep this function call here 
print(FindIntersection(input()))