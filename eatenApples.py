class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        apple_list=[]
        day_list=[]
        apple_eaten=0
        index=0
        n=len(apples)
        if n==1:
            return min(days[0],apples[0])

        while True:
            i=min(index,n)
            if index>=n and apple_list==[]:
                break
            else:
                if i<=n-1:
                    if apples[i]>0 and days[i]>0:

                        apple_list.append(apples[i])
                        day_list.append(days[i])
                for j in range(len(apple_list[:i])):
                    day_list[j]-=1
                    if day_list[j]<0:
                        day_list.remove(day_list[j])
                        apple_list.remove(apple_list[j])
                min_index=day_list.index(min(day_list))
                apple_list[min_index]-=1
                apple_eaten+=1
                if apple_list[min_index]==0:
                    apple_list.remove(apple_list[min_index])
                    day_list.remove(day_list[min_index])
            index+=1
            print(apple_list, day_list)
        return apple_eaten



                    


    #   to_apple=0
    #   to_eatable=0
    #   to_rot=0
    #   days_left=days
    #   n=len(days)
    #   to_eaten=0
    #   # for i in range(len(apples)):

    #   #   days_left[i]-=n
    #   # for i in range(len(apples)):
    #   #   if days_left[i]>=0:
    #   #       e+=apples[i]
    #   #inite:
    #   if n==1:
    #       return min(apples[0],days[0])
    #   # index=0
    #   # while True:
    #   #   to_eatable=0
    #   #   for i in range(min(index,n)):
    #   #       days_left[i]-=1
    #   #       if days_left[i]>=0:
    #   #           to_eatable+=apples[i]
    #   #   if to_eatable>0:
                
    #   #       to_eatable-=1
    #   #       to_eaten+=1
    #   #   elif to_eatable==0 and index>=n:##>=??
    #   #       break
    #   #   index+=1
    #   #   print("to_eatable",to_eatable,"to_eaten",to_eaten)
    #   # return to_eaten
    #   days_num=0
    #   while True:
    #       if to_eatable==0 and days_num>n:
    #           break
    #       else:
                # for i in range(min(index,n)):
                #   days_left[i]-=1     
    #           pass

# Input:
# [2,1,10]
# [2,10,1]
# Output:
# 11
# Expected:
# 4