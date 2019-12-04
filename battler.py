#Christopher Kazakis, ck7aj
import pandas as pd
import pokemondata as pkd
moves_list = pkd.moves()
pokemon_list = pkd.poke_list()
type_matrix = pkd.poke_types()
import random as rd

preset_moves = {'Squirtle': ('Surf', 'Ice Beam', 'Growl', 'Quick Attack'),
                'Charmander': ('Ember', 'Flamethrower', 'Dig', 'Leer'),
                'Psyduck': ('Surf', 'Confusion', 'Bubble Beam', 'Hypnosis'),
                'Pikachu': ('Thunder', 'Quick Attack', 'Thunderbolt', 'Body Slam'),
                'Machamp': ('Low Kick', 'Submission', 'Pound', 'Leer'),
                'Sandshrew': ('Dig', 'Earthquake', 'Hyper Fang', 'Slash')}
pool = list(preset_moves.keys())

class Pokemon:
    def __init__(self, pk):
        self.name = pk
        name = pk
        a, b, c, d = preset_moves[name]
        self.m1 = a
        self.m2 = b
        self.m3 = c
        self.m4 = d
        self.hp = pokemon_list[name]['HP']
        self.t1 = pokemon_list[name]['Type1']
        self.t2 = pokemon_list[name]['Type2']
        self.atk = pokemon_list[name]['Attack']
        self.spatk = pokemon_list[name]['Sp. Atk']
        self.defe = pokemon_list[name]['Defense']
        self.spdefe = pokemon_list[name]['Sp. Def']
        self.speed = pokemon_list[name]['Speed']
        self.faint = False

class Trainer:
    def __init__(self, party):
        self.party1 = party[0]
        self.party2 = party[1]
        self.party3 = party[2]
        self.defeated = False
        self.active_pk = self.party1
        self.reserve = [self.party2, self.party3]
        self.party_ct = 3

    def swap(self, idx):
        if idx == False:
            return
        if self.party_ct > 0:
            placeholder = self.active_pk
            self.active_pk = self.reserve[idx]
            self.reserve[idx] = placeholder
            if self.active_pk.faint:
                if idx == 0:
                    self.active_pk = self.reserve[idx+1]
                else:
                    self.active_pk = self.reserve[idx-1]
        else:
            self.defeated = True


def attack(attacker, defender, move):
    power = moves_list[move]['Power']
    if power == 'None':
        power = 0
    dm = 0

    #attack defense coefficient based on move category
    if moves_list[move]['Category'] == 'Physical':
        dm = attacker.atk/defender.defe
    elif moves_list[move]['Category'] == 'Special':
        dm = attacker.spatk/defender.spdefe
    elif moves_list[move]['Category'] == 'Status':
        return 0
    else:
        pass
        #print(moves_list[move]['Category'])
        #print('DAMAGE CATEGORY ERROR')

    atk_t = moves_list[move]['Type']

    tmult = type_matrix[atk_t][defender.t1] # type multiplier
    try:
        b = type_matrix[atk_t][defender.t2]
        tmult = tmult*b
    except:
        pass

    stab = 1

    #Critical hit calculation
    crit = 1
    P = attacker.speed/512
    if rd.random() < P:
        crit = 2

    # same type attack bonus for using a move of your pokemon's type
    if moves_list[move]['Type'] == attacker.t1 or moves_list[move]['Type'] == attacker.t2:
        stab = 1.5
    rmult = rd.randrange(85, 101)/100

    #Miss calculation
    hit = 1
    ac = moves_list[move]['Accuracy']
    if ac == 'None':
        ac = 60
    ac = int(ac)
    if rd.random() > ac/100:
        hit = 0


    damage = ( crit *.2 * int(power) * dm + 2) * rmult * tmult * stab * hit

    defender.hp = defender.hp - damage

    if defender.hp < 0:
        defender.faint = True

def random_pokemon(): # returns a random pokemon
    return Pokemon(rd.choice(pool))

def random_party(n):
    k = n
    party = []
    names = []
    while k > 0:
        p = Pokemon(rd.choice(pool))
        if p.name not in names:
            names.append(p.name)
            party.append(p)
            k -= 1
    party.sort(key=lambda x: x.name)

    return party

def random_move(attacker, defender):
    choose = rd.random()
    if choose < .25:
        o = attacker.m1
    elif choose < .5:
        o = attacker.m2
    elif choose < .75:
        o = attacker.m3
    else:
        o = attacker.m4
    #print(attacker.name + ' used ' + o + '!')
    return o

def type_agent(attacker, defender):
    score = 0
    move = None
    for i in [attacker.m1, attacker.m2, attacker.m3, attacker.m4]:
        power = moves_list[i]['Power']
        if power != 'None':
            power = int(power)
        else:
            power = 10
        atk_t = moves_list[i]['Type']
        tmult = type_matrix[atk_t][defender.t1]
        try:
            b = type_matrix[atk_t][defender.t2]
            tmult = tmult*b
        except:
            pass
        if tmult*power > score:
            score = tmult
            move = i
    #print(attacker.name + ' used ' + move + '!')
    return move

def versusone(pa, pb, a_decsion=random_move, b_decision=random_move):
    if pa.faint:
        #print(pa.name + ' versus ' + pb.name)
        #print(pb.name + ' wins!')
        return 0
    if pb.faint:
        #print(pa.name + ' versus ' + pb.name)
        #print(pa.name + ' wins!')
        return 1
    if pa.speed > pb.speed:
        attack(pa, pb, a_decsion(pa, pb))
        attack(pb, pa, b_decision(pb, pa))
    else:
        attack(pb, pa, random_move(pb, pa))
        attack(pa, pb, random_move(pa, pb))
    return versusone(pa, pb)


def battle_step(pa, pb, a_decsion=random_move, b_decision=random_move, just_swapped_a=False, just_swapped_b=False):
    if pa.faint:
        #print(pa.name + ' fainted!')
        return 0
    if pb.faint:
        #print(pa.name + ' fainted!')
        return 1
    if pa.speed > pb.speed:
        attack(pa, pb, a_decsion(pa, pb))
        attack(pb, pa, b_decision(pb, pa))
    else:
        attack(pb, pa, random_move(pb, pa))
        attack(pa, pb, random_move(pa, pb))

def random_Trainer(You, Opponent):
    current = You.active_pk
    reserve = You.reserve

    if rd.random() > .1:
        if rd.random() > .5:
            return 0
        else:
            return 1
    return False


def battle(You, Opponent, You_decision=random_Trainer, Opponent_decision=random_Trainer, Your_move_decision=random_move, Opponent_move_decision=random_move):
    if You.party_ct == 0:
        return 0
    if Opponent.party_ct == 0:
        return 1
    Y = False
    O = False
    if You.active_pk.faint:
        You.party_ct -= 1
        alternate_1 = You_decision(You, Opponent)
        Y = True
    if Opponent.active_pk.faint:
        Opponent.party_ct -= 1
        alternate_2 = Opponent_decision(Opponent, You)
        O = True
    if Y:
        You.swap(alternate_1)
    if O:
        You.swap(alternate_2)
    s1 = You_decision(You, Opponent)
    s2 = Opponent_decision(Opponent, You)
    You.swap(s1)
    Opponent.swap(s2)
    #print('!!!')
    #print('Yours: ' + You.active_pk.name)
    #print('Yours: ' + str(You.party_ct))
    #print('*****')
    #print('Opponent: ' + Opponent.active_pk.name)
    #print('Opponent: ' + str(Opponent.party_ct))
    #print('!!!')
    battle_step(You.active_pk, Opponent.active_pk, a_decsion=Your_move_decision, b_decision=Opponent_move_decision, just_swapped_a=False, just_swapped_b=False)
    return battle(You, Opponent, You_decision, Opponent_decision, Your_move_decision, Opponent_move_decision)


#battle(Trainer(random_party(3)), Trainer(random_party(3)))

#k = random_party(4)
#for i in k:
#    print(i.name)
