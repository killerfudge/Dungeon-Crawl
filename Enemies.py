import SupportInfo
import random


class Goblin:
    def __init__(self, room, row, column):
        self.name = "Goblin"
        self.currentHP = 5
        self.maxHP = 5
        self.xp = 1
        self.strength = 0
        self.dexterity = 0
        self.equippedWeapon = SupportInfo.Weapon("Dagger", 1, 4, 0, 1)
        self.equippedArmor = SupportInfo.Armor("None", 0, 0)
        self.speed = 0
        self.current_row = row
        self.current_column = column
        self.previous = " "
        self.currentRoom = room

    def behavior(self, player):
        near_character = False
        character_row = 0
        character_column = 0
        check_row = self.current_row
        check_column = self.current_column
        up = True
        while not near_character:
            while not (self.currentRoom.room[check_row][check_column] == "W" or self.currentRoom.room[check_row][check_column] == "D") and not near_character:
                if self.currentRoom.room[check_row][check_column] == "Y":
                    near_character = True
                    character_row = check_row
                    character_column = check_column
                check_column -= 1
            check_column = self.current_column + 1
            while not (self.currentRoom.room[check_row][check_column] == "W" or self.currentRoom.room[check_row][check_column] == "D") and not near_character:
                if self.currentRoom.room[check_row][check_column] == "Y":
                    near_character = True
                    character_row = check_row
                    character_column = check_column
                check_column += 1
            check_column = self.current_column
            if (self.currentRoom.room[check_row][check_column] == "W" or self.currentRoom.room[check_row][check_column] == "D") and not near_character:
                if up:
                    up = False
                    check_row = self.current_row
                else:
                    break
            if up:
                check_row -= 1
            else:
                check_row += 1
        if near_character:
            row_distance = character_row - self.current_row
            column_distance = character_column - self.current_column
            if (abs(row_distance) == 1 and column_distance == 0) or (abs(column_distance) == 1 and row_distance == 0):
                print("The " + self.name + " attacks you!")
                SupportInfo.attack(self.strength, self.strength, self.equippedWeapon, player)
            elif row_distance < 0 and column_distance <= 0:
                check = self.currentRoom.room[self.current_row - 1][self.current_column]
                if check == " " or check == "t" or check == "T" or check == "c" or check == "C":
                    self.currentRoom.room[self.current_row][self.current_column] = self.previous
                    self.current_row -= 1
                    self.previous = self.currentRoom.room[self.current_row][self.current_column]
                    self.currentRoom.room[self.current_row][self.current_column] = "g"
            elif row_distance >= 0 and column_distance < 0:
                check = self.currentRoom.room[self.current_row][self.current_column - 1]
                if check == " " or check == "t" or check == "T" or check == "c" or check == "C":
                    self.currentRoom.room[self.current_row][self.current_column] = self.previous
                    self.current_column -= 1
                    self.previous = self.currentRoom.room[self.current_row][self.current_column]
                    self.currentRoom.room[self.current_row][self.current_column] = "g"
            elif row_distance > 0 and column_distance >= 0:
                check = self.currentRoom.room[self.current_row + 1][self.current_column]
                if check == " " or check == "t" or check == "T" or check == "c" or check == "C":
                    self.currentRoom.room[self.current_row][self.current_column] = self.previous
                    self.current_row += 1
                    self.previous = self.currentRoom.room[self.current_row][self.current_column]
                    self.currentRoom.room[self.current_row][self.current_column] = "g"
            elif row_distance <= 0 and column_distance > 0:
                check = self.currentRoom.room[self.current_row][self.current_column + 1]
                if check == " " or check == "t" or check == "T" or check == "c" or check == "C":
                    self.currentRoom.room[self.current_row][self.current_column] = self.previous
                    self.current_column += 1
                    self.previous = self.currentRoom.room[self.current_row][self.current_column]
                    self.currentRoom.room[self.current_row][self.current_column] = "g"


class GoblinScout:
    def __init__(self, room, row, column):
        self.name = "Goblin Scout"
        self.currentHP = 10
        self.maxHP = 10
        self.xp = 2
        self.strength = 1
        self.dexterity = 3
        self.equippedWeapon = SupportInfo.Weapon("Shortsword", 1, 6, 0, 1)
        self.equippedArmor = SupportInfo.Armor("Leather", 1, 1)
        self.speed = 0
        self.current_row = row
        self.current_column = column
        self.previous = " "
        self.currentRoom = room

    def behavior(self, player):
        near_character = False
        character_row = 0
        character_column = 0
        check_row = self.current_row
        check_column = self.current_column
        up = True
        while not near_character:
            while not (self.currentRoom.room[check_row][check_column] == "W" or
                       self.currentRoom.room[check_row][check_column] == "D") and not near_character:
                if self.currentRoom.room[check_row][check_column] == "Y":
                    near_character = True
                    character_row = check_row
                    character_column = check_column
                check_column -= 1
            check_column = self.current_column + 1
            while not (self.currentRoom.room[check_row][check_column] == "W" or
                       self.currentRoom.room[check_row][check_column] == "D") and not near_character:
                if self.currentRoom.room[check_row][check_column] == "Y":
                    near_character = True
                    character_row = check_row
                    character_column = check_column
                check_column += 1
            check_column = self.current_column
            if (self.currentRoom.room[check_row][check_column] == "W" or
                    self.currentRoom.room[check_row][check_column] == "D") and not near_character:
                if up:
                    up = False
                    check_row = self.current_row
                else:
                    break
            if up:
                check_row -= 1
            else:
                check_row += 1
        if near_character:
            row_distance = character_row - self.current_row
            column_distance = character_column - self.current_column
            if (abs(row_distance) == 1 and column_distance == 0) or (abs(column_distance) == 1 and row_distance == 0):
                print("The " + self.name + " attacks you!")
                SupportInfo.attack(self.strength, self.strength, self.equippedWeapon, player)
            elif row_distance < 0 and column_distance <= 0:
                check = self.currentRoom.room[self.current_row - 1][self.current_column]
                if check == " " or check == "t" or check == "T" or check == "c" or check == "C":
                    self.currentRoom.room[self.current_row][self.current_column] = self.previous
                    self.current_row -= 1
                    self.previous = self.currentRoom.room[self.current_row][self.current_column]
                    self.currentRoom.room[self.current_row][self.current_column] = "g"
            elif row_distance >= 0 and column_distance < 0:
                check = self.currentRoom.room[self.current_row][self.current_column - 1]
                if check == " " or check == "t" or check == "T" or check == "c" or check == "C":
                    self.currentRoom.room[self.current_row][self.current_column] = self.previous
                    self.current_column -= 1
                    self.previous = self.currentRoom.room[self.current_row][self.current_column]
                    self.currentRoom.room[self.current_row][self.current_column] = "g"
            elif row_distance > 0 and column_distance >= 0:
                check = self.currentRoom.room[self.current_row + 1][self.current_column]
                if check == " " or check == "t" or check == "T" or check == "c" or check == "C":
                    self.currentRoom.room[self.current_row][self.current_column] = self.previous
                    self.current_row += 1
                    self.previous = self.currentRoom.room[self.current_row][self.current_column]
                    self.currentRoom.room[self.current_row][self.current_column] = "g"
            elif row_distance <= 0 and column_distance > 0:
                check = self.currentRoom.room[self.current_row][self.current_column + 1]
                if check == " " or check == "t" or check == "T" or check == "c" or check == "C":
                    self.currentRoom.room[self.current_row][self.current_column] = self.previous
                    self.current_column += 1
                    self.previous = self.currentRoom.room[self.current_row][self.current_column]
                    self.currentRoom.room[self.current_row][self.current_column] = "g"


class GoblinWarrior:
    def __init__(self, room, row, column):
        self.name = "Goblin Warrior"
        self.currentHP = 15
        self.maxHP = 15
        self.xp = 2
        self.strength = 3
        self.dexterity = 1
        self.equippedWeapon = SupportInfo.Weapon("Longsword", 1, 8, 1.2, 1)
        self.equippedArmor = SupportInfo.Armor("Mail", 3, 1.5)
        self.speed = 0
        self.current_row = row
        self.current_column = column
        self.previous = " "
        self.currentRoom = room

    def behavior(self, player):
        near_character = False
        character_row = 0
        character_column = 0
        check_row = self.current_row
        check_column = self.current_column
        up = True
        while not near_character:
            while not (self.currentRoom.room[check_row][check_column] == "W" or
                       self.currentRoom.room[check_row][check_column] == "D") and not near_character:
                if self.currentRoom.room[check_row][check_column] == "Y":
                    near_character = True
                    character_row = check_row
                    character_column = check_column
                check_column -= 1
            check_column = self.current_column + 1
            while not (self.currentRoom.room[check_row][check_column] == "W" or
                       self.currentRoom.room[check_row][check_column] == "D") and not near_character:
                if self.currentRoom.room[check_row][check_column] == "Y":
                    near_character = True
                    character_row = check_row
                    character_column = check_column
                check_column += 1
            check_column = self.current_column
            if (self.currentRoom.room[check_row][check_column] == "W" or
                    self.currentRoom.room[check_row][check_column] == "D") and not near_character:
                if up:
                    up = False
                    check_row = self.current_row
                else:
                    break
            if up:
                check_row -= 1
            else:
                check_row += 1
        if near_character:
            row_distance = character_row - self.current_row
            column_distance = character_column - self.current_column
            if (abs(row_distance) == 1 and column_distance == 0) or (abs(column_distance) == 1 and row_distance == 0):
                print("The " + self.name + " attacks you!")
                SupportInfo.attack(self.strength, self.strength, self.equippedWeapon, player)
            elif row_distance < 0 and column_distance <= 0:
                check = self.currentRoom.room[self.current_row - 1][self.current_column]
                if check == " " or check == "t" or check == "T" or check == "c" or check == "C":
                    self.currentRoom.room[self.current_row][self.current_column] = self.previous
                    self.current_row -= 1
                    self.previous = self.currentRoom.room[self.current_row][self.current_column]
                    self.currentRoom.room[self.current_row][self.current_column] = "g"
            elif row_distance >= 0 and column_distance < 0:
                check = self.currentRoom.room[self.current_row][self.current_column - 1]
                if check == " " or check == "t" or check == "T" or check == "c" or check == "C":
                    self.currentRoom.room[self.current_row][self.current_column] = self.previous
                    self.current_column -= 1
                    self.previous = self.currentRoom.room[self.current_row][self.current_column]
                    self.currentRoom.room[self.current_row][self.current_column] = "g"
            elif row_distance > 0 and column_distance >= 0:
                check = self.currentRoom.room[self.current_row + 1][self.current_column]
                if check == " " or check == "t" or check == "T" or check == "c" or check == "C":
                    self.currentRoom.room[self.current_row][self.current_column] = self.previous
                    self.current_row += 1
                    self.previous = self.currentRoom.room[self.current_row][self.current_column]
                    self.currentRoom.room[self.current_row][self.current_column] = "g"
            elif row_distance <= 0 and column_distance > 0:
                check = self.currentRoom.room[self.current_row][self.current_column + 1]
                if check == " " or check == "t" or check == "T" or check == "c" or check == "C":
                    self.currentRoom.room[self.current_row][self.current_column] = self.previous
                    self.current_column += 1
                    self.previous = self.currentRoom.room[self.current_row][self.current_column]
                    self.currentRoom.room[self.current_row][self.current_column] = "g"


class GoblinArcher:
    def __init__(self, room, row, column):
        self.name = "Goblin Archer"
        self.currentHP = 10
        self.maxHP = 10
        self.xp = 2
        self.strength = 1
        self.dexterity = 2
        self.equippedWeapon = SupportInfo.Weapon("Shortbow", 4, 6, 2, 2)
        self.equippedArmor = SupportInfo.Armor("Leather", 1, 0.5)
        self.speed = 0
        self.current_row = row
        self.current_column = column
        self.previous = " "
        self.currentRoom = room

    def behavior(self, player):
        near_character = False
        character_row = 0
        character_column = 0
        check_row = self.current_row
        check_column = self.current_column
        up = True
        while not near_character:
            while not (self.currentRoom.room[check_row][check_column] == "W" or
                       self.currentRoom.room[check_row][check_column] == "D") and not near_character:
                if self.currentRoom.room[check_row][check_column] == "Y":
                    near_character = True
                    character_row = check_row
                    character_column = check_column
                check_column -= 1
            check_column = self.current_column + 1
            while not (self.currentRoom.room[check_row][check_column] == "W" or
                       self.currentRoom.room[check_row][check_column] == "D") and not near_character:
                if self.currentRoom.room[check_row][check_column] == "Y":
                    near_character = True
                    character_row = check_row
                    character_column = check_column
                check_column += 1
            check_column = self.current_column
            if (self.currentRoom.room[check_row][check_column] == "W" or
                    self.currentRoom.room[check_row][check_column] == "D") and not near_character:
                if up:
                    up = False
                    check_row = self.current_row
                else:
                    break
            if up:
                check_row -= 1
            else:
                check_row += 1
        if near_character:
            row_distance = character_row - self.current_row
            column_distance = character_column - self.current_column
            if abs(row_distance) + abs(column_distance) <= self.equippedWeapon.range:
                print("The " + self.name + " attacks you!")
                SupportInfo.attack(self.dexterity, self.strength, self.equippedWeapon, player)
            elif row_distance < 0 and column_distance <= 0:
                check = self.currentRoom.room[self.current_row - 1][self.current_column]
                if check == " " or check == "t" or check == "T" or check == "c" or check == "C":
                    self.currentRoom.room[self.current_row][self.current_column] = self.previous
                    self.current_row -= 1
                    self.previous = self.currentRoom.room[self.current_row][self.current_column]
                    self.currentRoom.room[self.current_row][self.current_column] = "g"
            elif row_distance >= 0 and column_distance < 0:
                check = self.currentRoom.room[self.current_row][self.current_column - 1]
                if check == " " or check == "t" or check == "T" or check == "c" or check == "C":
                    self.currentRoom.room[self.current_row][self.current_column] = self.previous
                    self.current_column -= 1
                    self.previous = self.currentRoom.room[self.current_row][self.current_column]
                    self.currentRoom.room[self.current_row][self.current_column] = "g"
            elif row_distance > 0 and column_distance >= 0:
                check = self.currentRoom.room[self.current_row + 1][self.current_column]
                if check == " " or check == "t" or check == "T" or check == "c" or check == "C":
                    self.currentRoom.room[self.current_row][self.current_column] = self.previous
                    self.current_row += 1
                    self.previous = self.currentRoom.room[self.current_row][self.current_column]
                    self.currentRoom.room[self.current_row][self.current_column] = "g"
            elif row_distance <= 0 and column_distance > 0:
                check = self.currentRoom.room[self.current_row][self.current_column + 1]
                if check == " " or check == "t" or check == "T" or check == "c" or check == "C":
                    self.currentRoom.room[self.current_row][self.current_column] = self.previous
                    self.current_column += 1
                    self.previous = self.currentRoom.room[self.current_row][self.current_column]
                    self.currentRoom.room[self.current_row][self.current_column] = "g"


def choose_enemies(room, row, column):
    if SupportInfo.characterLevel == 1:
        selection = 1
    else:
        selection = random.randrange(1, 5, 1)
    if selection == 1:
        return Goblin(room, row, column)
    elif selection == 2:
        return GoblinScout(room, row, column)
    elif selection == 3:
        return GoblinWarrior(room, row, column)
    else:
        return GoblinArcher(room, row, column)
