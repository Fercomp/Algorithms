class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head2 = Node(99)

def print_ll(h):
    if h is None:
        return
    cur = h
    while cur != None:
        print(cur.val)
        cur = cur.next

print_ll(head)
print_ll(None)
print_ll(head2)

def print_ll_recursive(h):
    if h is None:
        return
    print(h.val)
    print_ll_recursive(h.next)

print_ll_recursive(head)
print_ll_recursive(None)
print_ll_recursive(head2)

# Insert at front O(1) just change some pointers
def insert_front(h, v):
    new = Node(v)
    if h == None:
        return new
    new.next = h
    return new

# Insert at end O(n) traverse until end and change last pointer
def insert_end(h, v):
    new = Node(v)
    if h is None:
        return new
    cur = h
    # Update cur until i find a node with next equal to None (the last ll node)
    while cur.next:
        cur = cur.next
    cur.next = new
    return h

def insert_at_index(h, v, i):
    # Edge case if i want to insert before the first node
    if i < 1:
        return head
    
    new = Node(v)

    # Other edge case, if head is None, i just create a new node
    # and return, independing on the i
    if head == None:
        return new
    
    # Edge case, if i = 1, i just create a new node and add the rest of the list
    # in the end, don't need to traverse anything
    if i == 1:
        new.next = h
        return h
    
    cur = head
    # Range until the last value i want to insert
    for _ in range(1, i-1):
        if cur.next:
            cur = cur.next
        else:
            # Other edge case, when the list is smaller than the i
            # So i just add in the end and return
            cur.next = new
            return head
    
    if cur.next == None:
        cur.next = new
    else:
        n = cur.next
        cur.next = new
        new.next = n
    return head
            
def delete_beginning(h):
    if h is None:
        return None
    n = h.next
    h.next = None
    return n

def delete_end(h):
    # Edge case if head is None
    if h is None:
        return None
    
    # Edge case if head is a single node 
    # we just return None
    if not h.next:
        return None
    
    # I will keep two pointers, current and previus 
    # So wen current arrives in the last node of ll, previus will keep 
    # a reference to the penult
    cur = head
    previus = None
    
    while cur.next:
        # Previus is the current and current if next
        previus = cur
        cur = cur.next
    
    # Delete the penult reference to the last 
    previus.next = None

    return h

def delete_by_position(h, i):
    if i < 1:
        return h
    if i == 1:
        n = h.next
        h.next = None
        return n
    
    cur = h
    for _ in range(1, i):
        return
        
print("*" * 8)
print_ll_recursive(delete_end(head))