# CS2302 Data Structures
# Programmed by Luis Garcia.
# Last modified November 21, 2018.
# Instructor Diego Aguirre.
# Implementation of hashes in order to compare the time complexity
#lab 4

class HTNode(object):

    def __init__(self, item, next):
        self.item = item
        self.next = next

# Zybooks
'''HashInsert(hashTable, item) {
   if (HashSearch(hashTable, item->key) == null) {
      bucketList = hashTable[Hash(item->key)]
      node = Allocate new linked list node
      node->next = null
      node->data = item
      ListAppend(bucketList, node)
   }
}

HashRemove(hashTable, item) {
   bucketList = hashTable[Hash(item->key)]
   itemNode = ListSearch(bucketList, item->key)
   if (itemNode is not null) {
      ListRemove(bucketList, itemNode)
   } 
}

HashSearch(hashTable, key) {
   bucketList = hashTable[Hash(key)]
   itemNode = ListSearch(bucketList, key)
   if (itemNode is not null)
      return itemNode->data
   else
      return null
}
'''


class hashTable:

    def __init__(self, table_size):
        self.size = 0
        self.table = [None] * table_size

    def hashMultiplication(self, word, first_letter):
        return (word * first_letter) % len(self.table)
    '''def hashMultiplication(self, word, first_letter):
        return (word ** first_letter) % len(self.table)
    def hashMultiplication(self, word, first_letter):
        return (word + first_letter) % len(self.table)
    def hashMultiplication(self, word, first_letter):
        return (word - first_letter) % len(self.table)
'''
    def stringToASCII(self, word):
        sum = 0
        for char in word:
            sum += ord(char)
        return sum

# The insert method will insert the word where it corresponds.
    def insert(self, item):
        self.size += 1
        word = self.stringToASCII(item)
        first_letter = self.stringToASCII(item[:1])
        position = self.hashMultiplication(word, first_letter)
        self.table[position] = HTNode(item,self.table[position])


def comparisons(self):
    num_nodes = 0
    num = 0
    for i in range(len(self.table)):
        temp = self.table[i]
        if temp is not None:
            num += 1
        while temp is not None:
            num_nodes += 1
            temp = temp.next
    print('Number of nodes counted:', num)
    print('Total number of nodes:', num_nodes)
    print('Average:', num_nodes / num)


def load_factor(self):
    print('Load Factor:', self.size / len(self.table))


class better_hash_table:
    def __init__(self, table_size):
        self.size = 0
        self.table = [None] * table_size

    def hash_1(self, word):
        init_size = 5381
        for char in word:
            init_size = (init_size * 33) + self.stringToASCII(char)
        return init_size % len(self.table)

    def stringToASCII(self, word):
        sum = 0
        for char in word:
            sum += ord(char)
        return sum

    def insert(self, item):
        self.size += 1
        position = self.hash_1(item)
        self.table[position] = HTNode(item, self.table[position])

    def load_factor(self):
        print('Load Factor:', self.size / len(self.table))

    def comparisons(self):
        num_nodes = 0
        num = 0
        for i in range(len(self.table)):
            temp = self.table[i]
            if temp is not None:
                num += 1
            while temp is not None:
                num_nodes += 1
                temp = temp.next
        print('Number of nodes counted:', num)
        print('Total number of nodes:', num_nodes)
        print('Average:', num_nodes / num)


size = int(input('What is the size of the table?'))
table = hashTable(size)
second_table = better_hash_table(size)
words_file = open('words.txt', 'r')
for line in words_file:
    table.insert(line)
    second_table.insert(line)
print()
print('Hashed with the first hash function:')
table.load_factor()
table.comparisons()
print()
print('Hashed with the second hash function:')
second_table.load_factor()
second_table.comparisons()



