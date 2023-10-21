import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler,MinMaxScaler
import os
from django.conf import settings

path_to_csv = os.path.join(settings.STATIC_ROOT,'crime_df.csv')
crime_df = pd.read_csv(path_to_csv)

# Split the dataset into training and testing sets
train_size = int(len(crime_df) * 0.8)
train_data, test_data = crime_df[:train_size], crime_df[train_size:]

# Scale the features using StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(train_data[['latitude', 'longitude']])
y_train = train_data['Frequency'].values
X_test = scaler.transform(test_data[['latitude', 'longitude']])
y_test = test_data['Frequency'].values

# Train a KNN model on the training data
knn = KNeighborsRegressor(n_neighbors=5)
knn.fit(X_train, y_train)

def predict(coord):
    new_coords = [coord]  # Wrap the coord in a list
    X_new = scaler.transform(pd.DataFrame(new_coords, columns=['latitude', 'longitude']))
    y_pred = knn.predict(X_new)
    if y_pred[0] > 10 and y_pred[0]<95:
        return y_pred[0] # Return the first element of the array
    elif y_pred[0]<10:
        return 10
    else:
        return 95

