def is_anagram( a:str, b:str):
  # test if lenght are same otherwise they can't be anagram
    if len(a) != len(b):
        return False
    #calculate frequency for each char in first string
    freq= {}
    for x in a:
        if x in freq:
         freq[x]+=1
        else:
            freq[x]=1
     #Matching frequency with second string       
    for x in b:
        if x not in freq: return False
        elif freq[x]==1:  del freq[x]
        else: freq[x]=1
    return not freq
    
print(is_anagram( 'han', 'hen'))

      
