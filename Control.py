#!/usr/bin/env python2
import ProcessFile as pf
import PlotData as pld

# Loading and cleaning data

filename = "/data/higgsml/training.csv"

dataframe = pf.LoadFile(filename)

dataframe = pf.ReplaceValues(dataframe)

train_df, test_df = pf.SplitData(dataframe)

print len(train_df), len(test_df)

xtrain = pf.ProcessFrame(train_df, train_df.Label, 1)
ytrain = train_df.Label


print ytrain


datasignal = pf.ProcessFrame(dataframe, dataframe.Label, 1)
databack = pf.ProcessFrame(dataframe, dataframe.Label, 0)

# Generating/saving plots

figs = [pld.PlotData([datasignal, databack], var) for var in pf.GetVariables(datasignal)]
pld.SavePlots(figs)
pld.ClosePlots(figs)

# Training



# Testing model



# Saving model

