'''
GROUP:-B PRACTICAL NO..2
Implement a real-time event processing system using a Queue data structure. The system should support the following features: 
• Add an Event: When a new event occurs, it should be added to the event queue. 
• Process the Next Event: The system should process and remove the event that has      
  been in the queue the longest. 
• Display Pending Events: Show all the events currently waiting to be processed.
 • Cancel an Event: An event can be canceled if it has not been processed.
-----------------------------------------------------------------------------------------
Name:- Deore Om Yashwant
Roll No.:- 29
Batch:- SEA-2

'''
from collections import deque
class Q_demo:
	def __init__(self):
		self.q=deque()
	def add_event(self,event):
		self.q.append(event)
		print(f"Event '{event}' is added")
	def process(self):
		if self.q:
			evnt = self.q.popleft()
			print(f"Event {evnt} is processed")
		else:
			print("Event is already Processed")
	def cancel_event(self,evnt):
		if evnt in self.q:
			self.q.remove(evnt)
			print(f"Event {evnt} is Canceled")
		else:
			print(f"Event {evnt} is already processed or not in Queue")
	def display(self):
		print(f"Events in Queue:- {self.q}")
	def menu(self):
		while True:
			print("1. Add Event.")
			print("2. Processed Event")
			print("3. Cancel Event")
			print("4. Display Events")
			print("5. EXIT!!")
			choice = int(input("Enter your Choice:- "))
			if(choice==1):
				event = input("Enter Events you want to add:- ")
				self.add_event(event)
			elif(choice==2):
				self.process()
			elif(choice==3):
				evnt = input("Enter event you want to cancel:- ")
				self.cancel_event(evnt)
			elif(choice==4):
				self.display()
			elif(choice==5):
				print("!!!EXIT!!!")
				break
obj = Q_demo()
obj.menu()