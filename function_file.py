#Author: Perry

from class_file import Statistics
from pathlib import Path

# Changes:
    # Adjusted variable names in filter_by_year so that they didn't shadow (imitate too closely) the class name.
        # For the input notation, list[Statistics] makes it clear that you're inputting a List of Statistics.
            # I don't know if python likes it when you just do the brackets, even if it feels like a clear implication
        # Also changed it so that instead of returning a list, the function just returns the object outlining the
            # requested year. Since you're only calling the one year, you only need the one return!
def filter_by_year(data: list[Statistics], year: int) -> Statistics:
    for stat in data:
        if stat.year == year:
            return stat
    print("Year invalid. Please input 2008, 2010, 2012, 2014, 2016, or 2018.")
    return None

# Changes:
    # I adjusted the naming of the input variables and the internal variables so that the function could tell what we
        # were putting in and what it was supposed to be taking from it.
    # I also adjusted the reorganizing component; we don't technically need a whole other step if the years are in the
        # correct order, so I made it so that it does the correction only if necessary.
    # I adjusted key and value, too, so that they would be both strings. This lets us specify both the overall statistic
        # to compare and the value within.
    # I'm also swapping "key" and "value" with "domain" and "key" just because key is technically a term for dictionaries
        # but if you want to swap them back, feel free!
def is_increasing(set1: Statistics, set2: Statistics, domain: str, key: str, sub:None) -> bool:
    year1 = set1.year
    year2 = set2.year
    if year1 > year2:
        temp = set1
        set1 = set2
        set2 = temp
        temp = None
    if domain.lower() == "energy":
        if key.lower() == "btus per square foot":
            if set1.energy.get("BTUs per Square Foot") < set2.energy.get("BTUs per Square Foot"):
                return True
            else:
                return False

# All sources of Energy
        elif key.lower() == "sources of electricity":
            if (set1.energy.get("Sources of Electricity").get("Renewable") <
                    set2.energy.get("Sources of Electricity").get("Renewable")):
                return True
            else:
                return False
        elif key.lower() == "sources of electricity":
            if (set1.energy.get("Sources of Electricity").get("Large Hydro") <
                    set2.energy.get("Sources of Electricity").get("Large Hydro")):
                return True
            else:
                return False
        elif key.lower() == "sources of electricity":
            if (set1.energy.get("Sources of Electricity").get("Nuclear") <
                    set2.energy.get("Sources of Electricity").get("Nuclear")):
                return True
            else:
                return False
        elif key.lower() == "sources of electricity":
            if (set1.energy.get("Sources of Electricity").get("Natural Gas") <
                    set2.energy.get("Sources of Electricity").get("Natural Gas")):
                return True
            else:
                return False
        elif key.lower() == "sources of electricity":
            if (set1.energy.get("Sources of Electricity").get("Coal") <
                    set2.energy.get("Sources of Electricity").get("Coal")):
                return True
            else:
                return False
        elif key.lower() == "sources of electricity":
            if (set1.energy.get("Sources of Electricity").get("Unspecified") <
                    set2.energy.get("Sources of Electricity").get("Unspecified")):
                return True
            else:
                return False

        elif key.lower() == "% of campus vehicle fleet using alternative fuel":
            if (set1.energy.get("% of Campus Fleet Using Alternative Fuel") <
                set2.energy.get("% of Campus Fleet Using Alternative Fuel")):
                return True
            else:
                return False
        else:
            print("Invalid Key.")
            return None


    elif domain.lower() == "water":
        if key.lower() == "domestic water use":
            if set1.water.get("Domestic Water Use") < set2.water.get(
                    "Domestic Water Use"):
                return True
            else:
                return False
        elif key.lower() == "total delivered water":
            if (set1.water.get("Total Delivered Water") <
                    set2.water.get("Total Delivered Water")):
                return True
            else:
                return False
        elif key.lower() == "total indoor water use":
            if (set1.water.get("Total Indoor Water Use") <
                    set2.water.get("Total Indoor Water Use")):
                return True
            else:
                return False
        else:
            print("Invalid Key.")
            return None


    elif domain.lower() == "transportation":
            if key.lower() == "parking permits per student":
                if set1.transportation.get("Parking Permits per Student") < set2.transportation.get("Parking Permits per Student"):
                    return True
                else:
                    return False
            elif key.lower() == "% of student population living on campus":
                if (set1.transportation.get("% of Student Population Living on Campus") <
                        set2.transportation.get("% of Student Population Living on Campus")):
                    return True
                else:
                    return False
            elif key.lower() == "cp slo transit riders per year":
                if (set1.transportation.get("CP SLO Transit Riders per Year") <
                        set2.transportation.get("CP SLO Transit Riders per Year")):
                    return True
                else:
                    return False
            else:
                print("Invalid Key.")
                return None

    elif domain.lower() == "waste":
        if set1.waste < set2.waste:
            return False
        else:
            return True


def new_data() -> None:
    print("Please confirm the file you want the data to be written to is in the same directory as this file."+
          "\nA new file will be generated if one is not present.")
    ans = input("Y/N:")
    if ans.lower() == 'n':
        open("data.txt","x")
        f = open("data.txt","w")
        data = []
    elif ans.lower() == 'y':
        ans = input("Please input the file name. (Case sensitive): ")
        f = open(ans,"a")
        data = ["\n"]
    else:
        print("I can't read that. Terminating process.")
        return None
    data_list = ['year','energy','btus','sources_of_electricity','renewable','large_hydro','nuclear','natural_gas',
                 'coal','unspecified','percent_vehicle_fleet_using_alternate_fuel','transportation',
                 'parking_permits/student','percent_students_living_on-campus','cp_slo_transit_yearly_ridership',
                 'water','domestic','total','indoor','waste']
    prompt_list = ['What year is this dataset for?','[ENERGY] How many BTUs per Square Foot are used?',
                   '[ENERGY] What percentage of campus electricity is sourced from: Renewable?',
                   '[ENERGY] What percentage of campus electricity is sourced from: Large Hydro?',
                   '[ENERGY] What percentage of campus electricity is sourced from: Nuclear?',
                   '[ENERGY] What percentage of campus electricity is sourced from: Natural Gas?',
                   '[ENERGY] What percentage of campus electricity is sourced from: Coal?',
                   '[ENERGY] What percentage of campus electricity is sourced from: Unspecified?',
                   '[ENERGY] How much of the campus vehicle fleet uses alternative fuel? (Percent)',
                   '[TRANSPORT.] What is the number of parking permits per student?',
                   '[TRANSPORT.] What percent of the student population lives on-campus?',
                   '[TRANSPORT.] What was the ridership count for CP SLO Transit?',
                   '[WATER] What was the DOMESTIC (Residential, Sports Buildings, Treated Landscaping, Processes) ' +
                   'water usage in acre-ft?',
                   '[WATER] What was the TOTAL delivered water in acre-ft?',
                   '[WATER] What was the INDOOR water use in acre-ft?',
                   '[WASTE] What was the percentage of solid waste diverted from landfills?']
    loop = "y"
    while loop == "y":
        n_prompt = 0
        for n_data in range(len(data_list)):
            if (data_list[n_data] == 'energy' or data_list[n_data] =='sources of electricity' or
                data_list[n_data] == 'transportation' or data_list[n_data] == 'water'):
                data.append(data_list[n_data])
            else:
                data.append(data_list[n_data]+" "+input(prompt_list[n_prompt]+" "))
                n_prompt += 1
        loop = input("Would you like to input another year? Y/N ").lower()
        if loop.lower() == 'y':
            data.append("")
    print(data)
    finaldata = '\n'.join(data)
    f.write(finaldata)
    f.close()
    return None


def read_data() -> dict[int,Statistics]:
    file = input("Please input the name of the file containing the statistics. (Case sensitive): ")
    with open(file) as f:
        data = f.readlines()
    data = [line.replace('\n','') for line in data]
    data = [line.split(' ') for line in data]
    reports_by_year = {}
    for line in range(len(data)):
        if 'year' in data[line]:
            report = Statistics(year =  int(data[line][1]),
                                energy = {"BTUs per Square Foot":int(data[line+2][1]),
                                          "Sources of Electricity":{"Renewable":float(data[line+4][1]),
                                                                    "Large Hydro":float(data[line+5][1]),
                                                                    "Nuclear":float(data[line+6][1]),
                                                                    "Natural Gas":float(data[line+7][1]),
                                                                    "Coal":float(data[line+8][1]),
                                                                    "Unspecified":float(data[line+9][1])},
                                          "% of Campus Vehicle Fleet Using Alternative Fuel":float(data[line+10][1])},
                                transportation = {"Parking Permits per Student":float(data[line+12][1]),
                                                  "% of Student Population Living on Campus":float(data[line+13][1]),
                                                  "CP SLO Transit Riders per Year":int(data[line+14][1])},
                                water = {"Domestic Water Use":int(data[line+16][1]),
                                         "Total Delivered Water":int(data[line+17][1]),
                                         "Total Indoor Water Use":int(data[line+18][1])},
                                waste = float(data[line+19][1]))
            reports_by_year[int(data[line][1])] = report
    return reports_by_year

