class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        is_sorted=False
        while is_sorted==False:
            is_sorted=True
            for i in range(len(nums)-1):
                if nums[i]>nums[i+1]:
                    is_sorted=False
                    inter=nums[i]
                    nums[i]=nums[i+1]
                    nums[i+1]=inter
    def removeKdigits(self, num: str, k: int) -> str:
        num_list=list(num)
        remove_cnt=0
        while remove_cnt<=k:
            sum_list=[]
            for i in range(num_list):
                
                if head==[]:
                    head=0
                else:
                    head=int(num_list[:i])
                part1=head*10**(len(num_list[i:])-1)
                part2=int(num_list[i+1:])
                summ=part1+part2
                sum_list.append(summ)
            num_list=min(sum_list)
            remove_cnt+=1

    class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num_list=str(num)
        remove_cnt=0
        if num_list=="":
            return ""
        while remove_cnt<k:
            sum_list=[]
            for i in range(len(num_list)):
                head=num_list[:i]
                if head=="":
                    head=0
                else:
                    head=int(num_list[:i])
                part1=head*10**(len(num_list[i:])-1)
                if num_list[i+1:]=="":
                    part2=0
                else:
                    part2=int(num_list[i+1:])
                summ=part1+part2
                
                sum_list.append(summ)
            num_list=str(min(sum_list))
            remove_cnt+=1
        return str(num_list)
    def removeKdigits(self, num: str, k: int) -> str:
        remove_cnt=0
        for i in range(len(num))
            
        return str(num_list)
