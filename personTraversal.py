class Person:
    def __init__(self, name, children=[]):
        self.name = name
        self.children = children
        
personD = Person("D", [])
personE = Person("E", [])
personF = Person("F", [])

personB = Person("B", [personD,personE,personF])

personG = Person("G", [])
personH = Person("H", [])

personC = Person("C", [personG, personH])

personA = Person("A", [personB,personC])

def extractNames(personHead, branchStack):
    # Keep adding children to branch stack
    branchStack.append(personHead.name)
    if len(personHead.children) == 0:
        print(branchStack)
    for child in personHead.children:
        extractNames(child,branchStack)
        # After going till all children we will remove everything till the parent
        while (branchStack[-1] != personHead.name):
            branchStack.pop(-1)
    return
    
extractNames(personA,branchStack=[])

'''
Output: 
['A', 'B', 'D']
['A', 'B', 'E']
['A', 'B', 'F']
['A', 'C', 'G']
['A', 'C', 'H']
'''