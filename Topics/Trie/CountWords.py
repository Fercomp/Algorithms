class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False

def insert(root, word):
    current = root

    for w in word:
        index = ord(w.lower()) - ord("a")
        if current.children[index] == None:
            current.children[index] = TrieNode()
        current = current.children[index]
    current.isWord = True

root = TrieNode()
insert(root, "Fer")
insert(root, "Foot")
insert(root, "Dad")


def count_words(root):
    count = 0

    if root.isWord:
        count += 1

    for w in root.children:
        if w is not None:
            count += count_words(w)

    return count 