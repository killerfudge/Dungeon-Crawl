import traceback
import random
import os


def clear():
    # Clear the screen for Windows machines
    if os.name == 'nt':
        _ = os.system('cls')
    # Clear the screen for mac and linux
    else:
        _ = os.system('clear')


class ThrowingKnife:
    def __init__(self):
        self.name = "throwing knife"
        self.range = 1
        self.damageType = "Piercing"
        self.weight = 0
        self.hands = 0
        self.gold = 2
        self.traits = []
        self.isRanged = False
        self.quantity = 1

    def print_details(self):
        wstring = self.name
        wstring += "\nRange: 1"
        wstring += "\nDamage: 1 " + self.damageType
        wstring += "\nWeight: 0"
        wstring += "\nHands required: 0"
        wstring += "\nGold value: 2"
        return wstring

    def attack(self, accuracy, damage, target):
        try:
            armor = target.dexterity + target.equippedArmor.defense
            if random.randrange(1, 20) + accuracy > armor:
                damage += 1
                target.equippedArmor.take_damage(damage, self.damageType, target, self.traits)
            else:
                print("The attack misses!")
        except:
            f = open("error_report.txt", "a")
            print("An error occurred.")
            traceback.print_exc(None, f)
            f.close()


class Fist:
    def __init__(self):
        self.name = "Fist"
        self.range = 1
        self.damageType = "Bludgeoning"
        self.hands = 1
        self.weight = 0
        self.gold = 0
        self.traits = []
        self.isRanged = False
        self.quantity = 1

    def print_details(self):
        wstring = self.name
        wstring += "\nRange: 1"
        wstring += "\nDamage: 1 " + self.damageType
        wstring += "\nWeight: 1.2"
        wstring += "\nHands required: 1"
        wstring += "\nGold value: 7"
        return wstring

    def attack(self, accuracy, damage, target):
        try:
            armor = target.dexterity + target.equippedArmor.defense
            if random.randrange(1, 20) + accuracy > armor:
                damage += 1
                target.equippedArmor.take_damage(damage, self.damageType, target, self.traits)
            else:
                print("The attack misses!")
        except:
            f = open("error_report.txt", "a")
            print("An error occurred.")
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
        self.quantity = 1

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
                target.equippedArmor.take_damage(damage, self.damageType, target, self.traits)
            else:
                print("The attack misses!")
        except:
            f = open("error_report.txt", "a")
            print("An error occurred.")
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
        self.quantity = 1

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
                target.equippedArmor.take_damage(damage, self.damageType, target, self.traits)
            else:
                print("The attack misses!")
        except:
            f = open("error_report.txt", "a")
            print("An error occurred.")
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
        self.quantity = 1

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
                target.equippedArmor.take_damage(damage, self.damageType, target, self.traits)
            else:
                print("The attack misses!")
        except:
            f = open("error_report.txt", "a")
            print("An error occurred.")
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
        self.quantity = 1

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
                target.equippedArmor.take_damage(damage, self.damageType, target, self.traits)
            else:
                print("The attack misses!")
        except:
            f = open("error_report.txt", "a")
            print("An error occurred.")
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
        self.quantity = 1

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
                target.equippedArmor.take_damage(damage, self.damageType, target, self.traits)
            else:
                print("The attack misses!")
        except:
            f = open("error_report.txt", "a")
            print("An error occurred.")
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
        self.quantity = 1

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
                target.equippedArmor.take_damage(damage, self.damageType, target, self.traits)
            else:
                print("The attack misses!")
        except:
            f = open("error_report.txt", "a")
            print("An error occurred.")
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
        self.quantity = 1

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
                target.equippedArmor.take_damage(damage, self.damageType, target, self.traits)
            else:
                print("The attack misses!")
        except:
            f = open("error_report.txt", "a")
            print("An error occurred.")
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
        self.quantity = 1

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
                target.equippedArmor.take_damage(damage, self.damageType, target, self.traits)
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
        self.quantity = 1

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
                target.equippedArmor.take_damage(damage, self.damageType, target, self.traits)
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
        self.equipable = False
        self.quantity = 1

    def print_details(self):
        wstring = self.name
        wstring += "\ndefense: " + str(self.defense)
        wstring += "\nWeight: " + str(self.weight)
        return wstring

    def take_damage(self, damage, d_type, target, traits):
        target.currentHP -= damage
        print(target.name + " takes " + str(damage) + " points of damage!")


class Leather:
    def __init__(self):
        self.name = "Leather"
        self.defense = 1
        self.weight = 0.5
        self.gold = 2
        self.equipable = True
        self.quantity = 1

    def print_details(self):
        wstring = self.name
        wstring += "\ndefense: " + str(self.defense)
        wstring += "\nWeight: " + str(self.weight)
        wstring += "\nGold: " + str(self.gold)
        return wstring

    def take_damage(self, damage, d_type, target, traits):
        target.currentHP -= damage
        print(target.name + " takes " + str(damage) + " points of damage!")


class Hide:
    def __init__(self):
        self.name = "Hide"
        self.defense = 2
        self.weight = 1
        self.gold = 4
        self.equipable = True
        self.quantity = 1

    def print_details(self):
        wstring = self.name
        wstring += "\ndefense: " + str(self.defense)
        wstring += "\nWeight: " + str(self.weight)
        wstring += "\nGold: " + str(self.gold)
        return wstring

    def take_damage(self, damage, d_type, target, traits):
        target.currentHP -= damage
        print(target.name + " takes " + str(damage) + " points of damage!")


class StuddedLeather:
    def __init__(self):
        self.name = "Studded Leather"
        self.defense = 3
        self.weight = 1.5
        self.gold = 6
        self.equipable = True
        self.quantity = 1

    def print_details(self):
        wstring = self.name
        wstring += "\ndefense: " + str(self.defense)
        wstring += "\nWeight: " + str(self.weight)
        wstring += "\nGold: " + str(self.gold)
        return wstring

    def take_damage(self, damage, d_type, target, traits):
        target.currentHP -= damage
        print(target.name + " takes " + str(damage) + " points of damage!")


class Breastplate:
    def __init__(self):
        self.name = "Studded Leather"
        self.defense = 4
        self.weight = 2
        self.gold = 8
        self.equipable = True
        self.quantity = 1

    def print_details(self):
        wstring = self.name
        wstring += "\ndefense: " + str(self.defense)
        wstring += "\nWeight: " + str(self.weight)
        wstring += "\nGold: " + str(self.gold)
        return wstring

    def take_damage(self, damage, d_type, target, traits):
        target.currentHP -= damage
        print(target.name + " takes " + str(damage) + " points of damage!")


class Padded:
    def __init__(self):
        self.name = "Padded"
        self.defense = 1
        self.weight = 1
        self.gold = 5
        self.equipable = True
        self.quantity = 1

    def print_details(self):
        wstring = self.name
        wstring += "\ndefense: " + str(self.defense)
        wstring += "\nResists bludgeoning damage"
        wstring += "\nWeight: " + str(self.weight)
        wstring += "\nGold: " + str(self.gold)
        return wstring

    def take_damage(self, damage, d_type, target, traits):
        deflected = False
        if d_type == "Bludgeoning":
            versatile = False
            for trait in traits:
                if trait == "Versatile-Piercing" or trait == "Versatile-Slashing":
                    versatile = True
                    break
            if not versatile:
                damage -= 2
                deflected = True
        if deflected:
            if damage <= 0:
                print("The " + self.name + " deflects the blow, preventing any damage.")
            else:
                target.currentHP -= damage
                print("The " + self.name + " deflects some of the blow, but " + target.name + " still takes " +
                      str(damage) + " points of damage!")
        else:
            target.currentHP -= damage
            print(target.name + " takes " + str(damage) + " points of damage!")


class ChainShirt:
    def __init__(self):
        self.name = "Chain Shirt"
        self.defense = 1
        self.weight = 1
        self.gold = 5
        self.equipable = True
        self.quantity = 1

    def print_details(self):
        wstring = self.name
        wstring += "\ndefense: " + str(self.defense)
        wstring += "\nResists slashing damage"
        wstring += "\nWeight: " + str(self.weight)
        wstring += "\nGold: " + str(self.gold)
        return wstring

    def take_damage(self, damage, d_type, target, traits):
        deflected = False
        if d_type == "Slashing":
            versatile = False
            for trait in traits:
                if trait == "Versatile-Piercing" or trait == "Versatile-Bludgeoning":
                    versatile = True
                    break
            if not versatile:
                damage -= 2
                deflected = True
        if deflected:
            if damage <= 0:
                print("The " + self.name + " deflects the blow, preventing any damage.")
            else:
                target.currentHP -= damage
                print("The " + self.name + " deflects some of the blow, but " + target.name + " still takes " +
                      str(damage) + " points of damage!")
        else:
            target.currentHP -= damage
            print(target.name + " takes " + str(damage) + " points of damage!")


class Chainmail:
    def __init__(self):
        self.name = "Chainmail"
        self.defense = 2
        self.weight = 2
        self.gold = 10
        self.equipable = True
        self.quantity = 1

    def print_details(self):
        wstring = self.name
        wstring += "\ndefense: " + str(self.defense)
        wstring += "\nResists slashing damage"
        wstring += "\nWeight: " + str(self.weight)
        wstring += "\nGold: " + str(self.gold)
        return wstring

    def take_damage(self, damage, d_type, target, traits):
        deflected = False
        if d_type == "Slashing":
            versatile = False
            for trait in traits:
                if trait == "Versatile-Piercing" or trait == "Versatile-Bludgeoning":
                    versatile = True
                    break
            if not versatile:
                damage -= 4
                deflected = True
        if deflected:
            if damage <= 0:
                print("The " + self.name + " deflects the blow, preventing any damage.")
            else:
                target.currentHP -= damage
                print("The " + self.name + " deflects some of the blow, but " + target.name + " still takes " +
                      str(damage) + " points of damage!")
        else:
            target.currentHP -= damage
            print(target.name + " takes " + str(damage) + " points of damage!")


class ScaleMail:
    def __init__(self):
        self.name = "Scale Mail"
        self.defense = 2
        self.weight = 2
        self.gold = 10
        self.equipable = True
        self.quantity = 1

    def print_details(self):
        wstring = self.name
        wstring += "\ndefense: " + str(self.defense)
        wstring += "\nResists piercing damage"
        wstring += "\nWeight: " + str(self.weight)
        wstring += "\nGold: " + str(self.gold)
        return wstring

    def take_damage(self, damage, d_type, target, traits):
        deflected = False
        if d_type == "Piercing":
            versatile = False
            for trait in traits:
                if trait == "Versatile-Slashing" or trait == "Versatile-Bludgeoning":
                    versatile = True
                    break
            if not versatile:
                damage -= 4
                deflected = True
        if deflected:
            if damage <= 0:
                print("The " + self.name + " deflects the blow, preventing any damage.")
            else:
                target.currentHP -= damage
                print("The " + self.name + " deflects some of the blow, but " + target.name + " still takes " +
                      str(damage) + " points of damage!")
        else:
            target.currentHP -= damage
            print(target.name + " takes " + str(damage) + " points of damage!")


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

armorOptions = [Leather(), Hide(), StuddedLeather(), Breastplate(), Padded(), ChainShirt(), Chainmail(), ScaleMail()]

characterLevel = 1
