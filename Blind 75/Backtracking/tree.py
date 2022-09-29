class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

########
def serialize(root):
    serialized = ""
    if root is None:
        return ""
        
    stack = []
    stack.append(root)
    while (len(stack) != 0):
        curr = stack.pop()
        
        if curr is None:
            serialized = serialized + "," + "-1"
        else:
            serialized = serialized + "," + str(curr.value)
            stack.append(curr.left)
            stack.append(curr.right)
    
    return serialized


# 1,3,-1,-1,2,-1,-1

def deserialize(serialized):
    if serialized == "":
        return ""
    
    def addNode(arr, i):
        if arr[i] == "-1":
            # i+=1
            return None
        root = Tree(arr[i])
        i+=1
        root.left = addNode(arr,i)
        i+=1
        root.right = addNode(arr,i)
        return root
    
    return addNode(serialized.split(","), i=0)
            
    
tree = Tree(1, Tree(2), Tree(3))

print(serialize(tree))
print(serialize(deserialize("1,3,-1,-1,2,-1,-1")))

# standard 4 way intersection with green, yellow, and red in each direction (4 traffic lights)
#      | | ^ |
#      | | | |
#      | | | |
#      | v | |
# -----+     +-----
# <----  {-}  <----
# ---->  {-}  ---->
# -----+     +-----
#      | | ^ |
#      | | | |
#      | | | |
#      | v | |
#
#
# Light transitions are GREEN -> YELLOW -> RED, then repeat

class Direction(enum):
    north, south, east, west = 1,2,3,4
    
class Colour(enum):
    red, yellow, green = 1,2,3
    
class TrafficLight:
    def __init__(self, direction, colour):
        self.colour = colour
        self.direction = direction
    
    # Get Colour
    # Set Colour
    
    def changeLight(self, colour):
        self.colour = colour
        

class Traffic:
    def __init__(self):
        self.northBound = TrafficLight(Direction.north, Colour.green)
        self.southBound = TrafficLight(Direction.south, Colour.green)
        self.eastBound = TrafficLight(Direction.east, Colour.red)
        self.westBound = TrafficLight(Direction.west, Colour.red)
    
    def run():
        # If true then north/south will change to red
        changeColour = True 
        while True:
            setTimeout(200)
            self.northBound.changeLight(Colour.yellow)
            self.southBound.changeLight(Colour.yellow)
            self.eastBound.changeLight(Colour.yellow)
            self.westBound.changeLight(Colour.yellow)
            setTimeout(200)
            self.northBound.changeLight(changeColour ? Colour.red: Colour.red)
            self.southBound.changeLight(changeColour ? Colour.red)
            self.eastBound.changeLight(changeColour ? redColour)
            self.westBound.changeLight(changeColour ? redColour)
            changeColour = changeColour ? False : True
                
    
run()