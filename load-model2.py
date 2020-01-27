import pickle
import advancedfeatures as ad
df = ad.tf_idf()
data = df.iloc[:,5:22]
def gui_model():
	btnsubmit=tkinter.Button(root,text="submit",command=submit)
	btnsubmit.grid(row=2,column=0,padx=10,pady=10)
	btnexit=tkinter.Button(root,text="submit",command=sys.exit)
	btnexit.grid(row=3,column=1,padx=10,pady=10)
	
	lblouput=tkinter.Label(root,text="")
	
def submit():
	loaded_model = pickle.load(open('finalized_model.sav', 'rb'))
	return loaded_model
def output():
	z=submit()
	result = z.predict(data)
	print(result)
	

	