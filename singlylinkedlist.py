class Node():
    def __init__(self,value):
        self.value=value
        self.next=None

class SinglyLinkedList():
    def __init__(self):
        self.head=None
        self.size=0

    def get(self,index:int):
        if index<0 or index> self.size:
            return-1
        while (index!=0):
            self.head=self.head.next
            index-=1
        return (self.head)
        
    
    def AddAtHead(self,value:int):
        new_node=Node(value)

        if self.head is None:
            self.head=new_node
            self.tail=new_node

        else:
            new_node.next=self.head
            self.head=new_node
        self.size+=1

    def AddAtTail(self,value:int):
        new_node=Node(value)

        if self.tail is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.next=None

        self.size+=1
    
    def DeleteAtHead(self):
        if(self.head==None):
            return -1
        else:
            self.head=self.head.next
        self.size-=1
    '''def DeleteAtIndex(self,index):
        if(index<0 or index>self.size):
            return -1
        elif(index==0):
            self.DeleteAtHead()
        else:
            cur=self.head
            while index!=index-1:
                cur.next=cur.next.next

        self.size-=1
'''
            
obj=SinglyLinkedList()
obj.AddAtHead(10)
obj.AddAtTail(12)
obj.AddAtTail(8)
obj.AddAtTail(9)
obj.AddAtTail(2)

obj.DeleteAtHead()
#obj.DeleteAtIndex(3)
print(obj.get(2))
                
        