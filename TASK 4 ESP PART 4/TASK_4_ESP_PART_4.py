import datetime
import pandas as pd
import matplotlib.pyplot as plt
import time
import csv

df = pd.read_csv('Part1Task4a_data.csv')
file = open("Part1Task4a_data.csv","r")
datareader = csv.reader(file,delimiter=",")
all_data = []

for row in datareader:
    all_data.append(row)





def mainmenu():
    print("\t\t****Welcome to the Dashboard****")
    print("")
    print('1) Return all current data')
    print('2) Return data for a specific region')
    print('3) Return data for a specific property type')
    print("4 )")
    return int(input("Enter your selection :"))


def alldata():
    print(25*"\n")
    print(" ++ Viewing ALL DATA")
    print("--------------------------------------------------")
    df1 = df.loc[:, "Region Code":"Rooms"]
    print(df1)
    print("\n\n")
    print("--------------------------------------------------")
    input("Enter to proceed :")

def region_check(region, startdate, enddate):  # region, startdate, enddate
    print(25*"\n")
    print(f" ++ Viewing Region : {region}")
    print("------------------------------------------")

    df1 = df.loc[:, startdate:enddate]
    df2 = df.loc[:, 'Region Code':'Rooms']

    result = df2.where(df2["Region"] == region)
    result = pd.DataFrame(result)
    result.dropna(inplace=True)
    print(result)
    print("\n\n")
    print(" * Loading the Region Property Values")
    print("------------------------------------------")



    ave = df1.mean()
    ave.plot()
    plt.title("Region Value")
    plt.xlabel("Dates")
    plt.ylabel("Value")
    time.sleep(1.5)
    plt.show()
    return result6
    input("Enter to proceed :")
  

def property_type_check(property_input, startdate, enddate):  # region, startdate, enddate
    print(25*"\n")
    print(f" ++ Viewing Property Type : {property_input}")
    print("---------------------------------------------")
    
    df1 = df.loc[:, startdate:enddate]
    df2 = df.loc[:, 'Region Code':'Rooms']
 

    result = df2.where(df2["PropertyType"] == property_input)
    result = pd.DataFrame(result)
    result.dropna(inplace=True)
    print(result)
    print("\n\n")
    print(" * Loading the Property Type Values")
    print("---------------------------------------------")


    ave = df1.mean()
    ave.plot()
    plt.title("Property Type Value")
    plt.xlabel("Dates")
    plt.ylabel("Value")
    time.sleep(1.5)
    plt.show()
    return result
    input("Enter to proceed :")
    
def region_highest():
    length_of_array = len(all_data)

    for i in range(0,length_of_array):
        print(all_data[i])
        for j in range(4, len(all_data[0])):
            

                     
    
  
x = mainmenu()
while x == 1 or x == 2 or x == 3 or x == 4:
    if x == 1:
        alldata()

    elif x == 2:
        while True:
            print()

            all_regions = []
            regions_available = []
            #print(df[['Region']].to_string(index=False)) 

            # Extracts all of the regions and puts them in a list
            for ind in df.index:
                all_regions.append(df["Region"][ind])

            for i in range(0,len(all_regions)):
                if all_regions[i] in regions_available:
                    pass
                else:
                    regions_available.append(all_regions[i])
            
            print("- - - - - - - Available Regions to choose from - - - - - - - -\n")

            for regions_in_db in regions_available:
                print(f"{regions_in_db}")
            print()
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
            region = input("Please enter the name of the region you would like to check:")
            region = region.capitalize()
            if region in df.Region.values:
                while True:
                    startdate = input("PLEASE ENTER A START DATE AS |MONTH-YEAR|(e.g. JAN-20)  :")
                    startdate = startdate.capitalize()
                    if startdate not in df.columns:
                        print("Error start date not found")
                    else:
                        while True:
                            enddate = input("PLEASE ENTER AN END DATE AS |MONTH-YEAR| (e.g. JAN-20)  :")
                            enddate = enddate.capitalize()
                            if enddate not in df.columns:
                                print("Error end date not found")
                            else:
                                region_check(region, startdate, enddate)
                                break
                        break
                break
            else:
                print("Region not found")
    elif x == 3:
        while True:
            print()

            all_prop = []
            prop_available = []

            # Extracts all of the regions and puts them in a list
            for ind in df.index:
                all_prop.append(df["PropertyType"][ind])

            for i in range(0,len(all_prop)):
                if all_prop[i] in prop_available:
                    pass
                else:
                    prop_available.append(all_prop[i])
            
            print("- - - - - - - Property types to choose from - - - - - - - -\n")

            for prop_in_db in prop_available:
                print(f"{prop_in_db}")
            print()
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
            property_input = input("Please enter the name of the region you would like to check:")
            property_input = property_input.capitalize()
            if property_input in df.PropertyType.values:
                while True:
                    startdate = input("PLEASE ENTER A START DATE AS |MONTH-YEAR|(e.g. JAN-20)  :")
                    startdate = startdate.capitalize()
                    if startdate not in df.columns:
                        print("Error start date not found")
                    else:
                        while True:
                            enddate = input("PLEASE ENTER AN END DATE AS |MONTH-YEAR| (e.g. JAN-20)  :")
                            enddate = enddate.capitalize()
                            if enddate not in df.columns:
                                print("Error end date not found")
                            else:
                                property_type_check(property_input, startdate, enddate)
                                break
                        break
                break
            else:
                print("Region not found")
    elif x == 4:
        region_highest()


    x = mainmenu()
