import matplotlib.pyplot as plt
import io, urllib, base64
import pandas as pd
import numpy as np
    
# read the csv data and get the all data
data = pd.read_csv("HKcovid_individual.csv")
# browse the first 10 rows
data.head(10)

datelist = []
caseslist = []
x_labels = []

def plot_1():
    global datelist, caseslist, x_labels
    data["date_reported"] =  pd.to_datetime(data["Report date"], format="%d/%m/%Y")
    data.groupby("date_reported").size()
    datelist = list(data.groupby("date_reported").size().index)
    caseslist = list(data.groupby("date_reported").size().values)
    x_labels = ['2020-01', '2020-04', '2020-07', '2020-10', '2021-01', '2021-04', '2021-07',
            '2021-10', '2022-01']
    plt.figure(figsize=(15, 7), dpi=100)
    ax = plt.subplot()
    ax.plot(datelist, caseslist, linewidth=3)
    ax.set_title('Evolution of New Cases\n', fontdict={"fontsize": 15})
    ax.set_xlabel("time", fontsize=12)
    ax.set_ylabel("number of new daily cases", fontsize=12)
    ax.set_xticks(x_labels)
    plt.grid()

    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format = 'png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return uri    

def plot_2():
    global datelist, caseslist, x_labels
    data["date_reported"] =  pd.to_datetime(data["Report date"], format="%d/%m/%Y")
    csum = data.groupby("date_reported").size().cumsum()
    datelist = csum.index
    caseslist = list(csum.values)
    x_labels = ['2020-01', '2020-04', '2020-07', '2020-10', '2021-01', '2021-04', '2021-07',
                '2021-10', '2022-01']
    plt.figure(figsize=(12, 4), dpi=100)
    ax = plt.subplot()
    ax.plot(datelist, caseslist, linewidth=3, color='darkblue')
    ax.set_title('Cumulative Number of Cases\\n', fontdict={"fontsize": 15})
    ax.set_xlabel("time", fontsize=12)
    ax.set_ylabel("Cumulative number of cases", fontsize=12)
    ax.set_xticks(x_labels)
    plt.grid()
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format = 'png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return uri

def plot_3():
    global datelist, caseslist, x_labels
    deceased_data = data[data['Hospitalised/Discharged/Deceased'] == 'Deceased']    
    deceased_csum = deceased_data.groupby(['date_reported']).size().cumsum()    
    datelist2 = deceased_csum.index    
    deceasedlist = list(deceased_csum.values)    
        
    plt.figure(figsize=(12, 4), dpi=100)    
    ax = plt.subplot()    
    ax.plot(datelist, caseslist, linewidth=3, color='darkblue')    
    ax.set_xlabel("time", fontsize=12)    
    ax.set_ylabel("Cumulative number of cases", fontsize=12)    
    ax.set_xticks(x_labels)    
    ax2 = ax.twinx()    
    ax2.plot(datelist2, deceasedlist, color='red', linewidth=3)    
    ax2.set_title('Cumulative Number of Cases and Deceased\\n', fontdict={"fontsize": 15})    
    ax2.set_ylabel("Cumulative number of deceased", fontsize=12, color='red')    
    plt.grid()    
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format = 'png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return uri

def plot_4():
    global datelist, caseslist, x_labels
    cross_data = pd.crosstab(data["Age"], data["Gender"])
    male = []
    female = []
    height = 0.2
    for i in range(98, 0, -1):
        male.append(int(cross_data.loc[str(i), 'M']))
        female.append(int(cross_data.loc[str(i), 'F']))
    male.append(int(cross_data.loc['<1', 'M']))
    male.append(int(cross_data.loc['Pending', 'M']))
    female.append(int(cross_data.loc['<1', 'F']))
    female.append(int(cross_data.loc['Pending', 'F']))
    age_index = list(range(98, 0, -1)) + ['<1', 'Pending']
    y_ticks = range(len(age_index))[::-1]
    plt.figure(figsize=(18, 26))
    # fig, ax = plt.subplots()
    plt.barh(y_ticks, width=male, label='Male')
    plt.barh(y_ticks, width=female, left=male, label='Female')
    plt.yticks(y_ticks, age_index)
    plt.legend()
    plt.title("Number of cases", fontdict={"fontsize": 20})
    plt.ylabel("Age", fontdict={"fontsize": 15})
    plt.xlabel("Number of cases", fontdict={"fontsize": 15})
    plt.grid()
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format = 'png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return uri

solution_01 = plot_1()
solution_02 = plot_2()
solution_03 = plot_3()