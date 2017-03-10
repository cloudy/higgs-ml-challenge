#!/usr/bin/env python2
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_pdf import PdfPages
plt.rcParams.update({'figure.max_open_warning': 0})


def PlotData(dataframes, feature = None, weights = None, mis_feat = -999, datavtest = True):
	fig = plt.figure()
	if datavtest:
		sig = dataframes[0][feature]
		bac = dataframes[1][feature]
		sigl = (sig != mis_feat).index.tolist()
		bacl = (bac != mis_feat).index.tolist()
		plt.hist(sig[sigl], weights = weights[0][sigl], bins=100, histtype="step", color="red", label="signal", stacked=True)
		plt.hist(bac[bacl], weights = weights[1][bacl], bins=100, histtype="step", color="blue", label="background", stacked=True)
	else:
		plt.hist(dataframes[0],bins=100,histtype="step", color="red", label="signal",stacked=True)
		plt.hist(dataframes[1],bins=100,histtype="step", color="blue", label="background",stacked=True)

	plt.legend(loc='upper right')
	plt.title(feature)
	return fig

def SavePlots(figs, filename="dataplot.pdf"):
	with PdfPages(filename) as pdf:
		for fig in figs:
			pdf.savefig(fig)
	print "Plots were saved as: %s" % filename

#in retrospect it's pass by value
def ClosePlots(figs):
	for fig in figs:
		plt.close(fig)

