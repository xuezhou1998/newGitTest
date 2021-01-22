# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        rt_shts_val, rt_shts_dist=self.find_shortest(root)
        k_val,k_dist=self.find(root,k)
        dist_up=k_shts_dist+rt_shts_dist-1
        k_shts_val,k_shts_dist=self.find_shortest(k)
        if k_shts_dist<dist_up:
            return k_shts_val
        else:
            return rt_shts_val

    def find(self,source,target):
        if source.left==None and source.right==None:
            return source.val,0
        elif source.left==None:
            right_val,right_dist=self.find_shortest(source.right)

            return right_val,right_dist+1
        elif source.right==None:
            left_val,left_dist=self.find_shortest(source.left)
            return left_val,left_dist+1
        else:
            right_val,right_dist=self.find_shortest(source.right)
            left_val,left_dist=self.find_shortest(source.left)
            if right_dist<left_dist:
                return right_val,right_dist+1
            else:
                return left_val,left_dist+1
    def find_shortest(self,source):
        if source.left==None and source.right==None:
            return source.val,0
        elif source.left==None:
            right_val,right_dist=self.find_shortest(source.right)

            return right_val,right_dist+1
        elif source.right==None:
            left_val,left_dist=self.find_shortest(source.left)
            return left_val,left_dist+1
        else:
            right_val,right_dist=self.find_shortest(source.right)
            left_val,left_dist=self.find_shortest(source.left)
            if right_dist<left_dist:
                return right_val,right_dist+1
            else:
                return left_val,left_dist+1


            
        
    def find_down(self,root):
    def find_up(self,root,):
        pass