import tkinter 
import pandas as pd

def readfile():
	root=tkinter.Tk()
	root.geometry("300x200")
	lblquestion1 = tkinter.Label(root,text="question1")
	lblquestion1.grid(row=0,column=0,padx=10,pady=10)
	txtquestion1=tkinter.Entry(root)
	txtquestion1.grid(row=0,column=1)
	lblquestion2 = tkinter.Label(root,text="question2")
	lblquestion2.grid(row=0,column=0,padx=10,pady=10)
	txtquestion2=tkinter.Entry(root)
	txtquestion2.grid(row=1,column=1)
	
	
	
	df = pd.DataFrame(columns=['id','question1','question2'])
	l = []
	m = []
	l.append(str1)
	m.append(str2)
	df['question1'] = l
	df['question2'] = m
	q1 = df['question1'].values
	q2 = df['question2'].values
	df.index.name='id'
	df.insert(1,'qid1', ' ')
	df.insert(2,'qid2', ' ')
	l=[]
	m=[]
	n=[]
	for i in range(1,(len(q1)+len(q2))+1):
		if(i%2 == 0):
			m.append(i)
		else:
			l.append(i)
	for i in range(len(q1)):
		n.append(i)
	df['id'] = n
	df['qid1'] = l
	df['qid2'] = m
	
	return df
	root.mainloop()
	
	
def getId(df):
	return df.iloc[:1,0]
	
def getQues1id(df):
	return ddf.iloc[:1,1]
	
def getQues2id(df):
	return df.iloc[:1,2]
	
def getQues1(df):
	return df.iloc[:1,3]

def getQues2(df):
	return df.iloc[:1,4]
	
def getLenQues1(df):
	return df['len q1'].values

def getLenQues2(df):
	return df['len q2'].values
	
def setQues1(df,q1):
	x = getQues1(df)
	x = q1
	return x

def setQues2(df,q2):
	y = getQues2(df)
	y = q2
	return y

def IsDuplicate(df):
	return df['is_duplicate'].values
	
def setlen1(df,len1):
	df['len q1'] = len1
	return df['len q1'].values
	
def setlen2(df,len2):
	df['len q2'] = len2
	return df['len q2'].values
	
def setlen_diff(df,len):
	df['len_diff'] = len
	return df['len_diff'].values
	
def getlen_diff(df):
	return df['len_diff'].values
	
def setfcw(df,len):
	df['fcw'] = len
	return df['fcw'].values
	
def getfcw(df):
	return df['fcw'].values
	
def setcsw(df,len):
	df['samewords'] = len
	return df['samewords'].values
	
def getcsw(df):
	return df['samewords'].values
	
def setcdw(df,len):
	df['diffwords'] = len
	return df['diffwords'].values
	
def getcdw(df):
	return df['diffwords'].values
	
def setfuzz(df,len):
	df['fuzzywuzzy'] = len
	return df['fuzzywuzzy'].values
	
def getfuzz(df):
	return df['fuzzywuzzy'].values
	
def setfuzzsort(df,len):
	df['sortedfuzzy'] = len
	return df['sortedfuzzy'].values
	
def getfuzzsort(df):
	return df['sortedfuzzy'].values

def setwordshear(df,len):
	df['word_shear'] = len
	return df['word_shear'].values
	
def getwordshear(df):
	return df['word_shear'].values
	
def setjakard(df,len):
	df['jakard'] = len
	return df['jakard'].values
	
def getjakard(df):
	return df['jakard'].values
	
def setleven(df,len):
	df['levenshtein'] = len
	return df['levenshtein'].values
	
def getleven(df):
	return df['levenshtein'].values
	
def setcs(df,len):
	df['cs'] = len
	return df['cs'].values
	
def getcs(df):
	return df['cs'].values
	
def seteq(df,len):
	df['eq'] = len
	return df['eq'].values
	
def geteq(df):
	return df['eq'].values
	
def setpwm(df,len):
	df['pwm'] = len
	return df['pwm'].values
	
def getpwm(df):
	return df['pwm'].values
	
def setpwl(df,len):
	df['pwl'] = len
	return df['pwl'].values
	
def getpwl(df):
	return df['pwl'].values
	
def setmink(df,len):
	df['mink'] = len
	return df['mink'].values
	
def getmink(df):
	return df['mink'].values
	
def setcanb(df,len):
	df['canb'] = len
	return df['canb'].values
	
def getcanb(df):
	return df['canb'].values