# class Solution:
#     def maxUniqueSplit(self, s: str) -> int:
#         head=0
#         #### note: splitting means you cannot reuse the digits that you have passed.         
        
#         exist_list=[]
#         while True:
#             if head>=len(s):
                
#                 break
#             elif s[head] in exist_list:
#                 tail=head+1
#                 while True:
#                     if tail>len(s):

#                         break
#                     elif s[head:tail] in exist_list:
#                         tail+=1
#                     else:
#                         exist_list.append(s[head:tail])
                        
#                         break
#                 head=tail
#             else:
#                 exist_list.append(s[head])
#                 head+=1
#         print(exist_list)
#         return len(exist_list)

# class Solution:
    
#     def maxUniqueSplit(self, s: str) -> int:

#         my_set=set()
#         a=self.sub_function(s,my_set)
#         my_set, max_num= a[0],a[1]
#         print(my_set,"final")
#         return max_num 
#     def sub_function(self,s,my_set):
#         if len(s)==0:
#             return [0,my_set]
#         else:
#             max_num=0
#             return_set=set()
#             for i in range(len(s)):
#                 if s[:i] not in my_set and len(s[:i])>0:
#                     new_input_set=my_set
#                     new_input_set.add(s[:i])
#                     a=self.sub_function(s[i:],new_input_set)
#                     new_num, new_set=a[0],a[1]
#                     if max_num<1+new_num:
#                         max_num=1+new_num
#                         return_set=new_set
#             return [max_num,return_set] 

class Solution:
    
    def maxUniqueSplit(self, s: str) -> int:

        my_set=[]
        a=self.sub_function(s,my_set)
        my_set, max_num= a[1],a[0]
        print(my_set,"final")
        return max_num 
    def sub_function(self,s,my_set):
        
        max_num=0
        return_set=[]
        for i in range(1,len(s)+1):  #### the first case x + [x,x,x,...,x] and the last case: x....x + []
            if s[:i] not in my_set and len(s[:i])>0:
                new_input_set=my_set.copy()
                new_input_set.append(s[:i])
                a=self.sub_function(s[i:],new_input_set)
                new_num, new_set=a[0],a[1]
                #print(new_set,'new_set')
                if max_num<1+new_num:
                    max_num=1+new_num
                    return_set=new_set
        print(return_set,"xxx")
        return [max_num,return_set] 

# class Solution:
    
#     def maxUniqueSplit(self, s: str) -> int:

#         my_set=[]
#         a=self.sub_function(s,my_set)
        
        
#         return a 
#     def sub_function(self,s,my_set):
#         if len(s)==1:
#             if s in my_set:
#                 return 0
#             else:
#                 return 1
#         max_num=0
#         for i in range(len(s)):
#             if s[:i] not in my_set and len(s[:i])>0:
#                 new_input_set=my_set.copy()
#                 new_input_set.append(s[:i])
#                 a=self.sub_function(s[i:],new_input_set)
#                 new_num=a
#                 #print(new_set,'new_set')
#                 if max_num<1+new_num:
#                     max_num=1+new_num
                    
#         return max_num 



                        
class Solution:
    
    def maxUniqueSplit(self, s: str) -> int:

        my_set=()
        a=self.max_unique_substrings(s,my_set)
        # my_set, max_num= a[1],a[0]
        # print(my_set,"final")
        # return max_num
        return a
    def max_unique_substrings(self, s, seen=()):
        maximum = 0
        for i in range(1, len(s) + 1):
            candidate = s[:i]
            if candidate not in seen:
                maximum = max(maximum, 1 + self.max_unique_substrings(s[i:], {candidate, *seen}))
        return maximum            



                        
