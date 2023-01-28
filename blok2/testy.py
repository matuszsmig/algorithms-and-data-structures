def lewy(Tab):
    return Tab[1]

Tab = [[4,5,3,4],[4,2,3,1],[2,3,2,1],[1,4,2,2]]
print(sorted(Tab, key = lambda Tab: Tab[1]))