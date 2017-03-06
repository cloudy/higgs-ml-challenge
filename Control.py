#!/usr/bin/env python2
import ProcessFile as pf
#import PlotData as pld

from sklearn.linear_model import SGDClassifier
from sklearn import linear_model, svm



filename = "/data/higgsml/training.csv"

print filename

dataframe = pf.LoadFile(filename)

#print dataframe

datasignal = pf.ProcessFrame(dataframe, dataframe.Label, 's')

#print datasignal

databack = pf.ProcessFrame(dataframe, dataframe.Label, 'b')

#print databack

print pf.GetVariables(dataframe)[2]

datacleaned = pf.ProcessFrame(dataframe)

print datacleaned

print "original: ", dataframe.shape
print "cleaned : ", datacleaned.shape
print "signal d: ", datasignal.shape
print "backgr d: ", databack.shape