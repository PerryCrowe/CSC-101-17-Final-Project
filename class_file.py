
class Statistics:
    # Initializing a new Statistics object
    # input: Cal Poly's water usage data as a dictionary
    # input: Cal Poly's energy usage data as a dictionary
    # input: Cal Poly's transportation data as a dictionary
    # input: Cal Poly's waste data as a dictionary
    # input: Cal Poly's sustainability data year as an integer

    def __init__(self,
                 year: int,
                 water:dict[str,float],
                 energy:dict[str, float],
                 transportation:dict[str,float],
                 waste:float):
        self.year = year
        self.water = water
        self.energy = energy
        self.transportation = transportation
        self.waste = waste

    def __repr__(self):
        return 'Statistics({},{},{},{},{})'.format(
            self.year,
            self.water,
            self.energy,
            self.transportation,
            self.waste
        )
