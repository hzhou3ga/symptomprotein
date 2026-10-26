# import scipy.io as sp     # for .mat
# liu=sp.loadmat("Liu_dataset.mat") 
# train_pachta=np.concatenate((train_pa,train_ch,train_ta),axis=1)   (axis=1 extends column axis=0 extends row)
# x=liu['Transporters']
from sklearn import datasets
from sklearn.ensemble import RandomForestRegressor
from scipy.sparse import csr_matrix
import numpy as np
import pickle
from sklearn.externals import joblib
from sklearn.tree import DecisionTreeRegressor
#from sklearn.neural_network import MLPRegressor

#train_i,y0=datasets.load_svmlight_file("train_fea.txt")
test_i,y0=datasets.load_svmlight_file("test_fea.txt")
#clf=DecisionTreeRegressor()
#clf=MLPRegressor(hidden_layer_sizes=(64,128,256,512),activation='logistic')
clf=joblib.load('model/model_tree.pkl')
#pred=clf.predict(train_i)
#np.savetxt('pred/pred.txt',pred,delimiter='\t')
pred=clf.predict(test_i)
np.savetxt('pred/test_pred.txt',pred,delimiter='\t')
