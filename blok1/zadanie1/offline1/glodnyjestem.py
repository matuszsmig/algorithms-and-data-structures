def counting(T,itr):
    print(T)
    tablica = [0]*25
    for i in range(len(T)):
        tablica[ord(T[i][itr])-97]+=1
    for i in range(1,len(tablica)):
        tablica[i]+=tablica[i-1]
    tabtoreturn = [0]*(len(T))
    for i in range(len(T)-1,-1,-1):
        tabtoreturn[tablica[ord(T[i][0])-97]-1]=T[i]
        tablica[ord(T[i][0])-97]-=1
    for i in range(len(T)):
        T[i]=tabtoreturn[i]
    return T

def radixsort(T):
    maxx = 0
    for i in range(len(T)):
        if len(T[i])>maxx:
            maxx = len(T[i])
    itr = -1
    for i in range(maxx):
        counting(T,itr)
        itr-=1
    return T

#print(ord("a")) 97
#print(ord("z")) 122
T = ["cathedral", "arise", "content", "prejudice", "dozen", "interrupt", "reality", "mirror", "domination", "aluminium", "brave", "temptation", "business", "growth", "first", "trip", "contract", "cucumber", "treaty", "building", "delicate", "evolution", "tumour", "bind", "myth", "cat", "revise", "winner", "stretch", "know", "crown", "venture", "crystal", "tray", "me", "winter", "comprehensive", "mouth", "carry", "transport", "to", "appendix", "missile", "sword", "eagle", "pig", "coverage", "craftsman", "comedy", "democratic", "behead", "translate", "gregarious", "fashionable", "mathematics", "train", "fault", "village", "exclusive", "network", "exile", "transmission", "opposed", "parameter", "calculation", "bronze", "tie", "indulge", "eliminate", "sunday", "chimpanzee", "dribble", "swell", "related", "cat", "fitness", "theme", "frighten", "assume", "page", "delete", "ready", "rape", "embrace", "division", "adviser", "tissue", "determine", "driver", "rise", "frown", "spin", "tired", "party", "question", "excavation", "graduate", "garlic", "cooperation", "exhibition", "bind", "satellite", "day", "relation", "basketball", "voyage", "jet", "flex", "promotion", "ballot", "highlight", "result", "impress", "discovery", "drop", "theorist", "embryo", "superintendent", "river", "contribution", "decline", "rare", "margin", "tell", "slam", "credit", "temple", "ritual", "conspiracy", "lemon", "material", "remark", "groan", "interrupt", "contrast", "resignation", "bare", "enjoy", "abridge", "onion", "poetry", "despise", "directory", "bake", "oh", "split", "rumor", "motorcycle", "tasty", "popular" ]
print(radixsort(T))
