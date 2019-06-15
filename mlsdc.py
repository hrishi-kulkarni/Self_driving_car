import numpy as np
from os import listdir
from os.path import isfile, join
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import accuracy_score 
import pickle
import cv2

X = []
y = []
# load all the images and convert them

files_name = [f for f in listdir('data') if isfile(join('data', f)) and f != '.DS_Store']

for name in files_name:
    try:
        # load the image
        im_gray = cv2.imread(join('data', name), 0)
        # blur to remove details
        im_gray = cv2.resize(im_gray, (25, 25))
		#image_as_array = np.ndarray.flatten(np.asarray(img))
        (thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        image_as_array = np.ndarray.flatten(np.array(im_bw))
        # add our image to the dataset
        X.append(image_as_array)
        # retrive the direction from the filename
        y.append(name.split('_')[1].split('.')[0])
    except Exception as inst:
        print(name)
        print(inst)

# split for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# scale the data
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

clf = MLPClassifier(solver='lbfgs', alpha=0.01, batch_size=15, random_state=1, hidden_layer_sizes=100)
#predicted = cross_val_predict(clf, X, y,cv=5, verbose=2, n_jobs=1)
#print('CV: ', accuracy_score(y, predicted))
clf.fit(X_train, y_train)
print('score: ', clf.score(X_test, y_test))

fileName = 'model.pkl'
tmp = open(fileName, 'wb')
pickle.dump(clf, tmp)
tmp.close()