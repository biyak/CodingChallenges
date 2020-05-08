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
        child_found = False
        for child in node.children: # look through the nodes children
                                    # for the next letter
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
            child_found = False
    node.is_word = True
    #print(answer_string)

root = TrieNode("")
add(root, "ask")
add(root, "ass")
add(root, "assimilate")
add(root, "assimilater")
add(root, "asinine")
add(root, "be")
add(root, "bear")
add(root, "bearer")
add(root, "broke")

#you have populated the recently used words,
#now given 'as', give two options for autocomplete

def autocomplete(root, phrase: str):
    words = []
    node = root
    autoword = ""
    word = ""

    #get the last node of the phrase
    for letter in phrase:
        for child in node.children:
            if child.char == letter:
                autoword = autoword + letter
                node = child
                if autoword == phrase:
                    options = node.children
    print(options)
    for node in options:
        while node is not Null:
            autoword = autoword + node.char
            if node.is_word == True:
                words.append(autoword)
            
            
##        word = phrase + node.char
##        if node.is_word == True:
##            words.append(word)
##        
##            
##        for child in node.children:
##            word = word + child.char

def autohelp(node:TrieNode, s:str):
    s = s + node.char
    for each 
                            
autocomplete(root, "as")
