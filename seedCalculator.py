def seed_calculator(fountain_side, grass_width):
    '''
    Calculate number of kilograms of grass seed needed for a border around a square fountain.

        Parameters:
            fountain_side (num): length of 1 side of fountain in meters
            grass_width (num): width of grass border in meters

        Returns:
            seed (float): amount of seed (kg) needed for grass border
    '''
    # Area of fountains
    fountain_area = fountain_side**2

    # Total area
    total_area = (fountain_side + 2 * grass_width) **2

    # Area of grass border
    grass_area = total_area - fountain_area

    # Amount of seed nedded (35 g/sq.m)
    seed = grass_area * 35

    # Covert to kg
    seed = seed / 1000

    return seed

result = seed_calculator(12, 2)
print(result)
