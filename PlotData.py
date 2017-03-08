#!/usr/bin/env python2
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_pdf import PdfPages
plt.rcParams.update({'figure.max_open_warning': 0})


def PlotData(dataframes, variable):
	fig = plt.figure()
	plt.hist(dataframes[0][variable], bins=100, histtype="step", color="red", label="background", stacked=True)
	plt.hist(dataframes[1][variable], bins=100, histtype="step", color="blue", label="signal", stacked=True)
	plt.legend(loc='upper right')
	plt.title(variable)
	return fig

def SavePlots(figs, filename="dataplot.pdf"):
	with PdfPages(filename) as pdf:
		for fig in figs:
			pdf.savefig(fig)
	print "Plots were saved as: %s" % filename

def ClosePlots(figs):
	for fig in figs:
		plt.close(fig)