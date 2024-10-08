"""
author : adel.beghdadi@edu.esiee.fr
"""


FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    liste = []
    with open(filename,'r',encoding='utf-8') as f:
        for j in f:
            listen = []
            c = ''
            for l in j:
                if not l.isdigit():
                    listen.append(int(c))
                    c = ''
                else:
                    c += l
            liste.append(listen)
    return liste

def get_list_k(data, k):
    """retourne la k-ème ligne d'une liste de liste

    Args:
        data (list): la liste à traiter
        k (int) : le numéro de la liste à traiter
    Returns:
        l: la liste qui contient la k-ème ligne de la liste data
    """
    l = data[k]
    return l

def get_first(l):
    """retourne le premier élément d'une liste

    Args:
        l (list): la liste à traiter

    Returns:
        l[0]: le premier élément de la liste
    """
    return l[0]

def get_last(l):
    """retourne le dernier élément d'une liste
    Args:
        l (list): la liste à traiter

    Returns:
        l[-1]: le dernier élément de la liste
    """
    return l[-1]

def get_max(l):
    """retourne le maximum des valeurs d'une liste

    Args:
        l (list): la liste à traiter

    Returns:
        max(l): le maximum des entiers de la liste
    """
    return max(l)

def get_min(l):
    """retourne le minimum des valeurs d'une liste

    Args:
        l (list): la liste à traiter

    Returns:
        min(l): le minimum des entiers de la liste
    """
    return min(l)

def get_sum(l):
    """retourne la somme des valeurs d'une liste

    Args:
        l (list): la liste à traiter

    Returns:
        sum(l): la somme des entiers de la liste
    """
    return sum(l)


#### Fonction principale


def main():
    """Fonction principale

    Args:
        Null : aucun argument

    Returns:
        main : ne retourne rien
    """
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))
    print(get_first(get_list_k(data, 37)))
    print(get_last(get_list_k(data, 37)))
    print(get_max(get_list_k(data, 37)))
    print(get_min(get_list_k(data, 37)))
    print(get_sum(get_list_k(data, 37)))
if __name__ == "__main__":
    main()
