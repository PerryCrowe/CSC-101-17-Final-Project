import dataset
from dataset import reports_by_year
import sys

def gather_data ():
    user_input = []
    print("Would you like to compare two reports or look at one report?")
    ans = input("Please input 'One' or 'Two'")

    year = int(input("Enter Desired Year:"))
    report = reports_by_year[year]
    category = input("Enter category (energy, transportation, water, waste):")
    answer = input("")

    if category.lower () == "energy":
        print("BTUs per Square Foot, Sources of Electricity, or % of Campus Vehicle Fleet Using Alternative Fuel?")

        if answer == "BTUs per Square Foot":
            print(report.energy["BTUs per Square Foot"])
        elif answer == "% of Campus Vehicle Fleet Using Alternative Fuel":
            print(report.energy["% of Campus Vehicle Fleet Using Alternative Fuel"])
        elif answer == "Sources of Electricity":
            print ("Renewable, Large Hydro, Nuclear, Natural Gas, Coal, or Unspecified?")
            sub = input("")
            sources = report.energy["Sources of Electricity"]
            if sub in sources:
                print(sources[sub])


    if category.lower == "Transportation":
        print ("Parking Permits per Student, % of Student Population Living on Campus, or CP SLO Transit Riders per Year?")

        if answer == "Parking Permits per Student":
            print( report.transportation["Parking Permits per Student"])
        if answer == "% of Student Population Living on Campus":
            print(report.transportation["% of Student Population Living on Campus"])
        elif answer == "CP SLO Transit Riders per Year":
            print(report.transportation["CP SLO Transit Riders per Year"])

    if answer == "Water":
        print ("Domestic Water Use, Total Delivered Water, or Total Indoor Water Use?")
        if answer == "Domestic Water Use":
            print( report.water["Domestic Water Use"])
        if answer == "Total Delivered Water":
            print( report.water["Total Delivered Water"])
        if answer == "Total Indoor Water":
            print( report.water["total indoor Water"])

    if answer == "Waste":
        print( report.waste)






if __name__ == "__main__":
    user_input = gather_data()
    print(user_input)





  #  elif ans.lower() == 'two':
   #     user_input.append(input("Enter Desired Year:"))
    #    user_input.append(input("Enter Desired Year:"))
     #   user_input.append(input("Enter Statistic from list:"))

 #   return user_input

#print(gather_data())

#if __name__ == "__main__":
 #   user_input = gather_data()
  #  print(user_input)