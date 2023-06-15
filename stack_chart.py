import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_stack():
    datas = [  ["Johor", 2015513, 991355, 284735, 4039, 639],
    ["Kedah", 1153130, 403194, 97587, 1674, 308],
    ["Kelantan", 920675, 272658, 25176, 7, 144],
    ["Melaka", 480482, 285094, 13093, 334, 328],
    ["Negeri Sembilan", 730478, 271858, 12743, 796, 1],
    ["Pahang", 916891, 304561, 22109, 484, 106],
    ["Perak", 1311211, 568355, 89264, 377, 753],
    ["Perlis", 162706, 47672, 2587, 0, 0],
    ["Pulau Pinang", 844078, 550880, 214699, 915, 458],
    ["Sabah", 1782650, 514595, 94364, 11, 4358],
    ["Sarawak", 895391, 1488549, 45887, 0, 239],
    ["Selangor", 2307229, 2538656, 316030, 6222, 140],
    ["Terengganu", 577837, 311850, 23395, 0, 551],
    ["W.P. Kuala Lumpur", 906048, 1476633, 786424, 1154, 100],
    ["W.P. Labuan", 78811, 6534, 1, 0, 0],
    ["W.P. Putrajaya", 107838, 57672, 8, 15, 1]
    ]

    datas.sort(key=lambda row: (row[1]+row[2]+row[3]), reverse=True)

    state = []
    pfizer = []
    sinovac = []
    astra = []
    sinopharm = []
    cansino = []

    for data in datas:
        state.append(data[0])
        pfizer.append(data[1])
        sinovac.append(data[2])
        astra.append(data[3])
        sinopharm.append(data[4])
        cansino.append(data[5])

    state = np.array(state)
    pfizer= np.array(pfizer)
    sinovac=np.array(sinovac)
    astra = np.array(astra)
    sinopharm=np.array(sinopharm)
    cansino=np.array(cansino)

    print(len(state))
    print(len(pfizer))
    print(len(sinovac))
    print(len(astra))
    print(len(sinopharm))
    print(len(cansino))

    print(state)

    pfizer_percent = []
    sinovac_percent = []

    for data in datas:
        pfizer_percent.append((data[1]/(data[1]+data[2]+data[3]+data[4]+data[5]))*100)
        sinovac_percent.append((data[2]/(data[1]+data[2]+data[3]+data[4]+data[5]))*100)

    print(pfizer)
    print(len(pfizer_percent))
    print(sinovac_percent)
    
    # creating the bar plot
    plt.figure(figsize=(10,6))
    plt.bar(state, astra, color='orange')
    plt.bar(state, sinovac, bottom=astra, color='#ff6961')
    plt.bar(state, pfizer,bottom=astra+sinovac, color='#2c97f5')
    plt.legend(["Astrazeneca","Sinovac","Pfizer"])
    plt.ticklabel_format(style='plain', axis='y')
    plt.xticks(rotation='vertical', size=8)
    csfont = {'fontname':'sans-serif'}
    plt.title("Type of vaccine taken in each state",**csfont)
    i = 0
    extra = 0
    for data in datas:
        a = str(round(sinovac_percent[i],2))+"%"
        b = str(round(pfizer_percent[i],2))+"%"
        plt.text(-0.4+i, astra[i]*0.9+(sinovac[i]/2*0.9), a, size=6)
        plt.text(-0.4+i, astra[i]*0.9+sinovac[i]*0.9+(pfizer[i]/2*0.9)+extra, b, size=6)
        i+=1
        if i == 13:
            extra = 99999
    
    return plt