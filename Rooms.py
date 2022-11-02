from Enemies import *
from SupportInfo import *


activeCharacters = []
unopenedDoors = 0


class Shop:
    def __init__(self):
        self.knives = 20
        self.arrows = 20
        selection = random.randrange(0, len(weaponOptions), 1)
        self.weapon = weaponOptions[selection]
        selection = random.randrange(0, len(armorOptions), 1)
        self.armor = armorOptions[selection]

    def shop(self, character):
        selection = ""
        while selection.lower() != "leave" and selection.lower() != "nothing":
            if self.knives > 0:
                print(str(self.knives) + " throwing knives: 2 gold each")
            if self.arrows > 0:
                print(str(self.arrows) + " arrows: 5 gold each")
            if self.weapon:
                print(self.weapon.name + ": " + str(self.weapon.gold) + " gold")
            if self.armor:
                print(self.armor.name + ": " + str(self.armor.gold) + " gold")
            print("You have " + str(character.gold) + " gold.")
            selection = input("What would you like to buy? Or would you prefer to sell? ")
            if selection.lower() == "knives" or selection.lower() == "knife":
                number = input("How many knives do you want to buy? max: " + str(self.knives) + " ")
                if number.isdigit():
                    if int(number) > self.knives or int(number) <= 0:
                        print("Invalid number of knives.")
                    else:
                        if character.gold >= 2 * int(number):
                            character.knives += int(number)
                            character.gold -= 2 * int(number)
                            self.knives -= int(number)
                            print("Knives acquired.")
                        else:
                            print("You don't have enough gold.")
                else:
                    print("Invalid input.")
            elif selection.lower() == "arrows" or selection.lower() == "arrow":
                number = input("How many arrows do you want to buy? max: " + str(self.arrows) + " ")
                if number.isdigit():
                    if int(number) > self.knives or int(number) <= 0:
                        print("Invalid number of arrows.")
                    else:
                        if character.gold >= 5 * int(number):
                            character.arrows += int(number)
                            character.gold -= 5 * int(number)
                            self.arrows -= int(number)
                            print("Arrows acquired.")
                        else:
                            print("You don't have enough gold.")
                else:
                    print("Invalid input.")
            elif selection.lower() == self.weapon.name.lower():
                if character.gold >= self.weapon.gold:
                    character.gold -= self.weapon.gold
                    equip = input(self.weapon.name + " acquired. Would you like to equip it?")
                    if equip.lower() == "yes":
                        character.storedWeapons.append(character.equippedWeapon)
                        character.equippedWeapon = self.weapon
                    else:
                        print(self.weapon.name + " put away.")
                        character.storedWeapons.append(self.weapon)
                else:
                    print("You don't have enough gold.")
            elif selection.lower() == self.armor.name.lower():
                if character.gold >= self.armor.gold:
                    character.gold -= self.armor.gold
                    equip = input(self.armor.name + " armor acquired. Do you want to equip it? ")
                    if equip.lower() == "yes":
                        character.storedArmor.append(character.equippedArmor)
                        character.equippedArmor = self.armor
                    else:
                        print(self.armor.name + " put away.")
                        character.storedWeapons.append(self.armor)
                else:
                    print("You don't have enough gold.")
            elif selection.lower() == "sell":
                print("What would you like to sell?")
                print("Equipped weapon: " + character.equippedWeapon.print_details())
                for stored_weapon in character.storedWeapons:
                    print("Stored weapons: " + stored_weapon.print_details())
                if character.equippedArmor.name != "None":
                    print("Equipped armor: " + character.equippedArmor.print_details())
                for stored_armor in character.storedArmor:
                    if stored_armor.name != "None":
                        print("Stored armor: " + stored_armor.print_details())
                selling = input()
                if selling.lower() == character.equippedWeapon.name.lower():
                    print(character.equippedWeapon.name + " sold for " + str(character.equippedWeapon.gold))
                    character.gold += character.equippedWeapon.gold
                    if character.storedWeapons:
                        equipped = False
                        for stored_weapon in character.storedWeapons:
                            choice = input("Would you like to equip " + stored_weapon.name + "? ")
                            if choice.lower() == "yes":
                                character.equippedWeapon = stored_weapon
                                character.storedWeapons.remove(stored_weapon)
                                equipped = True
                                break
                        if not equipped:
                            character.equippedWeapon = Weapon("Fist", 1, 2, 0, 1)
                elif selling.lower() == character.equippedArmor.name.lower():
                    print(character.equippedArmor.name + " sold for " + str(character.equippedArmor.gold))
                    character.gold += character.equippedArmor.gold
                    if character.storedArmors:
                        equipped = False
                        for stored_armor in character.storedArmor:
                            choice = input("Would you like to equip " + stored_armor.name + "? ")
                            if choice.lower() == "yes":
                                character.equippedArmor = stored_armor
                                character.storedArmors.remove(stored_armor)
                                equipped = True
                                break
                        if not equipped:
                            character.equippedArmor = Armor("None", 0, 0)
                else:
                    sold = False
                    for item in character.storedWeapons:
                        if selling.lower() == item.name.lower():
                            print(item.name + " sold for " + str(item.gold))
                            character.gold += item.gold
                            character.storedWeapons.remove(item)
                            sold = True
                    for item in character.storedArmor:
                        if selling.lower() == item.name.lower():
                            print(item.name + " sold for " + str(item.gold))
                            character.gold += item.gold
                            character.storedWeapons.remove(item)
                            sold = True
                    if not sold:
                        print("You don't have that item to sell")
            else:
                if selection.lower() != "leave" or selection.lower() != "nothing":
                    print("Invalid input. If you would like to leave the shop, type 'leave'.")


def down_facing_doors(room, row, column):
    global unopenedDoors
    if unopenedDoors > 1:
        selection = random.randrange(1, 5, 1)
    else:
        selection = random.randrange(2, 5, 1)
    unopenedDoors -= 1
    if selection == 1:
        return SmallRoomBottomDoor(room, row, column)
    elif selection == 2:
        return LeftDoorLongTCorridor(room, "corridor down", row, column)
    elif selection == 3:
        return LeftDoorLongTCorridor(room, "end down", row, column)
    else:
        return VerticalCorridor(room, "down", row, column)


def up_facing_doors(room, row, column):
    global unopenedDoors
    if unopenedDoors > 1:
        selection = random.randrange(1, 6, 1)
    else:
        selection = random.randrange(3, 6, 1)
    unopenedDoors -= 1
    if selection == 1:
        return SmallRoomTopDoor(room, row, column)
    elif selection == 2:
        return MediumRoomTopDoor(room, row, column)
    elif selection == 3:
        return LeftDoorLongTCorridor(room, "corridor up", row, column)
    elif selection == 4:
        return LeftDoorLongTCorridor(room, "end up", row, column)
    else:
        return VerticalCorridor(room, "up", row, column)


def right_facing_doors(room, row, column):
    global unopenedDoors
    if unopenedDoors > 1:
        selection = 1 #random.randrange(1, 4, 1)
    else:
        selection = 3  # random.randrange(3, 5, 1)
    unopenedDoors -= 1
    if selection == 1:
        return MediumRoomRightDoor(room, row, column)
    elif selection == 2:
        return SmallRoomRightDoor(room, row, column)
    else:
        return VerticalCorridor(room, "right", row, column)


def left_facing_doors(room, row, column):
    global unopenedDoors
    if unopenedDoors > 1:
        selection = random.randrange(1, 4, 1)
    else:
        selection = random.randrange(2, 4, 1)
    unopenedDoors -= 1
    if selection == 1:
        return SmallRoomLeftDoor(room, row, column)
    elif selection == 2:
        return VerticalCorridor(room, "left", row, column)
    else:
        return LeftDoorLongTCorridor(room, "left", row, column)


class OpeningRoom:
    def __init__(self, character):
        self.room = [["W", "W", "W", "W", "W", "W", "W"],
                     ["W", " ", " ", " ", " ", " ", "W"],
                     ["W", " ", " ", " ", " ", " ", "W"],
                     ["W", "Y", " ", " ", " ", "g", "D"],
                     ["W", " ", " ", " ", " ", " ", "W"],
                     ["W", " ", " ", " ", " ", " ", "W"],
                     ["W", "W", "W", "W", "W", "W", "W"]]
        self.rightEntrance = 4
        self.rightEntranceConnection = LeftDoorLongTCorridor(self, "left", 3, 5)
        activeCharacters.append(character)
        activeCharacters.append(Goblin(self, 3, 5))

    def leave(self, mover, symbol):
        mover.currentRoom = self.rightEntranceConnection
        self.room[mover.current_row][mover.current_column - 1] = " "
        mover.current_row = 3
        mover.current_column = 1
        mover.currentRoom.room[mover.current_row][mover.current_column] = symbol


class MediumRoomRightDoor:
    def __init__(self, connection, row, column):
        self.room = [["W", "W", "W", "W", "W", "W", "W"],
                     ["W", " ", " ", " ", " ", " ", "W"],
                     ["W", " ", " ", " ", " ", " ", "W"],
                     ["W", " ", " ", " ", " ", " ", "D"],
                     ["W", " ", " ", " ", " ", " ", "W"],
                     ["W", " ", " ", " ", " ", " ", "W"],
                     ["W", "W", "W", "W", "W", "W", "W"]]
        self.door = connection
        self.startRow = 3
        self.startColumn = 5
        self.connectedRow = row
        self.connectedColumn = column
        self.tables = 0 #random.randrange(0, 4, 1)
        self.chests = 0 #random.randrange(0, 4, 1)
        self.enemies = 3 #random.randrange(0, 4, 1)
        if self.tables == 1:
            self.room[3][1] = 'T'
        elif self.tables == 2:
            self.room[5][1] = 'T'
            self.room[1][1] = 'T'
        elif self.tables == 3:
            self.room[3][1] = 'T'
            self.room[5][1] = 'T'
            self.room[1][1] = 'T'
        if self.chests == 1:
            if self.room[3][1] == " ":
                self.room[3][1] = 'C'
            else:
                self.room[2][1] = 'C'
        elif self.chests == 2:
            self.room[2][1] = 'C'
            self.room[4][1] = 'C'
        elif self.chests == 3:
            if self.room[3][1] == " ":
                self.room[3][1] = 'C'
            else:
                self.room[3][2] = 'C'
            self.room[2][1] = 'C'
            self.room[4][1] = 'C'
        if self.enemies == 1:
            if self.room[3][1] == " ":
                self.room[3][1] = "g"
                activeCharacters.append(choose_enemies(self, 3, 1))
            elif self.room[3][2] == " ":
                self.room[3][2] = "g"
                activeCharacters.append(choose_enemies(self, 3, 2))
            else:
                self.room[3][3] = "g"
                activeCharacters.append(choose_enemies(self, 3, 3))
        elif self.enemies == 2:
            if self.room[2][1] == " ":
                self.room[2][1] = 'g'
                self.room[4][1] = 'g'
                activeCharacters.append(choose_enemies(self, 2, 1))
                activeCharacters.append(choose_enemies(self, 4, 1))
            else:
                self.room[2][2] = 'g'
                self.room[4][2] = 'g'
                activeCharacters.append(choose_enemies(self, 2, 2))
                activeCharacters.append(choose_enemies(self, 4, 2))
        elif self.enemies == 3:
            if self.room[3][1] == " ":
                self.room[3][1] = 'g'
                self.room[2][1] = 'g'
                self.room[4][1] = 'g'
                activeCharacters.append(choose_enemies(self, 3, 1))
                activeCharacters.append(choose_enemies(self, 2, 1))
                activeCharacters.append(choose_enemies(self, 4, 1))
            elif self.room[2][1] == " ":
                if self.room[3][2] == " ":
                    self.room[3][2] = 'g'
                    activeCharacters.append(choose_enemies(self, 3, 2))
                else:
                    self.room[3][3] = 'g'
                    activeCharacters.append(choose_enemies(self, 3, 3))
                self.room[2][1] = 'g'
                self.room[4][1] = 'g'
                activeCharacters.append(choose_enemies(self, 2, 1))
                activeCharacters.append(choose_enemies(self, 4, 1))
            elif self.room[3][2] == " ":
                self.room[3][2] = 'g'
                self.room[2][2] = 'g'
                self.room[4][2] = 'g'
                activeCharacters.append(choose_enemies(self, 3, 2))
                activeCharacters.append(choose_enemies(self, 2, 2))
                activeCharacters.append(choose_enemies(self, 4, 2))
            else:
                self.room[3][3] = 'g'
                self.room[2][2] = 'g'
                self.room[4][2] = 'g'
                activeCharacters.append(choose_enemies(self, 3, 3))
                activeCharacters.append(choose_enemies(self, 2, 2))
                activeCharacters.append(choose_enemies(self, 4, 2))

    def leave(self, mover, symbol):
        self.room[mover.current_row][mover.current_column - 1] = " "
        mover.currentRoom = self.door
        mover.current_row = self.connectedRow
        mover.current_column = self.connectedColumn
        mover.currentRoom.room[mover.current_row][mover.current_column] = symbol


class MediumRoomTopDoor:
    def __init__(self, connection, row, column):
        self.room = [["W", "W", "W", "D", "W", "W", "W"],
                     ["W", " ", " ", " ", " ", " ", "W"],
                     ["W", " ", " ", " ", " ", " ", "W"],
                     ["W", " ", " ", " ", " ", " ", "W"],
                     ["W", " ", " ", " ", " ", " ", "W"],
                     ["W", " ", " ", " ", " ", " ", "W"],
                     ["W", "W", "W", "W", "W", "W", "W"]]
        self.door = connection
        self.startRow = 1
        self.startColumn = 3
        self.connectedRow = row
        self.connectedColumn = column
        self.tables = random.randrange(0, 4, 1)
        self.chests = random.randrange(0, 4, 1)
        self.enemies = random.randrange(0, 4, 1)
        if self.tables == 1:
            self.room[5][3] = 'T'
        elif self.tables == 2:
            self.room[5][1] = 'T'
            self.room[5][5] = 'T'
        elif self.tables == 3:
            self.room[5][3] = 'T'
            self.room[5][1] = 'T'
            self.room[5][5] = 'T'
        if self.chests == 1:
            if self.room[5][3] == " ":
                self.room[5][3] = 'C'
            else:
                self.room[5][2] = 'C'
        elif self.chests == 2:
            self.room[5][2] = 'C'
            self.room[5][4] = 'C'
        elif self.chests == 3:
            if self.room[5][3] == " ":
                self.room[5][3] = 'C'
            else:
                self.room[4][3] = 'C'
            self.room[5][2] = 'C'
            self.room[5][4] = 'C'
        if self.enemies == 1:
            if self.room[5][3] == " ":
                self.room[5][3] = "g"
                activeCharacters.append(choose_enemies(self, 5, 3))
            elif self.room[4][3] == " ":
                self.room[4][3] = "g"
                activeCharacters.append(choose_enemies(self, 4, 3))
            else:
                self.room[3][3] = "g"
                activeCharacters.append(choose_enemies(self, 3, 3))
        elif self.enemies == 2:
            if self.room[5][2] == " ":
                self.room[5][2] = 'g'
                self.room[5][4] = 'g'
                activeCharacters.append(choose_enemies(self, 5, 2))
                activeCharacters.append(choose_enemies(self, 5, 4))
            else:
                self.room[4][4] = 'g'
                self.room[4][2] = 'g'
                activeCharacters.append(choose_enemies(self, 4, 4))
                activeCharacters.append(choose_enemies(self, 4, 2))
        elif self.enemies == 3:
            if self.room[5][3] == " ":
                self.room[5][3] = 'g'
                self.room[5][2] = 'g'
                self.room[5][4] = 'g'
                activeCharacters.append(choose_enemies(self, 5, 2))
                activeCharacters.append(choose_enemies(self, 5, 3))
                activeCharacters.append(choose_enemies(self, 5, 4))
            elif self.room[5][2] == " ":
                if self.room[4][3] == " ":
                    self.room[4][3] = 'g'
                    activeCharacters.append(choose_enemies(self, 4, 3))
                else:
                    self.room[3][3] = 'g'
                    activeCharacters.append(choose_enemies(self, 3, 3))
                self.room[5][2] = 'g'
                self.room[5][4] = 'g'
                activeCharacters.append(choose_enemies(self, 5, 2))
                activeCharacters.append(choose_enemies(self, 5, 4))
            elif self.room[4][3] == " ":
                self.room[4][2] = 'g'
                self.room[4][3] = 'g'
                self.room[4][4] = 'g'
                activeCharacters.append(choose_enemies(self, 4, 2))
                activeCharacters.append(choose_enemies(self, 4, 3))
                activeCharacters.append(choose_enemies(self, 4, 4))
            else:
                self.room[3][3] = 'g'
                self.room[4][3] = 'g'
                self.room[4][4] = 'g'
                activeCharacters.append(choose_enemies(self, 3, 3))
                activeCharacters.append(choose_enemies(self, 4, 3))
                activeCharacters.append(choose_enemies(self, 4, 4))

    def leave(self, mover, symbol):
        self.room[mover.current_row][mover.current_column - 1] = " "
        mover.currentRoom = self.door
        mover.current_row = self.connectedRow
        mover.current_column = self.connectedColumn
        mover.currentRoom.room[mover.current_row][mover.current_column] = symbol


class LeftDoorLongTCorridor:
    def __init__(self, connection, direction, row, column):
        self.room = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'D', 'W'],
                     ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' ', 'W'],
                     ['W', 'W', 'D', 'W', 'W', 'W', 'W', 'W', ' ', 'W'],
                     ['D', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'g', 'W'],
                     ['W', 'W', 'W', 'W', 'W', 'D', 'W', 'W', ' ', 'W'],
                     ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' ', 'W'],
                     ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'D', 'W']]
        activeCharacters.append(choose_enemies(self, 3, 8))
        global unopenedDoors
        unopenedDoors += 4
        if direction == "left":
            self.leftEntrance = connection
            self.leftConnection = True
            self.startRow = 3
            self.startColumn = 1
            self.leftRow = row
            self.leftColumn = column
        else:
            self.leftEntrance = None
            self.leftConnection = False
            self.leftRow = 3
            self.leftColumn = 1
        if direction == "corridor up":
            self.corridorUp = connection
            self.corridorUpConnection = True
            self.startRow = 3
            self.startColumn = 2
            self.corridorUpRow = row
            self.corridorUpColumn = column
        else:
            self.corridorUp = None
            self.corridorUpConnection = False
            self.corridorUpRow = 3
            self.corridorUpColumn = 2
        if direction == "end up":
            self.endUp = connection
            self.endUpConnection = True
            self.startRow = 1
            self.startColumn = 8
            self.endUpRow = row
            self.endUpColumn = column
        else:
            self.endUp = None
            self.endUpConnection = False
            self.endUpRow = 1
            self.endUpColumn = 8
        if direction == "corridor down":
            self.corridorDown = connection
            self.corridorDownConnection = True
            self.startRow = 3
            self.startColumn = 5
            self.corridorDownRow = row
            self.corridorDownColumn = column
        else:
            self.corridorDown = None
            self.corridorDownConnection = False
            self.corridorDownRow = 3
            self.corridorDownColumn = 5
        if direction == "end down":
            self.endDown = connection
            self.endDownConnection = True
            self.startRow = 5
            self.startColumn = 8
            self.endDownRow = row
            self.endDownColumn = column
        else:
            self.endDown = None
            self.endDownConnection = False
            self.endDownRow = 5
            self.endDownColumn = 8

    def leave(self, mover, symbol):
        if mover.current_row == 3 and mover.current_column == 0:
            if self.leftConnection:
                self.room[mover.current_row][mover.current_column + 1] = " "
                mover.current_row = self.leftRow
                mover.current_column = self.leftColumn
                mover.currentRoom = self.leftEntrance
                mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
            else:
                self.room[mover.current_row][mover.current_column + 1] = " "
                self.leftEntrance = right_facing_doors(self, 3, 1)
                self.leftConnection = True
                self.leftRow = self.leftEntrance.startRow
                self.leftColumn = self.leftEntrance.startColumn
                mover.current_row = self.leftRow
                mover.current_column = self.leftColumn
                mover.currentRoom = self.leftEntrance
                mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
        elif mover.current_row == 2 and mover.current_column == 2:
            if self.corridorUpConnection:
                self.room[mover.current_row + 1][mover.current_column] = " "
                mover.currentRoom = self.corridorUp
                mover.current_row = self.corridorUpRow
                mover.current_column = self.corridorUpColumn
                mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
            else:
                self.room[mover.current_row + 1][mover.current_column] = " "
                self.corridorUp = down_facing_doors(self, 3, 2)
                self.corridorUpConnection = True
                self.corridorUpRow = self.corridorUp.startRow
                self.corridorUpColumn = self.corridorUp.startColumn
                mover.currentRoom = self.corridorUp
                mover.current_row = self.corridorUpRow
                mover.current_column = self.corridorUpColumn
                mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
        elif mover.current_row == 4 and mover.current_column == 5:
            if self.corridorDownConnection:
                self.room[mover.current_row - 1][mover.current_column] = " "
                mover.currentRoom = self.corridorDown
                mover.current_row = self.corridorDownRow
                mover.current_column = self.corridorDownColumn
                mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
            else:
                self.room[mover.current_row - 1][mover.current_column] = " "
                self.corridorDown = up_facing_doors(self, 3, 5)
                self.corridorDownConnection = True
                self.corridorDownRow = self.corridorDown.startRow
                self.corridorDownColumn = self.corridorDown.startColumn
                mover.currentRoom = self.corridorDown
                mover.current_row = self.corridorDownRow
                mover.current_column = self.corridorDownColumn
                mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
        elif mover.current_row == 0 and mover.current_column == 8:
            if self.endUpConnection:
                self.room[mover.current_row + 1][mover.current_column] = " "
                mover.currentRoom = self.endUp
                mover.current_row = self.endUpRow
                mover.current_column = self.endUpColumn
                mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
            else:
                self.room[mover.current_row + 1][mover.current_column] = " "
                self.endUp = down_facing_doors(self, 1, 8)
                self.endUpConnection = True
                self.endUpRow = self.endUp.startRow
                self.endUpColumn = self.endUp.startColumn
                mover.currentRoom = self.endUp
                mover.current_row = self.endUpRow
                mover.current_column = self.endUpColumn
                mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
        else:
            if self.endDownConnection:
                self.room[mover.current_row - 1][mover.current_column] = " "
                mover.currentRoom = self.endDown
                mover.current_row = self.endDownRow
                mover.current_column = self.endDownColumn
                mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
            else:
                self.room[mover.current_row - 1][mover.current_column] = " "
                self.endDown = up_facing_doors(self, 5, 8)
                self.endDownConnection = True
                self.endDownRow = self.endDown.startRow
                self.endDownColumn = self.endDown.startColumn
                mover.currentRoom = self.endDown
                mover.current_row = self.endDownRow
                mover.current_column = self.endDownColumn
                mover.currentRoom.room[mover.current_row][mover.current_column] = symbol


class SmallRoomBottomDoor:
    def __init__(self, connection, row, column):
        self.room = [['W', 'W', 'W', 'W', 'W'],
                     ['W', ' ', ' ', ' ', 'W'],
                     ['W', ' ', ' ', ' ', 'W'],
                     ['W', 'W', 'D', 'W', 'W']]
        self.door = connection
        self.startRow = 2
        self.startColumn = 2
        self.connectedRow = row
        self.connectedColumn = column
        contents = random.randrange(1, 4, 1)
        if contents == 1:
            self.room[1][2] = 'T'
        elif contents == 2:
            self.room[1][2] = 'C'
        elif contents == 3:
            self.room[1][2] = 's'
            self.shop = Shop()

    def leave(self, mover, symbol):
        self.room[mover.current_row - 1][mover.current_column] = " "
        mover.currentRoom = self.door
        mover.current_row = self.connectedRow
        mover.current_column = self.connectedColumn
        mover.currentRoom.room[mover.current_row][mover.current_column] = symbol


class SmallRoomLeftDoor:
    def __init__(self, connection, row, column):
        self.room = [['W', 'W', 'W', 'W'],
                     ['W', ' ', ' ', 'W'],
                     ['D', ' ', ' ', 'W'],
                     ['W', ' ', ' ', 'W'],
                     ['W', 'W', 'W', 'W']]
        self.door = connection
        self.startRow = 2
        self.startColumn = 1
        self.connectedRow = row
        self.connectedColumn = column
        contents = random.randrange(1, 4, 1)
        if contents == 1:
            self.room[2][2] = 'T'
        elif contents == 2:
            self.room[2][2] = 'C'
        elif contents == 3:
            self.room[2][2] = 's'
            self.shop = Shop()

    def leave(self, mover, symbol):
        self.room[mover.current_row][mover.current_column + 1] = " "
        mover.currentRoom = self.door
        mover.current_row = self.connectedRow
        mover.current_column = self.connectedColumn
        mover.currentRoom.room[mover.current_row][mover.current_column] = symbol


class SmallRoomRightDoor:
    def __init__(self, connection, row, column):
        self.room = [['W', 'W', 'W', 'W'],
                     ['W', ' ', ' ', 'W'],
                     ['W', ' ', ' ', 'D'],
                     ['W', ' ', ' ', 'W'],
                     ['W', 'W', 'W', 'W']]
        self.door = connection
        self.startRow = 2
        self.startColumn = 2
        self.connectedRow = row
        self.connectedColumn = column
        contents = random.randrange(1, 4, 1)
        if contents == 1:
            self.room[2][1] = 'T'
        elif contents == 2:
            self.room[2][1] = 'C'
        elif contents == 3:
            self.room[2][1] = 's'
            self.shop = Shop()

    def leave(self, mover, symbol):
        self.room[mover.current_row][mover.current_column - 1] = " "
        mover.currentRoom = self.door
        mover.current_row = self.connectedRow
        mover.current_column = self.connectedColumn
        mover.currentRoom.room[mover.current_row][mover.current_column] = symbol


class SmallRoomTopDoor:
    def __init__(self, connection, row, column):
        self.room = [['W', 'W', 'D', 'W', 'W'],
                     ['W', ' ', ' ', ' ', 'W'],
                     ['W', ' ', ' ', ' ', 'W'],
                     ['W', 'W', 'W', 'W', 'W']]
        self.door = connection
        self.startRow = 1
        self.startColumn = 2
        self.connectedRow = row
        self.connectedColumn = column
        contents = random.randrange(1, 4, 1)
        if contents == 1:
            self.room[2][2] = 'T'
        elif contents == 2:
            self.room[2][2] = 'C'
        elif contents == 3:
            self.room[2][2] = 's'
            self.shop = Shop()

    def leave(self, mover, symbol):
        self.room[mover.current_row + 1][mover.current_column] = " "
        mover.currentRoom = self.door
        mover.current_row = self.connectedRow
        mover.current_column = self.connectedColumn
        mover.currentRoom.room[mover.current_row][mover.current_column] = symbol


class VerticalCorridor:
    def __init__(self, connection, direction, row, column):
        self.room = [['W', 'D', 'W'],
                     ['W', ' ', 'W'],
                     ['W', ' ', 'W'],
                     ['W', ' ', 'W'],
                     ['D', ' ', 'D'],
                     ['W', ' ', 'W'],
                     ['W', ' ', 'W'],
                     ['W', ' ', 'W'],
                     ['W', 'D', 'W']]
        global unopenedDoors
        unopenedDoors += 3
        self.startColumn = 1
        if direction == "down":
            self.bottomEntrance = True
            self.bottomDoor = connection
            self.bottomRow = row
            self.bottomColumn = column
            self.startRow = 7
        else:
            self.bottomEntrance = False
            self.bottomDoor = None
            self.bottomRow = 7
            self.bottomColumn = 1
        if direction == "left":
            self.leftEntrance = True
            self.leftDoor = connection
            self.leftRow = row
            self.leftColumn = column
            self.startRow = 4
        else:
            self.leftEntrance = False
            self.leftDoor = None
            self.leftRow = 4
            self.leftColumn = 1
        if direction == "up":
            self.upEntrance = True
            self.upDoor = connection
            self.startRow = 1
            self.upRow = row
            self.upColumn = column
        else:
            self.upEntrance = False
            self.upDoor = None
            self.upRow = 1
            self.upColumn = 1
        if direction == "right":
            self.rightEntrance = True
            self.rightDoor = connection
            self.startRow = 4
            self.rightRow = row
            self.rightColumn = column
        else:
            self.rightEntrance = False
            self.rightDoor = None
            self.rightRow = 4
            self.rightColumn = 1

    def leave(self, mover, symbol):
        if mover.current_row == 0 and mover.current_column == 1:
            if self.upEntrance:
                self.room[mover.current_row + 1][mover.current_column] = " "
                mover.currentRoom = self.upDoor
                mover.current_row = self.upRow
                mover.current_column = self.upColumn
                mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
            else:
                self.room[mover.current_row + 1][mover.current_column] = " "
                self.upDoor = down_facing_doors(self, 1, 1)
                self.upEntrance = True
                self.upRow = self.upDoor.startRow
                self.upColumn = self.upDoor.startColumn
                mover.currentRoom = self.upDoor
                mover.current_row = self.upRow
                mover.current_column = self.upColumn
                mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
        elif mover.current_row == 8 and mover.current_column == 1:
            if self.bottomEntrance:
                self.room[mover.current_row - 1][mover.current_column] = " "
                mover.currentRoom = self.bottomDoor
                mover.current_row = self.bottomRow
                mover.current_column = self.bottomColumn
                mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
            else:
                self.room[mover.current_row - 1][mover.current_column] = " "
                self.bottomDoor = up_facing_doors(self, 7, 1)
                self.bottomEntrance = True
                self.bottomRow = self.bottomDoor.startRow
                self.bottomColumn = self.bottomDoor.startColumn
                mover.currentRoom = self.bottomDoor
                mover.current_row = self.bottomRow
                mover.current_column = self.bottomColumn
                mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
        elif mover.current_row == 4 and mover.current_column == 0:
            if self.leftEntrance:
                self.room[mover.current_row][mover.current_column + 1] = " "
                mover.currentRoom = self.leftDoor
                mover.current_row = self.leftRow
                mover.current_column = self.leftColumn
                mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
            else:
                self.room[mover.current_row][mover.current_column + 1] = " "
                self.leftDoor = right_facing_doors(self, 4, 1)
                self.leftEntrance = True
                self.leftRow = self.leftDoor.startRow
                self.leftColumn = self.leftDoor.startColumn
                mover.currentRoom = self.leftDoor
                mover.current_row = self.leftRow
                mover.current_column = self.leftColumn
                mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
        elif mover.current_row == 4 and mover.current_column == 2:
            if self.rightEntrance:
                self.room[mover.current_row][mover.current_column - 1] = " "
                mover.currentRoom = self.rightDoor
                mover.current_row = self.rightRow
                mover.current_column = self.rightColumn
                mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
            else:
                self.room[mover.current_row][mover.current_column - 1] = " "
                self.rightDoor = left_facing_doors(self, 4, 1)
                self.rightEntrance = True
                self.rightRow = self.rightDoor.startRow
                self.rightColumn = self.rightDoor.startColumn
                mover.currentRoom = self.rightDoor
                mover.current_row = self.rightRow
                mover.current_column = self.rightColumn
                mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
