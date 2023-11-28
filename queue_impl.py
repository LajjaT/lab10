# ADD YOUR IMPLEMENTATION OF THE Queue CLASS HERE
class Queue:
    def __init__(self):
        self._elements = [] #this is the queue

    def enqueue(self, elements):
        self._elements.append(elements) #enqueue adds elements (TO BACK)
    
    def front(self):
        if (self!=self.is_empty()): #if the queue isn't empty, return front element
            return self._elements[0]
    
    def dequeue(self):
        if (self!=self.is_empty()): #if queue isn't empty, remove front element
            return self._elements.pop(0)
    
    def is_empty(self):
        if len(self._elements) == 0: #if queue is empty
            return True #return true
        else:
            return False #if not empty, return false
    
    def __str__(self):
        return str(self._elements) #return string of elements

queue = Queue()
print(f'{queue.is_empty() = }')             # True
print(f'empty: {queue}')                    # [ ]
queue.enqueue(10)
print(f'after enqueue(10): {queue}')        # [ 10 ]
print(f'is_empty(): {queue.is_empty()}')    # False
queue.enqueue(1)
print(f'after enqueue(1): {queue}')         # [ 10 1 ]
print(f'dequeue(): {queue.dequeue()}')      # 10
print(f'after dequeue(): {queue}')          # [ 1 ]
queue.enqueue(2)
print(f'after enqueue(2): {queue}')         # [ 1 2 ]
queue.enqueue(3)
print(f'after enqueue(3): {queue}')         # [ 1 2 3 ]
queue.enqueue(4)
print(f'after enqueue(4): {queue}')         # [ 1 2 3 4 ]
print(f'dequeue(): {queue.dequeue()}')      # 1
print(f'after dequeue(): {queue}')          # [ 2 3 4 ]
print(f'dequeue(): {queue.dequeue()}')      # 2
print(f'after dequeue(): {queue}')          # [ 3 4 ]
print(f'dequeue(): {queue.dequeue()}')      # 3
print(f'after dequeue(): {queue}')          # [ 4 ]
print(f'dequeue(): {queue.dequeue()}')      # 4
print(f'after dequeue(): {queue}')          # [ ]
print(f'is_empty(): {queue.is_empty()}')    # True