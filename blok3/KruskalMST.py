def MST(G):
    Res = Kruskal(G)
    sum = 0
    #print(Res)
    for i in range(len(Res)):
        sum += Res[i][2]
    return sum

def Kruskal(G):
    n= len(G)
    Result = []
    Parent = []
    Rank = []
    i = 0
    e = 0 # len of Result
    for cos in range(n):
        Rank.append(0)
        Parent.append(cos)

    while i < n-1:
        u, v, w = G[i]
        i += 1
        x = u
        y = v
        while x != Parent[x]:
            x = Parent[x]
        while y != Parent[y]:
            y = Parent[y]
        if x!=y:
            e+=1
            Result.append([u,v,w])
            xroot = x
            yroot = y
            while xroot != Parent[xroot]:
                xroot = Parent[xroot]
            while yroot != Parent[yroot]:
                yroot = Parent[yroot]
            if xroot==yroot:
                pass
            elif Rank[xroot] > Rank[yroot]:
                Parent[yroot]=xroot
            else:
                Parent[xroot]=yroot
                if Rank[xroot]==Rank[yroot]:
                    Rank[yroot]+=1
    return Result



G = [[0,1,4],[0,7,8],[1,2,8],[1,7,11],[2,8,2],[2,3,7],[2,5,4],[3,5,14],[3,4,9],[4,5,10],[5,6,2],[6,7,1],[6,8,6],[7,8,7]]
newG = sorted(G, key=lambda x: x[2])
G2 = [[0, 1, 10],[0, 2, 6],[0, 3, 5],[1, 3, 15],[2, 3, 4]]
newG2 = sorted(G2, key=lambda x: x[2])
print(MST(newG))
#[[2, 3, 4], [0, 3, 5], [0, 1, 10]]