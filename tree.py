class Node():
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class Tree():
    def __init__(self,value):
        self.root=Node(value)

    def preorder(self,start,traversal):
        if start==None:
            return
        traversal.append(start.value)
        self.preorder(start.left,traversal)
        self.preorder(start.right,traversal)

        return traversal
    
tree=Tree(3)
tree.root.left=Node(4)
tree.root.right=Node(5)

print(tree.preorder(tree.root,[]))

        