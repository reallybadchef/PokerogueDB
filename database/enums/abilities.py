from enum import Enum

from database.enums import utils

def get_ability_enum(base_url: str) -> Enum:
    """
    Given a base URL, this function retrieves the text of the "abilities.ts" file
    from the PokeRogue repository. It then extracts the names of the abilities
    from this file and creates an Enum object with these names.

    Args:
        base_url (str): The base URL of the PokeRogue repository.

    Returns:
        Enum: An Enum object representing the abilities of the game.
    """
    # Construct the URL for the abilities file
    url = f'{base_url}/src/enums/abilities.ts'

    # Retrieve the text of the abilities file
    abilities = utils.get_response_text(url)

    # Extract the names of the abilities from the text
    abilities_list = [i.strip() for i in abilities.split('\n') if "{" not in i and "}" not in i and i != ""]

    # Create an Enum object with the extracted names
    enum_list = [i.replace(",", "") for i in abilities_list]
    Ability = Enum('Ability', enum_list)

    # Return the Enum object representing the abilities
    return Ability
