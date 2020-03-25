import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

path = 'time_series_covid19_confirmed_global.csv'
df = pd.read_csv(path)
#df = df.set_index('Country Code')
print(df.columns)


def findbyCountry(country,province=''):
    if (province == ''):
        foundCountry = df.loc[df['Country/Region'] == country]
    else:
        foundCountry = df.loc[(df['Country/Region']== country) & (df['Province/State']== province)]
    # Remove the fist 4 columns
    foundCountry = foundCountry.iloc[:,4:]
    # strip the nested List stuf [[0,0,0...]]
    foundCountry = foundCountry.values[0].tolist()
    return foundCountry


def debugDataSet(dataSet): 
    #print(type(germany_val ))
    #germany.plot(kind = 'barh')
    print(type(dataSet))
    print(dataSet)

def poltItemsFromDict(countryDict,xAxisLabels):
    legendHandles = []
    fig, ax = plt.subplots()
    for name, values in countryDict.items():
        plottedLine, = ax.plot(xAxisLabels,values, label=name)
        legendHandles.append(plottedLine)
    plt.legend(handles=legendHandles)
    tick_spacing = 10
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.show()

germany = findbyCountry("Germany")
wuhan = findbyCountry("China","Hubei")
italy = findbyCountry("Italy")
# Header of the file without the 4 first fields
xAxisLabels = list(df.iloc[:,4:].columns.values)

countriesToPlot = {'germany': germany, 'wuhan': wuhan,'italy': italy}

poltItemsFromDict(countriesToPlot,xAxisLabels)

