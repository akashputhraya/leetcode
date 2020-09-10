# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        trees = [root1,root2]
        trees = [t for t in trees if t]
        return_list = []
        for t in range(len(trees)):
            current_node = trees[t]
            to_process = [current_node]
            while len(to_process)>0:
                if current_node.val is not None:
                    return_list.append(current_node.val)
                    del to_process[0]
                    if current_node.left is not None:
                        to_process.append(current_node.left)
                    if current_node.right is not None:
                        to_process.append(current_node.right)
                if to_process:
                    current_node=to_process[0]
            return_list.sort()
        return return_list