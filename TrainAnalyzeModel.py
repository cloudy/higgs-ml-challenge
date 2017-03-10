#!/usr/bin/env python2
from sklearn.linear_model import SGDClassifier
from sklearn.externals import joblib
#import PlotData as pld

def Train(X, y, w, filename = "savedmodels/model.pkl"):
	mod = SGDClassifier()
	mod.fit(X, y, sample_weight = w)
	joblib.dump(mod, filename)
	return mod

def Decision(model, dataframe):
	return model.decision_function(dataframe)