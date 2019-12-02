class TrieNode:
    def __init__(self, char):
        
        self.char = char
        self.children = []
        self.is_word = False
        
def add(root: TrieNode, word: str):
    node = root
    answer_string = ""
    child_found = False

    for letter in word: # for every letter in the word
        for child in node.children: # look through the nodes children
                                    # for the next letter
            child_found = False
            if child.char == letter: # if the letter is in the children nodes
                                     # go to that node and look at IT'S children nodes 
                answer_string = answer_string + letter
                node = child
                child_found = True
                break               # once you've found the child then break out of
                                    # the children nodes and go to the next node
        if not child_found:
            #Then we need to build this tree
            newNode = TrieNode(letter)
            node.children.append(newNode)
            node = newNode
            answer_string = answer_string + letter
    print(answer_string)

root = TrieNode("")
add(root, "ask")
add(root, "assimilate")
add(root, "assimilater")
add(root, "be")
add(root, "bear")
add(root, "bearer")
add(root, "broke")

def ask(string):
    print("I sad")
