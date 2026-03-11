# Author: Gianella Gazzano

from dataset import reports_by_year
from function_file import is_increasing


def gather_data ():
    print("Would you like to compare two reports or look at one report?")
    ans = input("Please input 'One' or 'Two': ")

# One Comparison
    if ans.lower() == "one":
        year = int(input("Enter Desired Year: "))
        report = reports_by_year[year]
        category = input("Enter category (energy, transportation, water, waste): ")


    # Energy Category
        if category.lower () == "energy":
            print("BTUs per Square Foot, Sources of Electricity, or % of Campus Vehicle Fleet Using Alternative Fuel?")
            answer = input("")
            answer = answer.lower().strip()

            if answer.lower() == "btus per square foot":
                print(report.energy["BTUs per Square Foot"])
            elif answer.lower() == "% of campus vehicle fleet using alternative fuel":
                print(report.energy["% of Campus Vehicle Fleet Using Alternative Fuel"])
            #Sources of Electricity
            elif answer.lower() == "sources of electricity":
                sources = report.energy.get("Sources of Electricity")
                if sources is None:
                    print("2014 does not have data for sources of electricity.")
                    return
                print ("Renewable, Large Hydro, Nuclear, Natural Gas, Coal, or Unspecified?")
                sub = input("")
            if sub in sources:
                print(sources[sub])

    # Transportation Category
        if category.lower() == "transportation":
            print ("Parking Permits per Student, % of Student Population Living on Campus, or CP SLO Transit Riders per Year?")
            answer = input("")
            answer = answer.lower().strip()

            if answer.lower() == "parking permits per student":
                print(report.transportation["Parking Permits per Student"])
            elif answer.lower() == "% of student population living on campus":
                print(report.transportation["% of Student Population Living on Campus"])
            elif answer.lower() == "cp slo transit riders per year":
                print(report.transportation["CP SLO Transit Riders per Year"])

    # Water Category
        if category.lower() == "water":
            print ("Domestic Water Use, Total Delivered Water, or Total Indoor Water Use?")
            answer = input("")
            answer = answer.lower().strip()

            if answer.lower() == "domestic water use":
                print( report.water["Domestic Water Use"])
            elif answer.lower() == "total delivered water":
                print( report.water["Total Delivered Water"])
            elif answer.lower() == "total indoor water use":
                print( report.water["Total Indoor Water Use"])

    # Waste Category
        if category.lower() == "waste":
            print(report.waste)


# Two Comparison Years
    if ans.lower() == "two":
        year1 = int(input("Enter First Desired Year: "))
        year2 = int(input("Enter Second Desired Year: "))
        report1 = reports_by_year[year1]
        report2 = reports_by_year[year2]
        category = input("Enter category (energy, transportation, water, waste): ")

    #Energy Category
        if category.lower () == "energy":
            print("BTUs per Square Foot, Sources of Electricity, or % of Campus Vehicle Fleet Using Alternative Fuel? ")
            answer = input("")
            answer = answer.lower().strip()

            if answer.lower() == "btus per square foot":
                result = is_increasing(report1, report2, "energy", "BTUs per Square Foot",None)
            elif answer.lower() == "% of campus vehicle fleet using alternative fuel":
                result = is_increasing(report1, report2, "energy", "% of Campus Vehicle Fleet Using Alternative Fuel",None)
            elif answer.lower() == "sources of electricity":
                source1 = report1.energy.get("Sources of Electricity")
                source2 = report2.energy.get("Sources of Electricity")
                if source1 is None or source2 is None:
                    print("2014 does not have data for sources of electricity.")
                    return
                sub = input("Renewable, Large Hydro, Nuclear, Natural Gas, Coal, or Unspecified? ")
                result = is_increasing(report1, report2,"energy","Sources of Electricity", sub.title())

            if result is True:
                print("It increased.")
            if result is False:
                print("It did not increase.")

    #Transportation Category
        if category.lower() == "transportation":
            print ("Parking Permits per Student, % of Student Population Living on Campus, or CP SLO Transit Riders per Year?")
            answer = input("")
            answer = answer.lower().strip()

            if answer.lower() == "parking permits per student":
                result = is_increasing(report1, report2,"transportation","Parking Permits per Student",None)
            elif answer.lower() == "% of student population living on campus":
                result = is_increasing(report1, report2,"transportation","% of Student Population Living on Campus", None)
            elif answer.lower() == "cp slo transit riders per year":
                result = is_increasing(report1, report2,"transportation","CP SLO Transit Riders per Year",None)

            if result is True:
                print("It increased.")
            if result is False:
                print("It did not increase.")

    #Water Category
        if category.lower() == "water":
            print ("Domestic Water Use, Total Delivered Water, or Total Indoor Water Use?")
            answer = input("")
            answer = answer.lower().strip()

            if answer.lower() == "domestic water use":
                result = is_increasing(report1,report2,"water","Domestic Water Use",None)
            elif answer.lower() == "total delivered water":
                result = is_increasing(report1,report2,"water","Total Delivered Water",None)
            elif answer.lower() == "total indoor water":
                result = is_increasing(report1,report2,"water","Total Indoor Water Use",None)

            if result is True:
                print("It increased.")
            if result is False:
                print("It did not increase.")

        if category.lower() == "waste":
            result = is_increasing(report1,report2,"waste","Waste",None)

            if result is True:
                print("It increased.")
            if result is False:
                print("It did not increase.")


if __name__ == "__main__":
        gather_data()

    # except Exception as e:
    #     print(f"Critical error: {e}")
    #     exit()