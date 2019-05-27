#Programmer: Daiwei Li
#Date: 2019-04-28

import matplotlib.pyplot as plt
import numpy as np
#import pandas as pd
import csv

def read_csv(file_name):
    with open('data.csv') as f:
        reader = csv.reader(f)
    
    # eliminate blank rows if they exist
        rows = [row for row in reader if row]
    
        headings = rows[0]
        data = []
        for r in rows[1:]:
            r = [x for x in r]
            d = dict(zip(headings, r))
            data.append(d)

    return data



def find_data(data, bullet):
    raw_data = data
    x = []#data of bullet
    y = []#data of target which is potential
    for index in range(len(raw_data)):
        if raw_data[index][bullet] == "":
            raw_data[index][bullet] = "0"
        x.append(float(raw_data[index][bullet]))
        y.append(float(raw_data[index]["Potential"])-float(raw_data[index]["Overall"]))
    
    return x,y



def scattering_visualization(x, y, bullet):
    plt.xlabel(bullet)
    plt.ylabel("Real_Potential")
    plt.scatter(np.array(x), np.array(y), c='g', alpha=0.25)
    fname = bullet + ".pdf"
    plt.savefig(fname)
    plt.show()



def main():
    x = []
    y = []
    print("Let analyze soccer player informaiton in FIFA-2019")
    print("We are trying to find all cases could effect a player to improve himself")
    print("In this way, we will see some charts about potential with age, overall rate, sprintspeed, drippling, pass, and shoot")
    print("Please input file name:(/ --> data.csv) ")
    data = read_csv("data.csv")
    #age vs potential
    print("Analyze with potential:(/ --> Age) ")
    x,y = find_data(data, "Age")
    scattering_visualization(x, y, "Age")
    #overall vs potential
    print("Analyze with potential:(/ --> Overall) ")
    x,y = find_data(data, "Overall")
    scattering_visualization(x, y, "Overall")
    #sprintspeed vs potential
    print("Analyze with potential:(/ --> SprintSpeed) ")
    x,y = find_data(data, "SprintSpeed")
    scattering_visualization(x, y, "SprintSpeed")
    #drippling vs potential
    print("Analyze with potential:(/ --> Dribbling) ")
    x,y = find_data(data, "Dribbling")
    scattering_visualization(x, y, "Dribbling")
    #longpass vs potential
    print("Analyze with potential:(/ --> LongPassing) ")
    x,y = find_data(data, "LongPassing")
    scattering_visualization(x, y, "LongPassing")
    #shortpass vs potential
    print("Analyze with potential:(/ --> ShortPassing) ")
    x,y = find_data(data, "ShortPassing")
    scattering_visualization(x, y, "ShortPassing")
    #longshots vs potential
    print("Analyze with potential:(/ --> LongShots) ")
    x,y = find_data(data, "LongShots")
    scattering_visualization(x, y, "LongShots")
    print("All graphs are saved as pdf. Thank you~")
main()
