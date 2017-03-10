#!/usr/bin/env python2
import ProcessFile as pf
import PlotData as pld
import numpy as np
import TrainAnalyzeModel as tam

filename = "/data/higgsml/training.csv"

def graphdata(dataframe):
	datasignal, wsignal = pf.ProcessFrame(dataframe, dataframe.Label, 1)
	databack, wback = pf.ProcessFrame(dataframe, dataframe.Label, 0)
	figs = [pld.PlotData([datasignal, databack], feat, [wsignal, wback]) for feat in pf.GetVariables(datasignal)]
	pld.SavePlots(figs)
	pld.ClosePlots(figs)

def trainwdata(dataframe):
	train_df, test_df = pf.SplitData(dataframe)
	print dataframe.shape
	xtrain, w_xtr = pf.ProcessFrame(train_df)
	ytrain = train_df.Label
	print xtrain.shape, ytrain.shape, w_xtr.shape
	mod = tam.Train(xtrain, ytrain, w_xtr)	

	xtest, _ = pf.ProcessFrame(test_df)
	ytest = test_df.Label

	t_sig = pf.ProcessFrame(test_df, test_df.Label, 1)
	t_bac = pf.ProcessFrame(test_df, test_df.Label, 0)

	#x = tam.Decision(mod, t_sig)
	#y = tam.Decision(mod, t_bac)

def main():
	dataframe = pf.LoadFile(filename)
	dataframe = pf.ReplaceValues(dataframe)
	graphdata(dataframe)
	trainwdata(dataframe)


if __name__ == "__main__":
	main()