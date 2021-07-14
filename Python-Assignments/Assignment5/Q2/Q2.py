import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier as KNC
from sklearn import metrics as met
from sklearn.model_selection import train_test_split as train_ts

# Loading the data from the given file - Problem2.csv
name_of_file = "Problem2.csv"
data = pd.read_csv(name_of_file, delimiter=',')

# Dividing the data into 80% training set and 20% testing set for more accuracy
data_train, data_test = train_ts(data, test_size=0.2)

# Using the feature and label vectors from the training dataset
# Now Scaling The Feature Vectors in (0,1) Range For More Optimisation
x_train = np.array(data_train[data_train.columns[:-1]])
x_test = np.array(data_test[data_test.columns[:-1]])
y_train = np.array(data_train[data_train.columns[-1]])
y_test = np.array(data_test[data_test.columns[-1]])


# Declaring and then training the K-Nearest Neighbour model with the training dataset for k=3
k=3
knn = KNC(n_neighbors=k)
knn.fit(x_train,y_train)
# Then using the trained model, making predictions for the test dataset and finding the accuracy
knn_y_pred = knn.predict(x_test)
knn_accuracy = (met.accuracy_score(y_test, knn_y_pred))*100

# printing the predictions and accuracy of the K-Nearest Neighbour Algorithm Used
print(f"\nThe Test Accuracy for K-Nearest Neighbour : {knn_accuracy}%\n")
sample = [[5,132,80,0,0,26.8,0.186,42]]
preds = knn.predict(sample)
pred_species = [data.Outcome[p] for p in preds]
print("Taking random Sample Data for prediction: ",sample,'\n')
print("Predictions:",'Diabetic' if pred_species==[1] else 'Not Diabetic')

matplotlib.rcParams.update({'font.size': 9})
matplotlib.rcParams.update({'font.weight': 'bold'})

# plotting and visualizing the data
fig, ax = plt.subplots(2,2)
fig.tight_layout(pad=3)
pos = np.squeeze(np.where(y_train == 1))
neg = np.squeeze(np.where(y_train == 0))

x = np.array(data_train['Age'])
y = np.array(data_train['DiabetesPedigreeFunction'])
z = np.array(data_train['Glucose'])

# histogram of diabetic and non-diabetic people distributed
# on the basis of age, from training dataset

ax[0,0].hist([x[pos], x[neg]], bins=10, label=['Diabetic', 'Not Diabetic'])
ax[0,0].set_title('Distribution by Age')
ax[0,0].set_xlabel('Age')
ax[0,0].set_ylabel('Frequency')
ax[0,0].legend()

# histogram of diabetic and non-diabetic people distributed
# on the basis of DPF, from training dataset

ax[0,1].hist([y[pos], y[neg]], bins=10, label=['Diabetic', 'Not Diabetic'])
ax[0,1].set_title('Distribution by DPF')
ax[0,1].set_xlabel('Diabetes Pedigree Function (DPF)')
ax[0,1].set_ylabel('Frequency')
ax[0,1].legend()

# histogram of diabetic and non-diabetic people distributed
# on the basis of Glucose, from training dataset

ax[1,0].hist([z[pos], z[neg]], bins=10, label=['Diabetic', 'Not Diabetic'])
ax[1,0].set_title('Distribution by Glucose')
ax[1,0].set_xlabel('Glucose')
ax[1,0].set_ylabel('Frequency')
ax[1,0].legend()

# scatter plot of predictions

correct_pred = np.where(y_test == knn_y_pred)
wrong_pred = np.where(y_test != knn_y_pred)
ax[1,1].scatter(x_test[correct_pred, 6], x_test[correct_pred, 7], c='r', label='Correct Prediction')
ax[1,1].scatter(x_test[wrong_pred, 6], x_test[wrong_pred, 7], c='k', label='Wrong Prediction')
ax[1,1].set_title('Predictions')
ax[1,1].set_xlabel('DPF')
ax[1,1].set_ylabel('Age')
ax[1,1].legend()

plt.show()