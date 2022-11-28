"""
Handles Character interactions, including character class and the base actions in the game.
Use of the Keyboard library to handle input is a bit clunky. While it functions and allows binding actions to specific
keys instead of requiring the player to type their intent constantly, it requires wrapping every instance of player
input in a While True loop and breaking out when their input is finally read. Attempts to use the KEY_DOWN event instead
of KEY_UP lead to the event triggering constantly instead of only once.
"""
import traceback
from Rooms import OpeningRoom, activeCharacters
import SupportInfo
import random
import keyboard
import os
f = open("error_report.txt", "a")


# Calculate who's turn it is
def determine_turn(creatures):
    try:
        quickest = 0
        # Loop through all created creatures
        for creature in creatures:
            # Calculate how much a creatures carry weight is slowing them down
            slow = creature.equippedWeapon.weight + creature.equippedArmor.weight - creature.strength
            speed = 0
            # Prevent a creature having a higher strength than their weight from increasing their speed.
            if slow > 0:
                speed += 1 + creature.dexterity - slow
            else:
                speed += 1 + creature.dexterity
            # Set lowest speed increase
            if speed > 0.1:
                creature.speed += speed
            else:
                creature.speed += 0.1
            # Set first creature to quickest
            if quickest == 0:
                quickest = creature
            # If new creature has more speed than previous highest, set to creature
            elif quickest.speed < creature.speed:
                quickest = creature
        quickest.speed = 0
        return quickest
    except:
        print("An error occurred with the turn order.")
        traceback.print_exc(None, f)


# Class to deal with the character playing a fighter
class Fighter:
    def __init__(self):
        # Character stats
        self.name = "You"
        self.xp = 0
        self.gold = 0
        self.currentHP = 20
        self.maxHP = 20
        self.strength = 1
        self.dexterity = 1
        self.fortitude = 0
        self.magic = 0
        self.speed = 0
        # Equipable items
        self.equippedWeapon = SupportInfo.Shortsword()
        self.storedWeapons = []
        self.equippedArmor = SupportInfo.Armor("None", 0, 0)
        self.storedArmor = []
        # Throwing knives, used as a special attack
        self.knives = 0
        # Ammunition for ranged weapons
        self.arrows = 0
        # Consumable items
        self.minorPotions = 0
        self.moderatePotions = 0
        self.majorPotions = 0
        # Location information
        self.current_row = 3
        self.current_column = 1
        self.previous = " "
        self.currentRoom = OpeningRoom(self)

    # Print out the status of the character
    def print_details(self):
        print(str(self.currentHP) + "/" + str(self.maxHP) + " HP")
        print("Level: " + str(SupportInfo.characterLevel))
        print("XP: " + str(self.xp))
        print("Gold: " + str(self.gold))
        print("Strength: " + str(self.strength))
        print("Dexterity: " + str(self.dexterity))
        print("Fortitude: " + str(self.fortitude))
        print("Magic: " + str(self.magic))
        print("Weapon: " + self.equippedWeapon.print_details())
        print("Armor: " + self.equippedArmor.print_details())
        print(str(self.knives) + " throwing knives")
        print(str(self.arrows) + " arrows")
        print(str(self.minorPotions) + " minor potions")
        print(str(self.moderatePotions) + " moderate potions")
        print(str(self.majorPotions) + " major potions")

    # Determine how the character will attack and call the appropriate method
    def attack(self):
        try:
            # See if the character has throwing knives, and, if so, see if they wish to throw one for their attack.
            if self.knives > 0:
                print("Do you want to attack with your weapon or throw a knife? (t-throw, w-weapon)")
                while True:
                    decision = keyboard.read_event(suppress=True)
                    if decision.event_type == keyboard.KEY_UP:
                        break
            # Simulate a keyboard_event if there aren't enough knives to throw so that the following statement works
            # properly
            else:
                decision = keyboard._keyboard_event
                decision.event_type = keyboard.KEY_UP
                decision.name = "no knives"
            # Determine which attack method will be used.
            if decision.event_type == keyboard.KEY_UP and decision.name == "t":
                attacked = self.throw_knife()
            elif not self.equippedWeapon.isRanged:
                attacked = self.melee_attack()
            else:
                if (self.equippedWeapon.name == "Shortbow" or self.equippedWeapon.name == "Longbow") and self.arrows > 0:
                    attacked = self.ranged_attack()
                else:
                    print("You are out of arrows.")
                    attacked = False
            return attacked
        except:
            print("An error occurred. Cannot currently attack.")
            traceback.print_exc(None, f)

    # Attack with a throwing knife
    def throw_knife(self):
        try:
            target = None
            # Used to determine if the checker will progress towards the top of the screen or down after a column is
            # checked
            up = True
            row = character.current_row
            column = character.current_column - 1
            attacked = False
            # Check to see if an enemy is within range.
            while not attacked:
                # Set the starting distance from the character for the row. Used to prevent checking beyond the attack's
                # range. Throwing Knives have a range equal to 1 + character's dexterity
                distance = abs(self.current_column - column) + abs(self.current_row - row)
                while distance <= self.dexterity + 1 and not attacked:
                    # Cannot shoot through walls or doors
                    if self.currentRoom.room[row][column] == "W" or self.currentRoom.room[row][column] == "D":
                        break
                    # If the space isn't empty, check to see if there is an enemy there.
                    if self.currentRoom.room[row][column] != " ":
                        for creature in activeCharacters:
                            # If there is a creature in the space, see if the player wants to attack it.
                            if creature.current_row == row and creature.current_column == column and creature != self \
                                    and creature.currentRoom is self.currentRoom:
                                print("Throw at " + creature.name + "? (a-attack d-don't attack)")
                                while True:
                                    decision = keyboard.read_event(suppress=True)
                                    # If player says to attack, set variables for the attack section and exit the
                                    # search for an enemy section
                                    if decision.event_type == keyboard.KEY_UP and decision.name == "a":
                                        target = creature
                                        attacked = True
                                        break
                                    elif decision.event_type == keyboard.KEY_UP:
                                        break
                                # If an enemy is targeted, stop checking for enemies in that square.
                                if attacked:
                                    break
                    # Advance the checker one space to the left and increase the distance for the range checking.
                    column -= 1
                    distance = abs(self.current_column - column) + abs(self.current_row - row)
                # End of looking to the left, reset the column checker to one space to the right of the character's
                # column, since the character's column was checked above. Reset the distance tracker.
                column = self.current_column + 1
                distance = abs(self.current_column - column) + abs(self.current_row - row)
                while distance <= self.dexterity + 1 and not attacked:
                    # Cannot shoot through walls or doors
                    if self.currentRoom.room[row][column] == "W" or self.currentRoom.room[row][column] == "D":
                        break
                    # If the space isn't empty, check to see if there is an enemy there.
                    if self.currentRoom.room[row][column] != " ":
                        for creature in activeCharacters:
                            # If there is a creature in the space, see if the player wants to attack it.
                            if creature.current_row == row and creature.current_column == column and creature != self \
                                    and creature.currentRoom is self.currentRoom:
                                print("Throw at " + creature.name + "? (a-attack d-don't attack)")
                                while True:
                                    decision = keyboard.read_event(suppress=True)
                                    # If player says to attack, set variables for the attack section and exit the
                                    # search for an enemy section
                                    if decision.event_type == keyboard.KEY_UP and decision.name == "a":
                                        target = creature
                                        attacked = True
                                        break
                                    elif decision.event_type == keyboard.KEY_UP:
                                        break
                                # If an enemy is targeted, stop checking for enemies in that square.
                                if attacked:
                                    break
                    # Advance the checker one space to the right and increase the distance for the range checking.
                    column += 1
                    distance = abs(self.current_column - column) + abs(self.current_row - row)
                # Reset the column checker to the character's column
                column = self.current_column
                # Check to see if we are still checking the area above the character or below
                if up:
                    # Check to see if the row has reached the range limit. If not, continue up a row. Otherwise, switch
                    # to checking beneath the character and set the row checker one row below the character
                    if abs(row - self.current_row) < self.dexterity + 1:
                        row -= 1
                    else:
                        up = False
                        row = self.current_row + 1
                else:
                    # Check to see if the row checker has reached the range limit. If not, advance down a row.
                    # Otherwise, break out of the checker loop. There are no enemies to attack
                    if abs(row - self.current_row) < self.dexterity + 1:
                        row += 1
                    else:
                        break
                # If the space directly above the character is a wall or door, switch to checking below the character.
                # If the space directly below the character is a wall or door, break out of the checker loop.
                if self.currentRoom.room[row][column] == "W" or self.currentRoom.room[row][column] == "D":
                    if up:
                        up = False
                        row = self.current_row + 1
                    # This if statement is to prevent the checker from ignoring walls directly beneath the character
                    if self.currentRoom.room[row][column] == "W" or self.currentRoom.room[row][column] == "D":
                        break
            # If the player chose to attack an enemy
            if attacked:
                print("You throw a knife at " + target.name + ".")
                SupportInfo.ThrowingKnife().attack(self.dexterity, self.strength, target)
                # If the target is killed
                if target.currentHP <= 0:
                    print(target.name + " is slain!")
                    self.xp += target.xp
                    self.currentRoom.room[target.current_row][target.current_column] = target.previous
                    # If target's equipped weapon can be equipped by the player, put the weapon in their stored weapons
                    if target.equippedWeapon.equipable:
                        print(target.name + " dropped " + target.equippedWeapon.name + "! It is put in storage.")
                        found = False
                        for weapon in self.storedWeapons:
                            if target.equippedWeapon.name == weapon[0].name:
                                weapon[1] += 1
                                found = True
                        if not found:
                            self.storedWeapons.append([target.equippedWeapon, 1])
                    # If target's equipped armor can be equipped by the player, put the armor in their stored armor
                    if target.equippedArmor.equipable:
                        print(target.name + " dropped " + target.equippedArmor.name + "! It is put in storage.")
                        found = False
                        for armor in self.storedArmor:
                            if target.equippedArmor.name == armor.name:
                                armor.quantity += 1
                                found = True
                        if not found:
                            self.storedArmor.append(target.equippedArmor)
                    activeCharacters.remove(target)
                # Check if the character has enough experience to level up
                if self.xp >= SupportInfo.characterLevel * 10:
                    self.level_up()
                    self.xp = 0
                self.knives -= 1  # Character threw one of their knives.
            else:
                print("No available targets.")
            return attacked  # Used to determine if the player spent their action
        except:
            print("An error occurred. Cannot currently attack.")
            traceback.print_exc(None, f)

    # Attack with a ranged weapon
    def ranged_attack(self):
        try:
            target = None
            # Used to determine if the checker will progress towards the top of the screen or down after a column is
            # checked
            up = True
            row = character.current_row
            column = character.current_column - 1
            attacked = False
            # Check to see if an enemy is within range.
            while not attacked:
                # Set the starting distance from the character for the row. Used to prevent checking beyond the attack's
                # range.
                distance = abs(self.current_column - column) + abs(self.current_row - row)
                while distance <= self.equippedWeapon.range and not attacked:
                    # Cannot shoot through walls or doors
                    if self.currentRoom.room[row][column] == "W" or self.currentRoom.room[row][column] == "D":
                        break
                    # If the space isn't empty, check to see if there is an enemy there.
                    if self.currentRoom.room[row][column] != " ":
                        for creature in activeCharacters:
                            # If there is a creature in the space, see if the player wants to attack it.
                            if creature.current_row == row and creature.current_column == column and creature != self \
                                    and creature.currentRoom is self.currentRoom:
                                print("Attack " + creature.name + "? (a-attack d-don't attack)")
                                while True:
                                    decision = keyboard.read_event(suppress=True)
                                    # If player says to attack, set variables for the attack section and exit the
                                    # search for an enemy section
                                    if decision.event_type == keyboard.KEY_UP and decision.name == "a":
                                        target = creature
                                        attacked = True
                                        break
                                    elif decision.event_type == keyboard.KEY_UP:
                                        break
                                # If an enemy is targeted, stop checking for enemies in that square.
                                if attacked:
                                    break
                    # Advance the checker one space to the left and increase the distance for the range checking.
                    column -= 1
                    distance = abs(self.current_column - column) + abs(self.current_row - row)
                # End of looking to the left, reset the column checker to one space to the right of the character's
                # column, since the character's column was checked above. Reset the distance tracker.
                column = self.current_column + 1
                distance = abs(self.current_column - column) + abs(self.current_row - row)
                while distance <= self.equippedWeapon.range and not attacked:
                    # Cannot shoot through walls or doors
                    if self.currentRoom.room[row][column] == "W" or self.currentRoom.room[row][column] == "D":
                        break
                    # If the space isn't empty, check to see if there is an enemy there.
                    if self.currentRoom.room[row][column] != " ":
                        for creature in activeCharacters:
                            # If there is a creature in the space, see if the player wants to attack it.
                            if creature.current_row == row and creature.current_column == column and creature != self \
                                    and creature.currentRoom is self.currentRoom:
                                print("Attack " + creature.name + "? (a-attack d-don't attack)")
                                while True:
                                    # If player says to attack, set variables for the attack section and exit the
                                    # search for an enemy section
                                    decision = keyboard.read_event(suppress=True)
                                    if decision.event_type == keyboard.KEY_UP and decision.name == "a":
                                        target = creature
                                        attacked = True
                                        break
                                    elif decision.event_type == keyboard.KEY_UP:
                                        break
                                # If an enemy is targeted, stop checking for enemies in that square.
                                if attacked:
                                    break
                    # Advance the checker one space to the right and increase the distance for the range checking.
                    column += 1
                    distance = abs(self.current_column - column) + abs(self.current_row - row)
                # Reset the column checker to the character's column
                column = self.current_column
                # Check to see if we are still checking the area above the character or below
                if up:
                    # Check to see if the row has reached the range limit. If not, continue up a row. Otherwise, switch
                    # to checking beneath the character and set the row checker one row below the character
                    if abs(row - self.current_row) <= self.equippedWeapon.range:
                        row -= 1
                    else:
                        up = False
                        row = self.current_row + 1
                else:
                    # Check to see if the row checker has reached the range limit. If not, advance down a row.
                    # Otherwise, break out of the checker loop. There are no enemies to attack
                    if abs(row - self.current_row) <= self.equippedWeapon.range:
                        row += 1
                    else:
                        break
                # If the space directly above the character is a wall or door, switch to checking below the character.
                # If the space directly below the character is a wall or door, break out of the checker loop.
                if self.currentRoom.room[row][column] == "W" or self.currentRoom.room[row][column] == "D":
                    if up:
                        up = False
                        row = self.current_row + 1
                    # This if statement is to prevent the checker from ignoring walls directly beneath the character
                    if self.currentRoom.room[row][column] == "W" or self.currentRoom.room[row][column] == "D":
                        break
            # If the player chose to attack an enemy
            if attacked:
                print("You attack " + target.name + " with your " + self.equippedWeapon.name + ".")
                # If attack with a weapon that shoot arrows, decrease the number of arrows
                if self.equippedWeapon.name == "Shortbow" or self.equippedWeapon.name == "Longbow":
                    self.arrows -= 1
                    print("You have " + str(self.arrows) + " arrows remaining.")
                self.equippedWeapon.attack(self.dexterity, self.strength, target)
                # If the target is killed
                if target.currentHP <= 0:
                    print(target.name + " is slain!")
                    self.xp += target.xp
                    self.currentRoom.room[target.current_row][target.current_column] = target.previous
                    # If target's equipped weapon can be equipped by the player, put the weapon in their stored weapons
                    if target.equippedWeapon.equipable:
                        print(target.name + " dropped " + target.equippedWeapon.name + "! It is put in storage.")
                        found = False
                        for weapon in self.storedWeapons:
                            if target.equippedWeapon.name == weapon[0].name:
                                weapon[1] += 1
                                found = True
                        if not found:
                            self.storedWeapons.append([target.equippedWeapon, 1])
                    # If target's equipped armor can be equipped by the player, put the armor in their stored armor
                    if target.equippedArmor.equipable:
                        print(target.name + " dropped " + target.equippedArmor.name + "! It is put in storage.")
                        found = False
                        for armor in self.storedArmor:
                            if target.equippedArmor.name == armor.name:
                                armor.quantity += 1
                                found = True
                        if not found:
                            self.storedArmor.append(target.equippedArmor)
                    activeCharacters.remove(target)
                # Check if the character has enough experience to level up
                if self.xp >= SupportInfo.characterLevel * 10:
                    self.level_up()
                    self.xp = 0
            else:
                print("No available targets.")
            return attacked  # Used to determine if the player spent their action
        except:
            print("An error occurred. Cannot currently attack.")
            traceback.print_exc(None, f)

    # Attack with a melee weapon
    def melee_attack(self):
        try:
            target = None
            # Used to determine if the checker will progress towards the top of the screen or down after a column is
            # checked
            up = True
            row = character.current_row
            column = character.current_column - 1
            attacked = False
            # Check to see if an enemy is within range.
            while not attacked:
                # Set the starting distance from the character for the row. Used to prevent checking beyond the attack's
                # range.
                distance = abs(self.current_column - column) + abs(self.current_row - row)
                while distance <= self.equippedWeapon.range and not attacked:
                    # Cannot shoot through walls or doors
                    if self.currentRoom.room[row][column] == "W" or self.currentRoom.room[row][column] == "D":
                        break
                    # If the space isn't empty, check to see if there is an enemy there.
                    if self.currentRoom.room[row][column] != " ":
                        for creature in activeCharacters:
                            # If there is a creature in the space, see if the player wants to attack it.
                            if creature.current_row == row and creature.current_column == column and creature != self \
                                    and creature.currentRoom is self.currentRoom:
                                print("Attack " + creature.name + "? (a-attack d-don't attack)")
                                while True:
                                    decision = keyboard.read_event(suppress=True)
                                    # If player says to attack, set variables for the attack section and exit the
                                    # search for an enemy section
                                    if decision.event_type == keyboard.KEY_UP and decision.name == "a":
                                        target = creature
                                        attacked = True
                                        break
                                    elif decision.event_type == keyboard.KEY_UP:
                                        break
                                # If an enemy is targeted, stop checking for enemies in that square.
                                if attacked:
                                    break
                    # Advance the checker one space to the left and increase the distance for the range checking.
                    column -= 1
                    distance = abs(self.current_column - column) + abs(self.current_row - row)
                # End of looking to the left, reset the column checker to one space to the right of the character's
                # column, since the character's column was checked above. Reset the distance tracker.
                column = self.current_column + 1
                distance = abs(self.current_column - column) + abs(self.current_row - row)
                while distance <= self.equippedWeapon.range and not attacked:
                    # Cannot shoot through walls or doors
                    if self.currentRoom.room[row][column] == "W" or self.currentRoom.room[row][column] == "D":
                        break
                    # If the space isn't empty, check to see if there is an enemy there.
                    if self.currentRoom.room[row][column] != " ":
                        for creature in activeCharacters:
                            # If there is a creature in the space, see if the player wants to attack it.
                            if creature.current_row == row and creature.current_column == column and creature != self \
                                    and creature.currentRoom is self.currentRoom:
                                print("Attack " + creature.name + "? (a-attack d-don't attack)")
                                while True:
                                    decision = keyboard.read_event(suppress=True)
                                    # If player says to attack, set variables for the attack section and exit the
                                    # search for an enemy section
                                    if decision.event_type == keyboard.KEY_UP and decision.name == "a":
                                        target = creature
                                        attacked = True
                                        break
                                    elif decision.event_type == keyboard.KEY_UP:
                                        break
                                # If an enemy is targeted, stop checking for enemies in that square.
                                if attacked:
                                    break
                    # Advance the checker one space to the right and increase the distance for the range checking.
                    column += 1
                    distance = abs(self.current_column - column) + abs(self.current_row - row)
                # Reset the column checker to the character's column
                column = self.current_column
                # Check to see if we are still checking the area above the character or below
                if up:
                    # Check to see if the row has reached the range limit. If not, continue up a row. Otherwise, switch
                    # to checking beneath the character and set the row checker one row below the character
                    if abs(row - self.current_row) <= self.equippedWeapon.range:
                        row -= 1
                    else:
                        up = False
                        row = self.current_row + 1
                else:
                    # Check to see if the row checker has reached the range limit. If not, advance down a row.
                    # Otherwise, break out of the checker loop. There are no enemies to attack
                    if abs(row - self.current_row) <= self.equippedWeapon.range:
                        row += 1
                    else:
                        break
                # If the space directly above the character is a wall or door, switch to checking below the character.
                # If the space directly below the character is a wall or door, break out of the checker loop.
                if self.currentRoom.room[row][column] == "W" or self.currentRoom.room[row][column] == "D":
                    if up:
                        up = False
                        row = self.current_row + 1
                    # This if statement is to prevent the checker from ignoring walls directly beneath the character
                    if self.currentRoom.room[row][column] == "W" or self.currentRoom.room[row][column] == "D":
                        break
            # If the player chose to attack an enemy
            if attacked:
                print("You attack " + target.name + " with your " + self.equippedWeapon.name + ".")
                self.equippedWeapon.attack(self.strength, self.strength, target)
                # If the target is killed
                if target.currentHP <= 0:
                    print(target.name + " is slain!")
                    self.xp += target.xp
                    self.currentRoom.room[target.current_row][target.current_column] = target.previous
                    # If target's equipped weapon can be equipped by the player, put the weapon in their stored weapons
                    if target.equippedWeapon.equipable:
                        print(target.name + " dropped " + target.equippedWeapon.name + "! It is put in storage.")
                        found = False
                        for weapon in self.storedWeapons:
                            if target.equippedWeapon.name == weapon[0].name:
                                weapon[1] += 1
                                found = True
                        if not found:
                            self.storedWeapons.append([target.equippedWeapon, 1])
                    # If target's equipped armor can be equipped by the player, put the armor in their stored armor
                    if target.equippedArmor.equipable:
                        print(target.name + " dropped " + target.equippedArmor.name + "! It is put in storage.")
                        found = False
                        for armor in self.storedArmor:
                            if target.equippedArmor.name == armor.name:
                                armor.quantity += 1
                                found = True
                        if not found:
                            self.storedArmor.append(target.equippedArmor)
                    activeCharacters.remove(target)
                # Check if the character has enough experience to level up
                if self.xp >= SupportInfo.characterLevel * 10:
                    self.level_up()
                    self.xp = 0
                attacked = True
            else:
                print("No available targets.")
            return attacked  # Used to determine if the player spent their action
        except:
            print("An error occurred. Cannot currently attack.")
            traceback.print_exc(None, f)

    # Level up the character
    def level_up(self):
        try:
            print("Level up!")
            SupportInfo.characterLevel += 1  # This is stored in SupportInfo so it can be used in other files
            self.maxHP += 5 + self.fortitude
            self.currentHP = self.maxHP
            print("Current Strength: " + str(self.strength))
            print("Current Dexterity: " + str(self.dexterity))
            print("Current Magic: " + str(self.magic))
            print("Choose a stat to increase by one: s-strength, d-dexterity, a-magic")
            while True:
                choice = keyboard.read_event(suppress=True)
                if choice.event_type == keyboard.KEY_UP and choice.name == "s":
                    self.strength += 1
                    break
                elif choice.event_type == keyboard.KEY_UP and choice.name == "d":
                    self.dexterity += 1
                    break
                elif choice.event_type == keyboard.KEY_UP and choice.name == "a":
                    self.magic += 1
                    break
                elif choice.event_type == keyboard.KEY_UP:
                    print("Not a valid option.")
        except:
            print("An error occurred.")
            traceback.print_exc(None, f)

    # Use a consumable item
    def use_item(self):
        try:
            if self.minorPotions > 0 and self.moderatePotions > 0 and self.majorPotions > 0:
                print("You have " + str(self.minorPotions) + " minor potions(a), " + str(self.moderatePotions) +
                      " moderate potions(s), and " + str(self.majorPotions) +
                      " major potions(d). Which would you like to use? (f-none)")
                while True:
                    item = keyboard.read_event()
                    if item.event_type == keyboard.KEY_UP and item.name == "a":
                        self.minorPotions -= 1
                        heal = random.randrange(1, 11, 1) + self.magic
                        self.currentHP += heal
                        if self.currentHP > self.maxHP:
                            self.currentHP = self.maxHP
                            print("Healed to max hp.")
                        else:
                            print("Healed " + str(heal) + " hp.")
                        break
                    elif item.event_type == keyboard.KEY_UP and item.name == "s":
                        self.moderatePotions -= 1
                        heal = random.randrange(5, 16, 1) + self.magic
                        self.currentHP += heal
                        if self.currentHP > self.maxHP:
                            self.currentHP = self.maxHP
                            print("Healed to max hp.")
                        else:
                            print("Healed " + str(heal) + " hp.")
                        break
                    elif item.event_type == keyboard.KEY_UP and item.name == "d":
                        self.majorPotions -= 1
                        heal = random.randrange(10, 21, 1) + self.magic
                        self.currentHP += heal
                        if self.currentHP > self.maxHP:
                            self.currentHP = self.maxHP
                            print("Healed to max hp.")
                        else:
                            print("Healed " + str(heal) + " hp.")
                        break
                    elif item.event_type == keyboard.KEY_UP:
                        print("No item used.")
                        break
            elif self.minorPotions > 0 and self.moderatePotions > 0:
                print("You have " + str(self.minorPotions) + " minor potions(a), " + str(self.moderatePotions) +
                      " moderate potions(s). Which would you like to use? (f-none)")
                while True:
                    item = keyboard.read_event()
                    if item.event_type == keyboard.KEY_UP and item.name == "a":
                        self.minorPotions -= 1
                        heal = random.randrange(1, 11, 1) + self.magic
                        self.currentHP += heal
                        if self.currentHP > self.maxHP:
                            self.currentHP = self.maxHP
                            print("Healed to max hp.")
                        else:
                            print("Healed " + str(heal) + " hp.")
                        break
                    elif item.event_type == keyboard.KEY_UP and item.name == "s":
                        self.moderatePotions -= 1
                        heal = random.randrange(5, 16, 1) + self.magic
                        self.currentHP += heal
                        if self.currentHP > self.maxHP:
                            self.currentHP = self.maxHP
                            print("Healed to max hp.")
                        else:
                            print("Healed " + str(heal) + " hp.")
                        break
                    elif item.event_type == keyboard.KEY_UP:
                        print("No item used.")
                        break
            elif self.minorPotions > 0 and self.majorPotions > 0:
                print("You have " + str(self.minorPotions) + " minor potions(a) and " + str(self.majorPotions) +
                      " major potions(d). Which would you like to use? (f-none)")
                while True:
                    item = keyboard.read_event()
                    if item.event_type == keyboard.KEY_UP and item.name == "a":
                        self.minorPotions -= 1
                        heal = random.randrange(1, 11, 1) + self.magic
                        self.currentHP += heal
                        if self.currentHP > self.maxHP:
                            self.currentHP = self.maxHP
                            print("Healed to max hp.")
                        else:
                            print("Healed " + str(heal) + " hp.")
                        break
                    elif item.event_type == keyboard.KEY_UP and item.name == "d":
                        self.majorPotions -= 1
                        heal = random.randrange(10, 21, 1) + self.magic
                        self.currentHP += heal
                        if self.currentHP > self.maxHP:
                            self.currentHP = self.maxHP
                            print("Healed to max hp.")
                        else:
                            print("Healed " + str(heal) + " hp.")
                        break
                    elif item.event_type == keyboard.KEY_UP:
                        print("No item used.")
                        break
            elif self.moderatePotions > 0 and self.majorPotions > 0:
                print("You have " + str(self.moderatePotions) + " moderate potions(s), and " + str(self.majorPotions) +
                      " major potions(d). Which would you like to use? (f-none)")
                while True:
                    item = keyboard.read_event()
                    if item.event_type == keyboard.KEY_UP and item.name == "s":
                        self.moderatePotions -= 1
                        heal = random.randrange(5, 16, 1) + self.magic
                        self.currentHP += heal
                        if self.currentHP > self.maxHP:
                            self.currentHP = self.maxHP
                            print("Healed to max hp.")
                        else:
                            print("Healed " + str(heal) + " hp.")
                        break
                    elif item.event_type == keyboard.KEY_UP and item.name == "d":
                        self.majorPotions -= 1
                        heal = random.randrange(10, 21, 1) + self.magic
                        self.currentHP += heal
                        if self.currentHP > self.maxHP:
                            self.currentHP = self.maxHP
                            print("Healed to max hp.")
                        else:
                            print("Healed " + str(heal) + " hp.")
                        break
                    elif item.event_type == keyboard.KEY_UP:
                        print("No item used.")
                        break
            elif self.minorPotions > 0:
                print("You have " + str(self.minorPotions) + " minor potions(a). Would you like to use one? (f-no)")
                while True:
                    item = keyboard.read_event()
                    if item.event_type == keyboard.KEY_UP and item.name == "a":
                        self.minorPotions -= 1
                        heal = random.randrange(1, 11, 1) + self.magic
                        self.currentHP += heal
                        if self.currentHP > self.maxHP:
                            self.currentHP = self.maxHP
                            print("Healed to max hp.")
                        else:
                            print("Healed " + str(heal) + " hp.")
                        break
                    elif item.event_type == keyboard.KEY_UP:
                        print("No item used.")
                        break
            elif self.moderatePotions > 0:
                print("You have " + str(self.moderatePotions) +
                      " moderate potions(s). Would you like to use one? (f-no)")
                while True:
                    item = keyboard.read_event()
                    if item.event_type == keyboard.KEY_UP and item.name == "s":
                        self.moderatePotions -= 1
                        heal = random.randrange(5, 16, 1) + self.magic
                        self.currentHP += heal
                        if self.currentHP > self.maxHP:
                            self.currentHP = self.maxHP
                            print("Healed to max hp.")
                        else:
                            print("Healed " + str(heal) + " hp.")
                        break
                    elif item.event_type == keyboard.KEY_UP:
                        print("No item used.")
                        break
            elif self.majorPotions > 0:
                print("You have " + str(self.majorPotions) + " major potions(d). Would you like to use one? (f-no)")
                while True:
                    item = keyboard.read_event()
                    if item.event_type == keyboard.KEY_UP and item.name == "d":
                        self.majorPotions -= 1
                        heal = random.randrange(10, 21, 1) + self.magic
                        self.currentHP += heal
                        if self.currentHP > self.maxHP:
                            self.currentHP = self.maxHP
                            print("Healed to max hp.")
                        else:
                            print("Healed " + str(heal) + " hp.")
                        break
                    elif item.event_type == keyboard.KEY_UP:
                        print("No item used.")
                        break
            else:
                print("You have no items to use.")
        except:
            print("An error occurred.")
            traceback.print_exc(None, f)


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


# When the player wants to move to the right of the screen
def move_right():
    try:
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
        # If there is nothing preventing the character from moving, actually move
        if moved:
            character.currentRoom.room[character.current_row][character.current_column - 1] = character.previous
            character.previous = character.currentRoom.room[character.current_row][character.current_column]
            character.currentRoom.room[character.current_row][character.current_column] = "Y"
            acted = True
        return acted
    except:
        print("An error occurred. Cannot currently move right.")
        traceback.print_exc(None, f)


# When the player wants to move up on the screen
def move_up():
    try:
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
        # If there is nothing preventing the character from moving, actually move
        if moved:
            character.currentRoom.room[character.current_row + 1][character.current_column] = character.previous
            character.previous = character.currentRoom.room[character.current_row][character.current_column]
            character.currentRoom.room[character.current_row][character.current_column] = "Y"
            acted = True
        return acted
    except:
        print("An error occurred. Cannot currently move up.")
        traceback.print_exc(None, f)


# When the player wants to move down on the screen
def move_down():
    try:
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
        # If there is nothing preventing the character from moving, actually move
        if moved:
            character.currentRoom.room[character.current_row - 1][character.current_column] = character.previous
            character.previous = character.currentRoom.room[character.current_row][character.current_column]
            character.currentRoom.room[character.current_row][character.current_column] = "Y"
            acted = True
        return acted
    except:
        print("An error occurred. Cannot currently move down.")
        traceback.print_exc(None, f)


# When the player wants to move to the left of the screen
def move_left():
    try:
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
        # If there is nothing preventing the character from moving, actually move
        if moved:
            character.currentRoom.room[character.current_row][character.current_column + 1] = character.previous
            character.previous = character.currentRoom.room[character.current_row][character.current_column]
            character.currentRoom.room[character.current_row][character.current_column] = "Y"
            acted = True
        return acted
    except:
        print("An error occurred. Cannot currently move left.")
        traceback.print_exc(None, f)


# When the character wants to examine the contents of a square
def examine():
    try:
        print("Where do you want to examine? (arrows for direction, d-your square)")
        while True:
            direction = keyboard.read_event()
            # The character is examining the space above them
            if direction.event_type == keyboard.KEY_UP and direction.name == "up":
                # The space is empty
                if character.currentRoom.room[character.current_row - 1][character.current_column] == ' ':
                    print("There is nothing there.")
                # The space has an unexamined table
                elif character.currentRoom.room[character.current_row - 1][character.current_column] == 'T':
                    print("There is a table there. Would you like to examine it? (e-examine, d-don't)")
                    while True:
                        answer = keyboard.read_event()
                        if answer.event_type == keyboard.KEY_UP and answer.name == "e":
                            # Lower case t represents an examined table. Contents are randomly chosen from a list.
                            character.currentRoom.room[character.current_row - 1][character.current_column] = 't'
                            table = random.randrange(0, len(SupportInfo.tableOptions), 1)
                            if SupportInfo.tableOptions[table][0] == "knives":
                                print("You find " + str(SupportInfo.tableOptions[table][1]) + " throwing knives.")
                                character.knives += SupportInfo.tableOptions[table][1]
                            elif SupportInfo.tableOptions[table][0] == "minor potion":
                                print("You find " + str(SupportInfo.tableOptions[table][1]) +
                                      " minor potions of healing.")
                                character.minorPotions += SupportInfo.tableOptions[table][1]
                            elif SupportInfo.tableOptions[table][0] == "moderate potion":
                                print("You find " + str(SupportInfo.tableOptions[table][1]) +
                                      " moderate potions of healing.")
                                character.moderatePotions += SupportInfo.tableOptions[table][1]
                            elif SupportInfo.tableOptions[table][0] == "major potion":
                                print("You find " + str(SupportInfo.tableOptions[table][1]) +
                                      " major potions of healing.")
                                character.majorPotions += SupportInfo.tableOptions[table][1]
                            break
                        elif answer.event_type == keyboard.KEY_UP:
                            break
                # The space has a previously examined table
                elif character.currentRoom.room[character.current_row - 1][character.current_column] == 't':
                    print("You see a table. You've already searched it.")
                # The space has an unopened treasure chest
                elif character.currentRoom.room[character.current_row - 1][character.current_column] == 'C':
                    print("There is a chest on the floor. Do you want to open it? (e-open, d-don't)")
                    while True:
                        answer = keyboard.read_event()
                        if answer.event_type == keyboard.KEY_UP and answer.name == "e":
                            # Lower case c represent opened treasure chests.
                            character.currentRoom.room[character.current_row - 1][character.current_column] = 'c'
                            # Contents of chest are randomly chosen from a list in SupportInfo
                            table = random.randrange(0, len(SupportInfo.chestOptions), 1)
                            # The chest contains a weapon
                            if SupportInfo.chestOptions[table] == "Weapon":
                                # The weapon is randomly chosen from a list in SupportInfo
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
                                        # The character has an actual weapon equipped, instead of the placeholder.
                                        if character.equippedWeapon.name != "Fist":
                                            found = False
                                            for stored_weapon in character.storedWeapons:
                                                if stored_weapon[0].name == character.equippedWeapon.name:
                                                    stored_weapon[1] += 1
                                                    found = True
                                            if not found:
                                                character.storedWeapons.append([character.equippedWeapon, 1])
                                        character.equippedWeapon = weapon
                                        print(weapon.name + " equipped.")
                                        break
                                    elif equip.event_type == keyboard.KEY_UP:
                                        print(weapon.name + " put away.")
                                        found = False
                                        for stored_weapon in character.storedWeapons:
                                            if stored_weapon[0].name == weapon.name:
                                                stored_weapon[1] += 1
                                                found = True
                                                break
                                        if not found:
                                            character.storedWeapons.append([weapon, 1])
                                        break
                            # The chest contains a set of armor
                            elif SupportInfo.chestOptions[table] == "Armor":
                                # The armor is randomly chosen from a list in SupportInfo
                                armor = SupportInfo.armorOptions[random.randrange(0, len(SupportInfo.armorOptions), 1)]
                                print("You find a suit of " + armor.name + " armor. Do you want to equip it? (e-equip, d-don't)")
                                while True:
                                    equip = keyboard.read_event(suppress=True)
                                    if equip.event_type == keyboard.KEY_UP and equip.name == "e":
                                        if character.equippedArmor.name != "None":
                                            found = False
                                            for stored_armor in character.storedArmor:
                                                if stored_armor.name == armor.name:
                                                    stored_armor.quantity += 1
                                                    found = True
                                            if not found:
                                                character.storedArmor.append(character.equippedArmor)
                                        character.equippedArmor = armor
                                        print(armor.name + " armor equipped.")
                                        break
                                    elif equip.event_type == keyboard.KEY_UP:
                                        print(armor.name + " put away.")
                                        found = False
                                        for stored_armor in character.storedArmor:
                                            if stored_armor.name == armor.name:
                                                stored_armor.quantity += 1
                                                found = True
                                        if not found:
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
                            elif SupportInfo.tableOptions[table][0] == "minor potion":
                                print("You find " + str(SupportInfo.tableOptions[table][1]) +
                                      " minor potions of healing.")
                                character.minorPotions += SupportInfo.tableOptions[table][1]
                            elif SupportInfo.tableOptions[table][0] == "moderate potion":
                                print("You find " + str(SupportInfo.tableOptions[table][1]) +
                                      " moderate potions of healing.")
                                character.moderatePotions += SupportInfo.tableOptions[table][1]
                            elif SupportInfo.tableOptions[table][0] == "major potion":
                                print("You find " + str(SupportInfo.tableOptions[table][1]) +
                                      " major potions of healing.")
                                character.majorPotions += SupportInfo.tableOptions[table][1]
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
                                            found = False
                                            for stored_weapon in character.storedWeapons:
                                                if stored_weapon[0].name == character.equippedWeapon.name:
                                                    stored_weapon[1] += 1
                                                    found = True
                                            if not found:
                                                character.storedWeapons.append([character.equippedWeapon, 1])
                                        character.equippedWeapon = weapon
                                        print(weapon.name + " equipped.")
                                        break
                                    elif equip.event_type == keyboard.KEY_UP:
                                        print(weapon.name + " put away.")
                                        found = False
                                        for stored_weapon in character.storedWeapons:
                                            if stored_weapon[0].name == weapon.name:
                                                stored_weapon[1] += 1
                                                found = True
                                                break
                                        if not found:
                                            character.storedWeapons.append([weapon, 1])
                                        break
                            elif SupportInfo.chestOptions[table] == "Armor":
                                # The armor is randomly chosen from a list in SupportInfo
                                armor = SupportInfo.armorOptions[random.randrange(0, len(SupportInfo.armorOptions), 1)]
                                print("You find a suit of " + armor.name + " armor. Do you want to equip it? (e-equip, d-don't)")
                                while True:
                                    equip = keyboard.read_event(suppress=True)
                                    if equip.event_type == keyboard.KEY_UP and equip.name == "e":
                                        if character.equippedArmor.name != "None":
                                            found = False
                                            for stored_armor in character.storedArmor:
                                                if stored_armor.name == armor.name:
                                                    stored_armor.quantity += 1
                                                    found = True
                                            if not found:
                                                character.storedArmor.append(character.equippedArmor)
                                        character.equippedArmor = armor
                                        print(armor.name + " armor equipped.")
                                        break
                                    elif equip.event_type == keyboard.KEY_UP:
                                        print(armor.name + " put away.")
                                        found = False
                                        for stored_armor in character.storedArmor:
                                            if stored_armor.name == armor.name:
                                                stored_armor.quantity += 1
                                                found = True
                                        if not found:
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
                            elif SupportInfo.tableOptions[table][0] == "minor potion":
                                print("You find " + str(SupportInfo.tableOptions[table][1]) +
                                      " minor potions of healing.")
                                character.minorPotions += SupportInfo.tableOptions[table][1]
                            elif SupportInfo.tableOptions[table][0] == "moderate potion":
                                print("You find " + str(SupportInfo.tableOptions[table][1]) +
                                      " moderate potions of healing.")
                                character.moderatePotions += SupportInfo.tableOptions[table][1]
                            elif SupportInfo.tableOptions[table][0] == "major potion":
                                print("You find " + str(SupportInfo.tableOptions[table][1]) +
                                      " major potions of healing.")
                                character.majorPotions += SupportInfo.tableOptions[table][1]
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
                                            found = False
                                            for stored_weapon in character.storedWeapons:
                                                if stored_weapon[0].name == character.equippedWeapon.name:
                                                    stored_weapon[1] += 1
                                                    found = True
                                            if not found:
                                                character.storedWeapons.append([character.equippedWeapon, 1])
                                        character.equippedWeapon = weapon
                                        print(weapon.name + " equipped.")
                                        break
                                    elif equip.event_type == keyboard.KEY_UP:
                                        print(weapon.name + " put away.")
                                        found = False
                                        for stored_weapon in character.storedWeapons:
                                            if stored_weapon[0].name == weapon.name:
                                                stored_weapon[1] += 1
                                                found = True
                                                break
                                        if not found:
                                            character.storedWeapons.append([weapon, 1])
                                        break
                            elif SupportInfo.chestOptions[table] == "Armor":
                                # The armor is randomly chosen from a list in SupportInfo
                                armor = SupportInfo.armorOptions[random.randrange(0, len(SupportInfo.armorOptions), 1)]
                                print("You find a suit of " + armor.name + " armor. Do you want to equip it? (e-equip, d-don't)")
                                while True:
                                    equip = keyboard.read_event(suppress=True)
                                    if equip.event_type == keyboard.KEY_UP and equip.name == "e":
                                        if character.equippedArmor.name != "None":
                                            found = False
                                            for stored_armor in character.storedArmor:
                                                if stored_armor.name == armor.name:
                                                    stored_armor.quantity += 1
                                                    found = True
                                            if not found:
                                                character.storedArmor.append(character.equippedArmor)
                                        character.equippedArmor = armor
                                        print(armor.name + " armor equipped.")
                                        break
                                    elif equip.event_type == keyboard.KEY_UP:
                                        print(armor.name + " put away.")
                                        found = False
                                        for stored_armor in character.storedArmor:
                                            if stored_armor.name == armor.name:
                                                stored_armor.quantity += 1
                                                found = True
                                        if not found:
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
                            elif SupportInfo.tableOptions[table][0] == "minor potion":
                                print("You find " + str(SupportInfo.tableOptions[table][1]) +
                                      " minor potions of healing.")
                                character.minorPotions += SupportInfo.tableOptions[table][1]
                            elif SupportInfo.tableOptions[table][0] == "moderate potion":
                                print("You find " + str(SupportInfo.tableOptions[table][1]) +
                                      " moderate potions of healing.")
                                character.moderatePotions += SupportInfo.tableOptions[table][1]
                            elif SupportInfo.tableOptions[table][0] == "major potion":
                                print("You find " + str(SupportInfo.tableOptions[table][1]) +
                                      " major potions of healing.")
                                character.majorPotions += SupportInfo.tableOptions[table][1]
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
                                            found = False
                                            for stored_weapon in character.storedWeapons:
                                                if stored_weapon[0].name == character.equippedWeapon.name:
                                                    stored_weapon[1] += 1
                                                    found = True
                                            if not found:
                                                character.storedWeapons.append([character.equippedWeapon, 1])
                                        character.equippedWeapon = weapon
                                        print(weapon.name + " equipped.")
                                        break
                                    elif equip.event_type == keyboard.KEY_UP:
                                        print(weapon.name + " put away.")
                                        found = False
                                        for stored_weapon in character.storedWeapons:
                                            if stored_weapon[0].name == weapon.name:
                                                stored_weapon[1] += 1
                                                found = True
                                                break
                                        if not found:
                                            character.storedWeapons.append([weapon, 1])
                                        break
                            elif SupportInfo.chestOptions[table] == "Armor":
                                # The armor is randomly chosen from a list in SupportInfo
                                armor = SupportInfo.armorOptions[random.randrange(0, len(SupportInfo.armorOptions), 1)]
                                print("You find a suit of " + armor.name + " armor. Do you want to equip it? (e-equip, d-don't)")
                                while True:
                                    equip = keyboard.read_event(suppress=True)
                                    if equip.event_type == keyboard.KEY_UP and equip.name == "e":
                                        if character.equippedArmor.name != "None":
                                            found = False
                                            for stored_armor in character.storedArmor:
                                                if stored_armor.name == armor.name:
                                                    stored_armor.quantity += 1
                                                    found = True
                                            if not found:
                                                character.storedArmor.append(character.equippedArmor)
                                        character.equippedArmor = armor
                                        print(armor.name + " armor equipped.")
                                        break
                                    elif equip.event_type == keyboard.KEY_UP:
                                        print(armor.name + " put away.")
                                        found = False
                                        for stored_armor in character.storedArmor:
                                            if stored_armor.name == armor.name:
                                                stored_armor.quantity += 1
                                                found = True
                                        if not found:
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
                            elif SupportInfo.tableOptions[table][0] == "minor potion":
                                print("You find " + str(SupportInfo.tableOptions[table][1]) +
                                      " minor potions of healing.")
                                character.minorPotions += SupportInfo.tableOptions[table][1]
                            elif SupportInfo.tableOptions[table][0] == "moderate potion":
                                print("You find " + str(SupportInfo.tableOptions[table][1]) +
                                      " moderate potions of healing.")
                                character.moderatePotions += SupportInfo.tableOptions[table][1]
                            elif SupportInfo.tableOptions[table][0] == "major potion":
                                print("You find " + str(SupportInfo.tableOptions[table][1]) +
                                      " major potions of healing.")
                                character.majorPotions += SupportInfo.tableOptions[table][1]
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
                                            found = False
                                            for stored_weapon in character.storedWeapons:
                                                if stored_weapon[0].name == character.equippedWeapon.name:
                                                    stored_weapon[1] += 1
                                                    found = True
                                            if not found:
                                                character.storedWeapons.append([character.equippedWeapon, 1])
                                        character.equippedWeapon = weapon
                                        print(weapon.name + " equipped.")
                                        break
                                    elif equip.event_type == keyboard.KEY_UP:
                                        print(weapon.name + " put away.")
                                        found = False
                                        for stored_weapon in character.storedWeapons:
                                            if stored_weapon[0].name == weapon.name:
                                                stored_weapon[1] += 1
                                                found = True
                                                break
                                        if not found:
                                            character.storedWeapons.append([weapon, 1])
                                        break
                            elif SupportInfo.chestOptions[table] == "Armor":
                                # The armor is randomly chosen from a list in SupportInfo
                                armor = SupportInfo.armorOptions[random.randrange(0, len(SupportInfo.armorOptions), 1)]
                                print("You find a suit of " + armor.name + " armor. Do you want to equip it? (e-equip, d-don't)")
                                while True:
                                    equip = keyboard.read_event(suppress=True)
                                    if equip.event_type == keyboard.KEY_UP and equip.name == "e":
                                        if character.equippedArmor.name != "None":
                                            found = False
                                            for stored_armor in character.storedArmor:
                                                if stored_armor.name == armor.name:
                                                    stored_armor.quantity += 1
                                                    found = True
                                            if not found:
                                                character.storedArmor.append(character.equippedArmor)
                                        character.equippedArmor = armor
                                        print(armor.name + " armor equipped.")
                                        break
                                    elif equip.event_type == keyboard.KEY_UP:
                                        print(armor.name + " put away.")
                                        found = False
                                        for stored_armor in character.storedArmor:
                                            if stored_armor.name == armor.name:
                                                stored_armor.quantity += 1
                                                found = True
                                        if not found:
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
    except:
        print("An error occurred. Cannot currently examine that area.")
        traceback.print_exc(None, f)


def change_weapon():
    try:
        if len(character.storedWeapons) > 0:
            print("Equipped Weapon: " + character.equippedWeapon.print_details())
            print()
            print("Stored Weapons:")
            for weapon in character.storedWeapons:
                print(weapon[0].print_details())
                print()
            desired = input("Which weapon do you want to equip? ")
            equipped = False
            for weapon in character.storedWeapons:
                if weapon[0].name == desired:
                    equipped = True
                    if character.equippedWeapon.name != "Fist":
                        found = False
                        for stow in character.storedWeapons:
                            if stow[0].name == character.equippedWeapon.name:
                                stow[1] += 1
                                found = True
                        if not found:
                            character.storedWeapons.append([character.equippedWeapon, 1])
                    character.equippedWeapon = weapon[0]
                    print(weapon[0].name + " equipped.")
                    if weapon[1] == 1:
                        character.storedWeapons.remove(weapon)
                    else:
                        weapon[1] -= 1
            if not equipped:
                print("You don't have that weapon.")
        else:
            print("You don't have any stored weapons to equip.")
    except:
        print("An error occurred. Cannot currently change weapons.")
        traceback.print_exc(None, f)


def change_armor():
    try:
        if len(character.storedArmor) > 0:
            print("Equipped Armor: " + character.equippedArmor.print_details())
            print()
            print("Stored Armor:")
            for armor in character.storedArmor:
                print(str(armor.quantity) + " " + armor.print_details())
                print()
            desired = input("Which armor do you want to equip? ")
            found = False
            for armor in character.storedArmor:
                if armor.name == desired:
                    if character.equippedArmor.name != "None":
                        stored = False
                        for stored_armor in character.storedArmor:
                            if stored_armor.name == character.equippedArmor.name:
                                stored_armor.quantity += 1
                                stored = True
                        if not stored:
                            character.storedArmor.append(character.equippedArmor)
                    character.equippedArmor = armor
                    armor.quantity -= 1
                    if armor.quantity == 0:
                        character.storedArmor.remove(armor)
                    print(armor.name + " equipped.")
                    found = True
            if not found:
                print("You don't have that armor.")
        else:
            print("You don't have any stored armor to equip.")
    except Exception as ArmorArgument:
        print("An error occurred. Cannot currently change armor.")
        traceback.print_exc(None, f)


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
print("Use item (z): Use a consumable item")
print("Menu (f): See this menu.")
print("Quit (q): Quit the game.")
try:
    while not quitGame:
        turn = determine_turn(activeCharacters)
        if turn == character:
            print("HP: " + str(character.currentHP) + "/" + str(character.maxHP))
            for row in character.currentRoom.room:
                print(row)
            acted = False
            while not acted:
                event = keyboard.read_event(suppress=True)
                if event.event_type == keyboard.KEY_UP and event.name == "right":
                    acted = move_right()
                    if acted:
                        clear()
                elif event.event_type == keyboard.KEY_UP and event.name == "left":
                    acted = move_left()
                    if acted:
                        clear()
                elif event.event_type == keyboard.KEY_UP and event.name == "up":
                    acted = move_up()
                    if acted:
                        clear()
                elif event.event_type == keyboard.KEY_UP and event.name == "down":
                    acted = move_down()
                    if acted:
                        clear()
                elif event.event_type == keyboard.KEY_UP and event.name == "a":
                    acted = character.attack()
                elif event.event_type == keyboard.KEY_UP and event.name == "w":
                    acted = True
                    clear()
                elif event.event_type == keyboard.KEY_UP and event.name == "e":
                    clearScreen = examine()
                    if clearScreen == "clear":
                        clear()
                        acted = True
                elif event.event_type == keyboard.KEY_UP and event.name == "c":
                    character.print_details()
                elif event.event_type == keyboard.KEY_UP and event.name == "s":
                    change_weapon()
                elif event.event_type == keyboard.KEY_UP and event.name == "d":
                    change_armor()
                elif event.event_type == keyboard.KEY_UP and event.name == "f":
                    print("Available actions:")
                    print("Move (arrow keys): Move a space in the given direction.")
                    print("Attack (a): See if there is an enemy in range to attack")
                    print("Examine (e): See if there is anything interesting in your square or a adjacent square.")
                    print("Wait (w): Pass your action.")
                    print("Character info (c): See your character's current status.")
                    print("Change Weapon (s): Switch your equipped weapon with one you have stored.")
                    print("Change Armor (d): Switch your equipped armor with one you have stored.")
                    print("Use item (z): Use a consumable item")
                    print("Menu (f): See this menu.")
                    print("Quit (q): quit the game.")
                elif event.event_type == keyboard.KEY_UP and event.name == "q":
                    quitGame = True
                    acted = True
                elif event.event_type == keyboard.KEY_UP and event.name == "z":
                    character.use_item()
                elif event.event_type == keyboard.KEY_UP:
                    print("Unknown command.")
        else:
            turn.behavior(character)
        if character.currentHP <= 0:
            print("You have died!")
            quitGame = True
            keyboard.wait()
except:
    traceback.print_exc(None, f)
f.close()
