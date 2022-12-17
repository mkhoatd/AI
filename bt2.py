#%%
class Tree:
    def __init__(self, data, cost=100000):
        self.data = data 
        self.cost = cost
        self.children = []
        self.parent = None
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    def get_data(self):
        return self.data
    def get_children(self):
        return self.children
    def get_parent(self):
        return self.parent
    def __lt__(self, other):
        return self.cost < other.cost

class Board:
    def __init__(self, data):
        self.data=data
    def __repr__(self):
        bc=self.data
        zero = 'O' if bc[0]==1 else ('X' if bc[0]==2 else ' ')
        one = 'O' if bc[1]==1 else ('X' if bc[1]==2 else ' ')
        two = 'O' if bc[2]==1 else ('X' if bc[2]==2 else ' ')
        three = 'O' if bc[3]==1 else ('X' if bc[3]==2 else ' ')
        four = 'O' if bc[4]==1 else ('X' if bc[4]==2 else ' ')
        five = 'O' if bc[5]==1 else ('X' if bc[5]==2 else ' ')
        six = 'O' if bc[6]==1 else ('X' if bc[6]==2 else ' ')
        seven = 'O' if bc[7]==1 else ('X' if bc[7]==2 else ' ')
        eight = 'O' if bc[8]==1 else ('X' if bc[8]==2 else ' ')
        a=(f"{zero} | {one} | {two} \n")
        b=(f"--|---|---\n")
        c=(f"{three} | {four} | {five} \n")
        d=(f"--|---|---\n")
        e=(f"{six} | {seven} | {eight} \n") 
        return a+b+c+d+e
    def __str__(self):
        bc=self.data
        zero = 'O' if bc[0]==1 else ('X' if bc[0]==2 else ' ')
        one = 'O' if bc[1]==1 else ('X' if bc[1]==2 else ' ')
        two = 'O' if bc[2]==1 else ('X' if bc[2]==2 else ' ')
        three = 'O' if bc[3]==1 else ('X' if bc[3]==2 else ' ')
        four = 'O' if bc[4]==1 else ('X' if bc[4]==2 else ' ')
        five = 'O' if bc[5]==1 else ('X' if bc[5]==2 else ' ')
        six = 'O' if bc[6]==1 else ('X' if bc[6]==2 else ' ')
        seven = 'O' if bc[7]==1 else ('X' if bc[7]==2 else ' ')
        eight = 'O' if bc[8]==1 else ('X' if bc[8]==2 else ' ')
        a=(f"{zero} | {one} | {two} \n")
        b=(f"--|---|---\n")
        c=(f"{three} | {four} | {five} \n")
        d=(f"--|---|---\n")
        e=(f"{six} | {seven} | {eight} \n") 
        return a+b+c+d+e
bc=[1,0,0,2,2,1,0,1,0]
A=Tree(Board(bc))