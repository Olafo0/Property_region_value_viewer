import datetime
from ftplib import all_errors
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
    print("4) Return highest region value increase")
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
    return result
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
    all_regions = []
    regions_available = []
    all_regions_increase = []
    region_ave = []
    region_ave_name = []
    
    for ind in df.index:
        all_regions.append(df["Region"][ind])

    for i in range(0,len(all_regions)):
        if all_regions[i] in regions_available:
            pass
        else:
            regions_available.append(all_regions[i])


    length_of_array = len(all_data)

    for i in range(1,length_of_array):
        total = 0
        for j in range(4, len(all_data[0])):
            temp_value_holder = float(all_data[i][j])
            temp_value_holder = round(temp_value_holder,2)
            total = total + temp_value_holder
            total = round(total,2)
        format_array = [all_data[i][1],total]
        all_regions_increase.append(format_array)

    for j in range(0,len(regions_available)):
        region_repeated = 0
        total_in_area_ = 0
        for places in all_regions_increase:
            if places[0] == regions_available[j]:
                total_in_area_ = places[1] + total_in_area_
                region_repeated += 1
                ave_in_reg = total_in_area_ / region_repeated
                region_cal = places[0]
        region_ave.append([region_cal,ave_in_reg])

    #Bubble sort
    has_swapped = True
    while has_swapped:
        has_swapped = False
        for h in range(0,len(region_ave)-1):
            print(region_ave)
            if region_ave[h][1] > region_ave[h+1][1]:
                temp= region_ave[h][1]
                temp_2 = region_ave[h][0]
                region_ave[h][1] = region_ave[h+1][1]
                region_ave[h][0] = region_ave[h+1][0]
                region_ave[h+1][1] = temp
                region_ave[h+1][0] = temp_2
                has_swapped = True
            else:
                 pass
    print(region_ave)
    length_of_region_ave = len(region_ave) - 1
    DUB_W = region_ave[length_of_region_ave]
    
    print(DUB_W)
    print(25*"\n")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print()
    print(f" * HIGHEST REGION VALUE INCREASE WAS {DUB_W[0]} WITH {DUB_W[1]} % ")
    print()
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print(2*"\n")
    



            
x = mainmenu()
while x == 1 or x == 2 or x == 3 or x == 4:
    global regions_available
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
