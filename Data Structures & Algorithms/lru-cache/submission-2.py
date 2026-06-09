class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity 
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.back = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            node.remove()
            self.insert(node)
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.remove()
            self.insert(node)
            node.val = value
        else:
            node = Node(value,key)
            self.cache[key] = node
            self.insert(node)
            if len(self.cache) > self.capacity:
                lru = self.tail.back
                del self.cache[lru.key]
                lru.remove()
    
    def insert(self, node: Node) -> None:
        tmp = self.head.next
        self.head.next = node
        node.back = self.head
        node.next = tmp
        tmp.back = node 

    

        
class Node:

    def __init__(self, val=0, key=0, next=None, back=None):
        self.val = val
        self.key = key
        self.next = next 
        self.back = back
    
    def remove(self) -> None:
        self.back.next = self.next 
        self.next.back = self.back

