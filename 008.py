def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"

    if not (isinstance(strength, int) and isinstance(intelligence, int) and isinstance(charisma, int)):
        return "All stats should be integers"

    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"

    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"

    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points"

    str_dots = "●" * strength + "○" * (10 - strength)
    int_dots = "●" * intelligence + "○" * (10 - intelligence)
    cha_dots = "●" * charisma + "○" * (10 - charisma)

    return f"{name}\nSTR {str_dots}\nINT {int_dots}\nCHA {cha_dots}"