import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv('data/data.csv')

X = data.drop('species', axis=1)
y = data['species']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X_scaled, y)

with open('models/model.pkl', 'wb') as file:
    pickle.dump(model, file)