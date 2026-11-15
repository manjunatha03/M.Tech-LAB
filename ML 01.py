
# MACHINE LEARNING LAB - PROGRAM 1
# Data Preprocessing Techniques

import pandas as pd
import numpy as np

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder


# STEP 1: CREATE DATASET

data = {
    'Name': ['Amit', 'Rahul', 'Priya', 'Sneha', 'Kiran', 'Arun'],
    'Age': [20, 22, np.nan, 24, 21, 23],
    'Marks': [85, 90, 78, np.nan, 88, 95],
    'Gender': ['Male', 'Male', 'Female', 'Female', np.nan, 'Male'],
    'City': ['Mysore', 'Bangalore', 'Mysore', 'Chennai',
             'Bangalore', 'Chennai']
}

df = pd.DataFrame(data)

print("\n========== ORIGINAL DATASET ==========")
print(df)


# STEP 2: CHECK MISSING VALUES

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())


# STEP 3: HANDLE MISSING VALUES

numerical_columns = ['Age', 'Marks']
categorical_columns = ['Gender', 'City']

# Fill numerical missing values using Mean

num_imputer = SimpleImputer(strategy='mean')

df[numerical_columns] = num_imputer.fit_transform(
    df[numerical_columns]
)

# Fill categorical missing values using Most Frequent

cat_imputer = SimpleImputer(strategy='most_frequent')

df[categorical_columns] = cat_imputer.fit_transform(
    df[categorical_columns]
)

print("\n========== AFTER HANDLING MISSING VALUES ==========")
print(df)


# STEP 4: NORMALIZATION

normalizer = MinMaxScaler()

normalized_data = normalizer.fit_transform(
    df[numerical_columns]
)

normalized_df = pd.DataFrame(
    normalized_data,
    columns=['Age_Normalized', 'Marks_Normalized']
)

print("\n========== NORMALIZED DATA ==========")
print(normalized_df.round(3))


# STEP 5: STANDARDIZATION

standardizer = StandardScaler()

standardized_data = standardizer.fit_transform(
    df[numerical_columns]
)

standardized_df = pd.DataFrame(
    standardized_data,
    columns=['Age_Standardized', 'Marks_Standardized']
)

print("\n========== STANDARDIZED DATA ==========")
print(standardized_df.round(3))


# STEP 6: FEATURE ENCODING

encoder = OneHotEncoder(
    sparse_output=False,
    handle_unknown='ignore'
)

encoded_data = encoder.fit_transform(
    df[categorical_columns]
)

encoded_df = pd.DataFrame(
    encoded_data,
    columns=encoder.get_feature_names_out(
        categorical_columns
    )
)

print("\n========== FEATURE ENCODING ==========")
print(encoded_df)


# STEP 7: FINAL PREPROCESSED DATASET

final_df = pd.concat(
    [
        df[['Name']].reset_index(drop=True),
        normalized_df.reset_index(drop=True),
        encoded_df.reset_index(drop=True)
    ],
    axis=1
)

print("\n========== FINAL PREPROCESSED DATASET ==========")
print(final_df)


# STEP 8: COMPLETION MESSAGE

print("\n======================================")
print("DATA PREPROCESSING COMPLETED SUCCESSFULLY!")
print("======================================")
