counter = 0
characters = int(input("How many characters do you want to create? "))


def character_name(number):
    name_character = input("What's the characters name")
    return name_character


def health_score(sides):
    import random
    health_score = random.randint(1, sides)

    def strength(one, two):
        import random
        health_1 = random.randint(1, one)
        health_2 = random.randint(1, two)
        strength = health_1 * health_2
        return strength

    strength = strength(6, 8)
    return strength * health_score


while True:
    health = health_score(8)
    character = character_name(characters)
    print("Your character's health is", health)
    counter += 1
    if counter < characters:
        continue
    else:
        exit()
