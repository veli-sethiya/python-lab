class ap:
    pass
class person:
    age=10
    def greet(self):
        print("hello")
obj=person()
print(obj.age)
obj.greet()

class pk:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("name ="+ self.name)
        print("age =" , self.age)
obj1=pk("amit",21)
obj1.show()

class MyClass:
  x = 8
p1 = MyClass()
print(p1.x)

class Queue:
  queue = list()
  def addtoq(self, dataval):
      if dataval not in self.queue:
          self.queue.insert(0, dataval)
          return True
      return False

  def size(self):
    return len(self.queue)

TheQueue = Queue()
TheQueue.addtoq("Mon")
TheQueue.addtoq("Tue")
TheQueue.addtoq("Wed")
print(TheQueue.size())

#stack
class Stack:
  def __init__(self):
    self.stack = []
  def add(self, dataval):
    if dataval not in self.stack:
      self.stack.append(dataval)
      return True
    else:
      return False
  def peek(self):
    return self.stack[-1]
AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.peek()
print(AStack.peek())
AStack.add("Wed")
AStack.add("Thu")
print(AStack.peek())