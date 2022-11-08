import random


class Weapon:
    def __init__(self, name, weapon_range, damage, weight, hands, gold=0):
        self.name = name
        self.range = weapon_range
        self.damage = damage
        self.weight = weight
        self.hands = hands
        self.gold = gold

    def print_details(self):
        wstring = self.name
        wstring += "\nRange: " + str(self.range)
        wstring += "\nDamage: 1 - " + str(self.damage)
        wstring += "\nWeight: " + str(self.weight)
        wstring += "\nHands required: " + str(self.hands)
        return wstring


class Armor:
    def __init__(self, name, defense, weight, gold=0):
        self.name = name
        self.defense = defense
        self.weight = weight
        self.gold = gold

    def print_details(self):
        wstring = self.name
        wstring += "\ndefense: " + str(self.defense)
        wstring += "\nWeight: " + str(self.weight)
        return wstring


tableOptions = [["knives", 1],
                ["knives", 2],
                ["knives", 3],
                ["knives", 4],
                ["knives", 5]]

chestOptions = ["Weapon", "Armor"]

weaponOptions = [
    Weapon("Longsword", 1, 8, 1.2, 1, 7),
    Weapon("Shortbow", 4, 6, 2, 2, 10),
    Weapon("Longbow", 8, 6, 3, 2, 12)
]

armorOptions = [Armor("Leather", 1, 0.5, 5)]

characterLevel = 1


def attack(accuracy, damage, weapon, target):
    armor = target.dexterity + target.equippedArmor.defense
    if random.randrange(1, 20) + accuracy > armor:
        if weapon.damage == 1:
            damage += 1
        else:
            damage = random.randrange((1 + damage), (weapon.damage + damage), 1)
        target.currentHP -= damage
        print(target.name + " takes " + str(damage) + " points of damage!")
    else:
        print("The attack misses!")
