from practice_func import *

years = range(1994,2010)
data = []; exchange_rate = []

for yr in years:
	fname = "./data/%d.txt" %yr
	f = open(fname, "r")

	process(f,exchange_rate)
