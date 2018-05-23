#Add an __iter__() method to the HashSet class so the Hash Set can be iterated. For an example, see the LinkedList code from a previous question. Note that you don't have to worry about the order of the elements.

from LinkedList import LinkedList

class HashSet:
    def __init__(self, capacity=10):
        # Create a list to use as the hash table
        self.table = [None] * capacity

    def add(self, item):
        # Find the hash code
        h = hash(item)
        index = h % len(self.table)

        # Check is it empty
        if self.table[index] == None:
            self.table[index] = LinkedList() # Need a new linked list for this entry

        if item not in self.table[index]:
            # Only add it if not already there (this is a set)
            self.table[index].add(item)

    # Provide an iterator function
    def __iter__(self):
        a = [] 
        ptr = None
        for i in range(0,len(self.table)):
            if self.table[i]:
                ptr = self.table[i].head 
                while ptr != None:
                    a.append(ptr.item)
                    ptr = ptr.next
        yield from sorted(a)
            
