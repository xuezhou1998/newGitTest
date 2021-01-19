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

class Solution:
    
    def maxUniqueSplit(self, s: str) -> int:

        my_set=set()
        my_set, max_num=self.sub_function(s,my_set)
        return max_num 
    def sub_function(self,s,my_set):
        if len(s)==0:
            return 0,my_set
        else:
            max_num=0
            for i in range(len(s)):
                if s[:i] not in my_set and len(s[:i])>0:
                    new_input_set=my_set
                    new_input_set.add(s[:i])
                    new_num, new_set=self.sub_function(s[i:],new_input_set)
                    max_num=max(max_num,1+new_num)
            return max_num,my_set



                        
            



                        
