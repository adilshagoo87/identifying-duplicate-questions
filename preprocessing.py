import data as dt
from nltk.tokenize import RegexpTokenizer
import pandas as pd

def lower():
	df = dt.readfile()
	x = dt.getQues1(df)
	y = dt.getQues2(df)
	for i in range(len(x)):
		x[i] = x[i].lower()
		y[i] = y[i].lower()
	dt.setQues1(df,x)
	dt.setQues2(df,y)
	print('lower')
	return df

	
def punc():
	l = []
	m = []
	df= lower()
	x = dt.getQues1(df)
	y = dt.getQues2(df) 
	tokenizer = RegexpTokenizer(r'\w+')
	for i in range(len(x)):
		x[i] = tokenizer.tokenize(x[i])
		y[i] = tokenizer.tokenize(y[i])
		if x[i] == l or y[i] == l:
			x[i] = " ".join(x[i])
			y[i] = " ".join(y[i])
			m.append(i)
		else:
			x[i] = " ".join(x[i])
			y[i] = " ".join(y[i])
	x = list(x)
	for index in sorted(m, reverse=True):
		del x[index]
	df = df.drop(df.index[m])
	dt.setQues1(df,x)
	dt.setQues2(df,y)
	print('punc')
	return df
