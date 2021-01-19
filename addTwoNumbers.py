# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution():
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ##num1
        num1=[]
        num2=[]
        list1=l1
        list2=l2
        s=""
        while True:
        	if list1!=None:
        	
        		num1.insert(0,str(list1.val))
        		list1=list1.next
        	if list2!=None:
        		num2.insert(0,str(list2.val))
        		list2=list2.next
        	if list1==None and list2==None:
        		break
       	num1=s.join(num1)
       	num2=s.join(num2)
       	sum_raw=int(num1)+int(num2)
       	sum_list=ListNode(0)
        res = [int(x) for x in str(sum_raw)]
        print(res)
        
        new_l=sum_list######### this means new_l is pointing to sum_list, while sum_list is unaffected
        				##### which means the left side is affected, the right side is being referred, 
        				##### is thus not affected.
        
        
        #############problem: how to keep the head of the linked list
       	for i in reversed(res):
            
            new_l.next=ListNode(i)
            new_l=new_l.next
       	return sum_list.next



