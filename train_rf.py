# import scipy.io as sp     # for .mat
# liu=sp.loadmat("/Users/hzhou2/fold/sider4-pub/Liu_dataset.mat") 
# train_pachta=np.concatenate((train_pa,train_ch,train_ta),axis=1)   (axis=1 extends column axis=0 extends row)
# x=liu['Transporters']
# clf=joblib.load('model/model_rf200_maccs.pkl')

from sklearn import datasets
from sklearn.ensemble import RandomForestRegressor
from scipy.sparse import csr_matrix
import numpy as np
import pickle
from sklearn.externals import joblib
#from sklearn.tree import DecisionTreeRegressor
#from sklearn.neural_network import MLPRegressor


train_i,y0=datasets.load_svmlight_file("train_fea.txt")

train_label_i,y0=datasets.load_svmlight_file("train_svmlabel.txt")
train_label=csr_matrix(train_label_i).toarray()

#clf=DecisionTreeRegressor()
#clf=MLPRegressor(hidden_layer_sizes=(64,128,256,512),activation='logistic')
#clf=RandomForestRegressor(n_estimators=200)
clf=RandomForestRegressor()

clf.fit(train_i,train_label)

joblib.dump(clf,'model/model_tree.pkl')


