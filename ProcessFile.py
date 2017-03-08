#!/usr/bin/env python2
import pandas as pd


def LoadFile(filedir):
	return pd.read_csv(filedir)

"""From the Challenge doc appendix: EventID, Weight, and Label
	are not to be used as features.
	"""
def ProcessFrame(df, feature=None, result=None):
	if result is not None and feature is not None:
		df = df[feature == result]	
	return df.drop(df.columns[[0, -2, -1]], axis=1)

def GetVariables(df):
	return list(df.columns.values)

def SplitData(df, percentsplit = 0.8):
	if percentsplit > 1 or percentsplit < 0:
		percentsplit = 0.8
	splitposition = int(len(df)*percentsplit)
	# return train, test
	return df[:splitposition], df[splitposition:]

def ReplaceValues(df, column = 'Label', mapping = {'s':1, 'b':0}):
	return df.replace({column: mapping})