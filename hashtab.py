class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def findHash(self, key):
        n = len(key)
        p = 31
        m = int(1e9 + 7)

        hashVal = 0
        pPow = 1

        for i in range(n):
            hashVal = (hashVal + (ord(key[i]) - ord('a') + 1) * pPow) % m
            pPow = (pPow * p) % m
        return hashVal % self.capacity
    
    def insert(self, key, value):
        index = self.findHash(key)

        if self.table[index] is None:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    def search(self, key):
        index = self.findHash(key)

        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next

        raise KeyError(key)


    def __str__(self):
        elements = []
        for i in range(self.capacity):
            current = self.table[i]
            while current:
                elements.append((current.key, current.value))
                current = current.next
        return str(elements)
    
    def __len__(self):
        return self.size
    
    def __contains__(self, key):
        try:
            self.search(key)
            return True
        except KeyError:
            return False