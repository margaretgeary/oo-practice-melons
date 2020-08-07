############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    casaba = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    casaba.add_pairing('mint')
    casaba.add_pairing('strawberry')
    all_melon_types.append(casaba)
    
    crenshaw = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    crenshaw.add_pairing("proschuitto")
    all_melon_types.append(crenshaw)
    
    yellow_watermelon = MelonType("yw", 2013, "yellow", False, True, "Yellow Watermelon")
    yellow_watermelon.add_pairing("ice cream")
    all_melon_types.append(yellow_watermelon)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        for pairing in melon.pairings:
            print(f"{melon.name} pairs with {pairing}")


print_pairing_info(make_melon_types())

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}
    for melon in melon_types:
        melon_dict[melon.code] = melon.name
    print(melon_dict)

make_melon_type_lookup(make_melon_types())

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape, color, field, harvester):
        self.type = melon_type
        self.shape = shape
        self.color = color
        self.field = field
        self.harvester = harvester
    
    def is_sellable(self):
        if self.shape > 5 and self.field != 3:
            return True

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    
    # melon_by_id = make_melon_type_lookup(make_melon_types())

    # melon1 = Melon(melon_by_id['yw'], 8, 7, 2, 'Sheila')
    # melon2 = Melon(melon_by_id['yw'], 3, 4, 2, 'Sheila')
    # melon3 = Melon(melon_by_id['yw'], 9, 8, 3, 'Sheila')
    # melon4 = Melon(melon_by_id['cas'], 10, 6, 35, 'Sheila')
    # melon5 = Melon(melon_by_id['cren'], 8, 9, 35, 'Michael')
    # melon6 = Melon(melon_by_id['cren'], 8, 2, 35, 'Michael')
    # melon7 = Melon(melon_by_id['cren'], 2, 3, 4, 'Michael')
    # melon8 = Melon(melon_by_id['musk'], 6, 7, 4, 'Michael')
    # melon9 = Melon(melon_by_id['yw'], 7, 10, 3, 'Sheila')
    
    return [
    Melon('yw', 8, 7, 2, 'Sheila'), 
    Melon('yw', 3, 4, 2, 'Sheila'), 
    Melon('yw', 9, 8, 3, 'Sheila'), 
    Melon('cas', 10, 6, 35, 'Sheila'), 
    Melon('cren', 8, 9, 35, 'Michael'), 
    Melon('cren', 8, 2, 35, 'Michael'), 
    Melon('cren', 2, 3, 4, 'Michael'), 
    Melon('musk', 6, 7, 4, 'Michael'), 
    Melon('yw', 7, 10, 3, 'Sheila')
    ]

    

print(make_melons(make_melon_types()))
    

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



