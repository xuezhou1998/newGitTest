class Solution():
    def findMedianSortedArrays( self,nums1, nums2):
        # print(self.display(nums1,nums2),len(nums1+nums2))
        
        total_len=len(nums1)+len(nums2)
        if len(nums1)<2 or len(nums2)<2:
            x=nums1+nums2
            x.sort()
            if total_len%2 ==1:
                return x[total_len//2]
            else:
                return (x[total_len//2-1]+x[total_len//2])/2
            
        if total_len%2==1 :
            
            
            middle=total_len//2+1
        else:

            middle=total_len//2

        chunck_a=[]
        chunck_a_p=[]
        chunck_b=[]
        chunck_b_p=[]

        if len(nums1)<len(nums2):
            larger=nums2
            smaller=nums1
        else:
            larger=nums1
            smaller=nums2
        head_index=0
        tail_index=len(smaller)-1
        a_mid=(head_index+tail_index)//2
        chunck_a=smaller[0:a_mid]
        chunck_a_p=smaller[a_mid:]
        chunck_b=larger[0:middle - a_mid]
        chunck_b_p=larger[middle - a_mid:]
        print("chunck_a",chunck_a,"chunck_b",chunck_b,"chunck_a_p",chunck_a_p,"chunck_b_p",chunck_b_p,"chunks")
        check=False
        check=(len(chunck_a)+len(chunck_b)==middle and len(chunck_a_p)+len(chunck_b_p)==total_len-middle)
        if check==False:
            return -1

        if total_len%2==1 :
            while True:
                lower=max(chunck_a[len(chunck_a)-1],chunck_b[len(chunck_b)-1])
                upper=min(chunck_b_p[0],chunck_a_p[0])

                if lower <= upper:
                    result=lower
                    return result
                else:
                    if chunck_a[len(chunck_a)-1]>chunck_b_p[0]:
                        tail_index=a_mid

                        
                    elif chunck_b[len(chunck_b)-1]>chunck_a_p[0]:
                        head_index=a_mid 
                    else:
                        return -2
                    a_mid=(head_index+tail_index)//2
                    chunck_a=smaller[0:a_mid]
                    chunck_a_p=smaller[a_mid:]
                    chunck_b=larger[0:middle - a_mid]
                    chunck_b_p=larger[middle - a_mid:]




                # chunck_a=nums_a[0:middle]
                # chunck_a_p=nums_b[0:total_len//2+1-middle]
                # chunck_b=nums_a[middle:len(nums_a)]
                # chunck_b_p=nums_b[total_len//2+1-middle:len(nums_b)]
                # lower=max(chunck_a[len(chunck_a)-1],chunck_a_p[len(chunck_a_p)-1])
                # upper=min(chunck_b[0],chunck_b_p[0])

                # if lower <= upper:

                #   result= lower
                #   break
                # else:
                #   if :
                #       pass
                #   middle-=1
                # if middle<0:
                #   break


        else:
            while True:
                print("chunck_a",chunck_a,"chunck_b",chunck_b,"chunck_a_p",chunck_a_p,"chunck_b_p",chunck_b_p,"while")
                if chunck_a==[]:
                    lower=chunck_b[len(chunck_b)-1]
                elif chunck_b==[]:
                    lower=chunck_a[len(chunck_a)-1]
                else:
                    lower=max(chunck_a[len(chunck_a)-1],chunck_b[len(chunck_b)-1])

                if chunck_a_p==[]:
                    upper=chunck_b_p[0]
                elif chunck_b_p==[]:
                    upper=chunck_a_p[0]
                else:
                    upper=min(chunck_b_p[0],chunck_a_p[0])

                if lower <= upper:
                    result=(lower+upper)/2
                    return result
                else:
                    if chunck_a[len(chunck_a)-1]>chunck_b_p[0]:
                        tail_index=a_mid

                        
                    elif chunck_b[len(chunck_b)-1]>chunck_a_p[0]:
                        head_index=a_mid 
                    else:
                        return -2
                    a_mid=(head_index+tail_index)//2
                    chunck_a=smaller[0:a_mid]
                    chunck_a_p=smaller[a_mid:]
                    chunck_b=larger[0:middle - a_mid]
                    chunck_b_p=larger[middle - a_mid:]
        return -3

    def display(self,nums1,nums2):
        a=nums2+nums1
        a.sort()
        return a
a = Solution()
# output1=a.findMedianSortedArrays([1,2,4,5,7,11,12],[3,4,7,8,9,10])
# # print(a.display([1,2,4,5,7,11,12],[3,4,7,8,9,10]))
# print(output1)

# output2=a.findMedianSortedArrays([3,4,7,8,8,8,9,9,10,10,12,13,15],[2,3,5,6,8,9,11,13,14])
# # print(a.display([1,2,4,5,7,11,12],[3,4,7,8,9,10]))
# print(output2)

output2=a.findMedianSortedArrays([1,2,3],[4,5,6])
# print(a.display([1,2,4,5,7,11,12],[3,4,7,8,9,10]))
print(output2)
        # rightsize=False

        # head=0
        # tail=len(nums1)-1
        # ###initial_pos=abs(tail-head)//2
        # result=nums1[0]
        # total_len=len(nums1)+len(nums2)
        # pos_two=0
        # initial_pos=total_len//2+1
        # chunck_a=[]
        # chunck_a_p=[]
        # chunck_b=[]
        # chunck_b_p=[]
        # while rightsize==False:
        #   chunck_a=nums1[0:initial_pos]
        #   chunck_a_p=nums2[0:total_len//2+1-initial_pos]
        #   chunck_b=nums1[initial_pos:len(nums1)]
        #   chunck_b_p=nums2[total_len//2+1-initial_pos:len(nums2)]
        #   lower=max(chunck_a[len(chunck_a)-1],chunck_a_p[len(chunck_a_p)])
        #   upper=min(chunck_b[0],chunck_b_p[0])
        #   if lower <= upper:
        #       result= (lower+upper)/2
        #       break
        #   else:
        #       initial_pos-=1
        #   if initial_pos<0:
        #       break

        # return result
