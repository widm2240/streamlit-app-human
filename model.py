import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import joblib
from sklearn.linear_model import LogisticRegression

data = pd.read_csv('data/iris.csv')
le = LabelEncoder()
print(le.fit(data['species']))
data['species'] = le.fit_transform(data['species'])
print(le.classes_) # [setosa ~ ]

X = data.drop(columns=['species'])
y = data['species']

# 데이터 셋 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# 모델 만들기
model = LogisticRegression()
model.fit(X_train, y_train)

# 모델 내보내기(혹은 배포)
model_file = open('models/logistic_regression_model_iris_221208.pkl', 'wb')
joblib.dump(model, model_file)
model_file.close()