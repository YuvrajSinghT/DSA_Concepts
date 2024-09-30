class node():
    def __init__(self,value) :
        self.value =value
        self.left =None
        self.right =None

class BinaryTree():
    def __init__(self,value):
        self.root=node(value) 

    def preorder(self,start,traversal):
        if start is None:
            return
        traversal.append(start.value)
        self.preorder(start.left,traversal)
        self.preorder(start.right,traversal)
        
        return traversal
    
    #postorder
    def postorder(self,start,traversal):
        if start is None:
            return
        
        self.postorder(start.left,traversal)
        self.postorder(start.right,traversal)
        traversal.append(start.value)

        return traversal
    
    #inorder
    def inorder(self,start,traversal):
        if start is None:
            return
        
        self.inorder(start.left,traversal)
        traversal.append(start.value)
        self.inorder(start.right,traversal)
        

        return traversal
    

tree=BinaryTree(3)
tree.root.left=node(4)

tree.root.left.left=node(6)
tree.root.left.right=node(7)

tree.root.right=node(5)

tree.root.right.left=node(8)
tree.root.right.right=node(9)

    
print(tree.preorder(tree.root,[]))
print(tree.postorder(tree.root,[]))
print(tree.inorder(tree.root,[]))