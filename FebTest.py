# College Library 

def libraryproblem(arr, n, m, curr_min):
    studentsRequired = 1
    sum = 0
    for i in range(n):
        if (arr[i] > curr_min):
            return False
        if (sum + arr[i] > curr_min):
            studentsRequired += 1
            sum = arr[i]
            if (studentsRequired > m):
                return False
        else:
            sum += arr[i]
    return True
def findPages(arr, n, m):
    sum = 0
    if (n < m):
        return -1
    for i in range(n):
        sum += arr[i]
    start, end = 0, sum
    result = 10**9
    while (start <= end):
        mid = (start + end) // 2
        if (libraryproblem(arr, n, m, mid)):
            result = min(result, mid)
            end = mid - 1
        else:
            start = mid + 1
    return result
arr = input().split()
new = [int(x) for x in arr]
n = len(arr)
m = int(input())
print(findPages(new, n, m))



# Remove Duplicate Linkedlist


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList(object):
    def __init__(self, data):
        self.data = None
        self.head = None
        self.next = None
        self.length = 0
        if type(data) == type(str()):
            arr = [int(x) for x in data.strip().split()]
        elif type(data) == type(int()):
            arr = [data]
        elif type(data) == type(list()):
            arr = data
        else:
            return self.head
        for x in arr:
            self.append(x)
    def insert(self, data, index=0):
        node = Node(data)
        if index > self.length:
            index = self.length
        self.length += 1
        if self.head == None:
            self.next = self.head = node
            return self.head
        if index == 0:
            node.next = self.head
            self.head = node
            return self.head
        if index == self.length-1:
            self.next.next = node
            self.next = node
            return self.head
        Headdupli = self.head
        for x in range(1, index):
            Headdupli = Headdupli.next
        node.next, Headdupli.next = Headdupli.next, node
        return self.head
    def append(self, data):
        self.insert(data, self.length)
    def remove(self, index=0):
        if self.length == 0:
            return None
        if index >= self.length:
            index = self.length-1
        self.length -= 1
        if self.head == self.next:
            data = self.head.data
            self.head = self.next = None
            return data
        if index == 0:
            data = self.head.data
            self.head = self.head.next
            return data
        currentPtr = self.head
        for ind in range(index-1):
            currentPtr = currentPtr.next
        if currentPtr.next == self.next:
            data = self.next
            self.next = currentPtr
            currentPtr.next = None
            return data
        data = currentPtr.next.data
        currentPtr.next = currentPtr.next.next
        return data
inp = input()
myList = LinkedList(inp)
currentNode = myList.head
while currentNode and currentNode.next:
    if currentNode.data == currentNode.next.data:
        currentNode.next = currentNode.next.next
    else:
        currentNode = currentNode.next
Headdupli = myList.head
while Headdupli:
    print(Headdupli.data, end=" ")
    Headdupli = Headdupli.next

# Giant Numbers

num1, num2 =map(int,input().split())
result = num1 * num2
print(result)
