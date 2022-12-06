import SupportInfo
import random
import traceback


class Space:
    def __init__(self, symbol):
        self.symbol = symbol
        self.current_pass = False  # Current path has been through this square
        self.previous_pass = False  # A previous path routed through this square
        self.blocked = False  # This space cannot be moved through


# Tier 1
class Goblin:
    def __init__(self, room, row, column):
        self.name = "Goblin"
        self.symbol = "g"
        self.currentHP = 5
        self.maxHP = 5
        self.xp = 1
        self.strength = 0
        self.dexterity = 0
        self.equippedWeapon = SupportInfo.Dagger()
        self.equippedArmor = SupportInfo.Armor("None", 0, 0)
        self.equippedShield = False
        self.speed = 0
        self.current_row = row
        self.current_column = column
        self.previous = " "
        self.currentRoom = room

    def behavior(self, player):
        try:
            if self.currentRoom is player.currentRoom:
                near_character = False
                character_row = 0
                character_column = 0
                check_row = self.current_row
                check_column = self.current_column
                left_blocked = 0
                right_blocked = len(self.currentRoom.room[0]) - 1
                up = True
                while not near_character:
                    while check_column > left_blocked and not near_character:
                        if self.currentRoom.room[check_row][check_column] == "Y":
                            near_character = True
                            character_row = check_row
                            character_column = check_column
                        if self.currentRoom.room[check_row][check_column] == "W" or self.currentRoom.room[check_row][check_column] == "D":
                            left_blocked = check_column
                            break
                        check_column -= 1
                    check_column = self.current_column
                    while check_column < right_blocked and not near_character:
                        if self.currentRoom.room[check_row][check_column] == "Y":
                            near_character = True
                            character_row = check_row
                            character_column = check_column
                        if self.currentRoom.room[check_row][check_column] == "W" or self.currentRoom.room[check_row][check_column] == "D":
                            right_blocked = check_column
                            break
                        check_column += 1
                    check_column = self.current_column
                    if (self.currentRoom.room[check_row][check_column] == "W" or self.currentRoom.room[check_row][check_column] == "D") and not near_character:
                        if up:
                            up = False
                            check_row = self.current_row
                            left_blocked = 0
                            right_blocked = len(self.currentRoom.room[0]) - 1
                        else:
                            break
                    if up:
                        check_row -= 1
                    else:
                        check_row += 1
                if near_character:
                    row_distance = character_row - self.current_row
                    column_distance = character_column - self.current_column
                    # If the player is in range, attack them
                    if abs(row_distance) + abs(column_distance) <= self.equippedWeapon.range:
                        print("The " + self.name + " attacks you!")
                        self.equippedWeapon.attack(self.strength, self.strength, player)
                    # If the player is not in range, try to move closer
                    else:
                        current_route = []
                        past_routes = []
                        possible_routes = 0
                        check_column = self.current_column
                        check_row = self.current_row
                        # create a room stand-in to keep track of routes
                        check_room = []
                        row_index = 0
                        while row_index < len(self.currentRoom.room):
                            row = []
                            column_index = 0
                            while column_index < len(self.currentRoom.room[row_index]):
                                row.append(Space(self.currentRoom.room[row_index][column_index]))
                                column_index += 1
                            check_room.append(row)
                            row_index += 1
                        done = False  # All potential routes determined
                        while not done:
                            finished = False  # Current potential route determined
                            direction = ""
                            while not finished:
                                check = check_room[check_row][check_column].symbol
                                if check_room[check_row][check_column].current_pass:
                                    if possible_routes == 0:
                                        done = True
                                        break
                                check_room[check_row][check_column].current_pass = True
                                if check == " " or check == "c" or check == "C" or check == "T" or check == "t" or check == self.symbol:
                                    current_route.append([check_row, check_column])
                                    check_room[check_row][check_column].current_pass = True
                                    if not check_room[check_row - 1][check_column].current_pass and not check_room[check_row - 1][check_column].blocked:
                                        go_up = True
                                    else:
                                        go_up = False
                                    if not check_room[check_row][check_column - 1].current_pass and not check_room[check_row][check_column - 1].blocked:
                                        go_left = True
                                    else:
                                        go_left = False
                                    if not check_room[check_row + 1][check_column].current_pass and not check_room[check_row + 1][check_column].blocked:
                                        go_down = True
                                    else:
                                        go_down = False
                                    if not check_room[check_row][check_column + 1].current_pass and not check_room[check_row][check_column + 1].blocked:
                                        go_right = True
                                    else:
                                        go_right = False
                                    if go_up and not check_room[check_row - 1][check_column].previous_pass:
                                        possible_routes += 1
                                        direction = "up"
                                    if go_right and not check_room[check_row][check_column + 1].previous_pass:
                                        possible_routes += 1
                                        direction = "right"
                                    if go_left and not check_room[check_row][check_column - 1].previous_pass:
                                        possible_routes += 1
                                        direction = "left"
                                    if go_down and not check_room[check_row + 1][check_column].previous_pass:
                                        possible_routes += 1
                                        direction = "down"
                                    if direction == "up":
                                        check_row -= 1
                                        possible_routes -= 1
                                    elif direction == "left":
                                        check_column -= 1
                                        possible_routes -= 1
                                    elif direction == "down":
                                        check_row += 1
                                        possible_routes -= 1
                                    elif direction == "right":
                                        check_column += 1
                                        possible_routes -= 1
                                    else:
                                        if go_up:
                                            check_row -= 1
                                        elif go_left:
                                            check_column -= 1
                                        elif go_down:
                                            check_row += 1
                                        elif go_right:
                                            check_column += 1
                                        else:
                                            if check == self.symbol and possible_routes == 0:
                                                done = True
                                                break
                                            check_room[check_row][check_column].blocked = True
                                            current_route.remove([check_row, check_column])
                                            check_row = current_route[len(current_route) - 1][0]
                                            check_column = current_route[len(current_route) - 1][1]
                                elif check == "Y":
                                    past_routes.append(current_route)
                                    for space in current_route:
                                        check_room[space[0]][space[1]].previous_pass = True
                                    finished = True
                                else:
                                    check_room[check_row][check_column].blocked = True
                                    check_row = current_route[len(current_route) - 1][0]
                                    check_column = current_route[len(current_route) - 1][1]
                        if past_routes:
                            current_route = past_routes[0]
                            for route in past_routes:
                                if len(route) < len(current_route):
                                    current_route = route
                            next_row = current_route[1][0]  # The row number of the next space in the route
                            next_column = current_route[1][1]  # The column number of the next space in the route
                            if next_row > self.current_row:
                                self.current_row += 1
                            elif next_row < self.current_row:
                                self.current_row -= 1
                            elif next_column > self.current_column:
                                self.current_column += 1
                            else:
                                self.current_column -= 1
                            print("The " + self.name + "'s feet slap against the floor as it moves towards you.")
                        else:
                            print("The goblin twirls its dagger as it waits for you to come closer.")
                    '''
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
                    '''
        except:
            f = open("error_report.txt", "a")
            print("An error occurred when a goblin acted.")
            traceback.print_exc(None, f)
            f.close()


# Tier 2
class GoblinScout:
    def __init__(self, room, row, column):
        self.name = "Goblin Scout"
        self.symbol = "g"
        self.currentHP = 10
        self.maxHP = 10
        self.xp = 2
        self.strength = 1
        self.dexterity = 1
        self.equippedWeapon = SupportInfo.Dagger()
        self.equippedArmor = SupportInfo.Leather()
        self.equippedShield = False
        self.speed = 0
        self.current_row = row
        self.current_column = column
        self.previous = " "
        self.currentRoom = room

    def behavior(self, player):
        try:
            near_character = False
            character_row = 0
            character_column = 0
            check_row = self.current_row
            check_column = self.current_column
            left_blocked = 0
            right_blocked = len(self.currentRoom.room[0]) - 1
            up = True
            while not near_character:
                while check_column > left_blocked and not near_character:
                    if self.currentRoom.room[check_row][check_column] == "Y":
                        near_character = True
                        character_row = check_row
                        character_column = check_column
                    if self.currentRoom.room[check_row][check_column] == "W" or self.currentRoom.room[check_row][check_column] == "D":
                        left_blocked = check_column
                        break
                    check_column -= 1
                check_column = self.current_column
                while check_column < right_blocked and not near_character:
                    if self.currentRoom.room[check_row][check_column] == "Y":
                        near_character = True
                        character_row = check_row
                        character_column = check_column
                    if self.currentRoom.room[check_row][check_column] == "W" or self.currentRoom.room[check_row][check_column] == "D":
                        right_blocked = check_column
                        break
                    check_column += 1
                check_column = self.current_column
                if (self.currentRoom.room[check_row][check_column] == "W" or self.currentRoom.room[check_row][check_column] == "D") and not near_character:
                    if up:
                        up = False
                        check_row = self.current_row
                        left_blocked = 0
                        right_blocked = len(self.currentRoom.room[0]) - 1
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
                    self.equippedWeapon.attack(self.strength, self.strength, player)
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
        except:
            f = open("error_report.txt", "a")
            print("An error occurred when a goblin scout acted.")
            traceback.print_exc(None, f)
            f.close()


class GoblinWarrior:
    def __init__(self, room, row, column):
        self.name = "Goblin Warrior"
        self.symbol = "g"
        self.currentHP = 15
        self.maxHP = 15
        self.xp = 2
        self.strength = 2
        self.dexterity = 1
        self.equippedWeapon = SupportInfo.Shortsword()
        self.equippedArmor = SupportInfo.StuddedLeather()
        self.equippedShield = False
        self.speed = 0
        self.current_row = row
        self.current_column = column
        self.previous = " "
        self.currentRoom = room

    def behavior(self, player):
        try:
            near_character = False
            character_row = 0
            character_column = 0
            check_row = self.current_row
            check_column = self.current_column
            left_blocked = 0
            right_blocked = len(self.currentRoom.room[0]) - 1
            up = True
            while not near_character:
                while check_column > left_blocked and not near_character:
                    if self.currentRoom.room[check_row][check_column] == "Y":
                        near_character = True
                        character_row = check_row
                        character_column = check_column
                    if self.currentRoom.room[check_row][check_column] == "W" or self.currentRoom.room[check_row][check_column] == "D":
                        left_blocked = check_column
                        break
                    check_column -= 1
                check_column = self.current_column
                while check_column < right_blocked and not near_character:
                    if self.currentRoom.room[check_row][check_column] == "Y":
                        near_character = True
                        character_row = check_row
                        character_column = check_column
                    if self.currentRoom.room[check_row][check_column] == "W" or self.currentRoom.room[check_row][check_column] == "D":
                        right_blocked = check_column
                        break
                    check_column += 1
                check_column = self.current_column
                if (self.currentRoom.room[check_row][check_column] == "W" or self.currentRoom.room[check_row][check_column] == "D") and not near_character:
                    if up:
                        up = False
                        check_row = self.current_row
                        left_blocked = 0
                        right_blocked = len(self.currentRoom.room[0]) - 1
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
                    self.equippedWeapon.attack(self.strength, self.strength, player)
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
        except:
            f = open("error_report.txt", "a")
            print("An error occurred when a goblin warrior acted.")
            traceback.print_exc(None, f)
            f.close()


class GoblinArcher:
    def __init__(self, room, row, column):
        self.name = "Goblin Archer"
        self.symbol = "g"
        self.currentHP = 10
        self.maxHP = 10
        self.xp = 2
        self.strength = 1
        self.dexterity = 2
        self.equippedWeapon = SupportInfo.Shortbow()
        self.equippedArmor = SupportInfo.Leather()
        self.equippedShield = False
        self.speed = 0
        self.current_row = row
        self.current_column = column
        self.previous = " "
        self.currentRoom = room

    def behavior(self, player):
        try:
            near_character = False
            character_row = 0
            character_column = 0
            check_row = self.current_row
            check_column = self.current_column
            left_blocked = 0
            right_blocked = len(self.currentRoom.room[0]) - 1
            up = True
            while not near_character:
                while check_column > left_blocked and not near_character:
                    if self.currentRoom.room[check_row][check_column] == "Y":
                        near_character = True
                        character_row = check_row
                        character_column = check_column
                    if self.currentRoom.room[check_row][check_column] == "W" or self.currentRoom.room[check_row][check_column] == "D":
                        left_blocked = check_column
                        break
                    check_column -= 1
                check_column = self.current_column
                while check_column < right_blocked and not near_character:
                    if self.currentRoom.room[check_row][check_column] == "Y":
                        near_character = True
                        character_row = check_row
                        character_column = check_column
                    if self.currentRoom.room[check_row][check_column] == "W" or self.currentRoom.room[check_row][check_column] == "D":
                        right_blocked = check_column
                        break
                    check_column += 1
                check_column = self.current_column
                if (self.currentRoom.room[check_row][check_column] == "W" or self.currentRoom.room[check_row][check_column] == "D") and not near_character:
                    if up:
                        up = False
                        check_row = self.current_row
                        left_blocked = 0
                        right_blocked = len(self.currentRoom.room[0]) - 1
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
                    self.equippedWeapon.attack(self.dexterity, self.strength, player)
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
        except:
            f = open("error_report.txt", "a")
            print("An error occurred when a goblin archer acted.")
            traceback.print_exc(None, f)
            f.close()


# Tier 3
class GoblinDefender:
    def __init__(self, room, row, column):
        self.name = "Goblin Defender"
        self.symbol = "g"
        self.currentHP = 30
        self.maxHP = 20
        self.xp = 3
        self.strength = 2
        self.dexterity = 4
        self.equippedWeapon = SupportInfo.Longsword()
        self.equippedArmor = SupportInfo.Breastplate()
        self.equippedShield = SupportInfo.Shield()
        self.speed = 0
        self.current_row = row
        self.current_column = column
        self.previous = " "
        self.currentRoom = room

    def behavior(self, player):
        try:
            near_character = False
            character_row = 0
            character_column = 0
            check_row = self.current_row
            check_column = self.current_column
            left_blocked = 0
            right_blocked = len(self.currentRoom.room[0]) - 1
            up = True
            while not near_character:
                while check_column > left_blocked and not near_character:
                    if self.currentRoom.room[check_row][check_column] == "Y":
                        near_character = True
                        character_row = check_row
                        character_column = check_column
                    if self.currentRoom.room[check_row][check_column] == "W" or self.currentRoom.room[check_row][check_column] == "D":
                        left_blocked = check_column
                        break
                    check_column -= 1
                check_column = self.current_column
                while check_column < right_blocked and not near_character:
                    if self.currentRoom.room[check_row][check_column] == "Y":
                        near_character = True
                        character_row = check_row
                        character_column = check_column
                    if self.currentRoom.room[check_row][check_column] == "W" or self.currentRoom.room[check_row][check_column] == "D":
                        right_blocked = check_column
                        break
                    check_column += 1
                check_column = self.current_column
                if (self.currentRoom.room[check_row][check_column] == "W" or self.currentRoom.room[check_row][check_column] == "D") and not near_character:
                    if up:
                        up = False
                        check_row = self.current_row
                        left_blocked = 0
                        right_blocked = len(self.currentRoom.room[0]) - 1
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
                    self.equippedWeapon.attack(self.strength, self.strength, player)
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
        except:
            f = open("error_report.txt", "a")
            print("An error occurred when a goblin warrior acted.")
            traceback.print_exc(None, f)
            f.close()


class GoblinAssaulter:
    def __init__(self, room, row, column):
        self.name = "Goblin Assaulter"
        self.symbol = "g"
        self.currentHP = 40
        self.maxHP = 40
        self.xp = 3
        self.strength = 4
        self.dexterity = 2
        self.equippedWeapon = SupportInfo.Greatclub()
        self.equippedArmor = SupportInfo.Chainmail()
        self.equippedShield = False
        self.speed = 0
        self.current_row = row
        self.current_column = column
        self.previous = " "
        self.currentRoom = room

    def behavior(self, player):
        try:
            near_character = False
            character_row = 0
            character_column = 0
            check_row = self.current_row
            check_column = self.current_column
            left_blocked = 0
            right_blocked = len(self.currentRoom.room[0]) - 1
            up = True
            while not near_character:
                while check_column > left_blocked and not near_character:
                    if self.currentRoom.room[check_row][check_column] == "Y":
                        near_character = True
                        character_row = check_row
                        character_column = check_column
                    if self.currentRoom.room[check_row][check_column] == "W" or self.currentRoom.room[check_row][check_column] == "D":
                        left_blocked = check_column
                        break
                    check_column -= 1
                check_column = self.current_column
                while check_column < right_blocked and not near_character:
                    if self.currentRoom.room[check_row][check_column] == "Y":
                        near_character = True
                        character_row = check_row
                        character_column = check_column
                    if self.currentRoom.room[check_row][check_column] == "W" or self.currentRoom.room[check_row][check_column] == "D":
                        right_blocked = check_column
                        break
                    check_column += 1
                check_column = self.current_column
                if (self.currentRoom.room[check_row][check_column] == "W" or self.currentRoom.room[check_row][check_column] == "D") and not near_character:
                    if up:
                        up = False
                        check_row = self.current_row
                        left_blocked = 0
                        right_blocked = len(self.currentRoom.room[0]) - 1
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
                    self.equippedWeapon.attack(self.strength, self.strength, player)
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
        except:
            f = open("error_report.txt", "a")
            print("An error occurred when a goblin warrior acted.")
            traceback.print_exc(None, f)
            f.close()


def choose_enemies(room, row, column):
    try:
        if SupportInfo.characterLevel == 1:
            selection = 1
        elif SupportInfo.characterLevel == 2:
            selection = random.randrange(1, 5, 1)
        else:
            selection = random.randrange(1, 7, 1)
        if selection == 1:
            return Goblin(room, row, column)
        elif selection == 2:
            return GoblinScout(room, row, column)
        elif selection == 3:
            return GoblinWarrior(room, row, column)
        elif selection == 4:
            return GoblinArcher(room, row, column)
        elif selection == 5:
            return GoblinAssaulter(room, row, column)
        else:
            return GoblinDefender(room, row, column)
    except:
        f = open("error_report.txt", "a")
        print("An error occurred when generating enemies.")
        traceback.print_exc(None, f)
        f.close()
