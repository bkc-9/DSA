queue = []

def add(event):
    queue.append(event)
    print(event, "Added")

def process():
    if queue:
        print("Processed:", queue.pop(0))
    else:
        print("Queue is Empty")

def cancel(event):
    if event in queue:
        queue.remove(event)
        print(event, "Cancelled")
    else:
        print("Event Not Found")

def display():
    print("Pending Events:", queue)


add("Event1")
add("Event2")
add("Event3")

display()
process()
cancel("Event3")
display()