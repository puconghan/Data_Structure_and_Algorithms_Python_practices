'''
Access time O(1)
'''

class HashEntry:
	def __init__(self, key, value):
		self.data = value
		self.key = key
	def getkey(self):
		return self.key
	def getvalue(self):
		return self.data

#Open Addressing - Linear probling
class HashTable:
	def __init__(self, size):
		self.size = size
		self.table = [None]*size
	def push(self, key, value):
		entry = HashEntry(key, value)
		hashkey = key % self.size
		while self.table[hashkey] is not None and self.table[hashkey].getkey() != key:
			hashkey = (hashkey + 1) % self.size
		self.table[hashkey] = entry
	def get(self, key):
		hashkey = key % self.size
		while self.table[hashkey] is not None and self.table[hashkey].getkey() != key:
			hashkey = (hashkey + 1) % self.size
		if self.table[hashkey].getkey() == key:
			return self.table[hashkey].getvalue()
		else:
			return None, 'Key not found in hashtable'

'''
#Test cases
hashtable = HashTable(256)
hashtable.push(1, 'hello')
hashtable.push(11, 'world')
print hashtable.get(1), hashtable.get(11)
'''

#Seperate chaining
class HashTable:
	def __init__(self, size):
		self.size = size
		self.table = [None]*size
	def push(self, key, value):
		entry = HashEntry(key, value)
		hashkey = key % self.size
		if self.table[hashkey] is None:
			self.table[hashkey] = entry
		elif isinstance(self.table[hashkey], HashEntry):
			temp = self.table[hashkey]
			self.table[hashkey] = []
			self.table[hashkey].append(temp)
			self.table[hashkey].append(entry)
		else:
			self.table[hashkey].append(entry)
	def get(self, key):
		hashkey = key % self.size
		if self.table[hashkey] is None:
			return None
		elif isinstance(self.table[hashkey], HashEntry):
			return self.table[hashkey].getvalue()
		else:
			for item in self.table[hashkey]:
				if item.getkey() == key:
					return item.getvalue()
			return None, "Not Found"

'''
#Test cases
hashtable = HashTable(256)
hashtable.push(1, 'hello')
hashtable.push(11, 'world')
print hashtable.get(1), hashtable.get(11)
'''
