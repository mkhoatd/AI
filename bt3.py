#%%
class Node:
    def __init__(self, name):
        self.name=name
        self.children=[]
    def addChild(self, list):
        for c in list:
            self.children.append(c)

def DFS(initialState, goal):
    frontier=[initialState]
    explorerd=[]
    while frontier:
        state=frontier.pop()
        explorerd.append(state)
        if goal==state.name:
            return explorerd
        for child in state.children:
            if child not in (explorerd and frontier):
                frontier.append(child)

    return False

nodeS = Node("S")
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")
nodeH = Node("H")
nodeS.addChild([nodeA,nodeB,nodeC])
nodeA.addChild([nodeD])
nodeB.addChild([nodeD,nodeE,nodeG])
nodeC.addChild([nodeE])
nodeD.addChild([nodeF])
nodeE.addChild([nodeF,nodeH])
nodeF.addChild([nodeG])
nodeH.addChild([nodeG])

result=DFS(nodeS,'G')
if result:
    s='explored '
    for i in result:
        s+=i.name+" "
        print(s)
else:
    print('404 Not Found!')
# %%
# function DFS(initialState, goal):
#     frontier=Stack.new(initialState)
#     explorerd=Set.new()
#     while not frontier.isEmpty():
#         state=frontier.pop()
#         explorerd.add(state)
#         if goal==state.name:
#             return Success(state)
#         for neighbor in state.neighbors:
#             if neighbor not in (explorerd and frontier):
#                 frontier.push(child)

#     return Failure 
#%%


# %%
