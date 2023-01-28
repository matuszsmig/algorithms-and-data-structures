from queue import PriorityQueue

kolejkaE = PriorityQueue()

kolejkaE.put((2, 4))
kolejkaE.put((1, 3))
kolejkaE.put((5, 7))
kolejkaE.put((3, 90))


while kolejkaE:
    print(kolejkaE.get()[0])