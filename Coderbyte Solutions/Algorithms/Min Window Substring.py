def MinWindowSubstring(strArr):

  # code goes here
  N = strArr[0]
  K = strArr[1]
  mapSub = dict()
  for l in K:
      if(l in mapSub):
          mapSub[l] += 1
      else:
          mapSub[l] = 1
  substring = ""
  found = False
  for length in range(1, len(N)+1):
      for start in range(0,len(N)-length+1):
          strSl = N[start:start+length]
          mapSl = mapSub.copy()
          for l in strSl:
              if(l in mapSl):
                  mapSl[l] -= 1
          found = True
          for l in mapSl:
              if(mapSl[l] > 0):
                  found = False
                  break
          if(found):
              substring = strSl
              break
      if(found): 
        break
  return (substring)

# keep this function call here 
print(MinWindowSubstring(input()))