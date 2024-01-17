import time, math, random

player_attack = 1
player_defense = 0
player_health = 3
ruppee = 0

# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)

# === [kamer 7] === #
print('Je loopt de kamer in en vind je een ruppee')
ruppee += 1

kies_kamer_7 = input("naar welke kamer ga je? 2 of 3?")

# === [kamer 2] === #
if kies_kamer_7 == '2':
    print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
    print('Het standbeeld heeft een sleutel vast.')
    print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
    num1 = random.randint(10, 25)
    num2 = random.randint(-5, 75)
    print(f'Daarboven zie je een som staan {num1} + {num2}')
    antwoord = int(input('Wat toest je in?'))

    sleutel = False
    if antwoord == num1 + num2:
        print('Het stadbeeld laat de sleutel vallen en je pakt het op')
        sleutel = True
    else:
        print('Er gebeurt niets....')

    print('Je zie een deur achter het standbeeld.')
    print('')
    time.sleep(1)

    kies_kamer = input("naar welke kamer ga je? 6 of 3?")

else:
    pass



# === [kamer 6] === #
if kies_kamer_7 == '2':
    if kies_kamer == '6':
        zombie_attack = 1
        zombie_defense = 0
        zombie_health = 2
        print('je loopt de kamer binnen.')
        print('Je loopt tegen een zombie aan.')

        zombie_hit_damage = (zombie_attack - player_defense)
        if zombie_hit_damage <= 0:
            print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
        else:
            # Bereken het aantal aanvallen dat de zombie nodig heeft om de speler te verslaan (zombie_attack_amount)
            zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
            
            # Bereken de schade die de speler kan toebrengen (player_hit_damage)
            player_hit_damage = (player_attack - zombie_defense)
            # Bereken het aantal aanvallen dat de speler nodig heeft om de zombie te verslaan (player_attack_amount)
            player_attack_amount = math.ceil(zombie_health / player_hit_damage)

        # Als player_attack_amount kleiner is dan zombie_attack_amount:
            if player_attack_amount < zombie_attack_amount:
                # Verminder player_health met de totale schade van de zombie
                player_health -= zombie_attack_amount * zombie_hit_damage
                print(f'In {player_attack_amount} rondes versla je de zombie.')
                print(f'Je health is nu {player_health}.')
            else:
                print('Helaas is de zombie te sterk voor je.')
                print('Game over.')
                exit()
        print('')
        time.sleep(1)

    else:
        pass
else:
    pass

# === [kamer 3] === #
print("Je kan nu een item kopen.:")
items = ['schild', 'zwaard']
item = input("Kies je item uit schild of zwaard?")
if item == 'zwaard':
    player_attack += 2
    ruppee -= 1
else:
    player_defense += 1
    ruppee -= 1

print('Je duwt hem open en stap een hele lange kamer binnen.')
print(f'In deze kamer staat een tafel met daarop een {item}.')
print(f'Je pakt het {item} op en houd het bij je.')
print('Op naar de volgende deur.')
print('')
time.sleep(1)

# === [kamer 4] === #
monster_attack = 2
monster_defense = 0
monster_health = 3

print(f'Dapper met je nieuwe {item} loop je de kamer binnen.')
print('Je loopt tegen een monster aan.')

monster_hit_damage = (monster_attack - player_defense)
if monster_hit_damage <= 0:
    print('Jij hebt een te goede verdedigign voor de monster, hij kan je geen schade doen.')
else:
    # Bereken het aantal aanvallen dat de monster nodig heeft om de speler te verslaan (monster_attack_amount)
    monster_attack_amount = math.ceil(player_health / monster_hit_damage)
    
    # Bereken de schade die de speler kan toebrengen (player_hit_damage)
    player_hit_damage = (player_attack - monster_defense)
    # Bereken het aantal aanvallen dat de speler nodig heeft om de monster te verslaan (player_attack_amount)
    player_attack_amount = math.ceil(monster_health / player_hit_damage)

# Als player_attack_amount kleiner is dan zombie_attack_amount:
    if player_attack_amount < monster_attack_amount:
        # Verminder player_health met de totale schade van de monster
        player_health -= monster_attack_amount * monster_hit_damage
        print(f'In {player_attack_amount} rondes versla je de monster.')
        print(f'Je health is nu {player_health}.')
    else:
        print('Helaas is de monster te sterk voor je.')
        print('Game over.')
        exit()
print('')
time.sleep(1)

# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')
if sleutel:
    print('Met de sleutel die gevonden hebt open je de schatkst. Gefeliciteerd je hebt gewonnen!!!!')
else:
    print('Je hebt helaas geen sleutel om de schatkist te kunnen openen. je hebt verloren :(')
