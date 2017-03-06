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
def ProcessFrame(df, ftype):
	df = df[df.Label == ftype]
	df.drop(df.columns[[0, -2, -1]], axis=1, inplace=True)
	return df

def GetVariables(df):
	return list(df.columns.values)

