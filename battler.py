#Christopher Kazakis, ck7aj
import pandas as pd
import pokemondata as pkd
moves_list = pkd.get_moves()
status_list = pkd.status_moves()
pokemon_list = pkd.poke_list()
type_matrix = pkd.poke_types()
import random as rd
import re

preset_moves = {
    'Weezing': ('Sludge', 'Zap Cannon', 'Selfdestruct', 'Haze'),
    'Rhyhorn': ('Earthquake', 'Rollout', 'Iron Tail', 'Scary Face'),
    'Rhydon': ('Dig', 'Stomp', 'Zap Cannon', 'Scary Face'),
    'Chansey': ('Egg Bomb', 'Blizzard', 'Dream Eater', 'Sing'),
    'Tangela': ('Giga Drain', 'Thief', 'Sleep Powder', 'Growth'),
    'Kangaskhan': ('Dizzy Punch', 'Bite', 'Surf', 'Leer'),
    'Horsea': ('Hydro Pump', 'Blizzard', 'Rain Dance', 'Smokescreen'),
    'Seadra': ('Surf', 'Dragonbreath', 'Swift', 'Smokescreen'),
    'Goldeen': ('Surf', 'Horn Attack', 'Horn Drill', 'Supersonic'),
    'Seaking': ('Waterfall', 'Flail', 'Horn Drill', 'Supersonic'),
    'Staryu': ('Psychic', 'Hydro Pump', 'Thunder', 'Recover'),
    'Starmie': ('Waterfall', 'Zap Cannon', 'Rapid Spin', 'Harden'),
    'Mr. Mime': ('Psybeam', 'Barrier', 'Baton Pass', 'Substitute'),
    'Scyther': ('Wing Attack', 'Pursuit', 'Swift', 'Focus Energy'),
    'Jynx': ('Ice Punch', 'Confusion', 'Lick', 'Mean Look'),
    'Electabuzz': ('Thunderpunch', 'Swift', 'Light Screen', 'Leer'),
    'Magmar': ('Fire Punch', 'Smog', 'Smokescreen', 'Confuse Ray'),
    'Pinsir': ('Fury Cutter', 'Vicegrip', 'Submission', 'Focus Energy'),
    'Tauros': ('Take Down', 'Pursuit', 'Rock Smash', 'Scary Face'),
    'Magikarp': ('Tackle', 'Flail', 'Splash'), 
    'Gyarados': ('Waterfall', 'Dragon Rage', 'Twister', 'Leer'),
    'Lapras': ('Whirlpool', 'Icy Wind', 'Perish Song', 'Mist'),
    'Ditto': (),
    'Eevee': ('Take Down', 'Iron Tail', 'Shadow Ball' 'Sand-attack'),
    'Vaporeon': ('Waterfall', 'Quick Attack', 'Acid Armor', 'Sand-attack'),
    'Jolteon': ('Zap Cannon', 'Pin Missile', 'Double Kick', 'Sand-attack'),
    'Flareon': ('Fire Blast', 'Smog', 'Quick Attack', 'Tail Whip'),
    'Porygon': ('Tri Attack', 'Blizzard', 'Shrapen', 'Conversion 2'),
    'Omanyte': ('Surf', 'Ancientpower', 'Blizzard', 'Protect'),
    'Omastar': ('Water Gun', 'Ancientpower', 'Spike Cannon', 'Bite'),
    'Kabuto': ('Rollout', 'Giga Drain', 'Blizzard', 'Attract'),
    'Kabutops': ('Ancientpower', 'Surf', 'Leer', 'Endure'),
    'Aerodactyl': ('Ancientpower', 'Bite', 'Curse', 'Supersonic'),
    'Snorlax': ('Headbutt', 'Fire Punch', 'Defense Curl', 'Curse'),
    'Articuno': ('Blizzard', 'Peck', 'Agility', 'Mist'),
    'Zapdos': ('Thunder', 'Rock Smash', 'Flash', 'Detect'),
    'Moltres': ('Fire Blast', 'Sky Attack', 'Roar', 'Endure'),
    'Dratini': ('Outrage', 'Headbutt', 'Safeguard', 'Thunder Wave'),
    'Dragonair': ('Outrage', 'Headbutt', 'Fire Blast', 'Thunder Wave'),
    'Dragonite': ('Twister', 'Wing Attack', 'Dragon Rage', 'Leer'),
    'Mew': ('Psychic', 'Ancientpower', 'Metronome', 'Flash')}
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
        print(pokemon_list[name].keys)
        self.hp = pokemon_list[name]['HP']
        self.t1 = pokemon_list[name]['Type1']
        self.t2 = pokemon_list[name]['Type2']
        self.atk = pokemon_list[name]['Attack']
        self.spatk = pokemon_list[name]['Sp. Atk']
        self.defe = pokemon_list[name]['Defense']
        self.spdefe = pokemon_list[name]['Sp. Def']
        self.speed = pokemon_list[name]['Speed']
        self.faint = False
        self.confused = False
        self.status = ""

class Trainer:
    def __init__(self, party1, party2, party3):
        self.party1 = party1
        self.party2 = party2
        self.party3 = party3
        self.defeated = False
        self.active_pk = party1

    def swtich(self, new):
        self.active_pk = new

def apply_status(attacker, defender, move):
    text = status_list[move]['Effect']
    
    percent = 1.00

    keyword_percent = re.search("\d+?%", text)
    if (keyword_percent):
        percent = float(keyword_percent.group().strip('%'))/100
        
        keyword_burn = re.search("burn", text)
            if keyword_burn and rd.random() < percent and defender.status is "":
                defender.status = "Burn"

        keyword_freeze = re.search("freeze", text)
            if keyword_freeze and rd.random() < percent and defender.status is "":
                defender.status = "Freeze"

        keyword_paralyze = re.search("paralyze", text)
            if keyword_paralyze and rd.random() < percent and defender.status is "":
                defender.status = "Paralyze"

        keyword_poison = re.search("poison", text)
            if keyword_poison and rd.random() < percent and defender.status is "":
                defender.status = "Poison"
        
        keyword_flinch = re.search("flinch", text)
            if keyword_flinch and rd.random() < percent and defender.status is "":
                defender.status = "Flinch"
        


def attack(attacker, defender, move):
    power = moves_list[move]['Power']
    if power == 'None':
        power = 0
    dm = 0

    apply_status(attacker, defender, move)

    #attack defense coefficient based on move category
    if moves_list[move]['Category'] == 'Physical':
        dm = attacker.atk/defender.defe
    elif moves_list[move]['Category'] == 'Special':
        dm = attacker.spatk/defender.spdefe
    elif moves_list[move]['Category'] == 'Status':
        return 0
    else:
        print(moves_list[move]['Category'])
        print('DAMAGE CATEGORY ERROR')

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
    print(attacker.name + ' used ' + o + '!')
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
    print(attacker.name + ' used ' + move + '!')
    return move

def versusone(pa, pb, a_decsion=random_move, b_decision=random_move):
    if pa.faint:
        print(pa.name + ' versus ' + pb.name)
        print(pb.name + ' wins!')
        return 0
    if pb.faint:
        print(pa.name + ' versus ' + pb.name)
        print(pa.name + ' wins!')
        return 1
    if pa.speed > pb.speed:
        attack(pa, pb, a_decsion(pa, pb))
        attack(pb, pa, b_decision(pb, pa))
    else:
        attack(pb, pa, random_move(pb, pa))
        attack(pa, pb, random_move(pa, pb))
    return versusone(pa, pb)

def Trainer_battle():
    pass

print(versusone(random_pokemon(), random_pokemon(), a_decsion=type_agent))
