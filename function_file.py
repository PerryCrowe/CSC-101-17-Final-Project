#Author: Perry

from class_file import Statistics

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



# --- to add: "def new_data( )"? Would be a very long input, unless we tailored the prompt... ---
def new_data():
    print("Please confirm the file you want the data to be written to is in the same directory as this file.")
    ans = input("Y/N:")
    if ans.lower() == 'n':
        f = open("data.txt","w")
    elif ans.lower() == 'y':
        ans = input("Please input the file name. (Case sensitive): ")
        f = open(ans,"a")
    else:
        print("I can't read that.")
