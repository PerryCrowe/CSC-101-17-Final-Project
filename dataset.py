from class_file import Statistics

report2008 = Statistics(
    energy = {"BTUs per Square Foot": 79000,
              "Renewable Sources of Electricity": {
                # [% of Cal Poly's Energy; Eligible as Renewable; Doesn't Emit Greenhouse Gases]
                  "Biomass and Waste": [4.0,True,False],
                  "Geothermal": [3.0,True,True],
                  "Small Hydro": [3.0,True,True],
                  "Solar": [1.0,True,True],
                  "Wind": [2.0, True, True],
                  "Large Hydro": [12.0,False,True],
                  "Nuclear": [24.0,False,True],
                  "Natural Gas": [49.0,False,False],
                  "Coal": [2.0,False,False]},
              "% of Campus Vehicle Fleet Using Alternative Fuel":26.0},
    transportation = {"Parking Permits per Student":5998,
                      "% of Student Population Living on Campus":19.5}

)

if dictionary[i][1] == true:
    += dictionary[1][0]