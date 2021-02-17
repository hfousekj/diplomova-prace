# soubor zaba a zk_dominantni_prvek jsou spíše kody na procvičení práce s Pythonem
def dominantni(A):

    """ Funkce, která ze zadaného pole určí dominantní prvek,
        tzn. hodnota, která se v poli vyskytuje více než u poloviny
        všech prvků.
        volání např. print(dominantni([1, 2, 3, 1, 4, 1, 1]))
    """

    if len(A) == 0:
        return 'Zadáno prázdné pole'

    A.sort()
    cisla = []

    for i in A:
        if i not in cisla:
            cisla.append(i)

    mnozstvi = 0
    kolikrat = list(range(len(cisla)))
    for i in cisla:
        kolikrat[mnozstvi] = A.count(i)
        mnozstvi += 1

    nejcasteji = max(kolikrat)
    cislo = kolikrat.index(nejcasteji)
    vysledek = A[cislo]

    indexy = []
    for i in range(0, len(A)):
        if vysledek == A[i]:
            vysledek_index = A.index(vysledek)

    if nejcasteji > len(A)//2:
        return vysledek
    else:
        return -1

# priklad volani
print(dominantni([1, 2, 3, 1, 4, 1, 1]))
