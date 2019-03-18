def process(f,ratio):
	for line in f:
		date, rate = line.split()
		yr, mh, dy = date.split("/")
		date = 10000*int(yr) + 100*int(mh) + int(dy)
		rate = 1/float(rate)

		ratio.append((date,rate))