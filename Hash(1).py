class HashTable:
	def __init__(self,size=10): 
	    self.size = size
	    self.table = [[] for _ in range (size)]
	
	def hash_function(self,key):
	    return key % self.size
	def insert(self,key):
	    index = self.hash_function(key)
	    if key not in self.table[index]:
	        self.table[index].append(key)
	def srch(self,key):
	    index = self.hash_function(key)
	    return key in self.table[index]
	def delete(self,key):
	    index = self.hash_function(key)
	    if key in self.table[index]:
	        self.table[index].remove(key)
	        return True
	    return False
	def display(self):
	    for i,bucket in enumerate(self.table):
	        print(f"Index {i} : {bucket} ")
	def menu(self):
	    while True:
	        print("-----------------------MENU-----------------------")
	        print("1. Insert")
	        print("2. Search")
	        print("3. Delete")
	        print("4. Display")
	        print("5. Exit")
	        choice = int(input("Enter your Choice:- "))
	        if choice==1:
	            key = int(input("Enter Key to Insert:- "))
	            self.insert(key)
	        elif choice==2:
	            key = int(input("Enter Key to Search: -"))
	            res= self.srch(key)
	            if res:
	                print("Key is Found")
	            else:
	                print("Key is Not Found")
	        elif choice==3:
	            key = int(input("Enter Key to Delete: -"))
	            res= self.delete(key)
	            if res:
	                print("Key is Deleted")
	            else:
	                print("Key is Not Found")
	        elif choice == 4:
	            self.display()
	        else:
	            print("EXITING>>>>>>>>>>")
	            break
ht = HashTable()
ht.menu()
