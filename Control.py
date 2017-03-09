#!/usr/bin/env python2
import ProcessFile as pf
import PlotData as pld


filename = "/data/higgsml/training.csv"

def graphdata(dataframe):
	datasignal = pf.ProcessFrame(dataframe, dataframe.Label, 1)
	databack = pf.ProcessFrame(dataframe, dataframe.Label, 0)
	figs = [pld.PlotData([datasignal, databack], var) for var in pf.GetVariables(datasignal)]
	pld.SavePlots(figs)
	pld.ClosePlots(figs)

def trainwdata(dataframe):
	train_df, test_df = pf.SplitData(dataframe)
	print len(train_df), len(test_df)
	xtrain = pf.ProcessFrame(train_df, train_df.Label, 1)
	ytrain = train_df.Label
	print ytrain

def main():
	dataframe = pf.LoadFile(filename)
	dataframe = pf.ReplaceValues(dataframe)
	graphdata(dataframe)
	trainwdata(dataframe)

if __name__ == "__main__":
	main()