from poke_env import PlayerConfiguration
from poke_env.player import Player
from poke_env.player import RandomPlayer
from numpy import np

my_player_config = PlayerConfiguration("my_username", "super-secret-password")

battle = ()
performance = []

## Double battle config

class MaxDamagePlayer(Player):
    pass
# Create Max Dmg Player
class MaxDamagePlayer(Player):
    def choose_move(self, battle):
        if battle.available_moves:

            best_move = max(battle.available_moves, key=lambda  move: move.base_power)
            return self.create_order(best_move)

        else:
            return self.choose_random_move(battle)



def teampreview_performance(pkmn_a, pkmn_b):
    a_vs_b = b_vs_a = -np.inf
    for type_ in pkmn_a.types:
        if type_:
            a_vs_b = max(a_vs_b, type_.damage_multiplier(*pkmn_b.types))

    for type_ in pkmn_b.types: 
        if type_:
            b_vs_a = max(b_vs_a, type.damage_multiplier(*pkmn_a.types))


    return a_vs_b - b_vs_a


def teampreview(self, battle):
    performance = {}

for i, pkmn in enumerate(battle.team.values()):
    performance[i] = np.mean([ 
    teampreview_performance(pkmn, opp)
for opp in battle.opponent_team.values()
])



# Performance 
ordered_mons = sorted(performance, key= lambda k: -performance[k])
# Use i + 1 since showdown's index start from 1

## Teams, SW/SH Meta' OU

team_1  = """"
Blaziken (F) @ Blazikenite
Ability: Speed Boost 
EVs: 252 Atk / 4 SpD / 252 Spe
Adamant Nature
IVs: 0 Atk
- Swords Dance
- Flare Blitz 
- Close Combat
- Thunder Punch

Sylveon (M) @ Leftovers
Ability: Pixilate
EVs: 248 HP / 244 Def / 16 SpD
Calm Nature
IVs: 0 Atk
- Hyper Voice
- Mystical Fire
- Protect
- Wish

Corviknight (M) @ Leftovers
Ability: Pressure
EVs: 248 HP / 80 SpD / 180 Spe
Impish Nature
- Defog
- Brave Bird
- Roost
- U-turn

Haxorus (F) @ Life Orb
Ability: Mold Breaker
EVs: 252 Atk / 4 SpD / 252 Spe
Jolly Nature 
- Swords Dance
- Outrage 
- Earthquake
- Poison Jab

"""

team_2 = """
Lucario (M) @ Life Orb
Ability: Inner Focus
EVs: 252 Atk / 4 SpD / 252 Spe
Jolly Nature 
- Close Combat
- Meteor Mash
- Swords Dance
- Extreme Speed

Tsareena (F) @ Heavy-Duty Boots
Ability: Queenly Majesty
EVs: 252 Atk / 4 Def / 252 Spe
Jolly Nature
- Power Whip
- Rapid Spin
- Knock Off
- Triple Axel

Magnezone (ng) @ Leftovers
Ability: Magnet Pull
EVs: 4 HP / 252 Def / 252 Spe
Timid Nature 
- Iron Defense
- Body Press
- Thunderbolt
- Toxic

Dragonite (M) @ Heavy-Duty Boots
Ability: Multiscale
EVs: 252 Atk / 4 SpD / 252 Spe
Adamant Nature
- Dragon Dance
- Dual Wingbeat
- Earthquake
- Roost
"""

#Creating the players 

random_player = RandomPlayer( 
    battle_format = "gen8ou",
    team=team_1,
    max_concurrent_battles=10,
)
max_dmg_player = MaxDamagePlayer(
    battle_format= "gen8ou",
    team =team_2,
    max_concurrent_battles=10,
)
