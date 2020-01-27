import pickle
import advancedfeatures as ad
df = ad.tf_idf()
data = df.iloc[:,5:17]
data.to_csv("aa.csv")
loaded_model = pickle.load(open('model1.sav', 'rb'))
result = loaded_model.predict(data)
print(result)
