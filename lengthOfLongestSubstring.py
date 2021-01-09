class Solution(object):
	# def lengthOfLongestSubstring(self, s):
	# 	if len(s)==0:
	# 		return 0
	# 	right=0
	# 	left=0
	# 	init=1
	# 	largest_len=0
	# 	if len(s)==1:
	# 		return 1
	# 	else:
	# 		while right<len(s):
	# 			print(left,right)
	# 			left=left+1
	# 			if left==len(s):
	# 				if init>largest_len:
	# 					largest_len=init
	# 				init=1
	# 				right=left
	# 			elif s[left] in s[right:left]:
	# 				myindex=s.index(s[left])
	# 				mylength=abs(myindex-left)+1
	# 				if init>largest_len:
	# 					largest_len=init
	# 				elif mylength>largest_len:
	# 					largest_len=mylength
	# 				init=1
	# 				right=left
	# 			else:
	# 				init+=1
	# 	return largest_len

	# the problem is that you cannot continue the parsing from the left, but to
	# continue the parsing for every element between right and left, refer to  you notes
	def lengthOfLongestSubstring(self,s):
		largest_len=1
		right=0
		left=0
		if len(s)==0:######## s has size 0
			return 0
		elif len(s)==1:######## s has size 1
			return 1
		elif len(s)==2:######## s has size 2
			if s[0]==s[1]:
				return 1
			else:
				return 2
		else:######### s has size 3 or larger
			while True:
				if right==len(s):
					largest_len=max(largest_len,abs(left-right))
					break
				elif right==left:				
					right+=1
				elif s[right] not in s[left:right]:
					right+=1	
				elif s[right] in s[left:right]:
					largest_len=max(largest_len,abs(left-right))
					left+=1
		return largest_len	

				
			



# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Example 4:

# Input: s = ""
# Output: 0
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.
a = Solution()
print(a.lengthOfLongestSubstring("dvxdfe"))
		