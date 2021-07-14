import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Loading the data from the given file - Problem1.txt
data=pd.read_csv('Problem1.txt',sep='\t')

sample = [[5, 4.5, 2]]
print("\nTaking random Sample Data for prediction: ",sample,'\n')

# Dividing the data into 80% training set and 20% testing set for more accuracy
data_train, data_test = train_test_split(data, test_size=0.2, random_state=1)

# Using the feature and label vectors from the training dataset
X_train = np.array(data_train[data_train.columns[4:]])
y_train = np.array(data_train[data_train.columns[0]])
X_test = np.array(data_test[data_test.columns[4:]])
y_test = np.array(data_test[data_train.columns[0]])

# Declaring and then training the K-Nearest Neighbour model with the training dataset for k=3
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# making predictions on the testing set
knn_y_pred = knn.predict(X_test)

# comparing actual response values (y_test) with predicted response values (knn_y_pred)
accKnn=accuracy_score(y_test, knn_y_pred)
print(f"The Test Accuracy for K-Nearest Neighbour : {accKnn*100}%")

# making prediction for out of sample data
preds = knn.predict(sample)
pred_species = [data.fruit_name[p] for p in preds]
pred_species1 = [data.fruit_subtype[p] for p in preds]
print(f"Predictions by KNN Algorithm: FruitName={pred_species} Subtype={pred_species1}\n")

# USING LOGISTIC REGRESSION ALGORITHM
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

x=data.iloc[:, [4,5,6]].values
y=data.iloc[:, 0].values

xtrain = data_train.iloc[:, [4,5,6]].values
ytrain = data_train.iloc[:, 0].values
xtest = data_test.iloc[:, [4,5,6]].values
ytest = data_test.iloc[:, 0].values

sc_x = StandardScaler()
xtrain = sc_x.fit_transform(xtrain) 
xtest = sc_x.transform(xtest)


classifier = LogisticRegression(random_state = 0)
classifier.fit(xtrain, ytrain)

log_reg_y_pred = classifier.predict(xtest)

accLr=accuracy_score(ytest, log_reg_y_pred)
print (f"The Test Accuracy for Logistic Regression : {accLr*100}%")

preds = classifier.predict(sample)
pred_species = [data.fruit_name[p] for p in preds]
pred_species1 = [data.fruit_subtype[p] for p in preds]
print(f"Predictions by LR Algorithm: FruitName={pred_species} Subtype={pred_species1}\n")

# Telling which algorithm gave better results
if(accKnn>accLr):
    print('KNN Algorithm had better Accuracy')
elif(accKnn<accLr):
    print('LR Algorithm had better Accuracy')
else:
    print('Both algorithms had the same Accuracy')

# PLOTTING
fig, ax = plt.subplots(2,2)
fig.set_size_inches(9, 5)
fig.tight_layout(pad=3.0)
ax[0,0].hist(y_train, 4, width=0.5)
label = ['Apple', 'Mandarin', 'Orange', 'Lemon']
rects = ax[0,0].patches
for rect, l in zip(rects, label):
    h = rect.get_height()
    ax[0,0].text((rect.get_x() + rect.get_width()/2), h+0.01, l, ha='center', va='bottom')
ax[0,0].set_title('Fruit Distribution in Training Dataset')
ax[0,0].set_xlabel('Fruits')
ax[0,0].set_ylabel('Frequency')

groups = data_train.groupby("fruit_name")
for name, group in groups:
    ax[0,1].plot(group["width"], group["height"], marker="o", linestyle="", label=name)
ax[0,1].set_title('Fruit Distribution according to Widht and Height')
ax[0,1].set_xlabel('Width')
ax[0,1].set_ylabel('Height')
ax[0,1].legend()

# scatter plot of fruit predictions using 
# K-Nearest Neighbour algorithm
knn_correct_pred = np.where(y_test == knn_y_pred)
knn_wrong_pred = np.where(y_test != knn_y_pred)

ax[1,0].scatter(X_test[knn_correct_pred, 1], X_test[knn_correct_pred, 2], c='r', label='Correct Prediction')
ax[1,0].scatter(X_test[knn_wrong_pred, 1], X_test[knn_wrong_pred, 2], c='k', label='Wrong Prediction')
ax[1,0].set_title('Predictions by K-Nearest Neighbour Algorithm')
ax[1,0].set_xlabel('Width')
ax[1,0].set_ylabel('Height')
ax[1,0].legend()


# scatter plot of fruit predictions using 
# Logistic Regression Algorithm
lr_correct_pred = np.where(ytest == log_reg_y_pred)
lr_wrong_pred = np.where(ytest != log_reg_y_pred)
ax[1,1].scatter(xtest[lr_correct_pred, 1], xtest[lr_correct_pred, 2], c='r', label='Correct Prediction')
ax[1,1].scatter(xtest[lr_wrong_pred, 1], xtest[lr_wrong_pred, 2], c='k', label='Wrong Prediction')
ax[1,1].set_title('Predictions by Logistic Regression Algorithm')
ax[1,1].set_xlabel('Width')
ax[1,1].set_ylabel('Height')
ax[1,1].legend()

plt.show()