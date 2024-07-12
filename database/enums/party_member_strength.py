#!/usr/bin/env python
# coding: utf-8

# In[4]:


from enum import Enum

from database import utils

def get_partymemberstrength_enum(base_url: str) -> Enum:
    """
    Given a base URL, this function retrieves the text of the "party-member-strengths.ts" file
    from the PokeRogue repository. It then extracts the names of the abilities
    from this file and creates an Enum object with these names.

    Args:
        base_url (str): The base URL of the PokeRogue repository.

    Returns:
        Enum: An Enum object representing the party member strength of the game.
    """
    # Construct the URL for the party member strength file
    url = f'{base_url}/src/enums/party-member-strength.ts'

    # Retrieve the text of the party member strength file
    party_member_strength = utils.get_response_text(url)

    # Extract the names of the party member strengths from the text
    party_member_strength_list = [i.strip() for i in party_member_strength.split('\n') if "{" not in i and "}" not in i and i != ""]

    # Create an Enum object with the extracted names
    enum_list = [i.replace(",", "") for i in party_member_strength_list]
    Party_Member_Strength = Enum('Party Member Strength', enum_list)

    # Return the Enum object representing the abilities
    return Party_Member_Strength

if __name__ == "__main__":
    repo = 'pagefaultgames/pokerogue/main'
    base = f'https://raw.githubusercontent.com/{repo}'
    PartyMemberStrength = get_partymemberstrength_enum(base)
    print([e.name for e in PartyMemberStrength])
    print([e.value for e in PartyMemberStrength])

