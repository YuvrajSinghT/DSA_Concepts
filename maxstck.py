class Maxstack():
    def __init__(self):
        self.stack=[]
        self.max=[]

    def push(self,x):
        self.stack.append(x)

        if self.max:
            if x>=self.max[-1]:
                self.max.append(x)
        else:
            self.max.append(x)
        

    def pop(self):
        if self.stack[-1] == self.max[-1] :
           self.max.pop()
        self.stack.pop()

    def top(self):

        return self.stack[-1]
    def getMax(self):
        return self.max[-1]
    
obj=Maxstack()
obj.push(8)
obj.push(10)
obj.pop()
obj.push(7)
obj.push(1)
obj.push(2)

result_top=obj.top()
print(result_top)

result_max=obj.getMax()
print(result_max)