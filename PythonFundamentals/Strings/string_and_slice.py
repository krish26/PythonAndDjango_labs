s='ProgrammingIsFun'
print('First letter is : ' , s[0])
print('Last 3 letters are : ' ,s[-3:] )
print('Every second letter : ', s[::2])
print('the word : ' ,s[0:11])

start=s.index('Fun')
result = s[start : start+len('Fun')]
print(result)

print('the reversed word : ' ,s[::-1])

#