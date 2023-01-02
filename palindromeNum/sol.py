class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            x= str(x)

            # calculate length
            l= len(x)

            # if odd:
            if l %2!= 0:
                x1= x[:int(l/2)]
                x2= x[int(l/2)+1:]
                x2= x2[::-1]

            #if even
            elif l %2== 0:
                x1= x[:int(l/2)]
                x2= x[int(l/2):]
                x2= x2[::-1]

            if x1 == x2:
                return True
            else:
                 return False
