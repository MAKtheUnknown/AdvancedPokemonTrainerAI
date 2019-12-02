#Christopher Kazakis, ck7aj
import pokemondata as pkd

pokemon = pkd.poke_list()
type_matrix = pkd.poke_types()

#print(type_matrix[pokemon[i]['Type1']].values())

#Bulbasaur Pikachu Squirtle Charmander Meowth Geodude
#Charmander Clefairy Sandshrew Bulbasaur Pikachu Squirtle
#Oddish Cubone Meowth Psyduck Magnemite Vulpix

def optimal_pick():
    a, b, c, d, e, f = input("Pokemon:").split()
    max_pokemon = None
    minscore = 999999999
    pool = [a, b, c, d, e, f]
    for i in pool:
        for j in pool:
            for k in pool:
                if i != j and j != k and i != k:
                    l1 = list(type_matrix[pokemon[i]['Type1']].values())
                    try:
                        l4 = type_matrix[pokemon[i]['Type2']].values()
                        for g in range(0, len(l1)):
                            l1[g] = (l1[g] + l4[g]) / 2
                    except:
                        pass
                    l2 = list(type_matrix[pokemon[j]['Type1']].values())
                    try:
                        l5 = type_matrix[pokemon[j]['Type2']].values()
                        for g in range(0, len(l1)):
                            l2[g] = (l2[g] + l5[g]) / 2
                    except:
                        pass
                    l3 = list(type_matrix[pokemon[k]['Type1']].values())
                    try:
                        l6 = type_matrix[pokemon[k]['Type2']].values()
                        for g in range(0, len(l1)):
                            l3[g] = (l3[g] + l6[g]) / 2
                    except:
                        pass
                    cumulative = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    for p in range(0, len(l1)):
                        cumulative[p] = (50-(l1[p]+l2[p]+l3[p]))**2
                    if sum(cumulative) < minscore:
                        minscore = sum(cumulative)
                        max_pokemon = i, j, k
    return max_pokemon

def optimal_counter():
    print("Enter your opponent's Pool:")
    opponent = optimal_pick()


print(optimal_pick())