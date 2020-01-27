import nltk
from similarity.levenshtein import Levenshtein
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
import basicfeatures as bf
import data as dt
from fuzzywuzzy import fuzz
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import pairwise_distances
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import pairwise_kernels
from scipy.spatial import distance

def Fuz():
	df = bf.compareDiffWords()
	q1=dt.getQues1(df)
	q2=dt.getQues2(df)
	l=[]
	for i in range(len(q1)):
		a=fuzz.ratio(q1[i],q2[i])
		a=a/100
		l.append(a)
	df.insert(11, 'fuzzywuzzy', " ")
	x = dt.setfuzz(df,l)	
	return df
	
def Fuz_sort():
	l=[]
	df = Fuz()
	q1=dt.getQues1(df)
	q2=dt.getQues2(df)
	for i in range(len(q1)):
		a=fuzz.token_sort_ratio(q1[i],q2[i])
		a=a/100
		l.append(a)
	df.insert(12, 'sortedfuzzy', " ")
	x = dt.setfuzzsort(df,l)
	return df

def word_shear():
	l=[]
	df = Fuz_sort()
	q1=dt.getQues1(df)
	q2=dt.getQues2(df)
	tokenizer = RegexpTokenizer(r'\w+')
	for i in range(len(q1)):
		w1 = tokenizer.tokenize(q1[i])
		w2 = tokenizer.tokenize(q2[i])
		f = ((1.0) * len(w1 and w2) )/ (len(w1) + len(w2))
		l.append(round(f,2))
	df.insert(13, 'word_shear', " ")
	x = dt.setwordshear(df,l)
	return df

def jac():
	l=[]
	df = word_shear()
	q1=dt.getQues1(df)
	q2=dt.getQues2(df)
	lemmatizer = WordNetLemmatizer()
	for i in range(len(q1)):
		word_list = nltk.word_tokenize(q1[i])
		word_list2 = nltk.word_tokenize(q2[i])
		lemmatized_output = [lemmatizer.lemmatize(w) for w in word_list]
		lemmatized_output2 = [lemmatizer.lemmatize(w) for w in word_list2]
		count = 0
		if len(lemmatized_output) >= len(lemmatized_output2):
			for j in range(len(lemmatized_output2)):
				if lemmatized_output2[j] == lemmatized_output[j]:
					count += 1
		else:
			for j in range(len(lemmatized_output)):
				if lemmatized_output[j] == lemmatized_output2[j]:
					count +=1
		z = round(float(count) / (len(lemmatized_output) + len(lemmatized_output2) - count),2)
		l.append(z)
	df.insert(14, 'jakard', " ")
	x = dt.setjakard(df,l)
	return df
	
def levention():
	l=[]
	df = jac()
	q1=dt.getQues1(df)
	q2=dt.getQues2(df)
	levenshtein = Levenshtein()
	for i in range(len(q1)):
		w1=q1[i]
		w2=q2[i]
		z=levenshtein.distance(w1,w2)
		l.append(z)
	df.insert(15, 'levenshtein', " ")
	x = dt.setleven(df,l)
	return df
	
def cs(m,n):
	k=[]
	for i in range(len(m)):
		k.append(cosine_similarity(m[i],n[i]))
	k = [l.tolist() for l in k]
	k = [y for x in k for y in x]
	k = [y for x in k for y in x]
	for i in range(len(k)):
		k[i] = round(k[i],2)
	return k

def eq(m,n):
	k=[]
	for i in range(len(m)):
		k.append(euclidean_distances(m[i],n[i]))
	k = [l.tolist() for l in k]
	k = [y for x in k for y in x]
	k = [y for x in k for y in x]
	for i in range(len(k)):
		k[i] = round(k[i],2)
	return k
	
def pwm(m,n):
	k=[]
	for i in range(len(m)):
		k.append(pairwise_distances(m[i],n[i],metric='manhattan'))
	k = [l.tolist() for l in k]
	k = [y for x in k for y in x]
	k = [y for x in k for y in x]
	for i in range(len(k)):
		k[i] = round(k[i],2)
	return k
	
def pwl(m,n):
	k=[]
	for i in range(len(m)):
		k.append(pairwise_kernels(m[i],n[i],metric='linear'))
	k = [l.tolist() for l in k]
	k = [y for x in k for y in x]
	k = [y for x in k for y in x]
	for i in range(len(k)):
		k[i] = round(k[i],2)
	return k
	
def mink(m,n):
	k=[]
	for i in range(len(m)):
		k.append(distance.minkowski(m[i],n[i],1))
	for i in range(len(k)):
		k[i] = k[i].tocoo()
		k[i] = k[i].data
	k = [l.tolist() for l in k]
	for i in range(len(k)):
		if len(k[i]) == 0 :
			k[i] = 0
		else:
			k[i] = round(sum(k[i])/len(k[i]),2)
	print('mink')
	return k

def canb(m,n):
	k=[]
	for i in range(len(m)):
		k.append(distance.canberra(m[i].toarray(),n[i].toarray()))
	for i in range(len(k)):
		k[i] = round(k[i],2)
	print('canb')
	return k
	
	
def tf_idf():
	l=[]
	df = levention()
	q1=dt.getQues1(df)
	q2=dt.getQues2(df)
	for i in range(len(q1)):
		l.append(q1[i])
		l.append(q2[i])
	vectorizer = TfidfVectorizer()
	vectorizer.fit(l)
	m=[]
	n=[]
	for i in range(len(q1)):
		m.append(vectorizer.transform([q1[i]]))
		n.append(vectorizer.transform([q2[i]]))
	p = cs(m,n)
	q = eq(m,n)
	r = pwm(m,n)
	s = pwl(m,n)
	t = mink(m,n)
	u = canb(m,n)
	df.insert(16, 'cs', " ")
	df.insert(17, 'eq', " ")
	df.insert(18, 'pwm', " ")
	df.insert(19, 'pwl', " ")
	df.insert(20, 'mink', " ")
	df.insert(21, 'canb', " ")
	x = dt.setcs(df,p)
	y = dt.seteq(df,q)
	z = dt.setpwm(df,r)
	a = dt.setpwl(df,s)
	b = dt.setmink(df,t)
	c = dt.setcanb(df,u)
	df[['id','qid1','qid2','question1','question2','len q1','len q2','len_diff','fcw','samewords','diffwords','fuzzywuzzy','sortedfuzzy','word_shear','jakard','levenshtein','cs','eq','pwm','pwl','mink','canb']]
	return df

