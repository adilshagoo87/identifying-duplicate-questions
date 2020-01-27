import data as dt
import preprocessing as pre
import pandas as pd
from nltk.tokenize import RegexpTokenizer
def leng():
	l = []
	m = []
	df = pre.punc()
	x = dt.getQues1(df)
	y = dt.getQues2(df)
	for i in range(len(x)):
		l.append(len(x[i]))
		m.append(len(y[i]))	
	df.insert(5, 'len q1', " ")
	df.insert(6, 'len q2', " ")
	dt.setlen1(df,l)
	dt.setlen2(df,m)
	return df

def leng_diff():
	l = []
	df = leng()
	q1 = dt.getLenQues1(df)
	q2 = dt.getLenQues2(df)
	for i in range(len(q1)):
		if (q1[i] - q2[i]) < 0:
			l.append((-1)*(q1[i] - q2[i]))
		else:
			l.append(q1[i] - q2[i])
	df.insert(7, 'len_diff', " ")
	dt.setlen_diff(df,l)
	return df
	
def compare():
	l =[]
	tokenizer = RegexpTokenizer(r'\w+')
	df = leng_diff()
	q1=dt.getQues1(df)
	q2=dt.getQues2(df)
	for i in range(len(q1)):
		x = tokenizer.tokenize(q1[i])
		y = tokenizer.tokenize(q2[i])
		if x[0] == y[0]:
			l.append(1)
		else:
			l.append(0)
	df.insert(8, 'fcw', " ")
	dt.setfcw(df,l)
	return df


def compareSameWords():
	l = []
	tokenizer = RegexpTokenizer(r'\w+')
	df = compare()
	q1=dt.getQues1(df)
	q2=dt.getQues2(df)
	for i in range(len(q1)):
		x = tokenizer.tokenize(q1[i])
		y = tokenizer.tokenize(q2[i])
		count = 0
		if len(x) >= len(y):
			for j in range(len(y)):
				if y[j] == x[j]:
					count += 1
			l.append(count)
		else:
			for j in range(len(x)):
				if x[j] == y[j]:
					count +=1
			l.append(count)		
	df.insert(9, 'samewords', " ")
	dt.setcsw(df,l)
	return df

def compareDiffWords():
	l = []
	tokenizer = RegexpTokenizer(r'\w+')
	df = compareSameWords()
	q1=dt.getQues1(df)
	q2=dt.getQues2(df)
	for i in range(len(q1)):
		x = tokenizer.tokenize(q1[i])
		y = tokenizer.tokenize(q2[i])
		count = 0
		if len(x) >= len(y):
			for j in range(len(y)):
				if y[j] != x[j]:
					count += 1
			count += (len(x) - len(y))
			l.append(count)
		else:
			for j in range(len(x)):
				if x[j] != y[j]:
					count +=1
			count += (len(y) - len(x))
			l.append(count)
	df.insert(10, 'diffwords', " ")
	dt.setcdw(df,l)
	return df
	
