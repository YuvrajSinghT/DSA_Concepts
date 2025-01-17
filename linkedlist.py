class Node():
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class LinkedList():
    def __init__(self):
       self.head=None
       self.tail=None
       self.size=0

    def get(self,index:int)->int:
        if index<0 or index>=self.size:
            return -1
        
        cur=self.head

        while index!=0:
            cur=cur.next
            index=index-1
        return cur.value
    
    def addAtHead(self,val:int)->None:
        new_node=Node(val)

        if self.head is None:
            self.head=new_node
            self.tail=new_node

        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node

        self.size+=1
    def  addAtTail(self,val:int)->None:
        new_node=Node(val)

        if self.tail is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.prev=self.tail
            self.tail.next=new_node
            self.tail=new_node

        self.size+=1
    def AddAtAindex(self,index:int,val:int)->None:
        if(index<0 or index>=self.size):
            return 
        
        new_node=Node(val)

        if(index==0):
            self.addAtHead(val)
        elif(index==self.size):
            self.addAtTail(val)
        else:
            cur=self.head
            while index-1 !=0:
                cur=cur.next
                index-=1

            new_node.next=cur.next
            cur.next.prev=new_node
            cur.next=new_node
            new_node.prev=cur

            self.size+=1
    def DeleteAtIndex(self,index:int)->None:
        if(index<0 or index>self.size):
            return -1
        elif(index==0):
            cur=self.head.next
            if cur:
                cur.prev=None
            self.head=self.head.next
            self.size-=1

            if self.size==0:
                self.tail=None
            
        elif(index==self.size-1):
            cur=self.tail.prev
            if cur:
                cur.next=None
            self.tail=self.tail.prev
            self.size-=1

            if(self.size==0):
                self.head==None

        else:
            cur=self.head
            while index-1 !=0:
                cur=cur.next
                index-=1

            cur.next=cur.next.next
            cur.next.prev=cur

            self.size-=1

obj = LinkedList()
obj.addAtHead(10)
obj.addAtTail(15)
obj.addAtTail(20)
obj.DeleteAtIndex(0)
obj.addAtHead(40)
 
print(obj.get(0))







