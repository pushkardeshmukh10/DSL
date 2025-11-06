'''
GROUP:-B PRACTICAL NO..1
PROBLEM STATEMENT:--> Implementing a real-time undo/redo system for a text editing application using a Stack data
structure. The system should support the following operations:
• Make a Change: A new change to the document is made.
• Undo Action: Revert the most recent change and store it for potential redo.
• Redo Action: Reapply the most recently undone action.
• Display Document State: Show the current state of the document after undoing or
redoing an action
-----------------------------------------------------------------------------------------
Name:- Deore Om Yashwant
Roll No.:- 29
Batch:- SEA-2
'''
class TextEditor:
    def __init__(self):
        self.document = ""
        self.undo_stack = []
        self.redo_stack = []
    def mke_chng(self, change):
        self.undo_stack.append(self.document)
        self.document += change
        print("\nChange is Done!!! ")
        self.display_state()
    def undo_action(self):
        if (self.undo_stack):
            self.redo_stack.append(self.document)
            self.document=self.undo_stack.pop()
            print("\nUndo Performed!!!")
        else:
            print("\nNo More Action TO Do!*!")
        self.display_state()
    def redo_action(self):
        if (self.redo_stack):
            self.undo_stack.append(self.document)
            self.document=self.redo_stack.pop()
            print("\nRedo Performed!!!")
        else:
            print("\nNo More Action TO Do!*!")
        self.display_state()
    def display_state(self):
        print("Current Document is:- '" +self.document + "'")
    
    def menu(self):
        while True:
            print("\n----------MENU---------")
            print("1. Make a change")
            print("2. Undo\n3. Redo \n4. Display Document")
            print("5. EXIT!!!")
            choice = int(input("Enter your Choice:- "))
            if (choice==1):
                change= input("Enter the Text to edit:- ")
                self.mke_chng(change)
            elif(choice==2):
                self.undo_action()
            elif(choice==3):
                self.redo_action()
            elif(choice==4):
                self.display_state()
            elif(choice==5):
                print("!!!EXIT!!!")
                break 
                
obj = TextEditor()
obj.menu()

'''
----------MENU---------
1. Make a change
2. Undo
3. Redo 
4. Display Document
5. EXIT!!!
Enter your Choice:- 1
Enter the Text to edit:- om

Change is Done!!! 
Current Document is:- 'om'

----------MENU---------
1. Make a change
2. Undo
3. Redo 
4. Display Document
5. EXIT!!!
Enter your Choice:- 1    
Enter the Text to edit:- deore

Change is Done!!! 
Current Document is:- 'omdeore'

----------MENU---------
1. Make a change
2. Undo
3. Redo 
4. Display Document
5. EXIT!!!
Enter your Choice:- 4
Current Document is:- 'omdeore'

----------MENU---------
1. Make a change
2. Undo
3. Redo 
4. Display Document
5. EXIT!!!
Enter your Choice:- 2

Undo Performed!!!
Current Document is:- 'om'

----------MENU---------
1. Make a change
2. Undo
3. Redo 
4. Display Document
5. EXIT!!!
Enter your Choice:- 2

Undo Performed!!!
Current Document is:- ''

----------MENU---------
1. Make a change
2. Undo
3. Redo 
4. Display Document
5. EXIT!!!
Enter your Choice:- 3

Redo Performed!!!
Current Document is:- 'om'

----------MENU---------
1. Make a change
2. Undo
3. Redo 
4. Display Document
5. EXIT!!!
Enter your Choice:- 3

Redo Performed!!!
Current Document is:- 'omdeore'

----------MENU---------
1. Make a change
2. Undo
3. Redo 
4. Display Document
5. EXIT!!!
Enter your Choice:- 3

No More Action TO Do!*!
Current Document is:- 'omdeore'

----------MENU---------
1. Make a change
2. Undo
3. Redo 
4. Display Document
5. EXIT!!!
Enter your Choice:- 5
!!!EXIT!!!

'''
