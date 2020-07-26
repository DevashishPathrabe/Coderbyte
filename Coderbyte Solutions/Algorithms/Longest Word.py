def LongestWord(sen):

  # code goes here
  longestWord = ''
  currentWord = ''
  for letter in sen:
      if (letter in '''!()-[]{};:'"\,<>./?@#$%^&*_~''' or letter == ' '):
          if (len(currentWord) > len(longestWord)):
              longestWord = currentWord
          currentWord = ''
      else:
          currentWord += letter
  if (len(currentWord) > len(longestWord)):
      longestWord = currentWord
  return (longestWord)

# keep this function call here 
print(LongestWord(input()))