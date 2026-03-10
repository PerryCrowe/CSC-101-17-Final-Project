from dataset import reports_by_year

def gather_data ():
    print("Would you like to compare two reports or look at one report?")
    ans = input("Please input 'One' or 'Two': ")

    year = int(input("Enter Desired Year: "))
    report = reports_by_year[year]
    category = input("Enter category (energy, transportation, water, waste): ")


    if category.lower () == "energy":
        print("BTUs per Square Foot, Sources of Electricity, or % of Campus Vehicle Fleet Using Alternative Fuel?")
        answer = input("")

        if answer.lower() == "btus per square foot":
            print(report.energy["BTUs per Square Foot"])
        elif answer.lower() == "% of campus vehicle fleet using alternative fuel":
            print(report.energy["% of Campus Vehicle Fleet Using Alternative Fuel"])
        elif answer.lower() == "sources of electricity":
            print ("Renewable, Large Hydro, Nuclear, Natural Gas, Coal, or Unspecified?")
            sub = input("")
            sources = report.energy["Sources of Electricity (print exactly):"]
            if sub in sources:
                print(sources[sub])


    if category.lower() == "transportation":
        print ("Parking Permits per Student, % of Student Population Living on Campus, or CP SLO Transit Riders per Year?")
        answer = input("")

        if answer.lower() == "parking permits per student":
            print(report.transportation["Parking Permits per Student"])
        elif answer.lower() == "% of student population living on campus":
            print(report.transportation["% of Student Population Living on Campus"])
        elif answer.lower() == "cp slo transit riders per year":
            print(report.transportation["CP SLO Transit Riders per Year"])


    if category.lower() == "water":
        print ("Domestic Water Use, Total Delivered Water, or Total Indoor Water Use?")
        answer = input("")

        if answer.lower() == "domestic water use":
            print( report.water["Domestic Water Use"])
        elif answer.lower() == "total delivered water":
            print( report.water["Total Delivered Water"])
        elif answer.lower() == "total indoor water":
            print( report.water["total indoor Water"])


    if category.lower() == "waste":
        print(report.waste)

if __name__ == "__main__":
    gather_data()





  #  elif ans.lower() == 'two':
   #     user_input.append(input("Enter Desired Year:"))
    #    user_input.append(input("Enter Desired Year:"))
     #   user_input.append(input("Enter Statistic from list:"))

 #   return user_input

#print(gather_data())

#if __name__ == "__main__":
 #   user_input = gather_data()
  #  print(user_input)