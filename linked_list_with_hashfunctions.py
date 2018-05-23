#Add a method to the HashSet class which will return the average length of the buckets. A bucket is the container which holds all the elements which hash to the same value, which in our case is a linked list. Ignore any entries in the hash table with zero elements. Your method should be called average_bucket_length().

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
   
   
    def average_bucket_length(self):
        t = [] 
        for i in self.table:
            if  i != None: 
                t.append(len(i)) 
                
        average = sum(t)/len(t) 
        return average
        
