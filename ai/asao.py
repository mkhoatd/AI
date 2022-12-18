from collections import defaultdict
from queue import PriorityQueue

data = defaultdict(list)
data['S'] = ['A', 5, 'B', 6, 'C', 5, 12]
data['A'] = ['D', 6, 'E', 7, 9]
data['B'] = ['F', 3, 'G', 4, 8]
data['C'] = ['H', 6, 'K', 4, 7]
data['D'] = ['M', 5, 'N', 8, 6]
data['E'] = ['I', 8, 5]
data['F'] = ['J', 4, 'L', 4, 4]
data['K'] = ['Z', 2, 3]
data['G'] = [10]
data['H'] = [10]
data['M'] = [9]
data['N'] = [10]
data['I'] = [6]
data['J'] = [0]
data['L'] = [0]
data['Z'] = [8]

class Node:
    def __init__(self, name, par=None, g=0, h=0):
        self.name = name
        self.parent = par
        self.g = g
        self.h = h
    def __lt__(self, other):
        if other == None:
            return False
        return self.g + self.h < other.g + other.h
    def __eq__(self, other):
        if other == None:
            return False
        return self.name == other.name
    
def equal(O, G):
    return O.name == G.name
    
def In(tmp, c):
    if tmp == None:
        return False
    return (tmp in c.queue)

def Path(O):
    print(O.name)
    if O.parent != None:
        Path(O.parent)
    else:
        return
    
def AStar(S=Node('S'), G=Node('I')):
    Frontier = PriorityQueue()
    Explored = PriorityQueue()
    S.h = data[S.name][-1] # ham heuristic cua trang thai S
    Frontier.put(S)
    while True:
        if Frontier.empty() == True:
            print('Tim kiem that bai')
            return
        O = Frontier.get() # lay trang thai co f min trong Frontier
        Explored.put(O) # dua trang thai vua lay ra khoi Frontier vao Explored
        print('Duyet: ', O.name, O.g, O.h)
        if equal(O, G) == True: # kiem tra xem trang thai O co bang trang thai dich G hay khong
            print('Tim kiem thanh cong')
            Path(O) # in duong di tu trang thai S den trang thai O
            print("Khoang cach: ", O.g+O.h) # in khoang cach cua trang thai O
            return
        i = 0
        while i < len(data[O.name])-1: # lap qua cac trang thai con cua trang thai O
            name = data[O.name][i] # lay ten trang thai con
            g = O.g + data[O.name][i+1] # tinh khoang cach tu trang thai S den trang thai con
            h = data[name][-1] # tinh ham heuristic cua trang thai con
            tmp = Node(name=name, g=g, h=h) # tao node moi
            tmp.parent = O # gan node cha cua node moi la node O
            tmp_in_Open = In(tmp, Frontier) # kiem tra xem trang thai con co nam trong Frontier hay khong
            tmp_in_Explored = In(tmp, Explored) # kiem tra xem trang thai con co nam trong Explored hay khong
            if not tmp_in_Open and not tmp_in_Explored: # neu trang thai con khong nam trong Frontier va Explored
                Frontier.put(tmp) # them trang thai con vao Frontier
            i += 2
AStar()