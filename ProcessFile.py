#!/usr/bin/env python2
import subprocess as sp
import pandas as pd

def LoadFile(filedir):
	return pd.read_csv(filedir)

"""From the Challenge doc appendix: EventID, Weight, and Label
	are not to be used as features.
	df = dataframe
	ftype = 's' or 'b'
	"""
def ProcessFrame(df, feature=None, result=None):
	if result is not None and feature is not None:
		df = df[feature == result]	
	return df.drop(df.columns[[0, -2, -1]], axis=1)

def GetVariables(df):
	return list(df.columns.values)

