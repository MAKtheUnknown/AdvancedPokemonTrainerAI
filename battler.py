#Christopher Kazakis, ck7aj
import pandas as pd
import pokemondata as pkd
moves_list = pkd.get_moves()
pokemon_list = pkd.poke_list()
type_matrix = pkd.poke_types()
#status_list = pkd.get_status_moves()
import random as rd
import re

preset_moves = {'Bulbasaur': ('Razor Leaf', 'Headbutt', 'Toxic', 'Growth'),
'Ivysaur': ('Solar Beam', 'Fury Cutter', 'Leech Seed', 'Sunny Day'),
'Venusaur': ('Giga Drain', 'Tackle', 'Poison Powder', 'Growl'),
'Charmander': ('Flamethrower', 'Slash', 'Dragon Breath', 'Sunny Day'),
'Charmeleon': ('Fire Blast', 'Strength', 'Dig', 'Smokescreen'),
'Charizard': ('Fire Punch', 'Wing Attack', 'Growl', 'Scary Face'),
'Squirtle': ('Surf', 'Bite', 'Blizzard', 'Rain Dance'),
'Wartortle': ('Waterfall', 'Icy Wind', 'Dig', 'Rapid Spin'),
'Blastoise': ('Hydro Pump', 'Rapid Spin', 'Mud-Slap', 'Withdraw'),
'Caterpie': ('Tackle', 'String Shot', 'Quick Attack', 'Harden'),
'Metapod': ('Harden', 'Harden', 'Harden', 'Harden'),
'Butterfree': ('Gust', 'Psychic', 'Hyper Beam', 'Stun Spore'),
'Weedle': ('Poison Sting', 'String Shot', 'Tackle', 'Pound'),
'Kakuna': ('Harden', 'Harden', 'Harden', 'Harden'),
'Beedrill': ('Twineedle', 'Sludge Bomb', 'Pursuit', 'Focus Energy'),
'Pidgey': ('Fly', 'Return', 'Steel Wing', 'Sand Attack'),
'Pidgeotto': ('Fly', 'Frustration', 'Steel Wing', 'Mirror Move'),
'Pidgeot': ('Fly', 'Swift', 'Steel Wing', 'Whirlwind'),
'Rattata': ('Super Fang', 'Headbutt', 'Shadow Ball', 'Focus Energy'),
'Raticate': ('Super Fang', 'Hyper Fang', 'Pursuit', 'Scary Face'),
'Spearow': ('Drill Peck', 'Frustration', 'Steel Wing', 'Mirror Move'),
'Fearow': ('Drill Peck', 'Hyper Beam', 'Pursuit', 'Toxic'),
'Ekans': ('Sludge Bomb', 'Earthquake', 'Strength', 'Glare'),
'Arbok': ('Sludge Bomb', 'Bite', 'Dig', 'Glare'),
'Pikachu': ('Thunderbolt', 'Surf', 'Iron Tail', 'Thunder Wave'),
'Raichu': ('Thunder', 'Quick Attack', 'Thunder Wave', 'Tail Whip'),
'Sandshrew': ('Earthquake', 'Slash', 'Fury Cutter', 'Sandstorm'),
'Sandslash': ('Earthquake', 'Fury Swipes', 'Sand Attack', 'Sandstorm'),
'Nidoran': ('Headbutt', 'Iron Tail', 'Blizzard', 'Toxic'),
'Nidorina': ('Strength', 'Bite', 'Blizzard', 'Toxic'),
'Nidoqueen': ('Body Slam', 'Ice Punch', 'Growl', 'Mud-Slap'),
'Nidorino': ('Strength', 'Double Kick', 'Thunder', 'Horn Drill'),
'Nidoking': ('Horn Attack', 'Mud-Slap', 'Thunder', 'Horn Drill'),
'Clefairy': ('Metronome', 'Strength', 'Psychic', 'Moonlight'),
'Clefable': ('Metronome', 'Headbutt', 'Ice Punch', 'Encore'),
'Vulpix': ('Flamethrower', 'Dig', 'Confuse Ray', 'Sunny Day'),
'Ninetales': ('Fire Blast', 'Quick Attack', 'Roar', 'Safeguard'),
'Jigglypuff': ('Body Slam', 'Rollout', 'Defense Curl', 'Sing'),
'Wigglytuff': ('Double-Edge', 'Fire Punch', 'Disable', 'Sing'),
'Zubat': ('Wing Attack', 'Giga Drain', 'Confuse Ray', 'Toxic'),
'Golbat': ('Wing Attack', 'Bite', 'Steel Wing', 'Haze'),
'Oddish': ('Giga Drain', 'Sludge Bomb', 'Moonlight', 'Stun Spore'),
'Gloom': ('Solar Beam', 'Sludge Bomb', 'Sleep Powder', 'Sunny Day'),
'Vileplume': ('Petal Dance', 'Acid', 'Sweet Scent', 'Poison Powder'),
'Paras': ('Giga Drain', 'Slash', 'Spore', 'Growth'),
'Parasect': ('Giga Drain', 'Slash', 'Fury Cutter', 'Spore'),
'Venonat': ('Sludge Bomb', 'Psychic', 'Supersonic', 'Stun Spore'),
'Venomoth': ('Sludge Bomb', 'Psychic', 'Leech Life', 'Pound'),
'Diglett': ('Earthquake', 'Slash', 'Fissure', 'Sand Attack'),
'Dugtrio': ('Magnitude', 'Slash', 'Attract', 'Curse'),
'Meowth': ('Slash', 'Feint Attack', 'Shadow Ball', 'Screech'),
'Persian': ('Headbutt', 'Bite', 'Roar', 'Growl'),
'Psyduck': ('Surf', 'Dig', 'Swagger', 'Confusion'),
'Golduck': ('Surf', 'Confusion', 'Ice Beam', 'Psybeam'),
'Mankey': ('Cross Chop', 'Strength', 'Double Team', 'Screech'),
'Primeape': ('Cross Chop', 'Thrash', 'Body Slam', 'Focus Energy'),
'Growlithe': ('Flamethrower', 'Dig', 'Sunny Day', 'Roar'),
'Arcanine': ('Flame Wheel', 'Extreme Speed', 'Leer', 'Fire Blast'),
'Poliwag': ('Hydro Pump', 'Body Slam', 'Hypnosis', 'Rain Dance'),
'Poliwhirl': ('Surf', 'Snore', 'Belly Drum', 'Rest'),
'Poliwrath': ('Dynamic Punch', 'Hydro Pump', 'Double Slap', 'Mind Reader'),
'Abra': ('Psychic', 'Ice Punch', 'Swagger', 'Attract'),
'Kadabra': ('Psychic', 'Thunder Punch', 'Reflect', 'Kinesis'),
'Alakazam': ('Psybeam', 'Future Sight', 'Kinesis', 'Confusion'),
'Machop': ('Cross Chop', 'Seismic Toss', 'Earthquake', 'Double Team'),
'Machoke': ('Vital Throw', 'Strength', 'Dig', 'Foresight'),
'Machamp': ('Submission', 'Scary Face', 'Thunder Punch', 'Fire Punch'),
'Bellsprout': ('Giga Drain', 'Sludge Bomb', 'Toxic', 'Growth'),
'Weepinbell': ('Razor Leaf', 'Sludge Bomb', 'Stun Spore', 'Growth'),
'Victreebel': ('Solar Beam', 'Acid', 'Sleep Powder', 'Growth'),
'Tentacool': ('Surf', 'Sludge Bomb', 'Blizzard', 'Screech'),
'Geodude': ('Earthquake', 'Rollout', 'Explosion', 'Defense Curl'),
'Tentacruel': ('Bubble Beam', 'Sludge Bomb', 'Wrap', 'Barrier'),
'Graveler': ('Earthquake', 'Rollout', 'Sandstorm', 'Rock Throw'),
'Golem': ('Magnitude', 'Rock Throw', 'Rock Smash', 'Harden'),
'Ponyta': ('Fire Blast', 'Headbutt', 'Iron Tail', 'Sunny Day'),
'Rapidash': ('Fire Spin', 'Stomp', 'Attract', 'Toxic'),
'Slowpoke': ('Surf', 'Psychic', 'Earthquake', 'Amnesia'),
'Slowbro': ('Surf', 'Confusion', 'Disable', 'Growl'),
'Magnemite': ('Thunder', 'Frustration', 'Supersonic', 'Thunder Wave'),
'Magneton': ('Thunder', 'Swift', 'Flash', 'Thunder Wave'),
'Farfetch\'d': ('Slash', 'Fly', 'Steel Wing', 'Swords Dance'),
'Doduo': ('Drill Peck', 'Tri Attack', 'Steel Wing', 'Double Team'),
'Dodrio': ('Tri Attack', 'Pursuit', 'Growl', 'Fly'),
'Seel': ('Surf', 'Ice Beam', 'Headbutt', 'Safeguard'),
'Dewgong': ('Waterfall', 'Aurora Beam', 'Sleep Talk', 'Rest'),
'Grimer': ('Sludge Bomb', 'Frustration', 'Toxic', 'Screech'),
'Muk': ('Sludge', 'Dynamic Punch', 'Disable', 'Acid Armor'),
'Shellder': ('Surf', 'Ice Beam', 'Swift', 'Supersonic'),
'Cloyster': ('Clamp', 'Aurora Beam', 'Spike Cannon', 'Withdraw'),
'Gastly': ('Shadow Ball', 'Psychic', 'Curse', 'Confuse Ray'),
'Haunter': ('Shadow Ball', 'Giga Drain', 'Spite', 'Destiny Bond'),
'Onix': ('Earthquake', 'Rock Throw', 'Strength', 'Sandstorm'),
'Gengar': ('Night Shade', 'Thief', 'Nightmare', 'Shadow Ball'),
'Drowzee': ('Psychic', 'Headbutt', 'Dream Eater', 'Hypnosis'),
'Hypno': ('Confusion', 'Dream Eater', 'Psych Up', 'Hypnosis'),
'Krabby': ('Strength', 'Blizzard', 'Guillotine', 'Crabhammer'),
'Kingler': ('Crabhammer', 'Vice Grip', 'Guillotine', 'Leer'),
'Voltorb': ('Thunder', 'Mirror Coat', 'Rain Dance', 'Thunderbolt'),
'Electrode': ('Thunder', 'Swift', 'Sonic Boom', 'Flash'),
'Exeggcute': ('Psychic', 'Giga Drain', 'Stun Spore', 'Leech Seed'),
'Exeggutor': ('Egg Bomb', 'Confusion', 'Nightmare', 'Sleep Powder'),
'Cubone': ('Bonemerang', 'Headbutt', 'Icy Wind', 'Focus Energy'),
'Marowak': ('Bone Rush', 'Thrash', 'Thunder Punch', 'Focus Energy'),
'Hitmonlee': ('High Jump Kick', 'Mega Kick', 'Reversal', 'Meditate'),
'Hitmonchan': ('Mach Punch', 'Strength', 'Ice Punch', 'Counter'),
'Lickitung': ('Hyper Beam', 'Shadow Ball', 'Surf', 'Supersonic'),
'Koffing': ('Sludge Bomb', 'Fire Blast', 'Toxic', 'Zap Cannon'),
    'Weezing': ('Sludge', 'Zap Cannon', 'Toxic', 'Haze'),
    'Rhyhorn': ('Earthquake', 'Rollout', 'Iron Tail', 'Scary Face'),
    'Rhydon': ('Dig', 'Stomp', 'Zap Cannon', 'Scary Face'),
    'Chansey': ('Egg Bomb', 'Blizzard', 'Dream Eater', 'Sing'),
    'Tangela': ('Giga Drain', 'Thief', 'Sleep Powder', 'Growth'),
    'Kangaskhan': ('Dizzy Punch', 'Bite', 'Surf', 'Leer'),
    'Horsea': ('Hydro Pump', 'Blizzard', 'Rain Dance', 'Smokescreen'),
    'Seadra': ('Surf', 'Dragon Breath', 'Swift', 'Smokescreen'),
    'Goldeen': ('Surf', 'Horn Attack', 'Horn Drill', 'Supersonic'),
    'Seaking': ('Waterfall', 'Flail', 'Horn Drill', 'Supersonic'),
    'Staryu': ('Psychic', 'Hydro Pump', 'Thunder', 'Recover'),
    'Starmie': ('Waterfall', 'Zap Cannon', 'Rapid Spin', 'Harden'),
    'Mr. Mime': ('Psybeam', 'Barrier', 'Baton Pass', 'Substitute'),
    'Scyther': ('Wing Attack', 'Pursuit', 'Swift', 'Focus Energy'),
    'Jynx': ('Ice Punch', 'Confusion', 'Lick', 'Mean Look'),
    'Electabuzz': ('Thunder Punch', 'Swift', 'Light Screen', 'Leer'),
    'Magmar': ('Fire Punch', 'Smog', 'Smokescreen', 'Confuse Ray'),
    'Pinsir': ('Fury Cutter', 'Vice Grip', 'Submission', 'Focus Energy'),
    'Tauros': ('Take Down', 'Pursuit', 'Rock Smash', 'Scary Face'),
    'Magikarp': ('Tackle', 'Flail', 'Splash', 'Water Gun'),
    'Gyarados': ('Waterfall', 'Dragon Rage', 'Twister', 'Leer'),
    'Lapras': ('Whirlpool', 'Icy Wind', 'Perish Song', 'Mist'),
    'Ditto': ('Fire Blast', 'Solar Beam', 'Hydro Pump', 'Steel Wing'),
    'Eevee': ('Take Down', 'Iron Tail', 'Shadow Ball', 'Sand Attack'),
    'Vaporeon': ('Waterfall', 'Quick Attack', 'Acid Armor', 'Sand Attack'),
    'Jolteon': ('Zap Cannon', 'Pin Missile', 'Double Kick', 'Sand Attack'),
    'Flareon': ('Fire Blast', 'Smog', 'Quick Attack', 'Tail Whip'),
    'Porygon': ('Tri Attack', 'Blizzard', 'Sharpen', 'Conversion 2'),
    'Omanyte': ('Surf', 'Ancient Power', 'Blizzard', 'Protect'),
    'Omastar': ('Water Gun', 'Ancient Power', 'Spike Cannon', 'Bite'),
    'Kabuto': ('Rollout', 'Giga Drain', 'Blizzard', 'Attract'),
    'Kabutops': ('Ancient Power', 'Surf', 'Leer', 'Endure'),
    'Aerodactyl': ('Ancient Power', 'Bite', 'Curse', 'Supersonic'),
    'Snorlax': ('Headbutt', 'Fire Punch', 'Defense Curl', 'Curse'),
    'Articuno': ('Blizzard', 'Peck', 'Agility', 'Mist'),
    'Zapdos': ('Thunder', 'Rock Smash', 'Flash', 'Detect'),
    'Moltres': ('Fire Blast', 'Sky Attack', 'Roar', 'Endure'),
    'Dratini': ('Outrage', 'Headbutt', 'Safeguard', 'Thunder Wave'),
    'Dragonair': ('Outrage', 'Headbutt', 'Fire Blast', 'Thunder Wave'),
    'Dragonite': ('Twister', 'Wing Attack', 'Dragon Rage', 'Leer'),
    'Mew': ('Psychic', 'Ancient Power', 'Metronome', 'Flash')}
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
        if idx is False:
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
            #print('NEW GUY:')
            #print(self.active_pk.name)
        else:
            self.defeated = True


# def apply_status(attacker, defender, move):
#     text = status_list[move]['Effect']
#
#     percent = 1.00
#
#     keyword_percent = re.search("\d+?%", text)
#     if (keyword_percent):
#         percent = float(keyword_percent.group().strip('%')) / 100
#
#         keyword_burn = re.search("burn", text)
#         if keyword_burn and rd.random() < percent and defender.status is "":
#             defender.status = "Burn"
#
#     keyword_freeze = re.search("freeze", text)
#     if keyword_freeze and rd.random() < percent and defender.status is "":
#         defender.status = "Freeze"
#
#
#     keyword_paralyze = re.search("paralyze", text)
#     if keyword_paralyze and rd.random() < percent and defender.status is "":
#         defender.status = "Paralyze"
#
#     keyword_poison = re.search("poison", text)
#     if keyword_poison and rd.random() < percent and defender.status is "":
#         defender.status = "Poison"
#
#     keyword_flinch = re.search("flinch", text)
#     if keyword_flinch and rd.random() < percent and defender.status is "":
#         defender.status = "Flinch"


def attack(attacker, defender, move):
    #print(move)
    power = moves_list[move]['Power']
    if power == 'None' or power is None:
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
    if atk_t == 'Fighting': atk_t = 'Fight'
    if defender.t1 == 'Fighting': defender.t1 = 'Fight'

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
    #print(attacker.name + ' random agent used ' + o + '!')
    return o

def type_agent(attacker, defender):
    score = 0
    move = attacker.m1
    for i in [attacker.m1, attacker.m2, attacker.m3, attacker.m4]:
        #print(i)
        power = moves_list[i]['Power']
        if power == 'None' or power is None:
            power = -1
        dm = 0
        # attack defense coefficient based on move category
        if moves_list[i]['Category'] == 'Physical':
            dm = attacker.atk / defender.defe
        elif moves_list[i]['Category'] == 'Special':
            dm = attacker.spatk / defender.spdefe
        elif moves_list[i]['Category'] == 'Status':
            pass
        else:
            pass
        atk_t = moves_list[i]['Type']
        
        if atk_t == 'Fighting': atk_t = 'Fight'
        if defender.t1 == 'Fighting': defender.t1 = 'Fight'

        tmult = type_matrix[atk_t][defender.t1]  # type multiplier
        try:
            b = type_matrix[atk_t][defender.t2]
            tmult = tmult * b
        except:
            pass
        stab = 1
        # same type attack bonus for using a move of your pokemon's type
        #print(attacker.t1)
        #print(attacker.t2)
        if moves_list[i]['Type'] == attacker.t1 or moves_list[i]['Type'] == attacker.t2:
            stab = 1.5

        damage = (.2 * int(power) * dm + 2) * tmult * stab
        if damage > score:
            #print(damage)
            #print(i)
            score = damage
            move = i
    #print(attacker.name + ' Type Agent used ' + move + '!')
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
        pass
    if pb.faint:
        #print(pa.name + ' fainted!')
        pass
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

def Type_Trainer(You, Opponent):
    current = You.active_pk
    op = Opponent.active_pk
    r1 = You.reserve[0]
    r2 = You.reserve[1]
    score = 0
    pokemon = None
    for i in [current, r1, r2]:
        mult1 = 1
        try:
            mult1 = type_matrix[current.t1][op.t1]/type_matrix[op.t1][current.t1]
        except:
            pass
        mult2 = 1
        mult3 = 1
        mult4 = 1
        mult5 = 1
        mult6 = 1
        mult7 = 1
        try:
            mult2 = type_matrix[i.t1][op.t2]
            mult6 = type_matrix[op.t2][i.t1]
        except:
            pass
        try:
            mult3 = type_matrix[i.t2][op.t1]
            mult5 = type_matrix[op.t1][i.t2]
        except:
            pass
        try:
            mult4 = type_matrix[i.t2][op.t2]
            mult7 = type_matrix[op.t2][i.t2]
        except:
            pass
        try:
            mult = mult1*mult2*mult3*mult4/(mult6*mult5*mult7)
        except:
            mult = 20
        if mult > score:
            score = mult
            pokemon = i
    if pokemon == r1:
        return 0
    if pokemon == r2:
        return 1
    return False




def battle(You, Opponent, You_decision=random_Trainer, Opponent_decision=random_Trainer, Your_move_decision=random_move, Opponent_move_decision=random_move, turns=0):
    if turns > 50:
        return .5
    if You.party_ct == 0:
        return 0 - Opponent.party_ct/6+.5
    if Opponent.party_ct == 0:
        return 0 + You.party_ct/6+.5
    if You.active_pk.faint:
        You.party_ct -= 1
        You.swap(0)
    if Opponent.active_pk.faint:
        Opponent.party_ct -= 1
        Opponent.swap(0)
    o = Opponent_decision(You, Opponent)
    y = You_decision(You, Opponent)
    You.swap(y)
    Opponent.swap(o)

    #print('!!!')
    #print('Yours: ' + You.active_pk.name)
    #print('Yours: ' + str(You.party_ct))
    #print('*****')
    #print('Opponent: ' + Opponent.active_pk.name)
    #print('Opponent: ' + str(Opponent.party_ct))
    #print('!!!')
    battle_step(You.active_pk, Opponent.active_pk, a_decsion=Your_move_decision, b_decision=Opponent_move_decision, just_swapped_a=False, just_swapped_b=False)
    return battle(You, Opponent, You_decision, Opponent_decision, Your_move_decision, Opponent_move_decision, turns+1)


wins = []
for i in range(0, 10000):
    wins.append(battle(Trainer(random_party(3)), Trainer(random_party(3)), You_decision=Type_Trainer, Your_move_decision=type_agent, Opponent_decision=Type_Trainer, Opponent_move_decision=type_agent))

print('%END%')
print(sum(wins)/len(wins))




#k = random_party(4)
#for i in k:
#    print(i.name)

