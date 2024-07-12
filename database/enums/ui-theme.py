#!/usr/bin/env python
# coding: utf-8

# In[1]:


from enum import Enum

from database import utils

def get_ui_theme_enum(base_url: str) -> Enum:
    """
    Given a base URL, this function retrieves the text of the "ui-theme.ts" file
    from the PokeRogue repository. It then extracts the names of the abilities
    from this file and creates an Enum object with these names.

    Args:
        base_url (str): The base URL of the PokeRogue repository.

    Returns:
        Enum: An Enum object representing the ui-themes of the game.
    """
    # Construct the URL for the ui-theme file
    url = f'{base_url}/src/enums/ui-theme.ts'

    # Retrieve the text of the ui themes file
    ui_theme = utils.get_response_text(url)

    # Extract the names of the ui themes from the text
    ui_theme_list = [i.strip() for i in ui_theme.split('\n') if "{" not in i and "}" not in i and i != ""]

    # Create an Enum object with the extracted names
    enum_list = [i.replace(",", "") for i in ui_theme_list]
    ui_theme = Enum('Ui Theme', enum_list)

    # Return the Enum object representing the abilities
    return ui_theme

if __name__ == "__main__":
    repo = 'pagefaultgames/pokerogue/main'
    base = f'https://raw.githubusercontent.com/{repo}'
    Ui_theme = get_ui_theme_enum(base)
    print([e.name for e in Ui_theme])
    print([e.value for e in Ui_theme])


# In[ ]:




