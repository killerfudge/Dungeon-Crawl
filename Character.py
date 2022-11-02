from Rooms import OpeningRoom, activeCharacters
import SupportInfo
import random


def determine_turn(creatures):
    quickest = 0
    for creature in creatures:
        slow = creature.equippedWeapon.weight + creature.equippedArmor.weight - creature.strength
        speed = 0
        if slow > 0:
            speed += 1 + creature.dexterity - slow
        else:
            speed += 1 + creature.dexterity
        if speed > 0.1:
            creature.speed += speed
        else:
            creature.speed += 0.1
        if quickest == 0:
            quickest = creature
        elif quickest.speed < creature.speed:
            quickest = creature
    quickest.speed = 0
    return quickest


class Fighter:
    def __init__(self):
        self.name = "You"
        self.xp = 0
        self.gold = 0
        self.currentHP = 20
        self.maxHP = 20
        self.strength = 1
        self.dexterity = 1
        self.magic = 0
        self.speed = 0
        self.equippedWeapon = SupportInfo.Weapon("Shortsword", 1, 6, 1, 1, 5)
        self.storedWeapons = []
        self.knives = 0
        self.arrows = 0
        self.equippedArmor = SupportInfo.Armor("None", 0, 0)
        self.storedArmor = []
        self.current_row = 3
        self.current_column = 1
        self.previous = " "
        self.currentRoom = OpeningRoom(self)

    def print_details(self):
        print(str(self.currentHP) + "/" + str(self.maxHP) + " HP")
        print("Level: " + str(SupportInfo.characterLevel))
        print("XP: " + str(self.xp))
        print("Gold: " + str(self.gold))
        print("Strength: " + str(self.strength))
        print("Dexterity: " + str(self.dexterity))
        print("Magic: " + str(self.magic))
        print("Weapon: " + self.equippedWeapon.print_details())
        print(str(self.knives) + " throwing knives")
        print(str(self.arrows) + " arrows")
        print("Armor: " + self.equippedArmor.print_details())

    def throw_knife(self):
        answer = ""
        target = None
        up = True
        row = character.current_row
        column = character.current_column - 1
        checked = False
        attacked = False
        while not checked:
            distance = abs(self.current_column - column) + abs(self.current_row - row)
            while distance <= self.dexterity + 1 and not checked:
                if self.currentRoom.room[row][column] == "W" or self.currentRoom.room[row][column] == "D":
                    break
                if self.currentRoom.room[row][column] != " ":
                    for creature in activeCharacters:
                        if creature.current_row == row and creature.current_column == column and creature != self and \
                                creature.currentRoom is self.currentRoom:
                            answer = input("Throw at " + creature.name + "? ")
                            if answer.lower() == "yes":
                                checked = True
                                target = creature
                                break
                column -= 1
                distance = abs(self.current_column - column) + abs(self.current_row - row)
            column = self.current_column + 1
            distance = abs(self.current_column - column) + abs(self.current_row - row)
            while distance <= self.dexterity + 1 and not checked:
                if self.currentRoom.room[row][column] == "W" or self.currentRoom.room[row][column] == "D":
                    break
                if self.currentRoom.room[row][column] != " ":
                    for creature in activeCharacters:
                        if creature.current_row == row and creature.current_column == column and creature != self and \
                                creature.currentRoom is self.currentRoom:
                            answer = input("Throw at " + creature.name + "? ")
                            if answer.lower() == "yes":
                                checked = True
                                target = creature
                                break
                column += 1
                distance = abs(self.current_column - column) + abs(self.current_row - row)
            column = self.current_column
            if up:
                if abs(row - self.current_row) <= self.dexterity:
                    row -= 1
                else:
                    up = False
                    row = self.current_row + 1
            else:
                if abs(row - self.current_row) <= self.dexterity:
                    row += 1
                else:
                    break
            if self.currentRoom.room[row][column] != ' ':
                if self.currentRoom.room[row][column] == "W" or self.currentRoom.room[row][column] == "D":
                    if up:
                        up = False
                        row = self.current_row + 1
                    else:
                        break
        if answer.lower() == "yes":
            print("You throw a knife at " + target.name + ".")
            SupportInfo.attack(self.dexterity, self.strength, SupportInfo.Weapon("Knife", self.dexterity + 1, 1, 0, 1),
                               target)
            if target.currentHP <= 0:
                print(target.name + " is slain!")
                self.xp += target.xp
                self.currentRoom.room[target.current_row][target.current_column] = target.previous
                activeCharacters.remove(target)
            if self.xp >= SupportInfo.characterLevel * 10:
                self.level_up()
            self.knives -= 1
            attacked = True
        elif answer.lower() == "no":
            print("No more available targets.")
        else:
            print("No available targets.")
        return attacked

    def ranged_attack(self):
        answer = ""
        target = None
        up = True
        row = character.current_row
        column = character.current_column - 1
        checked = False
        attacked = False
        while not checked:
            distance = abs(self.current_column - column) + abs(self.current_row - row)
            while distance <= self.equippedWeapon.range and not checked:
                if self.currentRoom.room[row][column] == "W" or self.currentRoom.room[row][column] == "D":
                    break
                if self.currentRoom.room[row][column] != " ":
                    for creature in activeCharacters:
                        if creature.current_row == row and creature.current_column == column and creature != self and \
                                creature.currentRoom is self.currentRoom:
                            answer = input("Attack " + creature.name + "? ")
                            if answer.lower() == "yes":
                                checked = True
                                target = creature
                                break
                column -= 1
                distance = abs(self.current_column - column) + abs(self.current_row - row)
            column = self.current_column + 1
            distance = abs(self.current_column - column) + abs(self.current_row - row)
            while distance <= self.equippedWeapon.range and not checked:
                if self.currentRoom.room[row][column] == "W" or self.currentRoom.room[row][column] == "D":
                    break
                if self.currentRoom.room[row][column] != " ":
                    for creature in activeCharacters:
                        if creature.current_row == row and creature.current_column == column and creature != self and \
                                creature.currentRoom is self.currentRoom:
                            answer = input("Attack " + creature.name + "? ")
                            if answer.lower() == "yes":
                                checked = True
                                target = creature
                                break
                column += 1
                distance = abs(self.current_column - column) + abs(self.current_row - row)
            column = self.current_column
            if up:
                if abs(row - self.current_row) <= self.equippedWeapon.range:
                    row -= 1
                else:
                    up = False
                    row = self.current_row + 1
            else:
                if abs(row - self.current_row) <= self.equippedWeapon.range:
                    row += 1
                else:
                    break
            if self.currentRoom.room[row][column] != ' ':
                if self.currentRoom.room[row][column] == "W" or self.currentRoom.room[row][column] == "D":
                    if up:
                        up = False
                        row = self.current_row + 1
                    else:
                        break
        if answer.lower() == "yes":
            print("You attack " + target.name + " with your " + self.equippedWeapon.name + ".")
            if self.equippedWeapon.name == "Shortbow" or self.equippedWeapon.name == "Longbow":
                self.arrows -= 1
                print("You have " + str(self.arrows) + " arrows remaining.")
            SupportInfo.attack(self.dexterity, self.strength, self.equippedWeapon, target)
            if target.currentHP <= 0:
                print(target.name + " is slain!")
                self.xp += target.xp
                self.currentRoom.room[target.current_row][target.current_column] = target.previous
                activeCharacters.remove(target)
            if self.xp >= SupportInfo.characterLevel * 10:
                self.level_up()
            attacked = True
        elif answer.lower() == "no":
            print("No more available targets.")
        else:
            print("No available targets.")
        return attacked

    def melee_attack(self):
        attacked = False
        reply = "no"
        target = None
        if self.currentRoom.room[self.current_row - 1][self.current_column] != ' ':
            for creature in activeCharacters:
                if creature.current_row == self.current_row - 1 and creature.current_column == self.current_column and \
                        creature.currentRoom is self.currentRoom:
                    reply = input("Attack " + creature.name + " above you? ")
                    if reply.lower() == "yes":
                        target = creature
                        break
        if self.currentRoom.room[self.current_row][self.current_column + 1] != ' ' and reply.lower() == "no":
            for creature in activeCharacters:
                if creature.current_row == self.current_row and creature.current_column == self.current_column + 1 and \
                        creature.currentRoom is self.currentRoom:
                    reply = input("Attack " + creature.name + " to your right? ")
                    if reply.lower() == "yes":
                        target = creature
                        break
        if self.currentRoom.room[self.current_row + 1][self.current_column] != ' ' and reply.lower() == "no":
            for creature in activeCharacters:
                if creature.current_row == self.current_row + 1 and creature.current_column == self.current_column and \
                        creature.currentRoom is self.currentRoom:
                    reply = input("Attack " + creature.name + " below you? ")
                    if reply.lower() == "yes":
                        target = creature
                        break
        if self.currentRoom.room[self.current_row][self.current_column - 1] != ' ' and reply.lower() == "no":
            for creature in activeCharacters:
                if creature.current_row == self.current_row and creature.current_column == self.current_column - 1 and \
                        creature.currentRoom is self.currentRoom:
                    reply = input("Attack " + creature.name + " to your left? ")
                    if reply.lower() == "yes":
                        target = creature
                        break
        if reply.lower() == "yes":
            print("You attack " + target.name + " with your " + self.equippedWeapon.name + ".")
            SupportInfo.attack(self.strength, self.strength, self.equippedWeapon, target)
            if target.currentHP <= 0:
                print(target.name + " is slain!")
                self.xp += target.xp
                self.currentRoom.room[target.current_row][target.current_column] = target.previous
                activeCharacters.remove(target)
            if self.xp >= SupportInfo.characterLevel * 10:
                self.level_up()
            attacked = True
        if reply.lower() == "no" or reply == "":
            print("No targets available.")
        return attacked

    def attack(self):
        reply = ""
        if self.knives > 0:
            reply = input("Do you want to attack with your weapon or throw a knife? ")
            if answer.lower() == "weapon":
                reply = "no"
        if reply.lower() == "throw a knife" or reply.lower() == "throw" or reply.lower() == "knife":
            attacked = self.throw_knife()
        elif self.equippedWeapon.range == 1:
            attacked = self.melee_attack()
        else:
            if (self.equippedWeapon.name == "Shortbow" or self.equippedWeapon.name == "Longbow") and self.arrows > 0:
                attacked = self.ranged_attack()
            else:
                print("You are out of arrows.")
                attacked = False
        return attacked

    def level_up(self):
        print("Level up!")
        SupportInfo.characterLevel += 1
        chosen = False
        self.maxHP += 5
        self.currentHP = self.maxHP
        while not chosen:
            print("Current Strength: " + str(self.strength))
            print("Current Dexterity: " + str(self.dexterity))
            print("Current Magic: " + str(self.magic))
            improve = input("Choose a stat to increase by one: ")
            if improve.lower() == "strength":
                self.strength += 1
                chosen = True
            elif improve.lower() == "dexterity":
                self.dexterity += 1
                chosen = True
            elif improve.lower() == "magic":
                self.magic += 1
                chosen = True
            else:
                print("Not a valid option.")


'''
character = None
chosen = False
while not chosen:
    print("Available classes:")
    print("Fighter")
    player_input = input("Select class: ")
    if player_input.lower() == "fighter":
        character = Fighter()
        chosen = True
    else:
        print("Invalid class.")
'''

quitGame = False
character = Fighter()
while not quitGame:
    turn = determine_turn(activeCharacters)
    if turn == character:
        for row in character.currentRoom.room:
            print(row)
        acted = False
        while not acted:
            player_input = input("What would you like to do? ")
            if player_input.lower() == "move up":
                moved = True
                character.current_row -= 1
                if character.currentRoom.room[character.current_row][character.current_column] == "W":
                    character.current_row += 1
                    print("You run into the wall and cannot move farther that direction")
                    moved = False
                elif character.currentRoom.room[character.current_row][character.current_column] == "D":
                    character.currentRoom.leave(character, 'Y')
                    moved = False
                    acted = True
                for creature in activeCharacters:
                    if character.currentRoom is creature.currentRoom and \
                            character.current_row == creature.current_row and \
                            character.current_column == creature.current_column and character != creature:
                        character.current_row += 1
                        print(creature.name + " blocks your path.")
                        moved = False
                if moved:
                    character.currentRoom.room[character.current_row + 1][character.current_column] = character.previous
                    character.previous = character.currentRoom.room[character.current_row][character.current_column]
                    character.currentRoom.room[character.current_row][character.current_column] = "Y"
                    acted = True
            elif player_input.lower() == "move down":
                moved = True
                character.current_row += 1
                if character.currentRoom.room[character.current_row][character.current_column] == "W":
                    character.current_row -= 1
                    print("You run into the wall and cannot move farther that direction")
                    moved = False
                elif character.currentRoom.room[character.current_row][character.current_column] == "D":
                    character.currentRoom.leave(character, 'Y')
                    moved = False
                    acted = True
                for creature in activeCharacters:
                    if character.currentRoom is creature.currentRoom and \
                            character.current_row == creature.current_row and \
                            character.current_column == creature.current_column and character != creature:
                        character.current_row -= 1
                        print(creature.name + " blocks your path.")
                        moved = False
                if moved:
                    character.currentRoom.room[character.current_row - 1][character.current_column] = character.previous
                    character.previous = character.currentRoom.room[character.current_row][character.current_column]
                    character.currentRoom.room[character.current_row][character.current_column] = "Y"
                    acted = True
            elif player_input.lower() == "move right":
                moved = True
                character.current_column += 1
                if character.currentRoom.room[character.current_row][character.current_column] == "W":
                    character.current_column -= 1
                    print("You run into the wall and cannot move farther that direction")
                    moved = False
                elif character.currentRoom.room[character.current_row][character.current_column] == "D":
                    character.currentRoom.leave(character, 'Y')
                    moved = False
                    acted = True
                for creature in activeCharacters:
                    if character.currentRoom is creature.currentRoom and \
                            character.current_row == creature.current_row and \
                            character.current_column == creature.current_column and character != creature:
                        character.current_column -= 1
                        print(creature.name + " blocks your path.")
                        moved = False
                if moved:
                    character.currentRoom.room[character.current_row][character.current_column - 1] = character.previous
                    character.previous = character.currentRoom.room[character.current_row][character.current_column]
                    character.currentRoom.room[character.current_row][character.current_column] = "Y"
                    acted = True
            elif player_input.lower() == "move left":
                moved = True
                character.current_column -= 1
                if character.currentRoom.room[character.current_row][character.current_column] == "W":
                    character.current_column += 1
                    print("You run into the wall and cannot move farther that direction")
                    moved = False
                elif character.currentRoom.room[character.current_row][character.current_column] == "D":
                    character.currentRoom.leave(character, 'Y')
                    moved = False
                    acted = True
                for creature in activeCharacters:
                    if character.currentRoom is creature.currentRoom and \
                            character.current_row == creature.current_row and \
                            character.current_column == creature.current_column and character != creature:
                        character.current_column += 1
                        print(creature.name + " blocks your path.")
                        moved = False
                if moved:
                    character.currentRoom.room[character.current_row][character.current_column + 1] = character.previous
                    character.previous = character.currentRoom.room[character.current_row][character.current_column]
                    character.currentRoom.room[character.current_row][character.current_column] = "Y"
                    acted = True
            elif player_input.lower() == "attack":
                acted = character.attack()
            elif player_input.lower() == "examine":
                answer = input("Where do you want to examine? ")
                if answer.lower() == "up":
                    if character.currentRoom.room[character.current_row - 1][character.current_column] == ' ':
                        print("There is nothing there.")
                    elif character.currentRoom.room[character.current_row - 1][character.current_column] == 'T':
                        answer = input("There is a table there. Would you like to examine it? ")
                        character.currentRoom.room[character.current_row - 1][character.current_column] = 't'
                        if answer.lower() == "yes":
                            table = random.randrange(0, len(SupportInfo.tableOptions), 1)
                            if SupportInfo.tableOptions[table][0] == "knives":
                                print("You find " + str(SupportInfo.tableOptions[table][1]) + " throwing knives.")
                                character.knives += SupportInfo.tableOptions[table][1]
                    elif character.currentRoom.room[character.current_row - 1][character.current_column] == 't':
                        print("You see a table. You've already searched it.")
                    elif character.currentRoom.room[character.current_row - 1][character.current_column] == 'C':
                        answer = input("There is a chest on the floor. Do you want to open it? ")
                        if answer.lower() == "yes":
                            character.currentRoom.room[character.current_row - 1][character.current_column] = 'c'
                            table = random.randrange(0, len(SupportInfo.chestOptions), 1)
                            if SupportInfo.chestOptions[table] == "Weapon":
                                weapon = SupportInfo.weaponOptions[random.randrange(0, len(SupportInfo.weaponOptions),
                                                                                    1)]
                                if weapon.name == "Shortbow" or weapon.name == "Longbow":
                                    answer = input("You find a " + weapon.name +
                                                   " and 10 arrows. Do you want to equip " + weapon.name + "? ")
                                    character.arrows += 10
                                else:
                                    answer = input("You find a " + weapon.name + ". Do you want to equip it? ")
                                if answer.lower() == "yes":
                                    if character.equippedWeapon.name != "Fist":
                                        character.storedWeapons.append(character.equippedWeapon)
                                    character.equippedWeapon = weapon
                                else:
                                    print(weapon.name + " put away.")
                                    character.storedWeapons.append(weapon)
                            elif SupportInfo.chestOptions[table] == "Armor":
                                armor = SupportInfo.armorOptions[random.randrange(0, len(SupportInfo.armorOptions), 1)]
                                answer = input("You find a suit of " + armor.name + " armor. Do you want to equip it? ")
                                if answer.lower() == "yes":
                                    if character.equippedArmor.name != "None":
                                        character.storedArmor.append(character.equippedArmor)
                                    character.equippedArmor = armor
                                else:
                                    print(armor.name + " put away.")
                                    character.storedArmor.append(armor)
                    elif character.currentRoom.room[character.current_row - 1][character.current_column] == 'c':
                        print("You see an open chest on the floor.")
                    elif character.currentRoom.room[character.current_row - 1][character.current_column] == 's':
                        answer = input("You see what appears to be a small shop. Do you want to check the wares? ")
                        if answer.lower() == "yes":
                            character.currentRoom.shop.shop(character)
                elif answer.lower() == "down":
                    if character.currentRoom.room[character.current_row + 1][character.current_column] == ' ':
                        print("There is nothing there.")
                    elif character.currentRoom.room[character.current_row + 1][character.current_column] == 'T':
                        answer = input("There is a table there. Would you like to examine it? ")
                        character.currentRoom.room[character.current_row + 1][character.current_column] = 't'
                        if answer.lower() == "yes":
                            table = random.randrange(0, len(SupportInfo.tableOptions), 1)
                            if SupportInfo.tableOptions[table][0] == "knives":
                                print("You find " + str(SupportInfo.tableOptions[table][1]) + " throwing knives.")
                                character.knives += SupportInfo.tableOptions[table][1]
                    elif character.currentRoom.room[character.current_row + 1][character.current_column] == 't':
                        print("You see a table. You've already searched it.")
                    elif character.currentRoom.room[character.current_row + 1][character.current_column] == 'C':
                        answer = input("There is a chest on the floor. Do you want to open it? ")
                        if answer.lower() == "yes":
                            character.currentRoom.room[character.current_row + 1][character.current_column] = 'c'
                            table = random.randrange(0, len(SupportInfo.chestOptions), 1)
                            if SupportInfo.chestOptions[table] == "Weapon":
                                weapon = SupportInfo.weaponOptions[random.randrange(0, len(SupportInfo.weaponOptions),
                                                                                    1)]
                                if weapon.name == "Shortbow" or weapon.name == "Longbow":
                                    answer = input("You find a " + weapon.name +
                                                   " and 10 arrows. Do you want to equip " + weapon.name + "? ")
                                    character.arrows += 10
                                else:
                                    answer = input("You find a " + weapon.name + ". Do you want to equip it? ")
                                if answer.lower() == "yes":
                                    if character.equippedWeapon.name != "Fist":
                                        character.storedWeapons.append(character.equippedWeapon)
                                    character.equippedWeapon = weapon
                                else:
                                    print(weapon.name + " put away.")
                                    character.storedWeapons.append(weapon)
                            elif SupportInfo.chestOptions[table] == "Armor":
                                armor = SupportInfo.armorOptions[random.randrange(0, len(SupportInfo.armorOptions), 1)]
                                answer = input("You find a suit of " + armor.name + " armor. Do you want to equip it? ")
                                if answer.lower() == "yes":
                                    if character.equippedArmor.name != "None":
                                        character.storedArmor.append(character.equippedArmor)
                                    character.equippedArmor = armor
                                else:
                                    print(armor.name + " put away.")
                                    character.storedArmor.append(armor)
                    elif character.currentRoom.room[character.current_row + 1][character.current_column] == 'c':
                        print("You see an open chest on the floor.")
                    elif character.currentRoom.room[character.current_row + 1][character.current_column] == 's':
                        answer = input("You see what appears to be a small shop. Do you want to check the wares? ")
                        if answer.lower() == "yes":
                            character.currentRoom.shop.shop(character)
                elif answer.lower() == "right":
                    if character.currentRoom.room[character.current_row][character.current_column + 1] == ' ':
                        print("There is nothing there.")
                    elif character.currentRoom.room[character.current_row][character.current_column + 1] == 'T':
                        answer = input("There is a table there. Would you like to examine it? ")
                        character.currentRoom.room[character.current_row][character.current_column + 1] = 't'
                        if answer.lower() == "yes":
                            table = random.randrange(0, len(SupportInfo.tableOptions), 1)
                            if SupportInfo.tableOptions[table][0] == "knives":
                                print("You find " + str(SupportInfo.tableOptions[table][1]) + " throwing knives.")
                                character.knives += SupportInfo.tableOptions[table][1]
                    elif character.currentRoom.room[character.current_row][character.current_column + 1] == 't':
                        print("You see a table. You've already searched it.")
                    elif character.currentRoom.room[character.current_row][character.current_column + 1] == 'C':
                        answer = input("There is a chest on the floor. Do you want to open it? ")
                        if answer.lower() == "yes":
                            character.currentRoom.room[character.current_row][character.current_column + 1] = 'c'
                            table = random.randrange(0, len(SupportInfo.chestOptions), 1)
                            if SupportInfo.chestOptions[table] == "Weapon":
                                weapon = SupportInfo.weaponOptions[random.randrange(0, len(SupportInfo.weaponOptions),
                                                                                    1)]
                                if weapon.name == "Shortbow" or weapon.name == "Longbow":
                                    answer = input("You find a " + weapon.name +
                                                   " and 10 arrows. Do you want to equip " + weapon.name + "? ")
                                    character.arrows += 10
                                else:
                                    answer = input("You find a " + weapon.name + ". Do you want to equip it? ")
                                if answer.lower() == "yes":
                                    if character.equippedWeapon.name != "Fist":
                                        character.storedWeapons.append(character.equippedWeapon)
                                    character.equippedWeapon = weapon
                                else:
                                    print(weapon.name + " put away.")
                                    character.storedWeapons.append(weapon)
                            elif SupportInfo.chestOptions[table] == "Armor":
                                armor = SupportInfo.armorOptions[random.randrange(0, len(SupportInfo.armorOptions), 1)]
                                answer = input("You find a suit of " + armor.name + " armor. Do you want to equip it? ")
                                if answer.lower() == "yes":
                                    if character.equippedArmor.name != "None":
                                        character.storedArmor.append(character.equippedArmor)
                                    character.equippedArmor = armor
                                else:
                                    print(armor.name + " put away.")
                                    character.storedArmor.append(armor)
                    elif character.currentRoom.room[character.current_row][character.current_column + 1] == 'c':
                        print("You see an open chest on the floor.")
                    elif character.currentRoom.room[character.current_row][character.current_column + 1] == 's':
                        answer = input("You see what appears to be a small shop. Do you want to check the wares? ")
                        if answer.lower() == "yes":
                            character.currentRoom.shop.shop(character)
                elif answer.lower() == "left":
                    if character.currentRoom.room[character.current_row][character.current_column - 1] == ' ':
                        print("There is nothing there.")
                    elif character.currentRoom.room[character.current_row][character.current_column - 1] == 'T':
                        answer = input("There is a table there. Would you like to examine it? ")
                        character.currentRoom.room[character.current_row][character.current_column - 1] = 't'
                        if answer.lower() == "yes":
                            table = random.randrange(0, len(SupportInfo.tableOptions), 1)
                            if SupportInfo.tableOptions[table][0] == "knives":
                                print("You find " + str(SupportInfo.tableOptions[table][1]) + " throwing knives.")
                                character.knives += SupportInfo.tableOptions[table][1]
                    elif character.currentRoom.room[character.current_row][character.current_column - 1] == 't':
                        print("You see a table. You've already searched it.")
                    elif character.currentRoom.room[character.current_row][character.current_column - 1] == 'C':
                        answer = input("There is a chest on the floor. Do you want to open it? ")
                        if answer.lower() == "yes":
                            character.currentRoom.room[character.current_row][character.current_column - 1] = 'c'
                            table = random.randrange(0, len(SupportInfo.chestOptions), 1)
                            if SupportInfo.chestOptions[table] == "Weapon":
                                weapon = SupportInfo.weaponOptions[random.randrange(0, len(SupportInfo.weaponOptions),
                                                                                    1)]
                                if weapon.name == "Shortbow" or weapon.name == "Longbow":
                                    answer = input("You find a " + weapon.name +
                                                   " and 10 arrows. Do you want to equip " + weapon.name + "? ")
                                    character.arrows += 10
                                else:
                                    answer = input("You find a " + weapon.name + ". Do you want to equip it? ")
                                if answer.lower() == "yes":
                                    if character.equippedWeapon.name != "Fist":
                                        character.storedWeapons.append(character.equippedWeapon)
                                    character.equippedWeapon = weapon
                                else:
                                    print(weapon.name + " put away.")
                                    character.storedWeapons.append(weapon)
                            elif SupportInfo.chestOptions[table] == "Armor":
                                armor = SupportInfo.armorOptions[random.randrange(0, len(SupportInfo.armorOptions), 1)]
                                answer = input("You find a suit of " + armor.name + " armor. Do you want to equip it? ")
                                if answer.lower() == "yes":
                                    if character.equippedArmor.name != "None":
                                        character.storedArmor.append(character.equippedArmor)
                                    character.equippedArmor = armor
                                else:
                                    print(armor.name + " put away.")
                                    character.storedArmor.append(armor)
                    elif character.currentRoom.room[character.current_row][character.current_column - 1] == 'c':
                        print("You see an open chest on the floor.")
                    elif character.currentRoom.room[character.current_row][character.current_column - 1] == 's':
                        answer = input("You see what appears to be a small shop. Do you want to check the wares? ")
                        if answer.lower() == "yes":
                            character.currentRoom.shop.shop(character)
                else:
                    if character.previous == ' ':
                        print("You are standing on the floor.")
                    elif character.previous == 'T':
                        answer = input("You are standing by a table. Would you like to examine it?")
                        character.previous = 't'
                        if answer.lower() == "yes":
                            table = random.randrange(0, len(SupportInfo.tableOptions), 1)
                            if SupportInfo.tableOptions[table][0] == "knives":
                                print("You find " + str(SupportInfo.tableOptions[table][1]) + " throwing knives.")
                                character.knives += SupportInfo.tableOptions[table][1]
                    elif character.previous == 't':
                        print("You are standing by a table. You've already searched it.")
                    elif character.previous == 'C':
                        answer = input("You are standing by a chest. Do you want to open it?")
                        character.previous = 'c'
                        if answer.lower() == "yes":
                            table = random.randrange(0, len(SupportInfo.chestOptions) - 1, 1)
                            if SupportInfo.chestOptions[table] == "Weapon":
                                weapon = SupportInfo.weaponOptions[random.randrange(0, len(SupportInfo.weaponOptions),
                                                                                    1)]
                                if weapon.name == "Shortbow" or weapon.name == "Longbow":
                                    answer = input("You find a " + weapon.name +
                                                   " and 10 arrows. Do you want to equip " + weapon.name + "? ")
                                    character.arrows += 10
                                else:
                                    answer = input("You find a " + weapon.name + ". Do you want to equip it? ")
                                if answer.lower() == "yes":
                                    if character.equippedWeapon.name != "Fist":
                                        character.storedWeapons.append(character.equippedWeapon)
                                    character.equippedWeapon = weapon
                                else:
                                    print(weapon.name + " put away.")
                                    character.storedWeapons.append(weapon)
                            elif SupportInfo.chestOptions[table] == "Armor":
                                armor = SupportInfo.armorOptions[random.randrange(0, len(SupportInfo.armorOptions), 1)]
                                answer = input("You find a suit of " + armor.name + " armor. Do you want to equip it? ")
                                if answer.lower() == "yes":
                                    if character.equippedArmor.name != "None":
                                        character.storedArmor.append(character.equippedArmor)
                                    character.equippedArmor = armor
                                else:
                                    print(armor.name + " put away.")
                                    character.storedArmor.append(armor)
                    elif character.previous == 'c':
                        print("You are standing by an open chest.")
                    elif character.currentRoom.room[character.current_row][character.current_column - 1] == 's':
                        answer = input("You see what appears to be a small shop. Do you want to check the wares? ")
                        if answer.lower() == "yes":
                            character.currentRoom.shop.shop()
            elif player_input.lower() == "wait":
                acted = True
            elif player_input.lower() == "character info" or player_input.lower() == "character":
                character.print_details()
            elif player_input.lower() == "change weapon":
                if len(character.storedWeapons) > 0:
                    print("Equipped Weapon: " + character.equippedWeapon.print_details())
                    print("Stored Weapons:")
                    for weapon in character.storedWeapons:
                        print(weapon.print_details())
                    desired = input("Which weapon do you want to equip? ")
                    equipped = False
                    for weapon in character.storedWeapons:
                        if weapon.name == desired:
                            equipped = True
                            if character.equippedWeapon.name != "Fist":
                                character.storedWeapons.append(character.equippedWeapon)
                            character.equippedWeapon = weapon
                            character.storedWeapons.remove(weapon)
                            print(weapon.name + " equipped.")
                    if not equipped:
                        print("You don't have that weapon.")
                else:
                    print("You don't have any stored weapons to equip.")
            elif player_input.lower() == "change armor":
                if len(character.storedArmor) > 0:
                    print("Equipped Armor: " + character.equippedArmor.print_details())
                    print("Stored Armor:")
                    for weapon in character.storedArmor:
                        print(weapon.print_details())
                    desired = input("Which armor do you want to equip? ")
                    for armor in character.storedArmor:
                        if armor.name == desired:
                            if character.equippedArmor.name != "None":
                                character.storedArmor.append(character.equippedArmor)
                            character.equippedArmor = armor
                            character.storedArmor.remove(armor)
                            print(armor.name + " equipped.")
                        else:
                            print("You don't have that armor.")
                else:
                    print("You don't have any stored armor to equip.")
            elif player_input.lower() == "menu":
                print("Available actions:")
                print("Move (direction): Move a space in the given direction.")
                print("Attack: See if there is an enemy in range to attack")
                print("Examine: See if there is anything interesting in your square or a adjacent square.")
                print("Wait: Pass your action.")
                print("Character info: See your character's current status.")
                print("Change Weapon: Switch your equipped weapon with one you have stored.")
                print("Quit: quit the game.")
            elif player_input.lower() == "quit":
                quitGame = True
                acted = True
            else:
                print("Unknown command.")
    else:
        turn.behavior(character)
    if character.currentHP <= 0:
        print("You have died!")
        quitGame = True
