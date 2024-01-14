# print number form 1 to 100, print Fizz is the number is divisible by 3 and
# print 5 if the number is divisble by Bizz and FizzBuzz if divisible by both
"""
num = 101
for i in range(1, num):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 7 == 0:
         print("Bazz")
    else:
        print(str(i))
"""
"""
class node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = None
class linkedlist:
    def __init__(self, head = None):
        self.head = None
    def addend(self, newvalue):
        newnode = node(newvalue)
        last = self.head
        if not self.head:
            self.head = newnode
            return
        while last.next:
            last = last.next
        last.next = newnode
        newnode.next = self.head
    def addbig(self, newvalue):
        newnode = node(newvalue)

        newnode.next = self.head
        self.head = newnode
    def addmid(self, newvalue, pos):
        newnode = node(newvalue)
        last = self.head
        st = 2
        while st < pos:
            last = last.next
            st += 1
        newnode.next = last.next
        last.next = newnode
    def delete(self, pos):
        last = self.head
        if pos == 1:
            self.head = last.next
            last.next = None
            return
        st = 2
        while st < pos:
            last = last.next
            st += 1
        newnode = last
        last = last.next
        newnode.next = last.next
        last.next = None
    def printit(self):
        if self.head == None:
            print("empty")
            return
        last = self.head
        while last:
          print(last.value)
          last = last.next
    def search(self, val):
        last = self.head
        while last.next:
            if last.value == val:
                return True
            else:
                return False
            last = last.next
addnode = linkedlist()
addnode.addend(5)
addnode.addend(6)
addnode.addend(7)
addnode.addend(8)
addnode.addbig(4)
addnode.addbig(3)
addnode.addmid(5.5, 4)
addnode.delete(1)
answer = addnode.search(9)
addnode.printit()
print(answer)

"""
class node:
    def __init__(self, value = None, next = None, pre = None):
        self.value = value
        self.next = None
        self.pre = None
class linkedlist:
    def __init__(self, head = None):
        self.head = None

    def addend(self, data):
        newnode = node(data)
        if self.head == None:
            last = newnode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newnode
        newnode.pre = last

    def printout(self):
        last = self.head
        while last:
            last = last.next
        while last:
            print(last.value)
            last = last.pre


add = linkedlist()
add.addend(2)
add.addend(3)
add.addend(4)
add.addend(5)
add.printout()













