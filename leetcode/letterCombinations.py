import itertools
from itertools import combinations


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_dict = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        num_lst = []
        let_lst = []
        if len(digits) == 1:
            return num_dict[int(digits)]
        elif len(digits) == 0:
            return []

        for i in digits:
            num_lst.append(int(i))
        fst = int(digits[0])

        let_lst = list(num_dict[fst])
        for i in range(1, len(digits)):
            scd_lst = list(num_dict[int(digits[i])])

            # new_lst = list(itertools.product(let_lst, scd_lst))
            new_lst=self.mul_lst(let_lst,scd_lst)
            let_lst = new_lst
        print(let_lst)
        for i in range(len(let_lst)):
            let_lst[i] = ''.join(let_lst[i])
        return let_lst
    def mul_lst(self, lst1,lst2):
        lst=[]
        for i in lst1:
            for j in lst2:
                lst.append(i+j)
        return lst



