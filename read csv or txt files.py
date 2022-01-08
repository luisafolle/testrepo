

import matplotlib.pyplot as plt
def readTxt():
    f = open(r"C:\file_location\file_name.txt", "r")
    data = {}
    
    for line in f:
        part1 = line.strip("\n").split(" ")
        dataName = part1[0] #this is the heading "Games", "At Base", "Hits"
        restData = part1[1:]
        
        finalData = [] #add all data in this variable, converting to int
        for x in restData:
            finalData.append(int(x))
            
            
        data[dataName] = finalData #save it in data dict. dataName is key, has value of finalData
        
    return data

def readCSV():
    f = open(r"C:\file_location\file_name.csv", "r")
    data = {}
    
    firstLine = f.readline().strip("\n").split(",")[1:]
    #firstLine = firstLine.strip("\n")
    #firstLine = firstLine.split(",")
    #same as the above in one line
    #[1:] removes index 0 and goes to the end
    
    for name in firstLine:
        data[name] = []
        #key data with the name 
        
    for line in f:
        processedLine = line.strip("\n").split(",")[1:]
       # print(processedLine)
       # indexCounter = 0
        #for name in firstLine:
         #   data[name].append(int(processedLine[indexCounter]))
           # indexCounter+= 1
         # use the above or the below, same result
         
         
        for index in range(len(processedLine)):
            name = firstLine[index]
            dataPoint = int(processedLine[index])
            data[name].append(dataPoint)
            
    return data
        
    
        
Data = readCSV()
print(Data.keys())

#1. Create a hits per at base variable
HPAB = []
for i in range(len(Data["Hits"])):
    if Data["AtBase"][i] != 0:
        HPAB.append(Data["Hits"][i]/Data["AtBase"][i]) #times they hit the ball divided by times they didnt at base
    else:
        HPAB.append (0)
        
#2. Create a figure named HPAB, with size 8,8
        
fig = plt.figure("HPABY", figsize=(8,8))

#3. Add an axis to the figure

ax = fig.add_subplot(1,1,1)

#4. Plot the HPAB against the number of games
#5. Make the size of the points appropriately small so you can see a good separation between the data
#6. Have all points plotted in green
#7. Show the plot

ax.scatter(Data["Games"],HPAB, s= 4, c = (0,1,0.3)) #c = "g", or "green" or RGB as colour

plt.show()



#print(csvVersionData["Games"][:5])
    
#txtVersionData = readTxt()      
#print(txtVersionData.keys())   

#can also use pandas to extract the data
