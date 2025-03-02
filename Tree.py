class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)
root.right.right=Node("anu")

def preOrder(root):
    if root==None:
        return
    else:
        print(root.data)
        preOrder(root.left)
        preOrder(root.right)
        
def inOrder(root):
    if root==None:
        return
    else:
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)
        
def postOrder(root):
    if root==None:
        return
    else:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data)
        
preOrder(root)
inOrder(root)
postOrder(root)
        
        
    

