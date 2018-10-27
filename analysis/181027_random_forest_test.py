import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

# read the csv file and convert it into a dataframe
data = pd.read_csv("cleaned_data_python.csv", delimiter= ";")

# read the test data
test_data = pd.read_csv("test_data_cleaned_python.csv", delimiter= ";")

# split independent and dependent variables
X_train=data[["Schwierigkeitsgrad", "words", "images", "instructions", "views", "likes", "comments", "follower", "following", "projects"]]
y_train=data["Winorloose"]
X_test=test_data[["Schwierigkeitsgrad", "words", "images", "instructions", "views", "likes", "comments", "follower", "following", "projects"]]
y_test=test_data["Winorloose"]

# create a gaussian classifier
clf = RandomForestClassifier(n_estimators=100)

# train the model
clf.fit(X_train, y_train)

#predict the results from the test set
y_pred = clf.predict(X_test)

# get model accuracy
print("Accuracy: ", metrics.accuracy_score(y_test, y_pred))

# print important features
#feature_imp = pd.Series(clf.feature_importances_, index=data)


