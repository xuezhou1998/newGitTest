class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # a=[{1,2,3},{4,5}]
        # b={1,3,2}
        # print(b in a)
        # return 0
        #         if len(nums)==0:
        #             return nums
        #         elif len(nums)==1:
        #             if nums==[]:
        #                 return []
        #             else:
        #                 return []
        #         output=[]
        #         left=0
        #         right=len(nums)-1
        #         nums=sorted(nums)
        #         print(nums)

        #         while True:
        #             sum_two=nums[right]+nums[left]
        #             third_exp=-1*sum_two
        #             if third_exp in nums[left+1:right]:

        #                 third_indx=nums.index(third_exp,left+1,right)
        #                 if third_indx!=right and third_indx!=left:
        #                     curr_set=[nums[third_indx],nums[right],nums[left]]
        #                     if curr_set not in output:
        #                         output.append(curr_set)
        #             if sum_two>=0:

        #                 right-=1
        #             else:
        #                 left+=1
        #             if right==left:
        #                 break

        #         for i in range(len(output)):
        #             output[i]=list(output[i])

        #         return output
        if len(nums) == 1:
            return []
        elif len(nums) == 2:
            return []

        comb_set = []
        # comb_set.add([1,2,3])
        left = 0
        right = len(nums) - 1
        pivot = 1
        nums = sorted(nums)
        while 0 < pivot < len(nums) - 1:
            comb_set = self.sub_proc(comb_set, pivot, nums)
            pivot += 1
        for i in range(len(comb_set)):
            comb_set[i] = list(comb_set[i])
        return comb_set

    def sub_proc(self, input_set, pivot, nums):
        left = 0
        right = len(nums) - 1

        while left != right:
            if left == pivot:
                left += 1
            elif right == pivot:
                right -= 1
            elif nums[left] + nums[right] + nums[pivot] == 0:
                new_e = [nums[left], nums[right], nums[pivot]]
                if sorted(new_e) not in input_set:
                    input_set.append(sorted(new_e))
                if nums[left] + nums[right] <= 0:
                    left += 1
                else:
                    right -= 1
            elif nums[left] + nums[right] + nums[pivot] < 0:
                left += 1
            else:
                right -= 1
        return input_set

