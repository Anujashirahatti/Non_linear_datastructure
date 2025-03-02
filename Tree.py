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

def height(root):
    if root==None:
        return -1
    elif root!=None and root.left==None and root.right==None:
        return 0
    else:
        return max(height(root.left),height(root.right))+1#root
    
def Counting(root):
    if root==None:
        return 0
    elif root!=None and root==None and root.right==None:
        return 1
    else:
        le=Counting(root.left)        
        rp=Counting(root.right)
        return le+rp+1
    
def countingleaf(root):
    count=0
    if root==None:
        return count
    elif root!=None and root.left==None and root.right==None:
        count+=1
        return count
    else:
        lp=countingleaf(root.left) 
        rp=countingleaf(root.right)
        return lp+rp
        
preOrder(root)
inOrder(root)
postOrder(root)
        
        
    

