#!/usr/bin/env python
# coding: utf-8

# In[5]:


from enum import Enum

from database import utils

def get_variant_tier_enum(base_url: str) -> Enum:
    """
    Given a base URL, this function retrieves the text of the "variant-tier.ts" file
    from the PokeRogue repository. It then extracts the names of the abilities
    from this file and creates an Enum object with these names.

    Args:
        base_url (str): The base URL of the PokeRogue repository.

    Returns:
        Enum: An Enum object representing the variant_tier of the game.
    """
    # Construct the URL for the variant tier file
    url = f'{base_url}/src/enums/variant-tier.ts'

    # Retrieve the text of the variant tier file
    variant_tier = utils.get_response_text(url)

    # Extract the names of the variant tier from the text
    variant_tier_list = [i.strip() for i in variant_tier.split('\n') if "{" not in i and "}" not in i and i != ""]

    # Create an Enum object with the extracted names
    enum_list = [i.replace(",", "") for i in variant_tier_list]
    Variant_tier = Enum('Variant tier', enum_list)

    # Return the Enum object representing the variant tier
    return Variant_tier

if __name__ == "__main__":
    repo = 'pagefaultgames/pokerogue/main'
    base = f'https://raw.githubusercontent.com/{repo}'
    variant_tier = get_variant_tier_enum(base)
    print([e.name for e in variant_tier])
    print([e.value for e in variant_tier])


# In[ ]:




