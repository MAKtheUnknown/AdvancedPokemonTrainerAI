#Christopher Kazakis, ck7aj
#Michael A. Klaczynski, mak4em
import pokemondata as pkd
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import battler
import random as rand #Let the Lord of Chaos rule!
pokemon = pkd.poke_list()
type_matrix = pkd.poke_types()

#print(type_matrix[pokemon[i]['Type1']].values())

#Bulbasaur Pikachu Squirtle Charmander Meowth Geodude
#Charmander Clefairy Sandshrew Bulbasaur Pikachu Squirtle
#Oddish Cubone Meowth Psyduck Magnemite Vulpix

typemap = ['Bug', 'Dragon', 'Electric', 'Fighting', 'Fire', 'Flying', 'Ghost', 'Grass', 'Ground', 'Ice', 'Normal', 'Poison', 'Psychic', 'Rock', 'Water', 'Fairy']

'''
class AttackQLearningAgent():

    q = torch.tensor(28, 28, 20)

    def __init__(learning_rate):
        self.learning_rate = learning_rate
    
    def get_q(self, md, od):
        md.sort(lambda p: p.atk)
        od.sort(lambda p: p.atk)
        
        

    #def update_q():
        

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
  
'''   
    
class DeepLearningAgent(nn.Module):

    def __init__(self):
        super(DeepLearningAgent, self).__init__()
        self.lin1 = nn.Linear(240, 120)
        self.lin2 = nn.Linear(120, 72)
        self.lin3 = nn.Linear(72, 64)
        self.lin4 = nn.Linear(64, 32)
        self.lin5 = nn.Linear(32, 6)

    def forward(self, x):
        x = torch.flatten(x)
        x = F.softmax(self.lin1(x))
        x = F.softmax(self.lin2(x))
        x = F.softmax(self.lin3(x))
        x = F.softmax(self.lin4(x))
        x = F.softmax(self.lin5(x))
        
        return x

    def input_to_tensor(self, my_pokes, their_pokes):
        x = torch.zeros(12, 20)
        for p in range(0, 6):
            poke = my_pokes[p]
            x[p][typemap.index(poke.t1)] = 1.0
            try:
                x[p][typemap.index(poke.t2)] = 1.0
            except (ValueError):
                x[p][10] = 1.0
            x[p][16] = poke.hp/100
            x[p][17] = poke.atk/100
            x[p][18] = poke.defe/100
            x[p][19] = poke.speed/100
        for p in range(6, 12):
            poke = their_pokes[p-6]
            x[p][typemap.index(poke.t1)] = 1.0
            try:
                x[p][typemap.index(poke.t2)] = 1.0
            except (ValueError):
                x[p][10] = 1.0
            x[p][16] = poke.hp/100
            x[p][17] = poke.atk/100
            x[p][18] = poke.defe/100
            x[p][19] = poke.speed/100
        return x

    def tensor_to_picks(self, tensor, my_pool):
        top3_vals = [0,0,0]
        top3_i = [0,1,2]
        top3 = []
        for i in range(len(tensor)):
            if tensor[i] > min(top3_vals):
                top3_vals[top3_vals.index(min(top3_vals))] = tensor[i]
                top3_i[top3_vals.index(min(top3_vals))] = i
        for i in top3_i:
            top3.append(my_pool[i])
        return top3


criterion = nn.BCELoss()

ash = DeepLearningAgent()
def train_deep(n):
    
    optimizer = optim.SGD(ash.parameters(), lr=0.001, momentum=0.9)

    for i in range(n):
        
        #print(i)
    
        pool1 = battler.random_party(6)
        pool2 = battler.random_party(6)
        # I choose you!

        vals1 = ash(ash.input_to_tensor(pool1, pool2))
        vals2 = ash(ash.input_to_tensor(pool2, pool1))
        
        picks1 = ash.tensor_to_picks(vals1, pool1)
        picks2 = ash.tensor_to_picks(vals2, pool2)
        
        results = torch.tensor(float(battler.battle(battler.Trainer(picks1), battler.Trainer(picks2), battler.Type_Trainer, battler.Type_Trainer, battler.type_agent, battler.type_agent)))
        results.requires_grad = True

        optimizer.zero_grad()

        loss1 = criterion(results, torch.tensor([1.0]))
        loss2 = criterion(results, torch.tensor([0.0]))

        loss1.backward()
        loss2.backward()
        optimizer.step()

        if i%20000 == 0:
            test_deep(50)
    test_deep(500)

        
def test_deep(n):
    wins = 0
    for i in range(n):
        pool1 = battler.random_party(6)
        pool2 = battler.random_party(6)
        team_ash = ash.tensor_to_picks(ash(ash.input_to_tensor(pool1, pool2)), pool1)
        team_rocket = pool2[:3]
        results = torch.tensor(float(battler.battle(battler.Trainer(team_ash), battler.Trainer(team_rocket), battler.Type_Trainer, battler.random_Trainer, battler.type_agent, battler.type_agent)))
        if int(results+.5) == 1:
            wins-=-1
    print(wins/n*100)


train_deep(200000)

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


#print(optimal_pick())
