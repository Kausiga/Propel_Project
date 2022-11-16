from numpy import double
import pandas as pd
path = "C:\\Users\\kausi\\OneDrive\\Desktop\\project\\yolov4-custom-functions\\data\\video\\video.txt"
res_path = path[:path.rfind("\\")]+"\\"+path.split("\\")[-1].split(".")[0]+".csv"
file = open(path, 'r')
Lines = file.readlines()
  
frames = []
bicyles = []
car = []
person = []
fps = []
# Strips the newline character
for line in Lines:
    
    if(line.find("FRAME") != -1):
        if(len(fps)!=len(frames)):
            fps.append("0")
        if(len(bicyles)!=len(frames)):
            bicyles.append("0")
        if(len(car)!=len(frames)):
            car.append("0")
        if(len(person)!=len(frames)):
            person.append("0")
        frames.append(int(line.split(":")[1].strip()))
    elif(line.find("persons") != -1):
        person.append(int(line.split(":")[1].strip()))
    elif(line.find("bicycles") != -1):
        bicyles.append(int(line.split(":")[1].strip()))
    elif(line.find("cars") != -1):
        car.append(int(line.split(":")[1].strip()))
    elif(line.find("FPS") != -1):
        fps.append(double(line.split(":")[1].strip()))

df = pd.DataFrame({"Frame Number": frames, "Person": person, "Bicycle": bicyles,"Car": car,"FPS": fps})
df.to_csv(res_path, index = False)