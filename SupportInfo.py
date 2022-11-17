import traceback
import random


class Weapon:
    def __init__(self, name, weapon_range, damage, weight, hands, gold=0):
        self.name = name
        self.range = weapon_range
        self.damage = damage
        self.weight = weight
        self.hands = hands
        self.gold = gold
        self.isRanged = False

    def print_details(self):
        wstring = self.name
        wstring += "\nRange: " + str(self.range)
        wstring += "\nDamage: 1 - " + str(self.damage)
        wstring += "\nWeight: " + str(self.weight)
        wstring += "\nHands required: " + str(self.hands)
        return wstring

    def attack(self, accuracy, damage, target):
        try:
            armor = target.dexterity + target.equippedArmor.defense
            if random.randrange(1, 20) + accuracy > armor:
                if self.damage == 1:
                    damage += 1
                else:
                    damage = random.randrange((1 + damage), (self.damage + damage + 1), 1)
                target.currentHP -= damage
                print(target.name + " takes " + str(damage) + " points of damage!")
            else:
                print("The attack misses!")
        except:
            f = open("error_report.txt", "a")
            print("An error occured.")
            traceback.print_exc(None, f)
            f.close()


class Longsword:
    def __init__(self):
        self.name = "Longsword"
        self.range = 1
        self.gold = 7
        self.hands = 1
        self.weight = 1.2
        self.equipable = True
        self.damageType = "Slashing"
        self.traits = ["Versatile-Piercing"]
        self.isRanged = False

    def print_details(self):
        wstring = self.name
        wstring += "\nRange: 1"
        wstring += "\nDamage: 2 - 8 " + self.damageType
        wstring += "\nTraits: "
        for trait in self.traits:
            wstring += trait + " "
        wstring += "\nWeight: 1.2"
        wstring += "\nHands required: 1"
        wstring += "\nGold value: 7"
        return wstring

    def attack(self, accuracy, damage, target):
        try:
            armor = target.dexterity + target.equippedArmor.defense
            if random.randrange(1, 20) + accuracy > armor:
                damage = random.randrange((2 + damage), (9 + damage), 1)
                target.currentHP -= damage
                print(target.name + " takes " + str(damage) + " points of damage!")
            else:
                print("The attack misses!")
        except:
            f = open("error_report.txt", "a")
            print("An error occured.")
            traceback.print_exc(None, f)
            f.close()


class Shortsword:
    def __init__(self):
        self.name = "Shortsword"
        self.range = 1
        self.gold = 5
        self.hands = 1
        self.weight = 1
        self.equipable = True
        self.damageType = "Slashing"
        self.traits = ["Versatile-Piercing"]
        self.isRanged = False

    def print_details(self):
        wstring = self.name
        wstring += "\nRange: " + str(self.range)
        wstring += "\nDamage: 1 - 6 " + self.damageType
        wstring += "\nTraits: "
        for trait in self.traits:
            wstring += trait + " "
        wstring += "\nWeight: " + str(self.weight)
        wstring += "\nHands required: " + str(self.hands)
        wstring += "\nGold value: " + str(self.gold)
        return wstring

    def attack(self, accuracy, damage, target):
        try:
            armor = target.dexterity + target.equippedArmor.defense
            if random.randrange(1, 20) + accuracy > armor:
                damage = random.randrange((1 + damage), (7 + damage), 1)
                target.currentHP -= damage
                print(target.name + " takes " + str(damage) + " points of damage!")
            else:
                print("The attack misses!")
        except:
            f = open("error_report.txt", "a")
            print("An error occured.")
            traceback.print_exc(None, f)
            f.close()


class Axe:
    def __init__(self):
        self.name = "Axe"
        self.range = 1
        self.gold = 8
        self.hands = 1
        self.weight = 2
        self.equipable = True
        self.damageType = "Slashing"
        self.traits = []
        self.isRanged = False

    def print_details(self):
        wstring = self.name
        wstring += "\nRange: " + str(self.range)
        wstring += "\nDamage: 4 - 6 " + self.damageType
        wstring += "\nWeight: " + str(self.weight)
        wstring += "\nHands required: " + str(self.hands)
        wstring += "\nGold value: " + str(self.gold)
        return wstring

    def attack(self, accuracy, damage, target):
        try:
            armor = target.dexterity + target.equippedArmor.defense
            if random.randrange(1, 20) + accuracy > armor:
                damage = random.randrange((4 + damage), (7 + damage), 1)
                target.currentHP -= damage
                print(target.name + " takes " + str(damage) + " points of damage!")
            else:
                print("The attack misses!")
        except:
            f = open("error_report.txt", "a")
            print("An error occured.")
            traceback.print_exc(None, f)
            f.close()


class Club:
    def __init__(self):
        self.name = "Club"
        self.range = 1
        self.gold = 5
        self.hands = 1
        self.weight = 1
        self.equipable = True
        self.damageType = "Bludgeoning"
        self.traits = []
        self.isRanged = False

    def print_details(self):
        wstring = self.name
        wstring += "\nRange: " + str(self.range)
        wstring += "\nDamage: 1 - 6 " + self.damageType
        wstring += "\nWeight: " + str(self.weight)
        wstring += "\nHands required: " + str(self.hands)
        wstring += "\nGold value: " + str(self.gold)
        return wstring

    def attack(self, accuracy, damage, target):
        try:
            armor = target.dexterity + target.equippedArmor.defense
            if random.randrange(1, 20) + accuracy > armor:
                damage = random.randrange((1 + damage), (7 + damage), 1)
                target.currentHP -= damage
                print(target.name + " takes " + str(damage) + " points of damage!")
            else:
                print("The attack misses!")
        except:
            f = open("error_report.txt", "a")
            print("An error occured.")
            traceback.print_exc(None, f)
            f.close()


class Warhammer:
    def __init__(self):
        self.name = "Warhammer"
        self.range = 1
        self.gold = 10
        self.hands = 1
        self.weight = 2.2
        self.equipable = True
        self.damageType = "Bludgeoning"
        self.traits = []
        self.isRanged = False

    def print_details(self):
        wstring = self.name
        wstring += "\nRange: " + str(self.range)
        wstring += "\nDamage: 4 - 8 " + self.damageType
        wstring += "\nWeight: " + str(self.weight)
        wstring += "\nHands required: " + str(self.hands)
        wstring += "\nGold value: " + str(self.gold)
        return wstring

    def attack(self, accuracy, damage, target):
        try:
            armor = target.dexterity + target.equippedArmor.defense
            if random.randrange(1, 20) + accuracy > armor:
                damage = random.randrange((4 + damage), (9 + damage), 1)
                target.currentHP -= damage
                print(target.name + " takes " + str(damage) + " points of damage!")
            else:
                print("The attack misses!")
        except:
            f = open("error_report.txt", "a")
            print("An error occured.")
            traceback.print_exc(None, f)
            f.close()


class Dagger:
    def __init__(self):
        self.name = "Dagger"
        self.range = 1
        self.gold = 2
        self.hands = 1
        self.weight = 0
        self.equipable = True
        self.damageType = "Piercing"
        self.traits = []
        self.isRanged = False

    def print_details(self):
        wstring = self.name
        wstring += "\nRange: " + str(self.range)
        wstring += "\nDamage: 1 - 4 " + self.damageType
        wstring += "\nWeight: " + str(self.weight)
        wstring += "\nHands required: " + str(self.hands)
        wstring += "\nGold value: " + str(self.gold)
        return wstring

    def attack(self, accuracy, damage, target):
        try:
            armor = target.dexterity + target.equippedArmor.defense
            if random.randrange(1, 20) + accuracy > armor:
                damage = random.randrange((1 + damage), (5 + damage), 1)
                target.currentHP -= damage
                print(target.name + " takes " + str(damage) + " points of damage!")
            else:
                print("The attack misses!")
        except:
            f = open("error_report.txt", "a")
            print("An error occured.")
            traceback.print_exc(None, f)
            f.close()


class Spear:
    def __init__(self):
        self.name = "Spear"
        self.range = 2
        self.gold = 5
        self.hands = 2
        self.weight = 1.5
        self.equipable = True
        self.damageType = "Piercing"
        self.traits = []
        self.isRanged = False

    def print_details(self):
        wstring = self.name
        wstring += "\nRange: " + str(self.range)
        wstring += "\nDamage: 1 - 6 " + self.damageType
        wstring += "\nWeight: " + str(self.weight)
        wstring += "\nHands required: " + str(self.hands)
        wstring += "\nGold value: " + str(self.gold)
        return wstring

    def attack(self, accuracy, damage, target):
        try:
            armor = target.dexterity + target.equippedArmor.defense
            if random.randrange(1, 20) + accuracy > armor:
                damage = random.randrange((1 + damage), (7 + damage), 1)
                target.currentHP -= damage
                print(target.name + " takes " + str(damage) + " points of damage!")
            else:
                print("The attack misses!")
        except Exception as Argument:
            f = open("error_report.txt", "a")
            print("An error occured.")
            traceback.print_exc(None, f)
            f.close()


class Shortbow:
    def __init__(self):
        self.name = "Shortbow"
        self.range = 4
        self.gold = 10
        self.hands = 2
        self.weight = 2
        self.equipable = True
        self.damageType = "Piercing"
        self.traits = []
        self.isRanged = True

    def print_details(self):
        wstring = self.name
        wstring += "\nRange: " + str(self.range)
        wstring += "\nDamage: 1 - 6 " + self.damageType
        wstring += "\nWeight: " + str(self.weight)
        wstring += "\nHands required: " + str(self.hands)
        wstring += "\nGold value: " + str(self.gold)
        return wstring

    def attack(self, accuracy, damage, target):
        try:
            armor = target.dexterity + target.equippedArmor.defense
            if random.randrange(1, 20) + accuracy > armor:
                damage = int(damage / 2)
                damage = random.randrange((1 + damage), (7 + damage), 1)
                target.currentHP -= damage
                print(target.name + " takes " + str(damage) + " points of damage!")
            else:
                print("The attack misses!")
        except:
            f = open("error_report.txt", "a")
            print("An error occurred.")
            traceback.print_exc(None, f)
            f.close()


class Longbow:
    def __init__(self):
        self.name = "Longbow"
        self.range = 8
        self.gold = 12
        self.hands = 2
        self.weight = 3
        self.equipable = True
        self.damageType = "Piercing"
        self.traits = []
        self.isRanged = True

    def print_details(self):
        wstring = self.name
        wstring += "\nRange: " + str(self.range)
        wstring += "\nDamage: 2 - 6 " + self.damageType
        wstring += "\nWeight: " + str(self.weight)
        wstring += "\nHands required: " + str(self.hands)
        wstring += "\nGold value: " + str(self.gold)
        return wstring

    def attack(self, accuracy, damage, target):
        try:
            armor = target.dexterity + target.equippedArmor.defense
            if random.randrange(1, 20) + accuracy > armor:
                damage = int(damage / 2)
                damage = random.randrange((2 + damage), (7 + damage), 1)
                target.currentHP -= damage
                print(target.name + " takes " + str(damage) + " points of damage!")
            else:
                print("The attack misses!")
        except:
            f = open("error_report.txt", "a")
            print("An error occurred.")
            traceback.print_exc(None, f)
            f.close()


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
                ["knives", 5],
                ["minor potion", 1],
                ["minor potion", 2],
                ["minor potion", 3],
                ["minor potion", 4],
                ["moderate potion", 1],
                ["moderate potion", 2],
                ["major potion", 1]]

chestOptions = ["Weapon", "Armor"]

weaponOptions = [Longsword(), Shortbow(), Longbow(), Axe(), Spear(), Warhammer(), Club()]

armorOptions = [Armor("Leather", 1, 0.5, 5)]

characterLevel = 1
