#Christopher Kazakis, ck7aj
import pokemondata as pkd
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
pokemon = pkd.poke_list()
type_matrix = pkd.poke_types()

#print(type_matrix[pokemon[i]['Type1']].values())

#Bulbasaur Pikachu Squirtle Charmander Meowth Geodude
#Charmander Clefairy Sandshrew Bulbasaur Pikachu Squirtle
#Oddish Cubone Meowth Psyduck Magnemite Vulpix

typemap = ['Bug', 'Dragon', 'Electric', 'Fighting', 'Fire', 'Flying', 'Ghost', 'Grass', 'Ground', 'Ice', 'Normal', 'Poison', 'Psychic', 'Rock', 'Water']

class AttackQLearningAgent():

    q = torch.tensor(28, 28, 20)

    def __init__(learning_rate):
        self.learning_rate = learning_rate
    
    def get_q(self, md, od):
        md.sort(lambda p: p.atk)
        od.sort(lambda p: p.atk)
        
        

    def update_q():
        

    def pick3(self, my_deck, opponents_deck):
        
        qs = self.get_q(my_deck, opponents_deck)
        chosen = qs.index(max(values))
        
        return my_deck[chosen]
    
    
def trainQ(n):
    ash = AttackQLearningAgent()
    misty = AttackQLearningAgent()
    
    for i in range(n):
        ash_pool = battle.random_party(6)
        misty_pool = battle.random_party(6)
        # I choose you!
        ash_picks = ash.choose3(ash_pool, misty_pool)
        misty_picks = misty.choose(misty_pool, ash_pool)
        
        results = battle.fight(ash_picks, misty_picks)
        
        ash.reward(results)
        misty.reward(-results)
  
      
    
def DeepLearningAgent1(nn.Model):

    def __init__(self):
        super(Model, self).__init__()
        self.lin1 = nn.Linear(72, 32)
        self.lin2 = nn.Linear(32, 32)
        self.lin3 = nn.Linear(32, 28)

    def forward(self, x):
        
        x = torch.flatten(x)
        x = F.relu(self.lin1(x))
        x = F.relu(self.lin2(x))
        x = self.lin3(x)
        
        return x

    def choose3(self, my_pokes, their_pokes):
        x = torch.zeros(12, 5)
        for p in range(0, 6):
            poke = my_pokes[p]
            x[p][0] = typemap.index(poke.t1)
            x[p][1] = typemap.index(poke.t2)
            x[p][2] = poke.hp
            x[p][3] = poke.atk
            x[p][4] = poke.defe
            x[p][5] = poke.speed
        for p in range(6, 12):
            poke = their_pokes[p-6]
            x[p][0] = typemap.index(poke.t1)
            x[p][1] = typemap.index(poke.t2)
            x[p][2] = poke.hp
            x[p][3] = poke.atk
            x[p][4] = poke.defe
            x[p][5] = poke.speed
        



criterion = nn.CrossEntropyLoss()

def trainDeep(n):
    ash = DeepLearningAgent()
    misty = DeepLearningAgent()
    
    ash_optimizer = optim.SGD(ash.parameters(), lr=0.001, momentum=0.9)
    misty_optimizer = optim.SGD(misty.parameters(), lr=0.001, momentum=0.9)

    for i in range(n):
        ash_pool = battle.random_party(6)
        misty_pool = battle.random_party(6)
        # I choose you!

        ash_picks = ash.choose3(ash_pool, misty_pool)
        misty_picks = misty.choose3(misty_pool, ash_pool)
        
        results = battle.fight(ash_picks, misty_picks)
        
    
        optimizer.zero_grad()
        ash_loss = criterion(results, 1)
        misty_loss = criterion(results, -1)
        
    

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
