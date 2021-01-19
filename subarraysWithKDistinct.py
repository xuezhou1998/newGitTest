class Solution():
    def subarraysWithKDistinct(self,A, K):
        
            # if right==len(A):
            #   if len(listFilled)==K:
            #       #listFilled.remove(A[left])###problem: listfilled may still contain element x after
            #       ####one of its instances is removed from the listfilled, because there may be multiple x instances
            #       #### inside listfilled 
            #       left+=1
            #       numberOfGood+=1
            #       break
            #   else:
            #       break
            # elif listFilled.has_key(A[right])==True:
            #   if len(listFilled)==K:
            #       right+=1
            #       numberOfGood+=1
            #   else:
            #       right+=1
            # elif listFilled.has_key(A[right])==False:
            #   if len(listFilled)==K:
            #       left+=1
            #       numberOfGood+=1
            #   else:
            #       listFilled.append(A[right])
            #       right+=1
            

        #   if right==len(A):
        #   elif A[right] in listFilled:
        #       if len(listFilled)==K:
        #           right+=1
        #           numberOfGood+=1
        #       else:
                    # right+=1
        #   elif A[right] not in listFilled:
        #       if len(listFilled)==K:
        #           if A[left] in A[left+1:right]:
        #               left+=1
        #               numberOfGood+=1
        #           else:
        #               listFilled.removed(A[left])
        #               left+=1
        #       else:
                    # listFilled.append(A[right])
                    # right+=1
        # numberOfGood=0
        # listFilled=[]
        # left=0
        # right=0
        # while True:
        #     if len(A)==0:
        #         return 0
        #     elif len(A)==1:
        #         return 1

        #     if right==len(A)-1:
        #         if len(listFilled)==K:
        #             if A[left] in A[left+1:right+1]:
        #                 left+=1
        #                 numberOfGood+=1
        #             else:
        #                 listFilled.remove(A[left]) 
        #                 left+=1
        #                 numberOfGood+=1
                                         
        #         else:
        #             break

            

        #     elif left==right:
        #         if A[right+1] in listFilled:
        #             right+=1
        #         else:
        #             right+=1
        #             listFilled.append(left)
        #     elif len(listFilled)==K:
        #         if A[right+1] in listFilled:
        #             right+=1
        #             numberOfGood+=1
        #         else:
        #             if A[left] in A[left+1:right]:
        #                 left+=1
        #                 numberOfGood+=1
        #             else:
        #                 listFilled.remove(A[left])
        #                 left+=1
        #                 numberOfGood+=1
                        
        #     elif len(listFilled)<K:
        #         if A[right+1] in listFilled:
        #             right+=1
                    
        #         else:
        #             right+=1
        #             listFilled.append(A[right])

        # return numberOfGood


                # numberOfGood=0
        # numberOfGood=0
        # if len(A)==0:
        #     return 0
        # elif len(A)==1:
        #     return 1
        # listFilled=set([A[0]])
        # left=0
        # right=0
        # # if K==1:
        # #     return len(A)
        # #has some problems with K==1
        # while True:
        #     right+=1
            
        #     if right==len(A)-1:
        #         left=0
        #         while left<=right:
        #             listFilled=set(A[left:right+1])
        #             if len(listFilled)==K:
        #                 numberOfGood+=1
        #                 left+=1
        #             elif len(listFilled)<K:
        #                 break
        #             else:
        #                 left+=1
        #         #print(right,numberOfGood,A)
        #         break
        #     else:
        #         left=0
        #         while left<=right:
        #             listFilled=set(A[left:right+1])
        #             if len(listFilled)==K:
        #                 numberOfGood+=1
        #                 left+=1
        #             elif len(listFilled)<K:
        #                 break
        #             else:
        #                 left+=1
        #     print(right,numberOfGood,A)
        # if K==1:
        #     return numberOfGood+1
        # else:
        
        #     return numberOfGood
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        numberOfGood=0
        if len(A)==0:
            return 0
        elif len(A)==1:
            return 1
        listFilled=set([A[0]])
        left=0
        right=0
        tail=0
        # if K==1:
        #     return len(A)
        while True:
            right+=1
            
            if right==len(A)-1:
                left=tail
                listFilled=set(A[left:right+1])
                set_len=len(listFilled)

                while left<=right:
                    
                    if set_len==K:
                        numberOfGood+=1
                        left+=1
                    elif set_len<K:
                        break
                    else:
                        left+=1
                #print(right,numberOfGood,A)
                break
            else:
                left=tail
                while left<=right:
                    listFilled=set(A[left:right+1])## try to move this out of the while loop
                    if len(listFilled)==K:
                        numberOfGood+=1
                        left+=1
                    elif len(listFilled)<K:
                        break
                    else:
                        left+=1
                        tail+=1
                        
                
            #print(right,numberOfGood,A)
        if K==1:
            return numberOfGood+1
        else:
            
            return numberOfGood
a=Solution()
print(a.subarraysWithKDistinct([1,2,1,2,3,2],2))
        #     if right==len(A)-1:
        #         if len(listFilled)==K:
        #             left=0
        #             numberOfGood+=1
        #             while left!=right:
        #                 if A[left] in A[left+1:right+1]:
        #                     numberOfGood+=1
        #                     left+=1
        #                 else:
        #                     break
        #             break
        #         elif len(listFilled)<K:
        #             break
        #         # right+=1
                
        #         # listFilled.add(A[left])
        #         # if len(listFilled)==K:
        #         #     numberOfGood+=1

                
        #     elif len(listFilled)==K:
        #         left=0
        #         numberOfGood+=1
        #         while left!=right:
        #             if A[left] in A[left+1:right+1]:
        #                 numberOfGood+=1
        #                 left+=1
        #             else:
        #                 break
        #         right+=1


        #         # if A[right+1] in listFilled:
        #         #     right+=1
        #         #     numberOfGood+=1
        #         # else:
        #         #     if A[left] in A[left+1:right+1]:
        #         #         left+=1
        #         #         numberOfGood+=1
        #         #     else:
        #         #         listFilled.discard(A[left])
        #         #         left+=1
        #                 # numberOfGood?
                        
        #     elif len(listFilled)<K:
        #         right+=1
        #         # right+=1
        #         # listFilled.add(A[right])
                

        # return numberOfGood




# Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.

# (For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

# Return the number of good subarrays of A.

 

# Example 1:

# Input: A = [1,2,1,2,3], K = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
# Example 2:

# Input: A = [1,2,1,3,4], K = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].