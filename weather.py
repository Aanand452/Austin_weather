import numpy as np
import pandas as pd


def weather():

    data = pd.read_csv(
        "/Users/anandkumar/Downloads/austin_weather.csv")

    print(data)

    # Before Analayze the data we should explore our data

    # it shows N numbers of rows in the data(by defalut,N=117)
    print(data.head())

    # # # it shows total number of rows and colums
    print(data.shape)

    # # This Atribute provides the index of the dataframe
    print(data.index)

    # # it shows the number of each columns
    print(data.columns)

    # # it shows the datatype of each column
    print(data.dtypes)

    # # it shows the number of uniques values in each columns and, it can be applied on a single column as well and whole data frame
    print(data.nunique())

    # # it shows the total numbers of non-null in each coulmn, it can be applied in single column and whole data frame as well
    print(data.count())

    # it shows all the unique values with their count, it can be applied on single column only
    print(data.value_counts())

    # provides the basic info of the dataframe
    print(data.info())

    print(data.head(3))

    print(data.columns)

    print(data.nunique())

    # Find All the unique values for WindHighMPH
    print(data['WindHighMPH'].nunique())

    print(data['WindHighMPH'].unique())

    print(data.TempLowF.value_counts())

    # Filtering the whiole dataframe for the specfing
    # print(data[data.Events == "Rain"])

    # groupby
    print(data.groupby("Events").get_group('Fog'))

    # Find the number of times when the TempHighF

    print(data[data.PrecipitationSumInches == '0'])

    # Find the null values from the Austin_dataFrame
    print(data.isnull().sum())
    print(data.notnull().sum())

    # Rename the column name Events of the dataframe to 'Events name'
    print(data.rename(columns={'Events': 'Events name'}, inplace=True))

    # What is the mean TeamHighF
    print(data.TempLowF.mean())

    # what is the standard Deviation of 'TempLowF'
    print(data.TempLowF.std())

    # find the varience of TempLowf
    print(data['TempLowF'].var())

    # Find the all the instance of TempLowF
    print(data['TempLowF'].value_counts())

    print(data[data['TempLowF'] == 30])

    # find the Templowf greaterthan 25 and TempLowF equal to 30
    print(data[(data['TempHighF'] > 30) & (data['TempLowF'] == 30)])

    # find the  each coluns of TempLowF against mean value

    print(data.groupby('HumidityLowPercent').mean())

    # what is the minmum and maximum value of each coulmn against each "TempLowF"
    print(data.groupby('TempHighF').min())

    print(data.groupby('TempHighF').max())

    print(data[data['Events'] == 'Fog'])
    print(data[(data['TempHighF'] == 60) | (data['TempLowF'] < 30)])

    print(data[(data['Events'] == 'Rain') & (
        data['TempHighF'] > 60) | (data['TempLowF'] < 60)])


weather()
