import pandas as pd

# Dosya yolu ve adı
dosya_yolu = r'D:\dersler4_1\DataMining\archive'
dosya_adi = 'ds_salaries.csv'

# CSV dosyasını oku
dosya_path = dosya_yolu + '\\' + dosya_adi  # Dosya yolunu birleştir
main_data = pd.read_csv(dosya_path)

# Veriyi ekrana yazdır veya işlemleri gerçekleştir
print(main_data)




# missing data observation
# Check for missing values in each column

missing_values = main_data.isnull().sum()

print("Missing values in each column:")
print(missing_values)




# Visualization missing values / Plot the missing values
import missingno as msno
import matplotlib.pyplot as plt

msno.matrix(main_data)
plt.show()




# Remove unrequired columns
# List of features to be dropped
features_to_drop = ['salary', 'salary_currency']

# Drop the specified features from the DataFrame
main_data_new = main_data.drop(features_to_drop, axis=1)

# Display the updated DataFrame
print(main_data_new)




# Outlier Data Detection / Box Plot

import seaborn as sns
import matplotlib.pyplot as plt

# Numeric features
numeric_features = ['work_year', 'salary_in_usd', 'remote_ratio']

# String (categorical) features
categorical_features = ['experience_level', 'employment_type', 'job_title', 'employee_residence', 'company_location']

# Create box plots for numeric features
plt.figure(figsize=(15, 10))
for i, numeric_feature in enumerate(numeric_features, 1):
    plt.subplot(2, 2, i)
    sns.boxplot(x='experience_level', y=numeric_feature, data=main_data)
    plt.title(f'Box Plot of {numeric_feature} by Experience Level')

plt.tight_layout()
plt.show()

# Create box plots for numeric features by other categorical features
for categorical_feature in categorical_features:
    plt.figure(figsize=(15, 5))
    sns.boxplot(x=categorical_feature, y='salary_in_usd', data=main_data)
    plt.title(f'Box Plot of Salary in USD by {categorical_feature}')
    plt.show()





# Outlier Data Detection / Z Score
from scipy import stats

numeric_features_for_zscore = ['salary_in_usd', 'remote_ratio']

# Identify outliers using z-scores
for numeric_feature in numeric_features_for_zscore:
    z_scores = stats.zscore(main_data_new[numeric_feature])
    outliers = (z_scores > 3) | (z_scores < -3)
    print(f'Outliers in {numeric_feature}:')
    print(main_data_new[outliers][[numeric_feature]])
    




# Heatmap for 'salary_in_usd'

# Encode categorical features using one-hot encoding
main_data_encoded = pd.get_dummies(main_data_new)

# Add 'salary_in_usd' to the list of features
features_of_interest = list(main_data_encoded.columns) + ['salary_in_usd']

# Create a correlation matrix
correlation_matrix = main_data_encoded[features_of_interest].corr()

# Create a heatmap
plt.figure(figsize=(14, 10))
sns.heatmap(correlation_matrix[['salary_in_usd']], annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()


