import keyboard
from Enemies import *
import SupportInfo


activeCharacters = []
unopenedDoors = 0


class Shop:
    def __init__(self):
        self.knives = 20
        self.arrows = 20
        self.minorPotions = random.randrange(0, 6, 1)
        self.moderatePotions = random.randrange(0, 4, 1)
        self.majorPotions = random.randrange(0, 2, 1)
        selection = random.randrange(0, len(SupportInfo.weaponOptions), 1)
        self.weapon = SupportInfo.weaponOptions[selection]
        selection = random.randrange(0, len(SupportInfo.armorOptions), 1)
        self.armor = SupportInfo.armorOptions[selection]

    def shop(self, character):
        try:
            done = False
            while not done:
                if self.arrows > 0:
                    print(str(self.arrows) + " arrows: 5 gold each (a)")
                if self.knives > 0:
                    print(str(self.knives) + " throwing knives: 2 gold each (s)")
                if self.minorPotions > 0:
                    print(str(self.minorPotions) + " minor potions: 5 gold each (z)")
                if self.moderatePotions > 0:
                    print(str(self.moderatePotions) + " moderate potions: 10 gold each (x)")
                if self.majorPotions > 0:
                    print(str(self.majorPotions) + " major potions: 15 gold each (c)")
                if self.weapon:
                    print(self.weapon.name + ": " + str(self.weapon.gold) + " gold (d)")
                if self.armor:
                    print(self.armor.name + ": " + str(self.armor.gold) + " gold (f)")
                print("You have " + str(character.gold) + " gold.")
                print("What would you like to buy? Or would you prefer to sell (g)? (leave-q)")
                while True:
                    event = keyboard.read_event(suppress=True)
                    if event.event_type == keyboard.KEY_UP and event.name == "a":
                        if self.arrows <= 0:
                            print("There are no arrows for sale.")
                        elif self.arrows > 1:
                            sold = False
                            quantity = 0
                            while not sold:
                                SupportInfo.clear()
                                print("How many arrows do you want to buy? f-confirm " + str(quantity))
                                while True:
                                    event = keyboard.read_event(suppress=True)
                                    if event.event_type == keyboard.KEY_UP and event.name == "up":
                                        if self.arrows > quantity:
                                            quantity += 1
                                        break
                                    elif event.event_type == keyboard.KEY_UP and event.name == "down":
                                        if quantity >= 0:
                                            quantity -= 1
                                        break
                                    elif event.event_type == keyboard.KEY_UP and event.name == "f":
                                        if character.gold >= 5 * quantity:
                                            character.arrows += quantity
                                            character.gold -= 5 * quantity
                                            self.arrows -= quantity
                                            print("Arrows acquired.")
                                            sold = True
                                            break
                                        else:
                                            print("You don't have enough gold.")
                                            break
                        else:
                            SupportInfo.clear()
                            if character.gold >= 5:
                                character.gold -= 5
                                character.arrows += 1
                                self.arrows -= 1
                                print("Arrow acquired.")
                            else:
                                print("You don't have enough gold.")
                        break
                    elif event.event_type == keyboard.KEY_UP and event.name == "s":
                        if self.knives <= 0:
                            print("There are no throwing knives for sale.")
                        elif self.knives > 1:
                            sold = False
                            quantity = 0
                            while not sold:
                                SupportInfo.clear()
                                print("How many knives do you want to buy? f-confirm " + str(quantity))
                                while True:
                                    event = keyboard.read_event(suppress=True)
                                    if event.event_type == keyboard.KEY_UP and event.name == "up":
                                        if self.knives > quantity:
                                            quantity += 1
                                        break
                                    elif event.event_type == keyboard.KEY_UP and event.name == "down":
                                        if quantity >= 0:
                                            quantity -= 1
                                        break
                                    elif event.event_type == keyboard.KEY_UP and event.name == "f":
                                        if character.gold >= 2 * quantity:
                                            character.knives += quantity
                                            character.gold -= 2 * quantity
                                            self.knives -= quantity
                                            print("Knives acquired.")
                                            sold = True
                                            break
                                        else:
                                            print("You don't have enough gold.")
                                            break
                        else:
                            SupportInfo.clear()
                            if character.gold >= 2:
                                character.knives += 1
                                character.gold -= 2
                                self.knives -= 1
                                print("Knife acquired.")
                            else:
                                print("You don't have enough gold.")
                        break
                    elif event.event_type == keyboard.KEY_UP and event.name == "z":
                        if self.minorPotions <= 0:
                            print("There are no minor potions for sale.")
                        elif self.minorPotions > 1:
                            sold = False
                            quantity = 0
                            while not sold:
                                SupportInfo.clear()
                                print("How many minor potions do you want to buy? f-confirm " + str(quantity))
                                while True:
                                    event = keyboard.read_event(suppress=True)
                                    if event.event_type == keyboard.KEY_UP and event.name == "up":
                                        if self.minorPotions > quantity:
                                            quantity += 1
                                        break
                                    elif event.event_type == keyboard.KEY_UP and event.name == "down":
                                        if quantity >= 0:
                                            quantity -= 1
                                        break
                                    elif event.event_type == keyboard.KEY_UP and event.name == "f":
                                        if character.gold >= 5 * quantity:
                                            character.gold -= 5 * quantity
                                            character.minorPotions += quantity
                                            self.minorPotions -= quantity
                                            print("Minor potions acquired.")
                                            sold = True
                                            break
                                        else:
                                            print("You don't have enough gold.")
                                            break
                        else:
                            SupportInfo.clear()
                            if character.gold >= 5:
                                character.gold -= 5
                                character.minorPotions += 1
                                self.minorPotions -= 1
                                print("Minor potion acquired.")
                            else:
                                print("You don't have enough gold.")
                        break
                    elif event.event_type == keyboard.KEY_UP and event.name == "x":
                        if self.moderatePotions <= 0:
                            print("There are no moderate potions for sale.")
                        elif self.moderatePotions > 1:
                            sold = False
                            quantity = 0
                            while not sold:
                                SupportInfo.clear()
                                print("How many moderate potions do you want to buy? f-confirm " + str(quantity))
                                while True:
                                    event = keyboard.read_event(suppress=True)
                                    if event.event_type == keyboard.KEY_UP and event.name == "up":
                                        if self.moderatePotions > quantity:
                                            quantity += 1
                                        break
                                    elif event.event_type == keyboard.KEY_UP and event.name == "down":
                                        if quantity >= 0:
                                            quantity -= 1
                                        break
                                    elif event.event_type == keyboard.KEY_UP and event.name == "f":
                                        if character.gold >= 10 * quantity:
                                            character.gold -= 10 * quantity
                                            character.moderatePotions += quantity
                                            self.moderatePotions -= quantity
                                            print("Moderate potions acquired.")
                                            sold = True
                                            break
                                        else:
                                            print("You don't have enough gold.")
                                            break
                        else:
                            SupportInfo.clear()
                            if character.gold >= 10:
                                character.gold -= 10
                                character.moderatePotions += 1
                                self.moderatePotions -= 1
                                print("Moderate potion acquired.")
                            else:
                                print("You don't have enough gold.")
                        break
                    elif event.event_type == keyboard.KEY_UP and event.name == "c":
                        if self.majorPotions <= 0:
                            print("There are no major potions for sale.")
                        elif self.majorPotions > 1:
                            sold = False
                            quantity = 0
                            while not sold:
                                SupportInfo.clear()
                                print("How many major potions do you want to buy? f-confirm " + str(quantity))
                                while True:
                                    event = keyboard.read_event(suppress=True)
                                    if event.event_type == keyboard.KEY_UP and event.name == "up":
                                        if self.majorPotions > quantity:
                                            quantity += 1
                                        break
                                    elif event.event_type == keyboard.KEY_UP and event.name == "down":
                                        if quantity >= 0:
                                            quantity -= 1
                                        break
                                    elif event.event_type == keyboard.KEY_UP and event.name == "f":
                                        if character.gold >= 15 * quantity:
                                            character.gold -= 15 * quantity
                                            character.majorPotions += quantity
                                            self.majorPotions -= quantity
                                            print("Major potions acquired.")
                                            sold = True
                                            break
                                        else:
                                            print("You don't have enough gold.")
                                            break
                        else:
                            SupportInfo.clear()
                            if character.gold >= 15:
                                character.gold -= 15
                                character.majorPotions += 1
                                self.majorPotions -= 1
                                print("Major potion acquired.")
                            else:
                                print("You don't have enough gold.")
                        break
                    elif event.event_type == keyboard.KEY_UP and event.name == "d":
                        if character.gold >= self.weapon.gold:
                            character.gold -= self.weapon.gold
                            SupportInfo.clear()
                            print(self.weapon.name + " acquired. Would you like to equip it? (d-yes, f-no")
                            while True:
                                event = keyboard.read_event(suppress=True)
                                if event.event_type == keyboard.KEY_UP and event.name == "d":
                                    found = False
                                    for weapon in character.storedWeapons:
                                        if weapon.name == character.equippedWeapon.name:
                                            weapon.quantity += 1
                                            found = True
                                    if not found:
                                        character.storedWeapons.append(character.equippedWeapon)
                                    character.equippedWeapon = self.weapon
                                elif event.event_type == keyboard.KEY_UP:
                                    SupportInfo.clear()
                                    found = False
                                    for weapon in character.storedWeapons:
                                        if weapon.name == self.weapon.name:
                                            weapon.quantity += 1
                                            found = True
                                    if not found:
                                        character.storedWeapons.append(self.weapon)
                        else:
                            print("You don't have enough gold.")
                        break
                    elif event.event_type == keyboard.KEY_UP and event.name == "f":
                        if character.gold >= self.armor.gold:
                            character.gold -= self.armor.gold
                            SupportInfo.clear()
                            print(self.armor.name + " armor acquired. Do you want to equip it? (d-yes, f-no)")
                            while True:
                                event = keyboard.read_event(suppress=True)
                                if event.event_type == keyboard.KEY_UP and event.name == "d":
                                    if character.equippedArmor.name != "None":
                                        found = False
                                        for armor in character.storedArmor:
                                            if armor.name == character.equippedArmor.name:
                                                armor.quantity += 1
                                                found = True
                                        if not found:
                                            character.storedArmor.append(character.equippedArmor)
                                    character.equippedArmor = self.armor
                                    break
                                elif event.event_type == keyboard.KEY_UP:
                                    SupportInfo.clear()
                                    found = False
                                    for armor in character.storedArmor:
                                        if armor.name == self.armor.name:
                                            armor.quantity += 1
                                            found = True
                                    if not found:
                                        character.storedArmor.append(self.armor)
                                    break
                        else:
                            print("You don't have enough gold.")
                        break
                    elif event.event_type == keyboard.KEY_UP and event.name == "g":
                        SupportInfo.clear()
                        print("What would you like to sell? (a-arrows, s-throwing knives, z-minor potions, "
                              "x-moderate potions, c-major potions, d-weapon, f-armor)")
                        while True:
                            event = keyboard.read_event(suppress=True)
                            if event.event_type == keyboard.KEY_UP and event.name == "a":
                                if character.arrows == 0:
                                    print("You don't have any arrows to sell.")
                                else:
                                    sold = False
                                    quantity = 0
                                    while not sold:
                                        SupportInfo.clear()
                                        print("You have " + str(character.arrows) + " arrows to sell. "
                                              "How many do you want to sell for 2 gold each? f-confirm " + str(quantity))
                                        while True:
                                            event = keyboard.read_event(suppress=True)
                                            if event.event_type == keyboard.KEY_UP and event.name == "up":
                                                if character.arrows > quantity:
                                                    quantity += 1
                                                break
                                            elif event.event_type == keyboard.KEY_UP and event.name == "down":
                                                if quantity >= 0:
                                                    quantity -= 1
                                                break
                                            elif event.event_type == keyboard.KEY_UP and event.name == "f":
                                                print(str(quantity) + " arrows sold.")
                                                self.arrows += quantity
                                                character.arrows -= quantity
                                                character.gold += 2 * quantity
                                                sold = True
                                                break
                                break
                            elif event.event_type == keyboard.KEY_UP and event.name == "s":
                                if character.knives == 0:
                                    print("You don't have any throwing knives to sell.")
                                else:
                                    sold = False
                                    quantity = 0
                                    while not sold:
                                        SupportInfo.clear()
                                        print("You have " + str(character.knives) + " throwing knives to sell. "
                                              "How many do you want to sell for 1 gold each? f-confirm " + str(quantity))
                                        while True:
                                            event = keyboard.read_event(suppress=True)
                                            if event.event_type == keyboard.KEY_UP and event.name == "up":
                                                if character.knives > quantity:
                                                    quantity += 1
                                                break
                                            elif event.event_type == keyboard.KEY_UP and event.name == "down":
                                                if quantity >= 0:
                                                    quantity -= 1
                                                break
                                            elif event.event_type == keyboard.KEY_UP and event.name == "f":
                                                print(str(quantity) + " throwing knives sold.")
                                                self.knives += quantity
                                                character.knives -= quantity
                                                character.gold += quantity
                                                sold = True
                                                break
                                break
                            elif event.event_type == keyboard.KEY_UP and event.name == "z":
                                if character.minorPotions == 0:
                                    print("You don't have any minor potions to sell.")
                                else:
                                    sold = False
                                    quantity = 0
                                    while not sold:
                                        SupportInfo.clear()
                                        print("You have " + str(character.minorPotions) + " minor potions to sell. "
                                              "How many do you want to sell for 2 gold each? f-confirm " + str(quantity))
                                        while True:
                                            event = keyboard.read_event(suppress=True)
                                            if event.event_type == keyboard.KEY_UP and event.name == "up":
                                                if character.minorPotions > quantity:
                                                    quantity += 1
                                                break
                                            elif event.event_type == keyboard.KEY_UP and event.name == "down":
                                                if quantity >= 0:
                                                    quantity -= 1
                                                break
                                            elif event.event_type == keyboard.KEY_UP and event.name == "f":
                                                print(str(quantity) + " minor potions sold.")
                                                self.minorPotions += quantity
                                                character.minorPotions -= quantity
                                                character.gold += 2 * quantity
                                                sold = True
                                                break
                                break
                            elif event.event_type == keyboard.KEY_UP and event.name == "x":
                                if character.moderatePotions == 0:
                                    print("You don't have any moderate potions to sell.")
                                else:
                                    sold = False
                                    quantity = 0
                                    while not sold:
                                        SupportInfo.clear()
                                        print("You have " + str(character.moderatePotions) + " moderate potions to sell. "
                                              "How many do you want to sell for 5 gold each? f-confirm " + str(quantity))
                                        while True:
                                            event = keyboard.read_event(suppress=True)
                                            if event.event_type == keyboard.KEY_UP and event.name == "up":
                                                if character.moderatePotions > quantity:
                                                    quantity += 1
                                                break
                                            elif event.event_type == keyboard.KEY_UP and event.name == "down":
                                                if quantity >= 0:
                                                    quantity -= 1
                                                break
                                            elif event.event_type == keyboard.KEY_UP and event.name == "f":
                                                print(str(quantity) + " moderate potions sold.")
                                                self.moderatePotions += quantity
                                                character.moderatePotions -= quantity
                                                character.gold += 5 * quantity
                                                sold = True
                                                break
                                break
                            elif event.event_type == keyboard.KEY_UP and event.name == "c":
                                if character.majorPotions == 0:
                                    print("You don't have any major potions to sell.")
                                else:
                                    sold = False
                                    quantity = 0
                                    while not sold:
                                        SupportInfo.clear()
                                        print("You have " + str(character.majorPotions) + " major potions to sell. "
                                              "How many do you want to sell for 5 gold each? f-confirm " + str(quantity))
                                        while True:
                                            event = keyboard.read_event(suppress=True)
                                            if event.event_type == keyboard.KEY_UP and event.name == "up":
                                                if character.majorPotions > quantity:
                                                    quantity += 1
                                                break
                                            elif event.event_type == keyboard.KEY_UP and event.name == "down":
                                                if quantity >= 0:
                                                    quantity -= 1
                                                break
                                            elif event.event_type == keyboard.KEY_UP and event.name == "f":
                                                print(str(quantity) + " major potions sold.")
                                                self.majorPotions += quantity
                                                character.majorPotions -= quantity
                                                character.gold += 5 * quantity
                                                sold = True
                                                break
                                break
                            elif event.event_type == keyboard.KEY_UP and event.name == "d":
                                SupportInfo.clear()
                                print("Do you want to sell your equipped weapon? (d-yes, f-no)")
                                while True:
                                    event = keyboard.read_event(suppress=True)
                                    if event.event_type == keyboard.KEY_UP and event.name == "d":
                                        print(character.equippedWeapon.name + " sold for " + str(character.equippedWeapon.gold))
                                        character.gold += character.equippedWeapon.gold
                                        if character.storedWeapons:
                                            equipped = False
                                            for stored_weapon in character.storedWeapons:
                                                print("Would you like to equip " + stored_weapon.name + "? (d-yes, f-no)")
                                                while True:
                                                    event = keyboard.read_event(suppress=True)
                                                    if event.event_type == keyboard.KEY_UP and event.name == "d":
                                                        character.equippedWeapon = stored_weapon
                                                        if stored_weapon.quantity == 1:
                                                            character.storedWeapons.remove(stored_weapon)
                                                        else:
                                                            stored_weapon.quantity -= 1
                                                        equipped = True
                                                        break
                                                if equipped:
                                                    break
                                            if not equipped:
                                                character.equippedWeapon = SupportInfo.Fist()
                                        else:
                                            character.equippedWeapon = SupportInfo.Fist()
                                        break
                                    elif event.event_type == keyboard.KEY_UP:
                                        SupportInfo.clear()
                                        if len(character.storedWeapons) > 0:
                                            print("Stored Weapons to sell:")
                                            for weapon in character.storedWeapons:
                                                print(str(weapon.quantity) + " " + weapon.print_details())
                                                print()
                                            print("Which weapon do you want to sell for half its value? (f-confirm, c-cancel)")
                                            index = 0
                                            selected = False
                                            while not selected:
                                                print()
                                                print(character.storedWeapons[index].print_details())
                                                while True:
                                                    event = keyboard.read_event(suppress=True)
                                                    if event.event_type == keyboard.KEY_UP and event.name == "up":
                                                        if index < len(character.storedWeapons) - 1:
                                                            index += 1
                                                        SupportInfo.clear()
                                                        break
                                                    elif event.event_type == keyboard.KEY_UP and event.name == "down":
                                                        if index >= 0:
                                                            index -= 1
                                                        SupportInfo.clear()
                                                        break
                                                    elif event.event_type == keyboard.KEY_UP and event.name == "c":
                                                        SupportInfo.clear()
                                                        selected = True
                                                        break
                                                    elif event.event_type == keyboard.KEY_UP and event.name == "f":
                                                        weapon = character.storedWeapons[index]
                                                        quantity = 0
                                                        sold = False
                                                        while not sold:
                                                            SupportInfo.clear()
                                                            print("You have " + str(weapon.quantity) + " " + weapon.name + " to sell. "
                                                                  "How many do you want to sell? (f-confirm) " + str(quantity))
                                                            while True:
                                                                event = keyboard.read_event(suppress=True)
                                                                if event.event_type == keyboard.KEY_UP and event.name == "up":
                                                                    if quantity < weapon.quantity:
                                                                        quantity += 1
                                                                    break
                                                                elif event.event_type == keyboard.KEY_UP and event.name == "down":
                                                                    if quantity > 0:
                                                                        quantity -= 1
                                                                    break
                                                                elif event.event_type == keyboard.KEY_UP and event.name == "f":
                                                                    value = int(weapon.gold / 2) * quantity
                                                                    print(str(quantity) + " " + weapon.name + "s sold for " + str(value))
                                                                    character.gold += value
                                                                    weapon.quantity -= quantity
                                                                    if weapon.quantity == 0:
                                                                        character.storedWeapons.remove(weapon)
                                                                    sold = True
                                                                    break
                                                        selected = True
                                                        break
                                        else:
                                            print("No stored weapons to sell.")
                                        break
                                break
                            elif event.event_type == keyboard.KEY_UP and event.name == "f":
                                SupportInfo.clear()
                                print("Do you want to sell your equipped armor? d=yes f=no")
                                while True:
                                    event = keyboard.read_event(suppress=True)
                                    if event.event_type == keyboard.KEY_UP and event.name == "d":
                                        print(character.equippedArmor.name + " sold for " + str(character.equippedArmor.gold))
                                        character.gold += character.equippedArmor.gold
                                        if character.storedArmor:
                                            equipped = False
                                            for stored_armor in character.storedArmor:
                                                print("Would you like to equip " + stored_armor.name + "? d=yes f=no")
                                                while True:
                                                    choice = keyboard.read_event(suppress=True)
                                                    if choice.event_type == keyboard.KEY_UP and event.name == "d":
                                                        character.equippedArmor = stored_armor
                                                        stored_armor.quantity -= 1
                                                        if stored_armor.quantity == 0:
                                                            character.storedArmor.remove(stored_armor)
                                                        equipped = True
                                                        break
                                                if equipped:
                                                    break
                                            if not equipped:
                                                character.equippedArmor = SupportInfo.Armor("None", 0, 0)
                                            break
                                        else:
                                            character.equippedArmor = SupportInfo.Armor("None", 0, 0)
                                            break
                                    elif event.event_type == keyboard.KEY_UP:
                                        if len(character.storedArmor) > 0:
                                            SupportInfo.clear()
                                            print("Stored Armor to sell:")
                                            for armor in character.storedArmor:
                                                print(str(armor.quantity) + " " + armor.print_details())
                                                print()
                                            print("Which armor do you want to sell for half its value? (f-confirm, c-cancel")
                                            index = 0
                                            selected = False
                                            while not selected:
                                                print()
                                                print(character.storedArmor[index].print_details())
                                                while True:
                                                    event = keyboard.read_event(suppress=True)
                                                    if event.event_type == keyboard.KEY_UP and event.name == "up":
                                                        if index < len(character.storedArmor) - 1:
                                                            index += 1
                                                        SupportInfo.clear()
                                                        break
                                                    elif event.event_type == keyboard.KEY_UP and event.name == "down":
                                                        if index >= 0:
                                                            index -= 1
                                                        SupportInfo.clear()
                                                        break
                                                    elif event.event_type == keyboard.KEY_UP and event.name == "c":
                                                        selected = True
                                                        SupportInfo.clear()
                                                        break
                                                    elif event.event_type == keyboard.KEY_UP and event.name == "f":
                                                        armor = character.storedArmor[index]
                                                        sold = False
                                                        quantity = 0
                                                        while not sold:
                                                            SupportInfo.clear()
                                                            print("You have " + str(armor.quantity) + " " + armor.name + " to sell. "
                                                                  "How many do you want to sell? f-confirm " + str(quantity))
                                                            while True:
                                                                event = keyboard.read_event(suppress=True)
                                                                if event.event_type == keyboard.KEY_UP and event.name == "up":
                                                                    if armor.quantity > quantity:
                                                                        quantity += 1
                                                                    break
                                                                elif event.event_type == keyboard.KEY_UP and event.name == "down":
                                                                    if quantity > 0:
                                                                        quantity -= 1
                                                                    break
                                                                elif event.event_type == keyboard.KEY_UP and event.name == "f":
                                                                    value = int(armor.gold / 2) * quantity
                                                                    print(str(quantity) + " " + armor.name + "s sold for " + str(value))
                                                                    character.gold += value
                                                                    armor.quantity -= quantity
                                                                    if armor.quantity == 0:
                                                                        character.storedArmor.remove(armor)
                                                                    sold = True
                                                                    break
                                                        selected = True
                                                        break
                                        else:
                                            print("No stored armor to sell.")
                                        break
                                break
                            elif event.event_type == keyboard.KEY_UP:
                                SupportInfo.clear()
                                print("Selling cancelled.")
                                break
                        break
                    elif event.event_type == keyboard.KEY_UP and event.name == "q":
                        done = True
                        break
        except:
            f = open("error_report.txt", "a")
            print("An error occurred when shopping.")
            traceback.print_exc(None, f)
            f.close()


def down_facing_doors(room, row, column):
    global unopenedDoors
    if unopenedDoors > 1:
        selection = random.randrange(1, 12, 1)
    else:
        selection = random.randrange(5, 12, 1)
    unopenedDoors -= 1
    if selection == 1:
        return SmallRoomBottomDoor(room, row, column)
    if selection == 2:
        return MediumRoomBottomDoor(room, row, column)
    if selection == 3 and SupportInfo.characterLevel > 3:
        return GoblinTrap(room, row, column)
    if selection == 3 and SupportInfo.characterLevel <= 3:
        selection += 1
    if selection == 4:
        return BottomSmallSpiral(room, row, column)
    if selection == 5:
        return LeftDoorLongTCorridor(room, "corridor down", row, column)
    if selection == 6:
        return LeftDoorLongTCorridor(room, "end down", row, column)
    if selection == 7:
        return DownDoorLongTCorridor(room, "down", row, column)
    if selection == 8:
        return RightDoorLongTCorridor(room, "corridor down", row, column)
    if selection == 9:
        return RightDoorLongTCorridor(room, "end down", row, column)
    if selection == 10:
        return HorizontalCorridor(room, "down", row, column)
    else:
        return VerticalCorridor(room, "down", row, column)


def up_facing_doors(room, row, column):
    global unopenedDoors
    if unopenedDoors > 1:
        selection = random.randrange(1, 12, 1)
    else:
        selection = random.randrange(5, 12, 1)
    unopenedDoors -= 1
    if selection == 1:
        return SmallRoomTopDoor(room, row, column)
    if selection == 2:
        return MediumRoomTopDoor(room, row, column)
    if selection == 3 and SupportInfo.characterLevel > 3:
        return GoblinTrap(room, row, column)
    if selection == 3 and SupportInfo.characterLevel <= 3:
        selection += 1
    if selection == 4:
        return TopSmallSpiral(room, row, column)
    if selection == 5:
        return LeftDoorLongTCorridor(room, "corridor up", row, column)
    if selection == 6:
        return LeftDoorLongTCorridor(room, "end up", row, column)
    if selection == 7:
        return UpDoorLongTCorridor(room, "up", row, column)
    if selection == 8:
        return RightDoorLongTCorridor(room, "corridor up", row, column)
    if selection == 9:
        return RightDoorLongTCorridor(room, "end up", row, column)
    if selection == 10:
        return HorizontalCorridor(room, "up", row, column)
    else:
        return VerticalCorridor(room, "up", row, column)


def right_facing_doors(room, row, column):
    global unopenedDoors
    if unopenedDoors > 1:
        selection = random.randrange(1, 12, 1)
    else:
        selection = random.randrange(5, 12, 1)
    unopenedDoors -= 1
    if selection == 1:
        return MediumRoomRightDoor(room, row, column)
    if selection == 2:
        return SmallRoomRightDoor(room, row, column)
    if selection == 3 and SupportInfo.characterLevel > 3:
        return GoblinTrap(room, row, column)
    if selection == 3 and SupportInfo.characterLevel <= 3:
        selection += 1
    if selection == 4:
        return RightSmallSpiral(room, row, column)
    if selection == 5:
        return UpDoorLongTCorridor(room, "corridor right", row, column)
    if selection == 6:
        return UpDoorLongTCorridor(room, "bottom right", row, column)
    if selection == 7:
        return RightDoorLongTCorridor(room, "right", row, column)
    if selection == 8:
        return DownDoorLongTCorridor(room, "corridor right", row, column)
    if selection == 9:
        return DownDoorLongTCorridor(room, "top right", row, column)
    if selection == 10:
        return HorizontalCorridor(room, "right", row, column)
    else:
        return VerticalCorridor(room, "right", row, column)


def left_facing_doors(room, row, column):
    global unopenedDoors
    if unopenedDoors > 1:
        selection = random.randrange(1, 12, 1)
    else:
        selection = random.randrange(5, 12, 1)
    unopenedDoors -= 1
    if selection == 1:
        return SmallRoomLeftDoor(room, row, column)
    if selection == 2:
        return MediumRoomLeftDoor(room, row, column)
    if selection == 3 and SupportInfo.characterLevel > 3:
        return GoblinTrap(room, row, column)
    if selection == 3 and SupportInfo.characterLevel <= 3:
        selection += 1
    if selection == 4:
        return LeftSmallSpiral(room, row, column)
    if selection == 5:
        return VerticalCorridor(room, "left", row, column)
    if selection == 6:
        return UpDoorLongTCorridor(room, "corridor left", row, column)
    if selection == 7:
        return UpDoorLongTCorridor(room, "bottom left", row, column)
    if selection == 8:
        return DownDoorLongTCorridor(room, "corridor left", row, column)
    if selection == 9:
        return DownDoorLongTCorridor(room, "top left", row, column)
    if selection == 10:
        return HorizontalCorridor(room, "left", row, column)
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
        try:
            mover.currentRoom = self.rightEntranceConnection
            self.room[mover.current_row][mover.current_column - 1] = " "
            mover.current_row = 3
            mover.current_column = 1
            mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
        except:
            f = open("error_report.txt", "a")
            print("An error occurred when leaving.")
            traceback.print_exc(None, f)
            f.close()


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
        self.tables = random.randrange(0, 4, 1)
        self.chests = random.randrange(0, 4, 1)
        self.enemies = random.randrange(0, 4, 1)
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
        try:
            self.room[mover.current_row][mover.current_column - 1] = " "
            mover.currentRoom = self.door
            mover.current_row = self.connectedRow
            mover.current_column = self.connectedColumn
            mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
        except:
            f = open("error_report.txt", "a")
            print("An error occurred when leaving.")
            traceback.print_exc(None, f)
            f.close()


class MediumRoomLeftDoor:
    def __init__(self, connection, row, column):
        self.room = [["W", "W", "W", "W", "W", "W", "W"],
                     ["W", " ", " ", " ", " ", " ", "W"],
                     ["W", " ", " ", " ", " ", " ", "W"],
                     ["D", " ", " ", " ", " ", " ", "W"],
                     ["W", " ", " ", " ", " ", " ", "W"],
                     ["W", " ", " ", " ", " ", " ", "W"],
                     ["W", "W", "W", "W", "W", "W", "W"]]
        self.door = connection
        self.startRow = 3
        self.startColumn = 1
        self.connectedRow = row
        self.connectedColumn = column
        self.tables = random.randrange(0, 4, 1)
        self.chests = random.randrange(0, 4, 1)
        self.enemies = random.randrange(0, 4, 1)
        if self.tables == 1:
            self.room[3][5] = 'T'
        elif self.tables == 2:
            self.room[5][5] = 'T'
            self.room[1][5] = 'T'
        elif self.tables == 3:
            self.room[3][5] = 'T'
            self.room[5][5] = 'T'
            self.room[1][5] = 'T'
        if self.chests == 1:
            if self.room[3][5] == " ":
                self.room[3][5] = 'C'
            else:
                self.room[2][5] = 'C'
        elif self.chests == 2:
            self.room[2][5] = 'C'
            self.room[4][5] = 'C'
        elif self.chests == 3:
            if self.room[3][5] == " ":
                self.room[3][5] = 'C'
            else:
                self.room[3][4] = 'C'
            self.room[2][5] = 'C'
            self.room[4][5] = 'C'
        if self.enemies == 1:
            if self.room[3][5] == " ":
                self.room[3][5] = "g"
                activeCharacters.append(choose_enemies(self, 3, 5))
            elif self.room[3][4] == " ":
                self.room[3][4] = "g"
                activeCharacters.append(choose_enemies(self, 3, 4))
            else:
                self.room[3][3] = "g"
                activeCharacters.append(choose_enemies(self, 3, 3))
        elif self.enemies == 2:
            if self.room[2][5] == " ":
                self.room[2][5] = 'g'
                self.room[4][5] = 'g'
                activeCharacters.append(choose_enemies(self, 2, 5))
                activeCharacters.append(choose_enemies(self, 4, 5))
            else:
                self.room[2][4] = 'g'
                self.room[4][4] = 'g'
                activeCharacters.append(choose_enemies(self, 2, 4))
                activeCharacters.append(choose_enemies(self, 4, 4))
        elif self.enemies == 3:
            if self.room[3][5] == " ":
                self.room[3][5] = 'g'
                self.room[2][5] = 'g'
                self.room[4][5] = 'g'
                activeCharacters.append(choose_enemies(self, 3, 5))
                activeCharacters.append(choose_enemies(self, 2, 5))
                activeCharacters.append(choose_enemies(self, 4, 5))
            elif self.room[2][5] == " ":
                if self.room[3][4] == " ":
                    self.room[3][4] = 'g'
                    activeCharacters.append(choose_enemies(self, 3, 4))
                else:
                    self.room[3][3] = 'g'
                    activeCharacters.append(choose_enemies(self, 3, 3))
                self.room[2][5] = 'g'
                self.room[4][5] = 'g'
                activeCharacters.append(choose_enemies(self, 2, 5))
                activeCharacters.append(choose_enemies(self, 4, 5))
            elif self.room[3][4] == " ":
                self.room[3][4] = 'g'
                self.room[2][4] = 'g'
                self.room[4][4] = 'g'
                activeCharacters.append(choose_enemies(self, 3, 4))
                activeCharacters.append(choose_enemies(self, 2, 4))
                activeCharacters.append(choose_enemies(self, 4, 4))
            else:
                self.room[3][3] = 'g'
                self.room[2][4] = 'g'
                self.room[4][4] = 'g'
                activeCharacters.append(choose_enemies(self, 3, 3))
                activeCharacters.append(choose_enemies(self, 2, 4))
                activeCharacters.append(choose_enemies(self, 4, 4))

    def leave(self, mover, symbol):
        try:
            self.room[mover.current_row][mover.current_column + 1] = " "
            mover.currentRoom = self.door
            mover.current_row = self.connectedRow
            mover.current_column = self.connectedColumn
            mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
        except:
            f = open("error_report.txt", "a")
            print("An error occurred when leaving.")
            traceback.print_exc(None, f)
            f.close()


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
        try:
            self.room[mover.current_row + 1][mover.current_column] = " "
            mover.currentRoom = self.door
            mover.current_row = self.connectedRow
            mover.current_column = self.connectedColumn
            mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
        except:
            f = open("error_report.txt", "a")
            print("An error occurred when leaving.")
            traceback.print_exc(None, f)
            f.close()


class MediumRoomBottomDoor:
    def __init__(self, connection, row, column):
        self.room = [["W", "W", "W", "W", "W", "W", "W"],
                     ["W", " ", " ", " ", " ", " ", "W"],
                     ["W", " ", " ", " ", " ", " ", "W"],
                     ["W", " ", " ", " ", " ", " ", "W"],
                     ["W", " ", " ", " ", " ", " ", "W"],
                     ["W", " ", " ", " ", " ", " ", "W"],
                     ["W", "W", "W", "D", "W", "W", "W"]]
        self.door = connection
        self.startRow = 5
        self.startColumn = 3
        self.connectedRow = row
        self.connectedColumn = column
        self.tables = random.randrange(0, 4, 1)
        self.chests = random.randrange(0, 4, 1)
        self.enemies = random.randrange(0, 4, 1)
        if self.tables == 1:
            self.room[1][3] = 'T'
        elif self.tables == 2:
            self.room[1][1] = 'T'
            self.room[1][5] = 'T'
        elif self.tables == 3:
            self.room[1][3] = 'T'
            self.room[1][1] = 'T'
            self.room[1][5] = 'T'
        if self.chests == 1:
            if self.room[1][3] == " ":
                self.room[1][3] = 'C'
            else:
                self.room[1][2] = 'C'
        elif self.chests == 2:
            self.room[1][2] = 'C'
            self.room[1][4] = 'C'
        elif self.chests == 3:
            if self.room[1][3] == " ":
                self.room[1][3] = 'C'
            else:
                self.room[2][3] = 'C'
            self.room[1][2] = 'C'
            self.room[1][4] = 'C'
        if self.enemies == 1:
            if self.room[1][3] == " ":
                self.room[1][3] = "g"
                activeCharacters.append(choose_enemies(self, 1, 3))
            elif self.room[2][3] == " ":
                self.room[2][3] = "g"
                activeCharacters.append(choose_enemies(self, 2, 3))
            else:
                self.room[3][3] = "g"
                activeCharacters.append(choose_enemies(self, 3, 3))
        elif self.enemies == 2:
            if self.room[1][2] == " ":
                self.room[1][2] = 'g'
                self.room[1][4] = 'g'
                activeCharacters.append(choose_enemies(self, 1, 2))
                activeCharacters.append(choose_enemies(self, 1, 4))
            else:
                self.room[2][4] = 'g'
                self.room[2][2] = 'g'
                activeCharacters.append(choose_enemies(self, 2, 4))
                activeCharacters.append(choose_enemies(self, 2, 2))
        elif self.enemies == 3:
            if self.room[1][3] == " ":
                self.room[1][3] = 'g'
                self.room[1][2] = 'g'
                self.room[1][4] = 'g'
                activeCharacters.append(choose_enemies(self, 1, 2))
                activeCharacters.append(choose_enemies(self, 1, 3))
                activeCharacters.append(choose_enemies(self, 1, 4))
            elif self.room[1][2] == " ":
                if self.room[2][3] == " ":
                    self.room[2][3] = 'g'
                    activeCharacters.append(choose_enemies(self, 2, 3))
                else:
                    self.room[3][3] = 'g'
                    activeCharacters.append(choose_enemies(self, 3, 3))
                self.room[1][2] = 'g'
                self.room[1][4] = 'g'
                activeCharacters.append(choose_enemies(self, 1, 2))
                activeCharacters.append(choose_enemies(self, 1, 4))
            elif self.room[2][3] == " ":
                self.room[2][2] = 'g'
                self.room[2][3] = 'g'
                self.room[2][4] = 'g'
                activeCharacters.append(choose_enemies(self, 2, 2))
                activeCharacters.append(choose_enemies(self, 2, 3))
                activeCharacters.append(choose_enemies(self, 2, 4))
            else:
                self.room[3][3] = 'g'
                self.room[2][3] = 'g'
                self.room[2][4] = 'g'
                activeCharacters.append(choose_enemies(self, 3, 3))
                activeCharacters.append(choose_enemies(self, 2, 3))
                activeCharacters.append(choose_enemies(self, 2, 4))

    def leave(self, mover, symbol):
        try:
            self.room[mover.current_row - 1][mover.current_column] = " "
            mover.currentRoom = self.door
            mover.current_row = self.connectedRow
            mover.current_column = self.connectedColumn
            mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
        except:
            f = open("error_report.txt", "a")
            print("An error occurred when leaving.")
            traceback.print_exc(None, f)
            f.close()


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
        try:
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
        except:
            f = open("error_report.txt", "a")
            print("An error occurred when leaving.")
            traceback.print_exc(None, f)
            f.close()


class RightDoorLongTCorridor:
    def __init__(self, connection, direction, row, column):
        self.room = [['W', 'D', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                     ['W', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                     ['W', ' ', 'W', 'W', 'D', 'W', 'W', 'W', 'W', 'W'],
                     ['W', 'g', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'D'],
                     ['W', ' ', 'W', 'W', 'W', 'W', 'W', 'D', 'W', 'W'],
                     ['W', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                     ['W', 'D', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]
        activeCharacters.append(choose_enemies(self, 3, 1))
        global unopenedDoors
        unopenedDoors += 4
        if direction == "right":
            self.right = connection
            self.rightConnection = True
            self.startRow = 3
            self.startColumn = 8
            self.rightRow = row
            self.rightColumn = column
        else:
            self.rightEntrance = None
            self.rightConnection = False
            self.rightRow = 3
            self.rightColumn = 8
        if direction == "corridor up":
            self.corridorUp = connection
            self.corridorUpConnection = True
            self.startRow = 3
            self.startColumn = 4
            self.corridorUpRow = row
            self.corridorUpColumn = column
        else:
            self.corridorUp = None
            self.corridorUpConnection = False
            self.corridorUpRow = 3
            self.corridorUpColumn = 4
        if direction == "end up":
            self.endUp = connection
            self.endUpConnection = True
            self.startRow = 1
            self.startColumn = 1
            self.endUpRow = row
            self.endUpColumn = column
        else:
            self.endUp = None
            self.endUpConnection = False
            self.endUpRow = 1
            self.endUpColumn = 1
        if direction == "corridor down":
            self.corridorDown = connection
            self.corridorDownConnection = True
            self.startRow = 3
            self.startColumn = 7
            self.corridorDownRow = row
            self.corridorDownColumn = column
        else:
            self.corridorDown = None
            self.corridorDownConnection = False
            self.corridorDownRow = 3
            self.corridorDownColumn = 7
        if direction == "end down":
            self.endDown = connection
            self.endDownConnection = True
            self.startRow = 5
            self.startColumn = 1
            self.endDownRow = row
            self.endDownColumn = column
        else:
            self.endDown = None
            self.endDownConnection = False
            self.endDownRow = 5
            self.endDownColumn = 1

    def leave(self, mover, symbol):
        try:
            if mover.current_row == 3 and mover.current_column == 9:
                if self.rightConnection:
                    self.room[mover.current_row][mover.current_column - 1] = " "
                    mover.current_row = self.rightRow
                    mover.current_column = self.rightColumn
                    mover.currentRoom = self.right
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
                else:
                    self.room[mover.current_row][mover.current_column - 1] = " "
                    self.right = left_facing_doors(self, 3, 8)
                    self.rightConnection = True
                    self.rightRow = self.right.startRow
                    self.rightColumn = self.right.startColumn
                    mover.current_row = self.rightRow
                    mover.current_column = self.rightColumn
                    mover.currentRoom = self.right
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
            elif mover.current_row == 2 and mover.current_column == 4:
                if self.corridorUpConnection:
                    self.room[mover.current_row + 1][mover.current_column] = " "
                    mover.currentRoom = self.corridorUp
                    mover.current_row = self.corridorUpRow
                    mover.current_column = self.corridorUpColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
                else:
                    self.room[mover.current_row + 1][mover.current_column] = " "
                    self.corridorUp = down_facing_doors(self, 3, 4)
                    self.corridorUpConnection = True
                    self.corridorUpRow = self.corridorUp.startRow
                    self.corridorUpColumn = self.corridorUp.startColumn
                    mover.currentRoom = self.corridorUp
                    mover.current_row = self.corridorUpRow
                    mover.current_column = self.corridorUpColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
            elif mover.current_row == 4 and mover.current_column == 7:
                if self.corridorDownConnection:
                    self.room[mover.current_row - 1][mover.current_column] = " "
                    mover.currentRoom = self.corridorDown
                    mover.current_row = self.corridorDownRow
                    mover.current_column = self.corridorDownColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
                else:
                    self.room[mover.current_row - 1][mover.current_column] = " "
                    self.corridorDown = up_facing_doors(self, 3, 7)
                    self.corridorDownConnection = True
                    self.corridorDownRow = self.corridorDown.startRow
                    self.corridorDownColumn = self.corridorDown.startColumn
                    mover.currentRoom = self.corridorDown
                    mover.current_row = self.corridorDownRow
                    mover.current_column = self.corridorDownColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
            elif mover.current_row == 0 and mover.current_column == 1:
                if self.endUpConnection:
                    self.room[mover.current_row + 1][mover.current_column] = " "
                    mover.currentRoom = self.endUp
                    mover.current_row = self.endUpRow
                    mover.current_column = self.endUpColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
                else:
                    self.room[mover.current_row + 1][mover.current_column] = " "
                    self.endUp = down_facing_doors(self, 1, 1)
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
                    self.endDown = up_facing_doors(self, 5, 1)
                    self.endDownConnection = True
                    self.endDownRow = self.endDown.startRow
                    self.endDownColumn = self.endDown.startColumn
                    mover.currentRoom = self.endDown
                    mover.current_row = self.endDownRow
                    mover.current_column = self.endDownColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
        except:
            f = open("error_report.txt", "a")
            print("An error occurred when leaving.")
            traceback.print_exc(None, f)
            f.close()


class UpDoorLongTCorridor:
    def __init__(self, connection, direction, row, column):
        self.room = [['W', 'W', 'W', 'D', 'W', 'W', 'W'],
                     ['W', 'W', 'W', ' ', 'W', 'W', 'W'],
                     ['W', 'W', 'W', ' ', 'D', 'W', 'W'],
                     ['W', 'W', 'W', ' ', 'W', 'W', 'W'],
                     ['W', 'W', 'W', ' ', 'W', 'W', 'W'],
                     ['W', 'W', 'D', ' ', 'W', 'W', 'W'],
                     ['W', 'W', 'W', ' ', 'W', 'W', 'W'],
                     ['W', 'W', 'W', ' ', 'W', 'W', 'W'],
                     ['D', ' ', ' ', 'g', ' ', ' ', 'D'],
                     ['W', 'W', 'W', 'W', 'W', 'W', 'W']]
        activeCharacters.append(choose_enemies(self, 8, 3))
        global unopenedDoors
        unopenedDoors += 4
        if direction == "bottom left":
            self.bottomLeft = connection
            self.bottomLeftConnection = True
            self.startRow = 8
            self.startColumn = 1
            self.bottomLeftRow = row
            self.bottomLeftColumn = column
        else:
            self.bottomLeft = None
            self.bottomLeftConnection = False
            self.bottomLeftRow = 8
            self.bottomLeftColumn = 1
        if direction == "corridor left":
            self.corridorLeft = connection
            self.corridorLeftConnection = True
            self.startRow = 5
            self.startColumn = 3
            self.corridorLeftRow = row
            self.corridorLeftColumn = column
        else:
            self.corridorLeft = None
            self.corridorLeftConnection = False
            self.corridorLeftRow = 5
            self.corridorLeftColumn = 3
        if direction == "bottom right":
            self.bottomRight = connection
            self.bottomRightConnection = True
            self.startRow = 8
            self.startColumn = 5
            self.bottomRightRow = row
            self.bottomRightColumn = column
        else:
            self.bottomRight = None
            self.bottomRightConnection = False
            self.bottomRightRow = 8
            self.bottomRightColumn = 5
        if direction == "corridor right":
            self.corridorRight = connection
            self.corridorRightConnection = True
            self.startRow = 2
            self.startColumn = 3
            self.corridorRightRow = row
            self.corridorRightColumn = column
        else:
            self.corridorRight = None
            self.corridorRightConnection = False
            self.corridorRightRow = 2
            self.corridorRightColumn = 3
        if direction == "up":
            self.up = connection
            self.upConnection = True
            self.startRow = 1
            self.startColumn = 3
            self.upRow = row
            self.upColumn = column
        else:
            self.up = None
            self.upConnection = False
            self.upRow = 1
            self.upColumn = 3

    def leave(self, mover, symbol):
        try:
            if mover.current_row == 8 and mover.current_column == 0:
                if self.bottomLeftConnection:
                    self.room[mover.current_row][mover.current_column + 1] = " "
                    mover.current_row = self.bottomLeftRow
                    mover.current_column = self.bottomLeftColumn
                    mover.currentRoom = self.bottomLeft
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
                else:
                    self.room[mover.current_row][mover.current_column + 1] = " "
                    self.bottomLeft = right_facing_doors(self, 8, 1)
                    self.bottomLeftConnection = True
                    self.bottomLeftRow = self.bottomLeft.startRow
                    self.bottomLeftColumn = self.bottomLeft.startColumn
                    mover.current_row = self.bottomLeftRow
                    mover.current_column = self.bottomLeftColumn
                    mover.currentRoom = self.bottomLeft
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
            elif mover.current_row == 5 and mover.current_column == 2:
                if self.corridorLeftConnection:
                    self.room[mover.current_row][mover.current_column + 1] = " "
                    mover.currentRoom = self.corridorLeft
                    mover.current_row = self.corridorLeftRow
                    mover.current_column = self.corridorLeftColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
                else:
                    self.room[mover.current_row][mover.current_column + 1] = " "
                    self.corridorLeft = right_facing_doors(self, 5, 3)
                    self.corridorLeftConnection = True
                    self.corridorLeftRow = self.corridorLeft.startRow
                    self.corridorLeftColumn = self.corridorLeft.startColumn
                    mover.currentRoom = self.corridorLeft
                    mover.current_row = self.corridorLeftRow
                    mover.current_column = self.corridorLeftColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
            elif mover.current_row == 8 and mover.current_column == 6:
                if self.bottomRightConnection:
                    self.room[mover.current_row][mover.current_column - 1] = " "
                    mover.currentRoom = self.bottomRight
                    mover.current_row = self.bottomRightRow
                    mover.current_column = self.bottomRightColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
                else:
                    self.room[mover.current_row][mover.current_column - 1] = " "
                    self.bottomRight = left_facing_doors(self, 8, 5)
                    self.bottomRightConnection = True
                    self.bottomRightRow = self.bottomRight.startRow
                    self.bottomRightColumn = self.bottomRight.startColumn
                    mover.currentRoom = self.bottomRight
                    mover.current_row = self.bottomRightRow
                    mover.current_column = self.bottomRightColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
            elif mover.current_row == 2 and mover.current_column == 4:
                if self.corridorRightConnection:
                    self.room[mover.current_row][mover.current_column - 1] = " "
                    mover.currentRoom = self.corridorRight
                    mover.current_row = self.corridorRightRow
                    mover.current_column = self.corridorRightColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
                else:
                    self.room[mover.current_row][mover.current_column - 1] = " "
                    self.corridorRight = left_facing_doors(self, 2, 3)
                    self.corridorRightConnection = True
                    self.corridorRightRow = self.corridorRight.startRow
                    self.corridorRightColumn = self.corridorRight.startColumn
                    mover.currentRoom = self.corridorRight
                    mover.current_row = self.corridorRightRow
                    mover.current_column = self.corridorRightColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
            else:
                if self.upConnection:
                    self.room[mover.current_row + 1][mover.current_column] = " "
                    mover.currentRoom = self.up
                    mover.current_row = self.upRow
                    mover.current_column = self.upColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
                else:
                    self.room[mover.current_row + 1][mover.current_column] = " "
                    self.up = down_facing_doors(self, 1, 3)
                    self.upConnection = True
                    self.upRow = self.up.startRow
                    self.upColumn = self.up.startColumn
                    mover.currentRoom = self.up
                    mover.current_row = self.upRow
                    mover.current_column = self.upColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
        except:
            f = open("error_report.txt", "a")
            print("An error occurred when leaving.")
            traceback.print_exc(None, f)
            f.close()


class DownDoorLongTCorridor:
    def __init__(self, connection, direction, row, column):
        self.room = [['W', 'W', 'W', 'W', 'W', 'W', 'W'],
                     ['D', ' ', ' ', 'g', ' ', ' ', 'D'],
                     ['W', 'W', 'W', ' ', 'W', 'W', 'W'],
                     ['W', 'W', 'W', ' ', 'W', 'W', 'W'],
                     ['W', 'W', 'W', ' ', 'D', 'W', 'W'],
                     ['W', 'W', 'W', ' ', 'W', 'W', 'W'],
                     ['W', 'W', 'W', ' ', 'W', 'W', 'W'],
                     ['W', 'W', 'D', ' ', 'W', 'W', 'W'],
                     ['W', 'W', 'W', ' ', 'W', 'W', 'W'],
                     ['W', 'W', 'W', 'D', 'W', 'W', 'W']]
        activeCharacters.append(choose_enemies(self, 1, 3))
        global unopenedDoors
        unopenedDoors += 4
        if direction == "top left":
            self.topLeft = connection
            self.topLeftConnection = True
            self.startRow = 1
            self.startColumn = 1
            self.topLeftRow = row
            self.topLeftColumn = column
        else:
            self.topLeft = None
            self.topLeftConnection = False
            self.topLeftRow = 1
            self.topLeftColumn = 1
        if direction == "corridor left":
            self.corridorLeft = connection
            self.corridorLeftConnection = True
            self.startRow = 7
            self.startColumn = 3
            self.corridorLeftRow = row
            self.corridorLeftColumn = column
        else:
            self.corridorLeft = None
            self.corridorLeftConnection = False
            self.corridorLeftRow = 7
            self.corridorLeftColumn = 3
        if direction == "top right":
            self.topRight = connection
            self.topRightConnection = True
            self.startRow = 1
            self.startColumn = 5
            self.topRightRow = row
            self.topRightColumn = column
        else:
            self.topRight = None
            self.topRightConnection = False
            self.topRightRow = 1
            self.topRightColumn = 5
        if direction == "corridor right":
            self.corridorRight = connection
            self.corridorRightConnection = True
            self.startRow = 4
            self.startColumn = 3
            self.corridorRightRow = row
            self.corridorRightColumn = column
        else:
            self.corridorRight = None
            self.corridorRightConnection = False
            self.corridorRightRow = 4
            self.corridorRightColumn = 3
        if direction == "down":
            self.down = connection
            self.downConnection = True
            self.startRow = 8
            self.startColumn = 3
            self.downRow = row
            self.downColumn = column
        else:
            self.down = None
            self.downConnection = False
            self.downRow = 8
            self.downColumn = 3

    def leave(self, mover, symbol):
        try:
            if mover.current_row == 1 and mover.current_column == 0:
                if self.topLeftConnection:
                    self.room[mover.current_row][mover.current_column + 1] = " "
                    mover.current_row = self.topLeftRow
                    mover.current_column = self.topLeftColumn
                    mover.currentRoom = self.topLeft
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
                else:
                    self.room[mover.current_row][mover.current_column + 1] = " "
                    self.topLeft = right_facing_doors(self, 1, 1)
                    self.topLeftConnection = True
                    self.topLeftRow = self.topLeft.startRow
                    self.topLeftColumn = self.topLeft.startColumn
                    mover.current_row = self.topLeftRow
                    mover.current_column = self.topLeftColumn
                    mover.currentRoom = self.topLeft
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
            elif mover.current_row == 7 and mover.current_column == 2:
                if self.corridorLeftConnection:
                    self.room[mover.current_row][mover.current_column + 1] = " "
                    mover.currentRoom = self.corridorLeft
                    mover.current_row = self.corridorLeftRow
                    mover.current_column = self.corridorLeftColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
                else:
                    self.room[mover.current_row][mover.current_column + 1] = " "
                    self.corridorLeft = right_facing_doors(self, 7, 3)
                    self.corridorLeftConnection = True
                    self.corridorLeftRow = self.corridorLeft.startRow
                    self.corridorLeftColumn = self.corridorLeft.startColumn
                    mover.currentRoom = self.corridorLeft
                    mover.current_row = self.corridorLeftRow
                    mover.current_column = self.corridorLeftColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
            elif mover.current_row == 1 and mover.current_column == 6:
                if self.topRightConnection:
                    self.room[mover.current_row][mover.current_column - 1] = " "
                    mover.currentRoom = self.topRight
                    mover.current_row = self.topRightRow
                    mover.current_column = self.topRightColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
                else:
                    self.room[mover.current_row][mover.current_column - 1] = " "
                    self.topRight = left_facing_doors(self, 1, 5)
                    self.topRightConnection = True
                    self.topRightRow = self.topRight.startRow
                    self.topRightColumn = self.topRight.startColumn
                    mover.currentRoom = self.topRight
                    mover.current_row = self.topRightRow
                    mover.current_column = self.topRightColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
            elif mover.current_row == 4 and mover.current_column == 4:
                if self.corridorRightConnection:
                    self.room[mover.current_row][mover.current_column - 1] = " "
                    mover.currentRoom = self.corridorRight
                    mover.current_row = self.corridorRightRow
                    mover.current_column = self.corridorRightColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
                else:
                    self.room[mover.current_row][mover.current_column - 1] = " "
                    self.corridorRight = left_facing_doors(self, 4, 3)
                    self.corridorRightConnection = True
                    self.corridorRightRow = self.corridorRight.startRow
                    self.corridorRightColumn = self.corridorRight.startColumn
                    mover.currentRoom = self.corridorRight
                    mover.current_row = self.corridorRightRow
                    mover.current_column = self.corridorRightColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
            else:
                if self.downConnection:
                    self.room[mover.current_row - 1][mover.current_column] = " "
                    mover.currentRoom = self.down
                    mover.current_row = self.downRow
                    mover.current_column = self.downColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
                else:
                    self.room[mover.current_row - 1][mover.current_column] = " "
                    self.down = up_facing_doors(self, 8, 3)
                    self.downConnection = True
                    self.downRow = self.down.startRow
                    self.downColumn = self.down.startColumn
                    mover.currentRoom = self.down
                    mover.current_row = self.downRow
                    mover.current_column = self.downColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
        except:
            f = open("error_report.txt", "a")
            print("An error occurred when leaving.")
            traceback.print_exc(None, f)
            f.close()


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
        try:
            self.room[mover.current_row - 1][mover.current_column] = " "
            mover.currentRoom = self.door
            mover.current_row = self.connectedRow
            mover.current_column = self.connectedColumn
            mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
        except:
            f = open("error_report.txt", "a")
            print("An error occurred when leaving.")
            traceback.print_exc(None, f)
            f.close()


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
        try:
            self.room[mover.current_row][mover.current_column + 1] = " "
            mover.currentRoom = self.door
            mover.current_row = self.connectedRow
            mover.current_column = self.connectedColumn
            mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
        except:
            f = open("error_report.txt", "a")
            print("An error occurred when leaving.")
            traceback.print_exc(None, f)
            f.close()


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
        try:
            self.room[mover.current_row][mover.current_column - 1] = " "
            mover.currentRoom = self.door
            mover.current_row = self.connectedRow
            mover.current_column = self.connectedColumn
            mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
        except:
            f = open("error_report.txt", "a")
            print("An error occurred when leaving.")
            traceback.print_exc(None, f)
            f.close()


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
        try:
            self.room[mover.current_row + 1][mover.current_column] = " "
            mover.currentRoom = self.door
            mover.current_row = self.connectedRow
            mover.current_column = self.connectedColumn
            mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
        except:
            f = open("error_report.txt", "a")
            print("An error occurred when leaving.")
            traceback.print_exc(None, f)
            f.close()


class VerticalCorridor:
    def __init__(self, connection, direction, row, column):
        self.room = [['W', 'W', 'D', 'W', 'W'],
                     ['W', 'W', ' ', 'W', 'W'],
                     ['W', ' ', ' ', ' ', 'W'],
                     ['W', 'W', ' ', 'W', 'W'],
                     ['W', 'D', ' ', 'D', 'W'],
                     ['W', 'W', ' ', 'W', 'W'],
                     ['W', ' ', ' ', ' ', 'W'],
                     ['W', 'W', ' ', 'W', 'W'],
                     ['W', 'W', 'D', 'W', 'W']]
        global unopenedDoors
        unopenedDoors += 3
        self.startColumn = 2
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
            self.bottomColumn = 2
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
            self.leftColumn = 2
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
            self.upColumn = 2
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
            self.rightColumn = 2
        enemies = random.randrange(0, 5, 1)
        if enemies == 1:
            location = random.randrange(1, 5, 1)
            if location == 1:
                self.room[2][1] = 'g'
                activeCharacters.append(choose_enemies(self, 2, 1))
            elif location == 2:
                self.room[2][3] = 'g'
                activeCharacters.append(choose_enemies(self, 2, 3))
            elif location == 3:
                self.room[6][1] = 'g'
                activeCharacters.append(choose_enemies(self, 6, 1))
            else:
                self.room[6][3] = 'g'
                activeCharacters.append(choose_enemies(self, 6, 3))
        elif enemies == 2:
            location1 = random.randrange(1, 5, 1)
            location2 = random.randrange(1, 5, 1)
            if location2 == location1:
                location2 += 1
                if location2 > 4:
                    location2 -= 2
            if location1 == 1 or location2 == 1:
                self.room[2][1] = 'g'
                activeCharacters.append(choose_enemies(self, 2, 1))
            if location1 == 2 or location2 == 2:
                self.room[2][3] = 'g'
                activeCharacters.append(choose_enemies(self, 2, 3))
            if location1 == 3 or location2 == 3:
                self.room[6][1] = 'g'
                activeCharacters.append(choose_enemies(self, 6, 1))
            if location1 == 4 or location2 == 4:
                self.room[6][3] = 'g'
                activeCharacters.append(choose_enemies(self, 6, 3))
        elif enemies == 3:
            location1 = random.randrange(1, 5, 1)
            location2 = random.randrange(1, 5, 1)
            location3 = random.randrange(1, 5, 1)
            if location2 == location1:
                location2 += 1
                if location2 > 4:
                    location2 -= 2
            while location3 == location2 or location3 == location1:
                location3 += 1
                if location3 > 4:
                    location3 = 1
            if location1 == 1 or location2 == 1 or location3 == 1:
                self.room[2][1] = 'g'
                activeCharacters.append(choose_enemies(self, 2, 1))
            if location1 == 2 or location2 == 2 or location3 == 2:
                self.room[2][3] = 'g'
                activeCharacters.append(choose_enemies(self, 2, 3))
            if location1 == 3 or location2 == 3 or location3 == 3:
                self.room[6][1] = 'g'
                activeCharacters.append(choose_enemies(self, 6, 1))
            if location1 == 4 or location2 == 4 or location3 == 4:
                self.room[6][3] = 'g'
                activeCharacters.append(choose_enemies(self, 6, 3))
        elif enemies == 4:
            self.room[2][1] = 'g'
            activeCharacters.append(choose_enemies(self, 2, 1))
            self.room[2][3] = 'g'
            activeCharacters.append(choose_enemies(self, 2, 3))
            self.room[6][1] = 'g'
            activeCharacters.append(choose_enemies(self, 6, 1))
            self.room[6][3] = 'g'
            activeCharacters.append(choose_enemies(self, 6, 3))

    def leave(self, mover, symbol):
        try:
            if mover.current_row == 0 and mover.current_column == 2:
                if self.upEntrance:
                    self.room[mover.current_row + 1][mover.current_column] = " "
                    mover.currentRoom = self.upDoor
                    mover.current_row = self.upRow
                    mover.current_column = self.upColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
                else:
                    self.room[mover.current_row + 1][mover.current_column] = " "
                    self.upDoor = down_facing_doors(self, 1, 2)
                    self.upEntrance = True
                    self.upRow = self.upDoor.startRow
                    self.upColumn = self.upDoor.startColumn
                    mover.currentRoom = self.upDoor
                    mover.current_row = self.upRow
                    mover.current_column = self.upColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
            elif mover.current_row == 8 and mover.current_column == 2:
                if self.bottomEntrance:
                    self.room[mover.current_row - 1][mover.current_column] = " "
                    mover.currentRoom = self.bottomDoor
                    mover.current_row = self.bottomRow
                    mover.current_column = self.bottomColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
                else:
                    self.room[mover.current_row - 1][mover.current_column] = " "
                    self.bottomDoor = up_facing_doors(self, 7, 2)
                    self.bottomEntrance = True
                    self.bottomRow = self.bottomDoor.startRow
                    self.bottomColumn = self.bottomDoor.startColumn
                    mover.currentRoom = self.bottomDoor
                    mover.current_row = self.bottomRow
                    mover.current_column = self.bottomColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
            elif mover.current_row == 4 and mover.current_column == 1:
                if self.leftEntrance:
                    self.room[mover.current_row][mover.current_column + 1] = " "
                    mover.currentRoom = self.leftDoor
                    mover.current_row = self.leftRow
                    mover.current_column = self.leftColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
                else:
                    self.room[mover.current_row][mover.current_column + 1] = " "
                    self.leftDoor = right_facing_doors(self, 4, 2)
                    self.leftEntrance = True
                    self.leftRow = self.leftDoor.startRow
                    self.leftColumn = self.leftDoor.startColumn
                    mover.currentRoom = self.leftDoor
                    mover.current_row = self.leftRow
                    mover.current_column = self.leftColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
            elif mover.current_row == 4 and mover.current_column == 3:
                if self.rightEntrance:
                    self.room[mover.current_row][mover.current_column - 1] = " "
                    mover.currentRoom = self.rightDoor
                    mover.current_row = self.rightRow
                    mover.current_column = self.rightColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
                else:
                    self.room[mover.current_row][mover.current_column - 1] = " "
                    self.rightDoor = left_facing_doors(self, 4, 2)
                    self.rightEntrance = True
                    self.rightRow = self.rightDoor.startRow
                    self.rightColumn = self.rightDoor.startColumn
                    mover.currentRoom = self.rightDoor
                    mover.current_row = self.rightRow
                    mover.current_column = self.rightColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
        except:
            f = open("error_report.txt", "a")
            print("An error occurred when leaving.")
            traceback.print_exc(None, f)
            f.close()


class HorizontalCorridor:
    def __init__(self, connection, direction, row, column):
        self.room = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                     ['W', 'W', ' ', 'W', 'D', 'W', ' ', 'W', 'W'],
                     ['D', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'D'],
                     ['W', 'W', ' ', 'W', 'D', 'W', ' ', 'W', 'W'],
                     ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]
        global unopenedDoors
        unopenedDoors += 3
        self.startRow = 2
        if direction == "down":
            self.bottomEntrance = True
            self.bottomDoor = connection
            self.bottomRow = row
            self.bottomColumn = column
            self.startColumn = 4
        else:
            self.bottomEntrance = False
            self.bottomDoor = None
            self.bottomRow = 2
            self.bottomColumn = 4
        if direction == "left":
            self.leftEntrance = True
            self.leftDoor = connection
            self.leftRow = row
            self.leftColumn = column
            self.startColumn = 1
        else:
            self.leftEntrance = False
            self.leftDoor = None
            self.leftRow = 2
            self.leftColumn = 1
        if direction == "up":
            self.upEntrance = True
            self.upDoor = connection
            self.startColumn = 4
            self.upRow = row
            self.upColumn = column
        else:
            self.upEntrance = False
            self.upDoor = None
            self.upRow = 2
            self.upColumn = 4
        if direction == "right":
            self.rightEntrance = True
            self.rightDoor = connection
            self.startColumn = 7
            self.rightRow = row
            self.rightColumn = column
        else:
            self.rightEntrance = False
            self.rightDoor = None
            self.rightRow = 2
            self.rightColumn = 7
        enemies = random.randrange(0, 5, 1)
        if enemies == 1:
            location = random.randrange(1, 5, 1)
            if location == 1:
                self.room[1][2] = 'g'
                activeCharacters.append(choose_enemies(self, 1, 2))
            elif location == 2:
                self.room[3][2] = 'g'
                activeCharacters.append(choose_enemies(self, 3, 2))
            elif location == 3:
                self.room[1][6] = 'g'
                activeCharacters.append(choose_enemies(self, 1, 6))
            else:
                self.room[3][6] = 'g'
                activeCharacters.append(choose_enemies(self, 3, 6))
        elif enemies == 2:
            location1 = random.randrange(1, 5, 1)
            location2 = random.randrange(1, 5, 1)
            if location2 == location1:
                location2 += 1
                if location2 > 4:
                    location2 -= 2
            if location1 == 1 or location2 == 1:
                self.room[1][2] = 'g'
                activeCharacters.append(choose_enemies(self, 1, 2))
            if location1 == 2 or location2 == 2:
                self.room[3][2] = 'g'
                activeCharacters.append(choose_enemies(self, 3, 2))
            if location1 == 3 or location2 == 3:
                self.room[1][6] = 'g'
                activeCharacters.append(choose_enemies(self, 1, 6))
            if location1 == 4 or location2 == 4:
                self.room[3][6] = 'g'
                activeCharacters.append(choose_enemies(self, 3, 6))
        elif enemies == 3:
            location1 = random.randrange(1, 5, 1)
            location2 = random.randrange(1, 5, 1)
            location3 = random.randrange(1, 5, 1)
            if location2 == location1:
                location2 += 1
                if location2 > 4:
                    location2 -= 2
            while location3 == location2 or location3 == location1:
                location3 += 1
                if location3 > 4:
                    location3 = 1
            if location1 == 1 or location2 == 1 or location3 == 1:
                self.room[1][2] = 'g'
                activeCharacters.append(choose_enemies(self, 1, 2))
            if location1 == 2 or location2 == 2 or location3 == 2:
                self.room[3][2] = 'g'
                activeCharacters.append(choose_enemies(self, 3, 2))
            if location1 == 3 or location2 == 3 or location3 == 3:
                self.room[1][6] = 'g'
                activeCharacters.append(choose_enemies(self, 1, 6))
            if location1 == 4 or location2 == 4 or location3 == 4:
                self.room[3][6] = 'g'
                activeCharacters.append(choose_enemies(self, 3, 6))
        elif enemies == 4:
            self.room[1][2] = 'g'
            activeCharacters.append(choose_enemies(self, 1, 2))
            self.room[3][2] = 'g'
            activeCharacters.append(choose_enemies(self, 3, 2))
            self.room[1][6] = 'g'
            activeCharacters.append(choose_enemies(self, 1, 6))
            self.room[3][6] = 'g'
            activeCharacters.append(choose_enemies(self, 3, 6))

    def leave(self, mover, symbol):
        try:
            if mover.current_row == 1 and mover.current_column == 4:
                if self.upEntrance:
                    self.room[mover.current_row + 1][mover.current_column] = " "
                    mover.currentRoom = self.upDoor
                    mover.current_row = self.upRow
                    mover.current_column = self.upColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
                else:
                    self.room[mover.current_row + 1][mover.current_column] = " "
                    self.upDoor = down_facing_doors(self, 2, 4)
                    self.upEntrance = True
                    self.upRow = self.upDoor.startRow
                    self.upColumn = self.upDoor.startColumn
                    mover.currentRoom = self.upDoor
                    mover.current_row = self.upRow
                    mover.current_column = self.upColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
            elif mover.current_row == 3 and mover.current_column == 4:
                if self.bottomEntrance:
                    self.room[mover.current_row - 1][mover.current_column] = " "
                    mover.currentRoom = self.bottomDoor
                    mover.current_row = self.bottomRow
                    mover.current_column = self.bottomColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
                else:
                    self.room[mover.current_row - 1][mover.current_column] = " "
                    self.bottomDoor = up_facing_doors(self, 2, 4)
                    self.bottomEntrance = True
                    self.bottomRow = self.bottomDoor.startRow
                    self.bottomColumn = self.bottomDoor.startColumn
                    mover.currentRoom = self.bottomDoor
                    mover.current_row = self.bottomRow
                    mover.current_column = self.bottomColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
            elif mover.current_row == 2 and mover.current_column == 0:
                if self.leftEntrance:
                    self.room[mover.current_row][mover.current_column + 1] = " "
                    mover.currentRoom = self.leftDoor
                    mover.current_row = self.leftRow
                    mover.current_column = self.leftColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
                else:
                    self.room[mover.current_row][mover.current_column + 1] = " "
                    self.leftDoor = right_facing_doors(self, 2, 1)
                    self.leftEntrance = True
                    self.leftRow = self.leftDoor.startRow
                    self.leftColumn = self.leftDoor.startColumn
                    mover.currentRoom = self.leftDoor
                    mover.current_row = self.leftRow
                    mover.current_column = self.leftColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
            elif mover.current_row == 2 and mover.current_column == 8:
                if self.rightEntrance:
                    self.room[mover.current_row][mover.current_column - 1] = " "
                    mover.currentRoom = self.rightDoor
                    mover.current_row = self.rightRow
                    mover.current_column = self.rightColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
                else:
                    self.room[mover.current_row][mover.current_column - 1] = " "
                    self.rightDoor = left_facing_doors(self, 2, 7)
                    self.rightEntrance = True
                    self.rightRow = self.rightDoor.startRow
                    self.rightColumn = self.rightDoor.startColumn
                    mover.currentRoom = self.rightDoor
                    mover.current_row = self.rightRow
                    mover.current_column = self.rightColumn
                    mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
        except:
            f = open("error_report.txt", "a")
            print("An error occurred when leaving.")
            traceback.print_exc(None, f)
            f.close()


class GoblinTrap:
    def __init__(self, connection, row, column):
        self.room = [['W', 'D', 'W'],
                     ['W', 'g', 'W'],
                     ['W', 'g', 'W'],
                     ['W', 'g', 'W'],
                     ['W', ' ', 'W'],
                     ['W', 'W', 'W']]
        self.door = connection
        self.startRow = 4
        self.startColumn = 1
        self.connectedRow = row
        self.connectedColumn = column
        activeCharacters.append(GoblinArcher(self, 1, 1))
        activeCharacters.append(GoblinArcher(self, 2, 1))
        activeCharacters.append(GoblinWarrior(self, 3, 1))

    def leave(self, mover, symbol):
        try:
            self.room[mover.current_row + 1][mover.current_column] = " "
            mover.currentRoom = self.door
            mover.current_row = self.connectedRow
            mover.current_column = self.connectedColumn
            mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
        except:
            f = open("error_report.txt", "a")
            print("An error occurred when leaving.")
            traceback.print_exc(None, f)
            f.close()


class TopSmallSpiral:
    def __init__(self, connection, row, column):
        self.room = [['W', 'D', 'W', 'W', 'W', 'W', 'W'],
                     ['W', ' ', ' ', ' ', ' ', ' ', 'W'],
                     ['W', 'W', 'W', 'W', 'W', ' ', 'W'],
                     ['W', ' ', ' ', ' ', 'W', ' ', 'W'],
                     ['W', ' ', 'W', ' ', 'W', ' ', 'W'],
                     ['W', ' ', 'W', 'W', 'W', ' ', 'W'],
                     ['W', ' ', ' ', ' ', ' ', ' ', 'W'],
                     ['W', 'W', 'W', 'W', 'W', 'W', 'W']]
        self.door = connection
        self.startRow = 1
        self.startColumn = 1
        self.connectedRow = row
        self.connectedColumn = column
        self.chests = random.randrange(1, 5, 1)
        self.tables = random.randrange(0, 5, 1)
        self.enemies = random.randrange(1, 16, 1)
        if self.tables + self.chests > 4:
            self.tables -= self.chests
        elif self.tables + self.chests < 4:
            self.room[4][3] = 's'
            self.shop = Shop()
        if self.tables + self.chests - 1 + self.enemies > 11:
            self.enemies -= self.tables + self.chests - 1
        while self.chests >= 1:
            if self.room[4][3] == ' ':
                self.room[4][3] = 'C'
            elif self.room[3][1] == ' ':
                self.room[3][1] = 'C'
            elif self.room[6][1] == ' ':
                self.room[6][1] = 'C'
            elif self.room[6][5] == ' ':
                self.room[6][5] = 'C'
            self.chests -= 1
        while self.tables >= 1:
            if self.room[4][3] == ' ':
                self.room[4][3] = 'T'
            elif self.room[3][1] == ' ':
                self.room[3][1] = 'T'
            elif self.room[6][1] == ' ':
                self.room[6][1] = 'T'
            elif self.room[6][5] == ' ':
                self.room[6][5] = 'T'
            self.tables -= 1
        while self.enemies >= 1:
            if self.room[3][3] == ' ':
                self.room[3][3] = 'g'
                activeCharacters.append(choose_enemies(self, 3, 3))
            elif self.room[3][2] == ' ':
                self.room[3][2] = 'g'
                activeCharacters.append(choose_enemies(self, 3, 2))
            elif self.room[3][1] == ' ':
                self.room[3][1] = 'g'
                activeCharacters.append(choose_enemies(self, 3, 1))
            elif self.room[4][1] == ' ':
                self.room[4][1] = 'g'
                activeCharacters.append(choose_enemies(self, 4, 1))
            elif self.room[5][1] == ' ':
                self.room[5][1] = 'g'
                activeCharacters.append(choose_enemies(self, 5, 1))
            elif self.room[6][1] == ' ':
                self.room[6][1] = 'g'
                activeCharacters.append(choose_enemies(self, 6, 1))
            elif self.room[6][2] == ' ':
                self.room[6][2] = 'g'
                activeCharacters.append(choose_enemies(self, 6, 2))
            elif self.room[6][3] == ' ':
                self.room[6][3] = 'g'
                activeCharacters.append(choose_enemies(self, 6, 3))
            elif self.room[6][4] == ' ':
                self.room[6][4] = 'g'
                activeCharacters.append(choose_enemies(self, 6, 4))
            elif self.room[6][5] == ' ':
                self.room[6][5] = 'g'
                activeCharacters.append(choose_enemies(self, 6, 5))
            elif self.room[5][5] == ' ':
                self.room[5][5] = 'g'
                activeCharacters.append(choose_enemies(self, 5, 5))
            elif self.room[4][5] == ' ':
                self.room[4][5] = 'g'
                activeCharacters.append(choose_enemies(self, 4, 5))
            elif self.room[3][5] == ' ':
                self.room[3][5] = 'g'
                activeCharacters.append(choose_enemies(self, 3, 5))
            elif self.room[2][5] == ' ':
                self.room[2][5] = 'g'
                activeCharacters.append(choose_enemies(self, 2, 5))
            elif self.room[1][5] == ' ':
                self.room[1][5] = 'g'
                activeCharacters.append(choose_enemies(self, 1, 5))
            self.enemies -= 1

    def leave(self, mover, symbol):
        try:
            self.room[mover.current_row + 1][mover.current_column] = " "
            mover.currentRoom = self.door
            mover.current_row = self.connectedRow
            mover.current_column = self.connectedColumn
            mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
        except:
            f = open("error_report.txt", "a")
            print("An error occurred when leaving.")
            traceback.print_exc(None, f)
            f.close()


class BottomSmallSpiral:
    def __init__(self, connection, row, column):
        self.room = [['W', 'W', 'W', 'W', 'W', 'W', 'W'],
                     ['W', ' ', ' ', ' ', ' ', ' ', 'W'],
                     ['W', ' ', 'W', 'W', 'W', ' ', 'W'],
                     ['W', ' ', 'W', ' ', 'W', ' ', 'W'],
                     ['W', ' ', 'W', ' ', ' ', ' ', 'W'],
                     ['W', ' ', 'W', 'W', 'W', 'W', 'W'],
                     ['W', ' ', ' ', ' ', ' ', ' ', 'W'],
                     ['W', 'W', 'W', 'W', 'W', 'D', 'W']]
        self.door = connection
        self.startRow = 6
        self.startColumn = 5
        self.connectedRow = row
        self.connectedColumn = column
        self.chests = random.randrange(1, 5, 1)
        self.tables = random.randrange(0, 5, 1)
        self.enemies = random.randrange(1, 16, 1)
        if self.tables + self.chests > 4:
            self.tables -= self.chests
        elif self.tables + self.chests < 4:
            self.room[3][3] = 's'
            self.shop = Shop()
        if self.tables + self.chests - 1 + self.enemies > 11:
            self.enemies -= self.tables + self.chests - 1
        while self.chests >= 1:
            if self.room[3][3] == ' ':
                self.room[3][3] = 'C'
            elif self.room[4][5] == ' ':
                self.room[4][5] = 'C'
            elif self.room[1][5] == ' ':
                self.room[1][5] = 'C'
            elif self.room[1][1] == ' ':
                self.room[1][1] = 'C'
            self.chests -= 1
        while self.tables >= 1:
            if self.room[3][3] == ' ':
                self.room[3][3] = 'T'
            elif self.room[4][5] == ' ':
                self.room[4][5] = 'T'
            elif self.room[1][5] == ' ':
                self.room[1][5] = 'T'
            elif self.room[1][1] == ' ':
                self.room[1][1] = 'T'
            self.tables -= 1
        while self.enemies >= 1:
            if self.room[4][3] == ' ':
                self.room[4][3] = 'g'
                activeCharacters.append(choose_enemies(self, 4, 3))
            elif self.room[4][4] == ' ':
                self.room[4][4] = 'g'
                activeCharacters.append(choose_enemies(self, 4, 4))
            elif self.room[4][5] == ' ':
                self.room[4][5] = 'g'
                activeCharacters.append(choose_enemies(self, 4, 5))
            elif self.room[3][5] == ' ':
                self.room[3][5] = 'g'
                activeCharacters.append(choose_enemies(self, 3, 5))
            elif self.room[2][5] == ' ':
                self.room[2][5] = 'g'
                activeCharacters.append(choose_enemies(self, 2, 5))
            elif self.room[1][5] == ' ':
                self.room[1][5] = 'g'
                activeCharacters.append(choose_enemies(self, 1, 5))
            elif self.room[1][4] == ' ':
                self.room[1][4] = 'g'
                activeCharacters.append(choose_enemies(self, 1, 4))
            elif self.room[1][3] == ' ':
                self.room[1][3] = 'g'
                activeCharacters.append(choose_enemies(self, 1, 3))
            elif self.room[1][2] == ' ':
                self.room[1][2] = 'g'
                activeCharacters.append(choose_enemies(self, 1, 2))
            elif self.room[1][1] == ' ':
                self.room[1][1] = 'g'
                activeCharacters.append(choose_enemies(self, 1, 1))
            elif self.room[2][1] == ' ':
                self.room[2][1] = 'g'
                activeCharacters.append(choose_enemies(self, 2, 1))
            elif self.room[3][1] == ' ':
                self.room[3][1] = 'g'
                activeCharacters.append(choose_enemies(self, 3, 1))
            elif self.room[4][1] == ' ':
                self.room[4][1] = 'g'
                activeCharacters.append(choose_enemies(self, 4, 1))
            elif self.room[5][1] == ' ':
                self.room[5][1] = 'g'
                activeCharacters.append(choose_enemies(self, 5, 1))
            elif self.room[6][1] == ' ':
                self.room[6][1] = 'g'
                activeCharacters.append(choose_enemies(self, 6, 1))
            self.enemies -= 1

    def leave(self, mover, symbol):
        try:
            self.room[mover.current_row - 1][mover.current_column] = " "
            mover.currentRoom = self.door
            mover.current_row = self.connectedRow
            mover.current_column = self.connectedColumn
            mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
        except:
            f = open("error_report.txt", "a")
            print("An error occurred when leaving.")
            traceback.print_exc(None, f)
            f.close()


class LeftSmallSpiral:
    def __init__(self, connection, row, column):
        self.room = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                     ['W', ' ', ' ', ' ', ' ', ' ', ' ', 'W'],
                     ['W', ' ', 'W', 'W', 'W', 'W', ' ', 'W'],
                     ['W', ' ', 'W', ' ', ' ', 'W', ' ', 'W'],
                     ['W', ' ', 'W', ' ', 'W', 'W', ' ', 'W'],
                     ['D', ' ', 'W', ' ', ' ', ' ', ' ', 'W'],
                     ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]
        self.door = connection
        self.startRow = 5
        self.startColumn = 1
        self.connectedRow = row
        self.connectedColumn = column
        self.chests = random.randrange(1, 5, 1)
        self.tables = random.randrange(0, 5, 1)
        self.enemies = random.randrange(1, 16, 1)
        if self.tables + self.chests > 4:
            self.tables -= self.chests
        elif self.tables + self.chests < 4:
            self.room[3][4] = 's'
            self.shop = Shop()
        if self.tables + self.chests - 1 + self.enemies > 11:
            self.enemies -= self.tables + self.chests - 1
        while self.chests >= 1:
            if self.room[3][4] == ' ':
                self.room[3][4] = 'C'
            elif self.room[5][3] == ' ':
                self.room[5][3] = 'C'
            elif self.room[5][6] == ' ':
                self.room[5][6] = 'C'
            elif self.room[1][6] == ' ':
                self.room[1][6] = 'C'
            self.chests -= 1
        while self.tables >= 1:
            if self.room[3][4] == ' ':
                self.room[3][4] = 'T'
            elif self.room[5][3] == ' ':
                self.room[5][3] = 'T'
            elif self.room[5][6] == ' ':
                self.room[5][6] = 'T'
            elif self.room[1][6] == ' ':
                self.room[1][6] = 'T'
            self.tables -= 1
        while self.enemies >= 1:
            if self.room[3][3] == ' ':
                self.room[3][3] = 'g'
                activeCharacters.append(choose_enemies(self, 3, 3))
            elif self.room[4][3] == ' ':
                self.room[4][3] = 'g'
                activeCharacters.append(choose_enemies(self, 4, 3))
            elif self.room[5][3] == ' ':
                self.room[5][3] = 'g'
                activeCharacters.append(choose_enemies(self, 5, 3))
            elif self.room[5][4] == ' ':
                self.room[5][4] = 'g'
                activeCharacters.append(choose_enemies(self, 5, 4))
            elif self.room[5][5] == ' ':
                self.room[5][5] = 'g'
                activeCharacters.append(choose_enemies(self, 5, 5))
            elif self.room[5][6] == ' ':
                self.room[5][6] = 'g'
                activeCharacters.append(choose_enemies(self, 5, 6))
            elif self.room[4][6] == ' ':
                self.room[4][6] = 'g'
                activeCharacters.append(choose_enemies(self, 4, 6))
            elif self.room[3][6] == ' ':
                self.room[3][6] = 'g'
                activeCharacters.append(choose_enemies(self, 3, 6))
            elif self.room[2][6] == ' ':
                self.room[2][6] = 'g'
                activeCharacters.append(choose_enemies(self, 2, 6))
            elif self.room[1][6] == ' ':
                self.room[1][6] = 'g'
                activeCharacters.append(choose_enemies(self, 1, 6))
            elif self.room[1][5] == ' ':
                self.room[1][5] = 'g'
                activeCharacters.append(choose_enemies(self, 1, 5))
            elif self.room[1][4] == ' ':
                self.room[1][4] = 'g'
                activeCharacters.append(choose_enemies(self, 1, 4))
            elif self.room[1][3] == ' ':
                self.room[1][3] = 'g'
                activeCharacters.append(choose_enemies(self, 1, 3))
            elif self.room[1][2] == ' ':
                self.room[1][2] = 'g'
                activeCharacters.append(choose_enemies(self, 1, 2))
            elif self.room[1][1] == ' ':
                self.room[1][1] = 'g'
                activeCharacters.append(choose_enemies(self, 1, 1))
            self.enemies -= 1

    def leave(self, mover, symbol):
        try:
            self.room[mover.current_row][mover.current_column + 1] = " "
            mover.currentRoom = self.door
            mover.current_row = self.connectedRow
            mover.current_column = self.connectedColumn
            mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
        except:
            f = open("error_report.txt", "a")
            print("An error occurred when leaving.")
            traceback.print_exc(None, f)
            f.close()


class RightSmallSpiral:
    def __init__(self, connection, row, column):
        self.room = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                     ['W', ' ', ' ', ' ', ' ', 'W', ' ', 'D'],
                     ['W', ' ', 'W', 'W', ' ', 'W', ' ', 'W'],
                     ['W', ' ', 'W', ' ', ' ', 'W', ' ', 'W'],
                     ['W', ' ', 'W', 'W', 'W', 'W', ' ', 'W'],
                     ['W', ' ', ' ', ' ', ' ', ' ', ' ', 'W'],
                     ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]
        self.door = connection
        self.startRow = 1
        self.startColumn = 6
        self.connectedRow = row
        self.connectedColumn = column
        self.chests = random.randrange(1, 5, 1)
        self.tables = random.randrange(0, 5, 1)
        self.enemies = random.randrange(1, 16, 1)
        if self.tables + self.chests > 4:
            self.tables -= self.chests
        elif self.tables + self.chests < 4:
            self.room[3][3] = 's'
            self.shop = Shop()
        if self.tables + self.chests - 1 + self.enemies > 11:
            self.enemies -= self.tables + self.chests - 1
        while self.chests >= 1:
            if self.room[3][3] == ' ':
                self.room[3][3] = 'C'
            elif self.room[1][4] == ' ':
                self.room[1][4] = 'C'
            elif self.room[1][1] == ' ':
                self.room[1][1] = 'C'
            elif self.room[5][1] == ' ':
                self.room[5][1] = 'C'
            self.chests -= 1
        while self.tables >= 1:
            if self.room[3][3] == ' ':
                self.room[3][3] = 'T'
            elif self.room[1][4] == ' ':
                self.room[1][4] = 'T'
            elif self.room[1][1] == ' ':
                self.room[1][1] = 'T'
            elif self.room[5][1] == ' ':
                self.room[5][1] = 'T'
            self.tables -= 1
        while self.enemies >= 1:
            if self.room[3][4] == ' ':
                self.room[3][4] = 'g'
                activeCharacters.append(choose_enemies(self, 3, 4))
            elif self.room[2][4] == ' ':
                self.room[2][4] = 'g'
                activeCharacters.append(choose_enemies(self, 2, 4))
            elif self.room[1][4] == ' ':
                self.room[1][4] = 'g'
                activeCharacters.append(choose_enemies(self, 1, 4))
            elif self.room[1][3] == ' ':
                self.room[1][3] = 'g'
                activeCharacters.append(choose_enemies(self, 1, 3))
            elif self.room[1][2] == ' ':
                self.room[1][2] = 'g'
                activeCharacters.append(choose_enemies(self, 1, 2))
            elif self.room[1][1] == ' ':
                self.room[1][1] = 'g'
                activeCharacters.append(choose_enemies(self, 1, 1))
            elif self.room[2][1] == ' ':
                self.room[2][1] = 'g'
                activeCharacters.append(choose_enemies(self, 2, 1))
            elif self.room[3][1] == ' ':
                self.room[3][1] = 'g'
                activeCharacters.append(choose_enemies(self, 3, 1))
            elif self.room[4][1] == ' ':
                self.room[4][1] = 'g'
                activeCharacters.append(choose_enemies(self, 4, 1))
            elif self.room[5][1] == ' ':
                self.room[5][1] = 'g'
                activeCharacters.append(choose_enemies(self, 5, 1))
            elif self.room[5][2] == ' ':
                self.room[5][2] = 'g'
                activeCharacters.append(choose_enemies(self, 5, 2))
            elif self.room[5][3] == ' ':
                self.room[5][3] = 'g'
                activeCharacters.append(choose_enemies(self, 5, 3))
            elif self.room[5][4] == ' ':
                self.room[5][4] = 'g'
                activeCharacters.append(choose_enemies(self, 5, 4))
            elif self.room[5][5] == ' ':
                self.room[5][5] = 'g'
                activeCharacters.append(choose_enemies(self, 5, 5))
            elif self.room[5][6] == ' ':
                self.room[5][6] = 'g'
                activeCharacters.append(choose_enemies(self, 5, 6))
            self.enemies -= 1

    def leave(self, mover, symbol):
        try:
            self.room[mover.current_row][mover.current_column - 1] = " "
            mover.currentRoom = self.door
            mover.current_row = self.connectedRow
            mover.current_column = self.connectedColumn
            mover.currentRoom.room[mover.current_row][mover.current_column] = symbol
        except:
            f = open("error_report.txt", "a")
            print("An error occurred when leaving.")
            traceback.print_exc(None, f)
            f.close()
