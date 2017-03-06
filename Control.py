#!/usr/bin/env python2
import ProcessFile as pf
#import PlotData as pld

filename = "/data/higgsml/training.csv"

print filename

dataframe = pf.LoadFile(filename)

print dataframe

datasignal = pf.ProcessFrame(dataframe, 's')

print datasignal

databack = pf.ProcessFrame(dataframe, 'b')

print databack

print pf.GetVariables(datasignal)
