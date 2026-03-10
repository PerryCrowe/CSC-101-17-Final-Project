from class_file import Statistics

report2008 = Statistics(
    year = 2008,
    energy = {"BTUs per Square Foot": 79000,
              "Sources of Electricity": {
                # [% of Cal Poly's Energy; Eligible as Renewable; Doesn't Emit Greenhouse Gases]
                  "Renewable": 13.0,
                  #"Biomass and Waste": [4.0,True,False],
                  #"Geothermal": [3.0,True,True],
                  #"Small Hydro": [3.0,True,True],
                  #"Solar": [1.0,True,True],
                  #"Wind": [2.0, True, True],
                  "Large Hydro": 12.0,
                  "Nuclear": 24.0,
                  "Natural Gas": 49.0,
                  "Coal": 2.0,
                  "Unspecified": 0.0},
              "% of Campus Vehicle Fleet Using Alternative Fuel":26.0},
    transportation = {"Parking Permits per Student":0.31, # Lower is considered better. Not a %!
                      "% of Student Population Living on Campus":19.5,
                      "CP SLO Transit Riders per Year": 545000},
    water = {"Domestic Water Use": 550000, # acre-feet
             "Total Delivered Water": 950, # acre-feet
             "Total Indoor Water Use": 215}, # acre-feet
    waste = 70.0 # % Solid Waste Diverted from Landfill
)

report2010 = Statistics(
    year = 2010,
    energy = {"BTUs per Square Foot": 71000,
              "Sources of Electricity": {
                # [% of Cal Poly's Energy; Eligible as Renewable; Doesn't Emit Greenhouse Gases]
                  "Renewable": 16.0,
                  #"Biomass and Waste": [4.0,True,False],
                  #"Geothermal": [4.0,True,True],
                  #"Small Hydro": [4.0,True,True],
                  #"Solar": [1.0,True,True],
                  #"Wind": [3.0, True, True],
                  "Large Hydro": 16.0,
                  "Nuclear": 20.0,
                  "Natural Gas": 47.0,
                  "Coal": 1.0,
                  "Unspecified": 0.0},
              "% of Campus Vehicle Fleet Using Alternative Fuel":47.0},
    transportation = {"Parking Permits per Student":0.22, # Lower is considered better. Not a %!
                      "% of Student Population Living on Campus":33.0,
                      "CP SLO Transit Riders per Year": 620000},
    water = {"Domestic Water Use": 600, # acre-feet
             "Total Delivered Water": 1200, # acre-feet
             "Total Indoor Water Use": 310}, # acre-feet
    waste = 53.0 # % Solid Waste Diverted from Landfill
)

report2012 = Statistics(
    year = 2012,
    energy = {"BTUs per Square Foot": 74000,
              "Sources of Electricity": {
                # [% of Cal Poly's Energy; Eligible as Renewable; Doesn't Emit Greenhouse Gases]
                  "Renewable":        17.0,
                  #"Biomass and Waste": [4.0,True,False],
                  #"Geothermal":        [5.0,True,True],
                  #"Small Hydro":       [3.0,True,True],
                  #"Solar":             [1.0,True,True],
                  #"Wind":              [4.0, True, True],
                  "Large Hydro":      16.0,
                  "Nuclear":          24.0,
                  "Natural Gas":      20.0,
                  "Coal":              1.0,
                  "Unspecified":      24.0},
              "% of Campus Vehicle Fleet Using Alternative Fuel":45.0},
    transportation = {"Parking Permits per Student":0.20, # Lower is considered better. Not a %!
                      "% of Student Population Living on Campus":43.0,
                      "CP SLO Transit Riders per Year": 665000},
    water = {"Domestic Water Use": 550, # acre-feet
             "Total Delivered Water": 1060, # acre-feet
             "Total Indoor Water Use": 290}, # acre-feet
    waste = 80.0 # % Solid Waste Diverted from Landfill
)

report2014 = Statistics(
    year = 2014,
    energy = {"BTUs per Square Foot": 650000,
              "Sources of Electricity": None,
              "% of Campus Vehicle Fleet Using Alternative Fuel":32.0},
    transportation = {"Parking Permits per Student":0.22, # Lower is considered better. Not a %!
                      "% of Student Population Living on Campus":37.5,
                      "CP SLO Transit Riders per Year": 670000},
    water = {"Domestic Water Use": 705, # acre-feet
             "Total Delivered Water": 1180, # acre-feet
             "Total Indoor Water Use": 260}, # acre-feet
    waste = 71.0 # % Solid Waste Diverted from Landfill
)

report2016 = Statistics(
    year = 2016,
    energy = {"BTUs per Square Foot": 58000,
              "Sources of Electricity": {
                # [% of Cal Poly's Energy; Eligible as Renewable; Doesn't Emit Greenhouse Gases]
                  "Renewable":        30.0,
                  "Large Hydro":       6.0,
                  "Nuclear":          23.0,
                  "Natural Gas":      25.0,
                  "Coal":              0.0,
                  "Unspecified":      17.0},
              "% of Campus Vehicle Fleet Using Alternative Fuel":28.0},
    transportation = {"Parking Permits per Student":0.18, # Lower is considered better. Not a %!
                      "% of Student Population Living on Campus":35.0,
                      "CP SLO Transit Riders per Year": 759102},
    water = {"Domestic Water Use": 452, # acre-feet
             "Total Delivered Water": 974, # acre-feet
             "Total Indoor Water Use": 210}, # acre-feet
    waste = 89.8
)

report2018 = Statistics(
    year = 2018,
    energy = {"BTUs per Square Foot": 57000,
              "Sources of Electricity": {
                # [% of Cal Poly's Energy; Eligible as Renewable; Doesn't Emit Greenhouse Gases]
                  "Renewable":        33.0,
                  "Large Hydro":      18.0,
                  "Nuclear":          27.0,
                  "Natural Gas":      20.0,
                  "Coal":              0.0,
                  "Unspecified":       2.0},
              "% of Campus Vehicle Fleet Using Alternative Fuel":29.0},
    transportation = {"Parking Permits per Student":0.19, # Lower is considered better. Not a %!
                      "% of Student Population Living on Campus":33.0,
                      "CP SLO Transit Riders per Year": 724647},
    water = {"Domestic Water Use": 507, # acre-feet
             "Total Delivered Water": 830, # acre-feet
             "Total Indoor Water Use": 270}, # acre-feet
    waste = 86.4
)

reports_by_year = {
    2008: report2008,
    2010: report2010,
    2012: report2012,
    2014: report2014,
    2016: report2016,
    2018: report2018
}
