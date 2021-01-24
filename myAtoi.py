class Solution:
    def myAtoi(self, s: str) -> int:
        index=0
        my_int=""
        s=s.strip(" ")
        Ispos=True

        while index<len(s):
            if index==0:
                if s[index]=="+":
                    Ispos=True
                elif s[index]=="-":
                    Ispos=False
                    
                elif s[index].isdigit()==True:
                    Ispos=True
                    if s[index]==0:
                        pass
                    else:
                        my_int+=s[index]
                else:
                    break
            elif s[index].isdigit()==True:
                my_int+=s[index]
            else:
                break
            index+=1
        print(my_int)
        
        if my_int=="":
            my_int=0
        elif my_int.isdigit()==True:
            if Ispos==True:
                
                my_int=int(my_int)
            else:
                my_int=-1*int(my_int)
        else:
            my_int=0
        upper=2**31-1
        lower=-2**31
        if lower<=my_int<=upper:
            return my_int
        elif my_int<lower:
            return lower
        elif my_int>upper:
            return upper

        
        