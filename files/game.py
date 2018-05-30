class Weapon:
    def __init__(self):
        raise NotImplementedError("Dop not create raw Weapon objects.")

    def __str__(self):
        return self.name


class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A fist sized rock, suitable fro bludgeoning."
        self.damage = 5


class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small dagger with some rust. " \
                           "Somewhat more dangerous than a rock."
        self.damage = 10


class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty Sword"
        self.description = "This sword is showing its age," \
                           " but still has some fight in it. "
        self.damage = 20


class Mazeltov(Weapon):
    def __init__(self):
        self.name = "MazelTov"
        self.description = "A Mazeltov to burn your enemies."
        self.damage = 100


class Crossbow(Weapon):
    def __init__(self):
        self.name = "Crossbow"
        self.description = "A crossbow to put holes into enemies."
        self.damage = 70


def play():
    inventory = [Rock(), Dagger(), "Gold(5)", "Crusty Bread"]
    print("Escape from Cave Terror!")
    while True:
        action_input = get_player_command()
        if action_input in ["n", "N"]:
            print("Go North!")
        elif action_input in ["s", "S"]:
            print("Go South!")
        elif action_input in ["e", "E"]:
            print("Go East!")
        elif action_input in ["w", "W"]:
            print("Go West!")
        elif action_input in ["i", "I"]:
            print("Inventory:")
            for item in inventory:
                print("*" + str(item))

        else:
            print("Invalid Action!")


def get_player_command():
    return input("Action: ")

def most_powerfull_weapon(inventory):
    max_damage = 0
    best_weapon = None

    for item in inventory:
        try:
            if item.damage > max_damage:
                best_weapon = item
                max_damage = item.damage
        except AttributeError:
            pass

    return best_weapon


play()
