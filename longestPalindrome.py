# class Solution():
#     def longestPalindrome(self, s: str) -> str:
#         head=0
#         tail=0
#         max_num=0
#         max_str=""
#         s_reversed=s[::-1]
#         while True:
#             if s[:tail]==s_reversed[tail:]:
                
#                 if max_num<len(s[:tail]):
#                     max_str=s[:tail]
#                     max_num=len(s[:tail])

#             else:
#                 while True:
#                     if len(s[head:tail])<=max_num:
                        
#                         break
#                     else:
                        
#                         if s[head:tail]==s[head:tail][::-1]:
#                             if max_num<len(s[head:tail]):
#                                 max_str=s[head:tail]
#                                 max_num=len(s[head:tail])

#                             break
#                         else:
#                             head+=1
#                     if head>tail:
#                         break
#                 head=0
#             tail+=1
#             if tail>len(s):
#                 break
#             print("max_num",max_num,"s",len(s))
#         return max_str

# class Solution():
#     def longestPalindrome(self, s: str) -> str:
#         left=0
#         right=0
#         head=0
#         max_num=0
#         max_str=""
#         while head<len(s):
#             curr_num=0
#             while left>=0 and right<len(s):
#                 if s[left]==s[right]:
#                     left-=1
#                     right+=1

#                     curr_num+=1

#                     if max_num<curr_num:
#                         max_str=s[left:right+1]
#                 else:

#                     break
            
#             head=right
#             left=right
#         return max_str
class Solution():
    def longestPalindrome(self, s: str) -> str:
        left=0
        right=0
        head=0
        max_num=0
        max_str=""
        if len(s)==1:
            return s
        while head<len(s):
            result1=self.center(s,head,head)
            result2=self.center(s,head,head-1)

            if result1[0]>=result2[0]:
                if max_num>=result1[0]:
                    head=result1[3]+1
                    
                else:
                    max_num=result1[0]
                    head=result1[3]+1
                    max_str=result1[1]
            else:
                if max_num>=result2[0]:
                    head=result2[3]+1
                else:
                    max_num=result2[0]
                    head=result2[3]+1
                    max_str=result2[1]
    def center(self,s,left,right):
        max_str=""

        curr_num=0

        while left>=0 and right<len(s):
            if s[left]==s[right]:
                if left==right:
                    curr_num=1
                elif left==right-1:
                    curr_num=2
                else:
                    curr_num+=2
                max_str=s[left:right+1]
                left-=1
                right+=1

            else:
                break
        # print(curr_num==len(max_str))
        return [curr_num,max_str,left-1,right-1]
                


# a=Solution()

# print(a.longestPalindrome("lipwawibllrziekxgwudqghfpvsafguorthpsdihcinuasyzmttzxdluhrnfdrawabwxdgpoqabfhutzowqfhkynrhobyuygesngyxpjyilqhwyeemklicinmatyishobtitukbkpqtxwioqnztlewilnewokfqkycfuvgqmogwuvkrxphyjvhbkhpcwywfnazsoulmgdoaxyngoynmfexdcpanoyidutpzcicibjnzmybvggqbpbejsvliocotewgrfcwyebisiywjsugjxxwupryxglvkgdugbejsibuscjofrvaeexqweieldfhriftlczbuzmuizjqzxovziflaigwxrxowmhdlvrbxzeaaqxmicvigolodopbukjvkzwvxexnnweodsoscnpmuwgjhmlurwdqbwrzavjjubsueahunqwemmewqnuhaeusbujjvazrwbqdwrulmhjgwumpncsosdoewnnxexvwzkvjkubpodologivcimxqaaezxbrvldhmwoxrxwgialfizvoxzqjziumzubzcltfirhfdleiewqxeeavrfojcsubisjebgudgkvlgxyrpuwxxjgusjwyisibeywcfrgwetocoilvsjebpbqggvbymznjbiciczptudiyonapcdxefmnyognyxaodgmluoszanfwywcphkbhvjyhpxrkvuwgomqgvufcykqfkowenliweltznqoiwxtqpkbkutitbohsiytamnicilkmeeywhqliyjpxygnsegyuybohrnykhfqwoztuhfbaqopgdxwbawardfnrhuldxzttmzysaunichidsphtrougfasvpfhgqduwgxkeizrllbiwawpil"))