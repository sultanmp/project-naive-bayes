import pandas as pd
import numpy as np

mm = pd.ExcelFile("Need_For_Speed_Unbound_Dataset.xlsx")
mn = pd.read_excel(mm, "Train")

def average(array):
    i = 0
    jumlah = 0
    while(i<len(array)):
        jumlah += array[i]
        i += 1
    rata = jumlah / i
    return rata

q = mn["Horsepower"]
w = mn["Top Speed"]

e = mn["Overpowered"]

def bilangan0(array):
    i = 0
    jumlah = 0
    while(i<len(array)):
        if(array[i] == 0):
            jumlah += 1
        i += 1
    return jumlah

def bilangan1(array):
    i = 0
    jumlah = 0
    while(i<len(array)):
        if(array[i] == 1):
            jumlah +=1
        i += 1
    return jumlah

eq = bilangan0(e)
ew = bilangan1(e)
print(eq,ew)

def array0(array1, array2):
    i = 0
    ar = []
    while(i<len(array2)):
        if(array2[i] == 0):
            ar.append(array1[i])
        i += 1
    return ar

def array1(array1, array2):
    i = 0
    ar = []
    while(i<len(array2)):
        if(array2[i] == 1):
            ar.append(array1[i])
        i +=1
    return ar

qe = array0(q,e)
qr = array1(q,e)
we = array0(w,e)
wr = array1(w,e)

qq = average(qe)
qw = average(qr)
wq = average(we)
ww = average(wr)

qt = np.std(qe)
qy = np.std(qr)
wt = np.std(we)
wy = np.std(wr)

mb = pd.read_excel(mm, 'Test')
n = mb["Horsepower"]
b = mb["Top Speed"]

def totalpeluang0(array1, array2):
    return 126/143 * array1 * array2

def totalpeluang1(array1,array2):
    return 17/143 * array1 * array2    

def normal_dist(x , mean , sd):
    prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
    return prob_density

qu = normal_dist(n, qq, qt)
qi = normal_dist(n, qw, qy)

wu = normal_dist(b, wq, wt)
wi = normal_dist(b, ww, wy)

vq = totalpeluang0(qu,wu)
vw = totalpeluang1(qi,wi)

def prediksi(totalpeluang0, totalpeluang1):
    hasil = []
    i = 0
    while(i<len(totalpeluang0)):
        if(totalpeluang0[i] > totalpeluang1[i]):
            hasil.append(0)
        elif(totalpeluang1[i] > totalpeluang0[i]):
            hasil.append(1)
        i += 1
    return hasil

zz = prediksi(vq,vw)

print(zz)