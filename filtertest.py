from scipy import signal

data=[]
with open("GSRfilter.csv") as read_object:
    lines=read_object.readlines()
for line in lines:
    data.append(int(line.rstrip()))
b, a = signal.butter(8, 0.04, 'lowpass')
filtedData = signal.filtfilt(b, a, data)
with open("GSRfilteddata.csv","a") as write_object:
    for fdata in filtedData:
        write_object.write(str(fdata)+"\n")
