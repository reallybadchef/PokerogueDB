#!/usr/bin/env python
# coding: utf-8

# In[3]:


from enum import Enum

from database.enums import utils

def get_trainer_types_enum(base_url: str) -> Enum:
    """
    Given a base URL, this function retrieves the text of the "trainer-types.ts" file
    from the PokeRogue repository. It then extracts the names of the abilities
    from this file and creates an Enum object with these names.

    Args:
        base_url (str): The base URL of the PokeRogue repository.

    Returns:
        Enum: An Enum object representing the trainer types in the game.
    """
    # Construct the URL for the trainer types file
    url = f'{base_url}/src/enums/trainer-type.ts'

    # Retrieve the text of the trainer types file
    trainer_types = utils.get_response_text(url)

    # Extract the names of the trainer types from the text
    trainer_types_list = [i.strip() for i in trainer_types.split('\n') if "{" not in i and "}" not in i and i != ""]

    # Create an Enum object with the extracted names
    enum_list = [i.replace(",", "") for i in trainer_types_list]
    trainer_type = Enum('Trainer type', enum_list)

    # Return the Enum object representing the trainer types
    return trainer_type

if __name__ == "__main__":
    repo = 'pagefaultgames/pokerogue/main'
    base = f'https://raw.githubusercontent.com/{repo}'
    trainer_type = get_trainer_types_enum(base)
    print([e.name for e in trainer_type])
    print([e.value for e in trainer_type])


# In[ ]:




