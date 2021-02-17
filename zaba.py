# soubor zaba a zk_dominantni_prvek jsou spíše kody na procvičení práce s Pythonem

def solution(X, A):

    """
      "hra", žába skáče přes potok o šířce X pres listy, může přeskákat
      jen když je celá délka zapadaná listy, funkce vrátí čas (index), který
      trvá, než se celá cesta zaplní
    """

    listy = []

    cas = 0
    pocet = 0

    for i in A:
        cas += 1
        if i not in listy:
            listy.append(i)
            pocet += 1
            #cas += 1
            #print(cas)
        if X in listy and pocet == X:
            break
    return cas

print(solution(5, [1, 3, 4, 4, 3, 2, 4, 7, 5]))
