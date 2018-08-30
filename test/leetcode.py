class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def arr2tree(arr):
    if arr:
        node = TreeNode(arr[0])
        node.left = arr2tree(arr[1:1+(len(arr)-1)/2])
        node.right = arr2tree(arr[1+(len(arr)-1)/2:])
        return node
