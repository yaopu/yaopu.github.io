#/usr/bin/python
def SqA():
	import matplotlib.pyplot as plt
	import pickle
	import numpy as np
	f = file('output1.pickle', 'r')
	unpickler = pickle.Unpickler(f)
	c = unpickler.load()
	#print len(c[0][0])
	#print len(c[3][0][0])
	q = np.array(c[0][0])
	sq = np.array(c[3][0][0])
	print q.shape
	print sq.shape
	print q*q*sq
	x=np.log10(q)
	y=np.log10(q*q*sq)
	x=np.delete(x,0)
	y=np.delete(y,0)
	print x
	print y
	plt.plot(x,y,color="red",linewidth=2.5,linestyle="-",label="log(q*q*sq)")
	plt.legend(loc='upper left')
	plt.xlabel('log(q)')
	plt.ylabel('log(q^2*sq)')
	plt.title('sq')
	plt.savefig('sq.png')
	plt.show()
	plt.close()
