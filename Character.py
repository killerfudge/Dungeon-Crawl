from Rooms import OpeningRoom, activeCharacters
import SupportInfo
import random
import keyboard
import os


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
        target = None
        up = True
        row = character.current_row
        column = character.current_column - 1
        attacked = False
        while not attacked:
            distance = abs(self.current_column - column) + abs(self.current_row - row)
            while distance <= self.dexterity + 1 and not attacked:
                if self.currentRoom.room[row][column] == "W" or self.currentRoom.room[row][column] == "D":
                    break
                if self.currentRoom.room[row][column] != " ":
                    for creature in activeCharacters:
                        if creature.current_row == row and creature.current_column == column and creature != self and \
                                creature.currentRoom is self.currentRoom:
                            print("Throw at " + creature.name + "? (a-attack d-don't attack)")
                            a = False
                            while True:
                                decision = keyboard.read_event(suppress=True)
                                if decision.event_type == keyboard.KEY_UP and decision.name == "a":
                                    target = creature
                                    attacked = True
                                    break
                                elif decision.event_type == keyboard.KEY_UP:
                                    break
                            if a:
                                break
                column -= 1
                distance = abs(self.current_column - column) + abs(self.current_row - row)
            column = self.current_column + 1
            distance = abs(self.current_column - column) + abs(self.current_row - row)
            while distance <= self.dexterity + 1 and not attacked:
                if self.currentRoom.room[row][column] == "W" or self.currentRoom.room[row][column] == "D":
                    break
                if self.currentRoom.room[row][column] != " ":
                    for creature in activeCharacters:
                        if creature.current_row == row and creature.current_column == column and creature != self and \
                                creature.currentRoom is self.currentRoom:
                            print("Throw at " + creature.name + "? (a-attack d-don't attack)")
                            a = False
                            while True:
                                decision = keyboard.read_event(suppress=True)
                                if decision.event_type == keyboard.KEY_UP and decision.name == "a":
                                    target = creature
                                    attacked = True
                                    break
                                elif decision.event_type == keyboard.KEY_UP:
                                    break
                            if a:
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
            if self.currentRoom.room[row][column] == "W" or self.currentRoom.room[row][column] == "D":
                if up:
                    up = False
                    row = self.current_row + 1
                else:
                    break
        if attacked:
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
        else:
            print("No available targets.")
        return attacked

    def ranged_attack(self):
        target = None
        up = True
        row = character.current_row
        column = character.current_column - 1
        attacked = False
        while not attacked:
            distance = abs(self.current_column - column) + abs(self.current_row - row)
            while distance <= self.equippedWeapon.range and not attacked:
                if self.currentRoom.room[row][column] == "W" or self.currentRoom.room[row][column] == "D":
                    break
                if self.currentRoom.room[row][column] != " ":
                    for creature in activeCharacters:
                        if creature.current_row == row and creature.current_column == column and creature != self and \
                                creature.currentRoom is self.currentRoom:
                            print("Attack " + creature.name + "? (a-attack d-don't attack)")
                            a = False
                            while True:
                                decision = keyboard.read_event(suppress=True)
                                if decision.event_type == keyboard.KEY_UP and decision.name == "a":
                                    target = creature
                                    attacked = True
                                    break
                                elif decision.event_type == keyboard.KEY_UP:
                                    break
                            if a:
                                break
                column -= 1
                distance = abs(self.current_column - column) + abs(self.current_row - row)
            column = self.current_column + 1
            distance = abs(self.current_column - column) + abs(self.current_row - row)
            while distance <= self.equippedWeapon.range and not attacked:
                if self.currentRoom.room[row][column] == "W" or self.currentRoom.room[row][column] == "D":
                    break
                if self.currentRoom.room[row][column] != " ":
                    for creature in activeCharacters:
                        if creature.current_row == row and creature.current_column == column and creature != self and \
                                creature.currentRoom is self.currentRoom:
                            print("Attack " + creature.name + "? (a-attack d-don't attack)")
                            a = False
                            while True:
                                decision = keyboard.read_event(suppress=True)
                                if decision.event_type == keyboard.KEY_UP and decision.name == "a":
                                    target = creature
                                    attacked = True
                                    break
                                elif decision.event_type == keyboard.KEY_UP:
                                    break
                            if a:
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
        if attacked:
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
        else:
            print("No available targets.")
        return attacked

    def melee_attack(self):
        attacked = False
        target = None
        if self.currentRoom.room[self.current_row - 1][self.current_column] != ' ':
            for creature in activeCharacters:
                if creature.current_row == self.current_row - 1 and creature.current_column == self.current_column and \
                        creature.currentRoom is self.currentRoom:
                    print("Attack " + creature.name + " above you? (a-attack, d-don't attack)")
                    a = False
                    while True:
                        decision = keyboard.read_event(suppress=True)
                        if decision.event_type == keyboard.KEY_UP and decision.name == "a":
                            target = creature
                            attacked = True
                            break
                        elif decision.event_type == keyboard.KEY_UP:
                            break
                    if a:
                        break
        if self.currentRoom.room[self.current_row][self.current_column + 1] != ' ' and not attacked:
            for creature in activeCharacters:
                if creature.current_row == self.current_row and creature.current_column == self.current_column + 1 and \
                        creature.currentRoom is self.currentRoom:
                    print("Attack " + creature.name + " to your right? (a-attack, d-don't attack)")
                    a = False
                    while True:
                        decision = keyboard.read_event(suppress=True)
                        if decision.event_type == keyboard.KEY_UP and decision.name == "a":
                            target = creature
                            attacked = True
                            break
                        elif decision.event_type == keyboard.KEY_UP:
                            break
                    if a:
                        break
        if self.currentRoom.room[self.current_row + 1][self.current_column] != ' ' and not attacked:
            for creature in activeCharacters:
                if creature.current_row == self.current_row + 1 and creature.current_column == self.current_column and \
                        creature.currentRoom is self.currentRoom:
                    print("Attack " + creature.name + " below you? (a-attack, d-don't attack)")
                    a = False
                    while True:
                        decision = keyboard.read_event(suppress=True)
                        if decision.event_type == keyboard.KEY_UP and decision.name == "a":
                            target = creature
                            attacked = True
                            break
                        elif decision.event_type == keyboard.KEY_UP:
                            break
                    if a:
                        break
        if self.currentRoom.room[self.current_row][self.current_column - 1] != ' ' and not attacked:
            for creature in activeCharacters:
                if creature.current_row == self.current_row and creature.current_column == self.current_column - 1 and \
                        creature.currentRoom is self.currentRoom:
                    print("Attack " + creature.name + " to your left? (a-attack, d-don't attack)")
                    a = False
                    while True:
                        decision = keyboard.read_event(suppress=True)
                        if decision.event_type == keyboard.KEY_UP and decision.name == "a":
                            target = creature
                            attacked = True
                            break
                        elif decision.event_type == keyboard.KEY_UP:
                            break
                    if a:
                        break
        if attacked:
            print("You attack " + target.name + " with your " + self.equippedWeapon.name + ".")
            SupportInfo.attack(self.strength, self.strength, self.equippedWeapon, target)
            if target.currentHP <= 0:
                print(target.name + " is slain!")
                self.xp += target.xp
                self.currentRoom.room[target.current_row][target.current_column] = target.previous
                activeCharacters.remove(target)
            if self.xp >= SupportInfo.characterLevel * 10:
                self.level_up()
        else:
            print("No targets available.")
        return attacked

    def attack(self):
        if self.knives > 0:
            print("Do you want to attack with your weapon or throw a knife? (t-throw, w-weapon)")
            while True:
                decision = keyboard.read_event(suppress=True)
                if decision.event_type == keyboard.KEY_UP:
                    break
        else:
            decision = keyboard._keyboard_event
            decision.event_type = keyboard.KEY_UP
            decision.name = "no knives"
        if decision.event_type == keyboard.KEY_UP and decision.name == "t":
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


def move_right():
    acted = False
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
        if character.currentRoom is creature.currentRoom and character.current_row == creature.current_row and \
                character.current_column == creature.current_column and character != creature:
            character.current_column -= 1
            print(creature.name + " blocks your path.")
            moved = False
    if moved:
        character.currentRoom.room[character.current_row][character.current_column - 1] = character.previous
        character.previous = character.currentRoom.room[character.current_row][character.current_column]
        character.currentRoom.room[character.current_row][character.current_column] = "Y"
        acted = True
    return acted


def move_up():
    acted = False
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
        if character.currentRoom is creature.currentRoom and character.current_row == creature.current_row and \
                character.current_column == creature.current_column and character != creature:
            character.current_row += 1
            print(creature.name + " blocks your path.")
            moved = False
    if moved:
        character.currentRoom.room[character.current_row + 1][character.current_column] = character.previous
        character.previous = character.currentRoom.room[character.current_row][character.current_column]
        character.currentRoom.room[character.current_row][character.current_column] = "Y"
        acted = True
    return acted


def move_down():
    acted = False
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
        if character.currentRoom is creature.currentRoom and character.current_row == creature.current_row and \
                character.current_column == creature.current_column and character != creature:
            character.current_row -= 1
            print(creature.name + " blocks your path.")
            moved = False
    if moved:
        character.currentRoom.room[character.current_row - 1][character.current_column] = character.previous
        character.previous = character.currentRoom.room[character.current_row][character.current_column]
        character.currentRoom.room[character.current_row][character.current_column] = "Y"
        acted = True
    return acted


def move_left():
    acted = False
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
        if character.currentRoom is creature.currentRoom and character.current_row == creature.current_row and \
                character.current_column == creature.current_column and character != creature:
            character.current_column += 1
            print(creature.name + " blocks your path.")
            moved = False
    if moved:
        character.currentRoom.room[character.current_row][character.current_column + 1] = character.previous
        character.previous = character.currentRoom.room[character.current_row][character.current_column]
        character.currentRoom.room[character.current_row][character.current_column] = "Y"
        acted = True
    return acted


def examine():
    print("Where do you want to examine? (arrows for direction, d-your square)")
    while True:
        direction = keyboard.read_event()
        if direction.event_type == keyboard.KEY_UP and direction.name == "up":
            if character.currentRoom.room[character.current_row - 1][character.current_column] == ' ':
                print("There is nothing there.")
            elif character.currentRoom.room[character.current_row - 1][character.current_column] == 'T':
                print("There is a table there. Would you like to examine it? (e-examine, d-don't)")
                while True:
                    answer = keyboard.read_event()
                    if answer.event_type == keyboard.KEY_UP and answer.name == "e":
                        character.currentRoom.room[character.current_row - 1][character.current_column] = 't'
                        table = random.randrange(0, len(SupportInfo.tableOptions), 1)
                        if SupportInfo.tableOptions[table][0] == "knives":
                            print("You find " + str(SupportInfo.tableOptions[table][1]) + " throwing knives.")
                            character.knives += SupportInfo.tableOptions[table][1]
                        break
                    elif answer.event_type == keyboard.KEY_UP:
                        break
            elif character.currentRoom.room[character.current_row - 1][character.current_column] == 't':
                print("You see a table. You've already searched it.")
            elif character.currentRoom.room[character.current_row - 1][character.current_column] == 'C':
                print("There is a chest on the floor. Do you want to open it? (e-open, d-don't)")
                while True:
                    answer = keyboard.read_event()
                    if answer.event_type == keyboard.KEY_UP and answer.name == "e":
                        character.currentRoom.room[character.current_row - 1][character.current_column] = 'c'
                        table = random.randrange(0, len(SupportInfo.chestOptions), 1)
                        if SupportInfo.chestOptions[table] == "Weapon":
                            weapon = SupportInfo.weaponOptions[random.randrange(0, len(SupportInfo.weaponOptions), 1)]
                            if weapon.name == "Shortbow" or weapon.name == "Longbow":
                                print("You find a " + weapon.name + " and 10 arrows. Do you want to equip "
                                      + weapon.name + "? (e-equip, d-don't)")
                                character.arrows += 10
                            else:
                                print("You find a " + weapon.name + ". Do you want to equip it? (e-equip, d-don't)")
                            while True:
                                equip = keyboard.read_event(suppress=True)
                                if equip.event_type == keyboard.KEY_UP and equip.name == "e":
                                    if character.equippedWeapon.name != "Fist":
                                        character.storedWeapons.append(character.equippedWeapon)
                                    character.equippedWeapon = weapon
                                    print(weapon.name + " equipped.")
                                    break
                                elif equip.event_type == keyboard.KEY_UP:
                                    print(weapon.name + " put away.")
                                    character.storedWeapons.append(weapon)
                                    break
                        elif SupportInfo.chestOptions[table] == "Armor":
                            armor = SupportInfo.armorOptions[random.randrange(0, len(SupportInfo.armorOptions), 1)]
                            print("You find a suit of " + armor.name + " armor. "
                                                                       "Do you want to equip it? (e-equip, d-don't)")
                            while True:
                                equip = keyboard.read_event(suppress=True)
                                if equip.event_type == keyboard.KEY_UP and equip.name == "e":
                                    if character.equippedArmor.name != "None":
                                        character.storedArmor.append(character.equippedArmor)
                                    character.equippedArmor = armor
                                    print(armor.name + " armor equipped.")
                                    break
                                elif equip.event_type == keyboard.KEY_UP:
                                    print(armor.name + " put away.")
                                    character.storedArmor.append(armor)
                                    break
                        break
                    elif answer.event_type == keyboard.KEY_UP:
                        break
            elif character.currentRoom.room[character.current_row - 1][character.current_column] == 'c':
                print("You see an open chest on the floor.")
            elif character.currentRoom.room[character.current_row - 1][character.current_column] == 's':
                print("You see what appears to be a small shop. Do you want to check the wares? (c-check, d-don't)")
                while True:
                    answer = keyboard.read_event(suppress=True)
                    if answer.event_type == keyboard.KEY_UP and answer.name == "c":
                        character.currentRoom.shop.shop(character)
                        return "clear"
                    elif answer.event_type == keyboard.KEY_UP:
                        break
            elif character.currentRoom.room[character.current_row - 1][character.current_column] == 'W':
                print("You see the dungeon wall.")
            elif character.currentRoom.room[character.current_row - 1][character.current_column] == 'D':
                print("You see a door.")
            else:
                for creature in activeCharacters:
                    if creature.current_row == character.current_row - 1 and \
                            creature.current_column == character.current_column and \
                            creature.currentRoom == character.currentRoom:
                        print("You see a " + creature.name)
                        break
            break
        elif direction.event_type == keyboard.KEY_UP and direction.name == "down":
            if character.currentRoom.room[character.current_row + 1][character.current_column] == ' ':
                print("There is nothing there.")
            elif character.currentRoom.room[character.current_row + 1][character.current_column] == 'T':
                print("There is a table there. Would you like to examine it? (e-examine, d-don't)")
                while True:
                    answer = keyboard.read_event()
                    if answer.event_type == keyboard.KEY_UP and answer.name == "e":
                        character.currentRoom.room[character.current_row + 1][character.current_column] = 't'
                        table = random.randrange(0, len(SupportInfo.tableOptions), 1)
                        if SupportInfo.tableOptions[table][0] == "knives":
                            print("You find " + str(SupportInfo.tableOptions[table][1]) + " throwing knives.")
                            character.knives += SupportInfo.tableOptions[table][1]
                        break
                    elif answer.event_type == keyboard.KEY_UP:
                        break
            elif character.currentRoom.room[character.current_row + 1][character.current_column] == 't':
                print("You see a table. You've already searched it.")
            elif character.currentRoom.room[character.current_row + 1][character.current_column] == 'C':
                print("There is a chest on the floor. Do you want to open it? (e-open, d-don't)")
                while True:
                    answer = keyboard.read_event()
                    if answer.event_type == keyboard.KEY_UP and answer.name == "e":
                        character.currentRoom.room[character.current_row + 1][character.current_column] = 'c'
                        table = random.randrange(0, len(SupportInfo.chestOptions), 1)
                        if SupportInfo.chestOptions[table] == "Weapon":
                            weapon = SupportInfo.weaponOptions[random.randrange(0, len(SupportInfo.weaponOptions), 1)]
                            if weapon.name == "Shortbow" or weapon.name == "Longbow":
                                print("You find a " + weapon.name + " and 10 arrows. Do you want to equip "
                                      + weapon.name + "? (e-equip, d-don't)")
                                character.arrows += 10
                            else:
                                print("You find a " + weapon.name + ". Do you want to equip it? (e-equip, d-don't)")
                            while True:
                                equip = keyboard.read_event(suppress=True)
                                if equip.event_type == keyboard.KEY_UP and equip.name == "e":
                                    if character.equippedWeapon.name != "Fist":
                                        character.storedWeapons.append(character.equippedWeapon)
                                    character.equippedWeapon = weapon
                                    print(weapon.name + " equipped.")
                                    break
                                elif equip.event_type == keyboard.KEY_UP:
                                    print(weapon.name + " put away.")
                                    character.storedWeapons.append(weapon)
                                    break
                        elif SupportInfo.chestOptions[table] == "Armor":
                            armor = SupportInfo.armorOptions[random.randrange(0, len(SupportInfo.armorOptions), 1)]
                            print("You find a suit of " + armor.name + " armor. "
                                                                       "Do you want to equip it? (e-equip, d-don't)")
                            while True:
                                equip = keyboard.read_event(suppress=True)
                                if equip.event_type == keyboard.KEY_UP and equip.name == "e":
                                    if character.equippedArmor.name != "None":
                                        character.storedArmor.append(character.equippedArmor)
                                    character.equippedArmor = armor
                                    print(armor.name + " armor equipped.")
                                    break
                                elif equip.event_type == keyboard.KEY_UP:
                                    print(armor.name + " put away.")
                                    character.storedArmor.append(armor)
                                    break
                        break
                    elif answer.event_type == keyboard.KEY_UP:
                        break
            elif character.currentRoom.room[character.current_row + 1][character.current_column] == 'c':
                print("You see an open chest on the floor.")
            elif character.currentRoom.room[character.current_row + 1][character.current_column] == 's':
                print("You see what appears to be a small shop. Do you want to check the wares? (c-check, d-don't)")
                while True:
                    answer = keyboard.read_event(suppress=True)
                    if answer.event_type == keyboard.KEY_UP and answer.name == "c":
                        character.currentRoom.shop.shop(character)
                        return "clear"
                    elif answer.event_type == keyboard.KEY_UP:
                        break
            elif character.currentRoom.room[character.current_row + 1][character.current_column] == 'W':
                print("You see the dungeon wall.")
            elif character.currentRoom.room[character.current_row + 1][character.current_column] == 'D':
                print("You see a door.")
            else:
                for creature in activeCharacters:
                    if creature.current_row == character.current_row + 1 and \
                            creature.current_column == character.current_column and \
                            creature.currentRoom == character.currentRoom:
                        print("You see a " + creature.name)
                        break
            break
        elif direction.event_type == keyboard.KEY_UP and direction.name == "right":
            if character.currentRoom.room[character.current_row][character.current_column + 1] == ' ':
                print("There is nothing there.")
            elif character.currentRoom.room[character.current_row][character.current_column + 1] == 'T':
                print("There is a table there. Would you like to examine it? (e-examine, d-don't)")
                while True:
                    answer = keyboard.read_event()
                    if answer.event_type == keyboard.KEY_UP and answer.name == "e":
                        character.currentRoom.room[character.current_row][character.current_column + 1] = 't'
                        table = random.randrange(0, len(SupportInfo.tableOptions), 1)
                        if SupportInfo.tableOptions[table][0] == "knives":
                            print("You find " + str(SupportInfo.tableOptions[table][1]) + " throwing knives.")
                            character.knives += SupportInfo.tableOptions[table][1]
                        break
                    elif answer.event_type == keyboard.KEY_UP:
                        break
            elif character.currentRoom.room[character.current_row][character.current_column + 1] == 't':
                print("You see a table. You've already searched it.")
            elif character.currentRoom.room[character.current_row][character.current_column + 1] == 'C':
                print("There is a chest on the floor. Do you want to open it? (e-open, d-don't)")
                while True:
                    answer = keyboard.read_event()
                    if answer.event_type == keyboard.KEY_UP and answer.name == "e":
                        character.currentRoom.room[character.current_row][character.current_column + 1] = 'c'
                        table = random.randrange(0, len(SupportInfo.chestOptions), 1)
                        if SupportInfo.chestOptions[table] == "Weapon":
                            weapon = SupportInfo.weaponOptions[random.randrange(0, len(SupportInfo.weaponOptions), 1)]
                            if weapon.name == "Shortbow" or weapon.name == "Longbow":
                                print("You find a " + weapon.name + " and 10 arrows. Do you want to equip "
                                      + weapon.name + "? (e-equip, d-don't)")
                                character.arrows += 10
                            else:
                                print("You find a " + weapon.name + ". Do you want to equip it? (e-equip, d-don't)")
                            while True:
                                equip = keyboard.read_event(suppress=True)
                                if equip.event_type == keyboard.KEY_UP and equip.name == "e":
                                    if character.equippedWeapon.name != "Fist":
                                        character.storedWeapons.append(character.equippedWeapon)
                                    character.equippedWeapon = weapon
                                    print(weapon.name + " equipped.")
                                    break
                                elif equip.event_type == keyboard.KEY_UP:
                                    print(weapon.name + " put away.")
                                    character.storedWeapons.append(weapon)
                                    break
                        elif SupportInfo.chestOptions[table] == "Armor":
                            armor = SupportInfo.armorOptions[random.randrange(0, len(SupportInfo.armorOptions), 1)]
                            print("You find a suit of " + armor.name + " armor. "
                                                                       "Do you want to equip it? (e-equip, d-don't)")
                            while True:
                                equip = keyboard.read_event(suppress=True)
                                if equip.event_type == keyboard.KEY_UP and equip.name == "e":
                                    if character.equippedArmor.name != "None":
                                        character.storedArmor.append(character.equippedArmor)
                                    character.equippedArmor = armor
                                    print(armor.name + " armor equipped.")
                                    break
                                elif equip.event_type == keyboard.KEY_UP:
                                    print(armor.name + " put away.")
                                    character.storedArmor.append(armor)
                                    break
                        break
                    elif answer.event_type == keyboard.KEY_UP:
                        break
            elif character.currentRoom.room[character.current_row][character.current_column + 1] == 'c':
                print("You see an open chest on the floor.")
            elif character.currentRoom.room[character.current_row][character.current_column + 1] == 's':
                print("You see what appears to be a small shop. Do you want to check the wares? (c-check, d-don't)")
                while True:
                    answer = keyboard.read_event(suppress=True)
                    if answer.event_type == keyboard.KEY_UP and answer.name == "c":
                        character.currentRoom.shop.shop(character)
                        return "clear"
                    elif answer.event_type == keyboard.KEY_UP:
                        break
            elif character.currentRoom.room[character.current_row][character.current_column + 1] == 'W':
                print("You see the dungeon wall.")
            elif character.currentRoom.room[character.current_row][character.current_column + 1] == 'D':
                print("You see a door.")
            else:
                for creature in activeCharacters:
                    if creature.current_row == character.current_row and \
                            creature.current_column == character.current_column + 1 and \
                            creature.currentRoom == character.currentRoom:
                        print("You see a " + creature.name)
                        break
            break
        elif direction.event_type == keyboard.KEY_UP and direction.name == "left":
            if character.currentRoom.room[character.current_row][character.current_column - 1] == ' ':
                print("There is nothing there.")
            elif character.currentRoom.room[character.current_row][character.current_column - 1] == 'T':
                print("There is a table there. Would you like to examine it? (e-examine, d-don't)")
                while True:
                    answer = keyboard.read_event()
                    if answer.event_type == keyboard.KEY_UP and answer.name == "e":
                        character.currentRoom.room[character.current_row][character.current_column - 1] = 't'
                        table = random.randrange(0, len(SupportInfo.tableOptions), 1)
                        if SupportInfo.tableOptions[table][0] == "knives":
                            print("You find " + str(SupportInfo.tableOptions[table][1]) + " throwing knives.")
                            character.knives += SupportInfo.tableOptions[table][1]
                        break
                    elif answer.event_type == keyboard.KEY_UP:
                        break
            elif character.currentRoom.room[character.current_row][character.current_column - 1] == 't':
                print("You see a table. You've already searched it.")
            elif character.currentRoom.room[character.current_row][character.current_column - 1] == 'C':
                print("There is a chest on the floor. Do you want to open it? (e-examine, d-don't)")
                while True:
                    answer = keyboard.read_event()
                    if answer.event_type == keyboard.KEY_UP and answer.name == "e":
                        character.currentRoom.room[character.current_row][character.current_column - 1] = 'c'
                        table = random.randrange(0, len(SupportInfo.chestOptions), 1)
                        if SupportInfo.chestOptions[table] == "Weapon":
                            weapon = SupportInfo.weaponOptions[random.randrange(0, len(SupportInfo.weaponOptions), 1)]
                            if weapon.name == "Shortbow" or weapon.name == "Longbow":
                                print("You find a " + weapon.name + " and 10 arrows. Do you want to equip "
                                      + weapon.name + "? (e-equip, d-don't)")
                                character.arrows += 10
                            else:
                                print("You find a " + weapon.name + ". Do you want to equip it? (e-equip, d-don't)")
                            while True:
                                equip = keyboard.read_event(suppress=True)
                                if equip.event_type == keyboard.KEY_UP and equip.name == "e":
                                    if character.equippedWeapon.name != "Fist":
                                        character.storedWeapons.append(character.equippedWeapon)
                                    character.equippedWeapon = weapon
                                    print(weapon.name + " equipped.")
                                    break
                                elif equip.event_type == keyboard.KEY_UP:
                                    print(weapon.name + " put away.")
                                    character.storedWeapons.append(weapon)
                                    break
                        elif SupportInfo.chestOptions[table] == "Armor":
                            armor = SupportInfo.armorOptions[random.randrange(0, len(SupportInfo.armorOptions), 1)]
                            print("You find a suit of " + armor.name + " armor. "
                                                                       "Do you want to equip it? (e-equip, d-don't)")
                            while True:
                                equip = keyboard.read_event(suppress=True)
                                if equip.event_type == keyboard.KEY_UP and equip.name == "e":
                                    if character.equippedArmor.name != "None":
                                        character.storedArmor.append(character.equippedArmor)
                                    character.equippedArmor = armor
                                    print(armor.name + " armor equipped.")
                                    break
                                elif equip.event_type == keyboard.KEY_UP:
                                    print(armor.name + " put away.")
                                    character.storedArmor.append(armor)
                                    break
                        break
                    elif answer.event_type == keyboard.KEY_UP:
                        break
            elif character.currentRoom.room[character.current_row][character.current_column - 1] == 'c':
                print("You see an open chest on the floor.")
            elif character.currentRoom.room[character.current_row][character.current_column - 1] == 's':
                print("You see what appears to be a small shop. Do you want to check the wares? (c-check, d-don't)")
                while True:
                    answer = keyboard.read_event(suppress=True)
                    if answer.event_type == keyboard.KEY_UP and answer.name == "c":
                        character.currentRoom.shop.shop(character)
                        return "clear"
                    elif answer.event_type == keyboard.KEY_UP:
                        break
            elif character.currentRoom.room[character.current_row][character.current_column - 1] == 'W':
                print("You see the dungeon wall.")
            elif character.currentRoom.room[character.current_row][character.current_column - 1] == 'D':
                print("You see a door.")
            else:
                for creature in activeCharacters:
                    if creature.current_row == character.current_row and \
                            creature.current_column == character.current_column - 1 and \
                            creature.currentRoom == character.currentRoom:
                        print("You see a " + creature.name)
                        break
            break
        elif direction.event_type == keyboard.KEY_UP:
            if character.previous == ' ':
                print("You are standing on the floor.")
            elif character.previous == 'T':
                print("You are standing by a table. Would you like to examine it? (e-examine, d-don't)")
                while True:
                    answer = keyboard.read_event()
                    if answer.event_type == keyboard.KEY_UP and answer.name == "e":
                        character.previous = 't'
                        table = random.randrange(0, len(SupportInfo.tableOptions), 1)
                        if SupportInfo.tableOptions[table][0] == "knives":
                            print("You find " + str(SupportInfo.tableOptions[table][1]) + " throwing knives.")
                            character.knives += SupportInfo.tableOptions[table][1]
                        break
                    elif answer.event_type == keyboard.KEY_UP:
                        break
            elif character.previous == 't':
                print("You are standing by a table. You've already searched it.")
            elif character.previous == 'C':
                print("You are standing by a chest. Do you want to open it? (e-open, d-don't)")
                while True:
                    answer = keyboard.read_event()
                    if answer.event_type == keyboard.KEY_UP and answer.name == "e":
                        character.previous = 'c'
                        table = random.randrange(0, len(SupportInfo.chestOptions), 1)
                        if SupportInfo.chestOptions[table] == "Weapon":
                            weapon = SupportInfo.weaponOptions[random.randrange(0, len(SupportInfo.weaponOptions), 1)]
                            if weapon.name == "Shortbow" or weapon.name == "Longbow":
                                print("You find a " + weapon.name + " and 10 arrows. Do you want to equip "
                                      + weapon.name + "? (e-equip, d-don't)")
                                character.arrows += 10
                            else:
                                print("You find a " + weapon.name + ". Do you want to equip it? (e-equip, d-don't)")
                            while True:
                                equip = keyboard.read_event(suppress=True)
                                if equip.event_type == keyboard.KEY_UP and equip.name == "e":
                                    if character.equippedWeapon.name != "Fist":
                                        character.storedWeapons.append(character.equippedWeapon)
                                    character.equippedWeapon = weapon
                                    print(weapon.name + " equipped.")
                                    break
                                elif equip.event_type == keyboard.KEY_UP:
                                    print(weapon.name + " put away.")
                                    character.storedWeapons.append(weapon)
                                    break
                        elif SupportInfo.chestOptions[table] == "Armor":
                            armor = SupportInfo.armorOptions[random.randrange(0, len(SupportInfo.armorOptions), 1)]
                            print("You find a suit of " + armor.name + " armor. "
                                                                       "Do you want to equip it? (e-equip, d-don't)")
                            while True:
                                equip = keyboard.read_event(suppress=True)
                                if equip.event_type == keyboard.KEY_UP and equip.name == "e":
                                    if character.equippedArmor.name != "None":
                                        character.storedArmor.append(character.equippedArmor)
                                    character.equippedArmor = armor
                                    print(armor.name + " armor equipped.")
                                    break
                                elif equip.event_type == keyboard.KEY_UP:
                                    print(armor.name + " put away.")
                                    character.storedArmor.append(armor)
                                    break
                        break
                    elif answer.event_type == keyboard.KEY_UP:
                        break
            elif character.previous == 'c':
                print("You are standing by an open chest.")
            elif character.previous == 's':
                print("You see what appears to be a small shop. Do you want to check the wares? (c-check, d-don't)")
                while True:
                    answer = keyboard.read_event(suppress=True)
                    if answer.event_type == keyboard.KEY_UP and answer.name == "c":
                        character.currentRoom.shop.shop(character)
                        return "clear"
                    elif answer.event_type == keyboard.KEY_UP:
                        break
            break
    return ""


def change_weapon():
    if len(character.storedWeapons) > 0:
        print("Equipped Weapon: " + character.equippedWeapon.print_details())
        print()
        print("Stored Weapons:")
        for weapon in character.storedWeapons:
            print(weapon.print_details())
            print()
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


def change_armor():
    if len(character.storedArmor) > 0:
        print("Equipped Armor: " + character.equippedArmor.print_details())
        print()
        print("Stored Armor:")
        for weapon in character.storedArmor:
            print(weapon.print_details())
            print()
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


def clear():
    # Clear the screen for Windows machines
    if os.name == 'nt':
        _ = os.system('cls')
    # Clear the screen for mac and linux
    else:
        _ = os.system('clear')


quitGame = False
character = Fighter()
print("Available actions:")
print("Move (arrow keys): Move a space in the given direction.")
print("Attack (a): See if there is an enemy in range to attack")
print("Examine (e): See if there is anything interesting in your square or a adjacent square.")
print("Wait (w): Pass your action.")
print("Character info (c): See your character's current status.")
print("Change Weapon (s): Switch your equipped weapon with one you have stored.")
print("Change Armor (d): Switch your equipped armor with one you have stored.")
print("Menu (f): See this menu.")
print("Quit (q): quit the game.")
while not quitGame:
    turn = determine_turn(activeCharacters)
    if turn == character:
        for row in character.currentRoom.room:
            print(row)
        acted = False
        while not acted:
            finished = False
            event = keyboard.read_event(suppress=True)
            if event.event_type == keyboard.KEY_UP and event.name == "right":
                acted = move_right()
                finished = True
                if acted:
                    clear()
            elif event.event_type == keyboard.KEY_UP and event.name == "left":
                acted = move_left()
                finished = True
                if acted:
                    clear()
            elif event.event_type == keyboard.KEY_UP and event.name == "up":
                acted = move_up()
                finished = True
                if acted:
                    clear()
            elif event.event_type == keyboard.KEY_UP and event.name == "down":
                acted = move_down()
                finished = True
                if acted:
                    clear()
            elif event.event_type == keyboard.KEY_UP and event.name == "a":
                acted = character.attack()
                finished = True
            elif event.event_type == keyboard.KEY_UP and event.name == "w":
                acted = True
                finished = True
                clear()
            elif event.event_type == keyboard.KEY_UP and event.name == "e":
                clearScreen = examine()
                finished = True
                if clearScreen == "clear":
                    clear()
                    acted = True
            elif event.event_type == keyboard.KEY_UP and event.name == "c":
                character.print_details()
                finished = True
            elif event.event_type == keyboard.KEY_UP and event.name == "s":
                change_weapon()
                finished = True
            elif event.event_type == keyboard.KEY_UP and event.name == "d":
                change_armor()
                finished = True
            elif event.event_type == keyboard.KEY_UP and event.name == "f":
                print("Available actions:")
                print("Move (arrow keys): Move a space in the given direction.")
                print("Attack (a): See if there is an enemy in range to attack")
                print("Examine (e): See if there is anything interesting in your square or a adjacent square.")
                print("Wait (w): Pass your action.")
                print("Character info (c): See your character's current status.")
                print("Change Weapon (s): Switch your equipped weapon with one you have stored.")
                print("Change Armor (d): Switch your equipped armor with one you have stored.")
                print("Menu (f): See this menu.")
                print("Quit (q): quit the game.")
                finished = True
            elif event.event_type == keyboard.KEY_UP and event.name == "q":
                quitGame = True
                acted = True
                finished = True
            elif event.event_type == keyboard.KEY_UP:
                print("Unknown command.")
                finished = True
    else:
        turn.behavior(character)
    if character.currentHP <= 0:
        print("You have died!")
        quitGame = True
        keyboard.wait()
