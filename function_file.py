
from class_file import Statistics

# Organize data based on the year
def filter_by_year(data: [Statistics], year: int) -> [Statistics]:
    result = []
    for statistics in data:
        if statistics.year == year:
            result.append(statistics)


# To add all the data of energy based on the year/years described
def energy_total (total:[Statistics],year:int) -> [Statistics]:
    total = 0
    for statistics in total:
        total += statistics.energy
    return total

def water_total (total:[Statistics],year:int) -> [Statistics]:
    total = 0
    for statistics in total:
        total += statistics.water
    return total



def waste_is_decreasing(year1: list[Statistics.year], year2=list[Statistics], key: int, value:str) -> bool:
    result = ''
    year1 = Statistics.year1
    year2 = Statistics.year
    if year1 < year2:
        year1 == year1
        year2 == year2
    else:
        year1 == year2
        year2 == year1

    for year in range(year1, year2):
        if year1 > year2:
            result['Cal Poly has decreased waste management since ', [year1]].append(key)
        else:
            result['Cal Poly needs to have more effort for waste management.'].append(key)

    return result






#total reneawable source of electricity
#if idx 1 is true

