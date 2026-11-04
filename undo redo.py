undo_stack= []
redo_stack= []
document= ""

def change (text):
    global document
    undo_stack.append (document)
    document= text
    redo_stack.clear()
    
def undo():
        global document
        if undo_stack:
            redo_stack.append(document)
            document= undo_stack.pop()
            
def redo():
        global document
        if redo_stack:
            undo_stack.append(document)
            document= redo_stack.pop()
            
change("Hello")
change("Hello World")
print("Current:", document)
undo()
print("Undo:", document)
redo()
print("Redo: ", document)