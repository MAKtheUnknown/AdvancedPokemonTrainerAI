#Christopher Kazakis, ck7aj
import pandas as pd
typedata = pd.read_excel('poketypes.xlsx')
pokemon = pd.read_csv('pokemon.csv')
moves = pd.read_csv('move-data.csv')
status_moves = pd.read_csv('move-data-status.csv')

moves = moves.loc[moves['Generation'].isin([1, 2])]

def get_moves():
    m = []
    for index, row in moves.iterrows():
        m.append(row['Name'])
    moves_dict = {}
    for index, row in moves.iterrows():
        moves_dict[row['Name']] = {'Type': row['Type'],'Category': row['Category'],'PP': row['PP'],'Power': row['Power'],'Accuracy': row['Accuracy']}
    return moves_dict

def status_moves():
    m = []
    for index, row in status_moves.iterrows():
        m.append(row['Name'])
    moves_dict = {}
    for index, row in moves.iterrows():
        moves_dict[row['Name']] = {'Effect': row['Effect']}
    return moves_dict

def poke_types():
    T = []
    for index, row in typedata.iterrows():
        T.append(row['Type'])
    type_dict = {}
    for index, row in typedata.iterrows():
        type_dict[row['Type']] = {T[0]: row[T[0]], T[1]: row[T[1]], T[2]: row[T[2]], T[3]: row[T[3]], T[4]: row[T[4]], T[5]: row[T[5]], T[6]: row[T[6]], T[7]: row[T[7]], T[8]: row[T[8]], T[9]: row[T[9]], T[10]: row[T[10]], T[11]: row[T[11]], T[12]: row[T[12]], T[13]: row[T[13]], T[14]: row[T[14]], T[15]: row[T[15]], T[16]: row[T[16]], T[17]: row[T[17]]}
    return type_dict

def poke_list():
    pokemon_dict = {}
    for index, row in pokemon.iterrows():
        pokemon_dict[row['Name']] = {'Type1': row['Type1'], 'Type2': row['Type2'], 'HP': row['HP'], 'Attack': row['Attack'], 'Defense': row['Defense'], 'Sp. Atk': row['Sp. Atk'], 'Sp. Def': row['Sp. Def'], 'Speed': row['Speed']}
    return pokemon_dict


e = poke_types()

