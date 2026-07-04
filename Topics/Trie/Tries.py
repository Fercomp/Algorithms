# Class definition of a Trie node
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False

root = TrieNode()

# Insert function O(n)
def insert(root, word):
    # Pointer to traverse the trie
    current = root

    for w in word:
        # Calculate the children index of the current letter in the trie array
        index = ord(w.lower()) - ord("a")

        # If i don't have nothing there i need to create a new TrieNode
        if current.children[index] == None:
            current.children[index] = TrieNode()
        
        # change current to the new Trie node
        current = current.children[index]

    # When we finish the word whe set the isWord flag to true
    current.isWord = True

# Search funciton O(n)
def search(root, word):
    # Pointer to traverse the trie
    curr = root

    for w in word:
        # Get index of letter
        index = ord(w.lower()) - ord("a")

        # If i don't have the index already return False 
        if curr.children[index] == None:
            return False
        
        curr = curr.children[index]

    return curr.isWord

# Is Prefix checker O(n)
# Is the same logic of search, but i don't need to end in a node with isWord
# i just need to have all the char
def isPrefix(root, word):
    curr = root
    for w in word:
        index = ord(w.lower()) - ord("a")
        if curr.children[index] is None:
            return False
        curr = curr.children[index]
    return True

insert(root, "Fer")
insert(root, "Foot")
insert(root, "Dad")

print(search(root, "Fer"))  # True
print(search(root, "Fe"))   # False
print(isPrefix(root, "Fe")) # True