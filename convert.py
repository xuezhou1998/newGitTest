class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        result_list=[]
        for i in range(numRows):
            result_list.append([])
        i=0
        tol=numRows+numRows-2
        isfromTop=True
        index_max=numRows-1
        row_num=0
        while i<len(s):
            if i%(numRows-1)==0 and (i/(numRows-1))%2==0:
                result_list[0].append(s[i])
                isfromTop=True
                i+=1

            elif i%(numRows-1)==0 and (i/(numRows-1))%2==1:
                result_list[index_max].append(s[i])
                isfromTop=False
                i+=1
            else:
                if isfromTop==False:
                    rest=i%index_max
                    print(rest)
                    my_index=index_max-rest
                    result_list[my_index].append(s[i])
                    i+=1
                else:
                    rest=i%index_max
                    print(rest)
                    my_index=rest
                    result_list[my_index].append(s[i])
                    i+=1
        result_str=""
        for x in range(len(result_list)):
            s=""
            a=s.join(result_list[x])
            result_str+=a
        return result_str


                            

