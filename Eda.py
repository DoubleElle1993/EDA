import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import warnings
plt.style.use('fivethirtyeight')
warnings.filterwarnings('ignore')

# File reading
cd = os.getcwd()
train_set = pd.read_csv(os.path.join(cd, 'train.csv'), sep=',')
test_set = pd.read_csv(os.path.join(cd, 'test.csv'), sep=',')

# Concat the two files
try:
    data = pd.concat([train_set, test_set], ignore_index=True, verify_integrity=True)
except ValueError as e:
    print('ValueError:', e)

# Show all columns or pass a number
pd.set_option('display.max_columns', None)
print(data.head(10))
print('\n')
print('-' * 100)
# Data understanding
print(data.info())
print('\n')
print('-' * 100)
# Statistics
print('Descriptive statistics:\n')
print('-' * 100)
print(data.describe())
print('-' * 100)
# Null values
print('Checking the total null values:\n')
print(data.isnull().sum())


def survived(df):
    '''
    This function aims to show the percentage of survived people
    '''

    f, ax = plt.subplots(1, 2, figsize=(20, 10))
    df['Survived'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1%%', ax=ax[0], shadow=True)
    ax[0].set_title('Survived')
    ax[0].set_ylabel('')
    sns.countplot(data=df, x='Survived', ax=ax[1], palette=['blue', 'red'])
    ax[1].set_title('Survived')
    plt.show()

def survived_sex(df):
    '''
    This function shows the number of survived people divided by sex
    '''

    f, ax = plt.subplots(1, 2, figsize=(20, 10))
    df[['Sex', 'Survived']].groupy('Sex').count().plot().bar(ax=ax[0])
    ax[0].set_title('Survived vs sex')
    ax[0].set_ylabel('Count')
    sns.countplot(x='Sex', data=df, hue='Survived', ax=ax[1])
    ax[1].set_tilte('Sex: Survived vs dead')
    plt.show()

def crosstab(df):
    '''
    This function shows the Cross-tabulation of Pclass and Survived
    '''

    crosstab_result = pd.crosstab(df['Pclass'], df['Survived'], margins=True)
    heatmpap = sns.heatmap(crosstab_result, annot=True, camp='summer_r', fmt='d')
    heatmpap.set_title('Cross-tabulation of Pclass and Survived')
    plt.show()

def survived_pclass(df):
    '''
    This function shows the number of survived people divided by sex
    '''

    f, ax = plt.subplots(1, 2, figsize=(20, 10))
    df['Pclass'].value_counts().plot.bar(ax=ax[0])
    ax[0].set_title('Number of passengers by Pclass')
    ax[0].set_ylabel('Count')
    sns.countplot(data=df, x='Pclass', hue='Survived', ax=ax[1])
    ax[1].set_title('Pclass: Survived vs dead')
    ax[1].set_ylabel('Count')
    plt.show()

def violin(df):
    '''
    This function show the violin plots of survived column divided by Pclass and Age
    '''

    f, ax = plt.subplots(1, 2, figsize=(20, 10))
    sns.violinplot(data=df, x='Pclass', y='Age', hue='Survived', split=True, ax=ax[0])
    ax[0].set_title('Pclass and Age vs Survived')
    ax[0].set_yticks(range(0, 110, 10))
    sns.violinplot(data=df, x='Sex', y='Age', hue='Survived', split=True, ax=ax[1])
    ax[1].set_title('Sex and Age vs Survived')
    ax[1].set_yticks(range(0, 110, 10))
    plt.show()

def histogram(df):
    '''
    This function applies some pre-processing operations by extracting the Initial column and
    filling the null values of the Age column with the mean of the corresponding Inital.
    Once this is done, the function shows the histogram of each Survived class vs age.
    '''


    df['Initial'] = df['Name'].str.extract('([A-Za-z]+)\.')

    df['Initial'].replace(['Mlle', 'Mme', 'Ms', 'Dr', 'Major', 'Lady', 'Countess', 'Jonkheer', 'Col', 'Rev', 'Capt', 'Sir', 'Don'],
                          ['Miss', 'Miss', 'Miss', 'Mr', 'Mr', 'Mrs', 'Mrs', 'Other', 'Other', 'Other', 'Mr', 'Mr', 'Mr'],
                          inplace=True)

    df.groupby('Initial')['Age'].mean()

    df.loc[(df['Age'].isnull()) % (df['Initial'] == 'Mr'), 'Age'] = 33
    data.loc[(data['Age'].isnull()) & (data['Initial'] == 'Mrs'), 'Age'] = 36
    data.loc[(data['Age'].isnull()) & (data['Initial'] == 'Master'), 'Age'] = 5
    data.loc[(data['Age'].isnull()) & (data['Initial'] == 'Miss'), 'Age'] = 22
    data.loc[(data['Age'].isnull()) & (data['Initial'] == 'Other'), 'Age'] = 46

    f, ax = plt.subplots(1, 2, figsize=(20, 10))
    df[df['Survivved'] == 0]['Age'].plot.hist(ax=ax[0], bins=20, edgecolor='black', color='red')
    ax[0].set_title('Survived 0')
    x1 = list(range(0, 85, 5))
    ax[0].set_yticks(x1)
    df[df['Survivved'] == 1]['Age'].plot.hist(ax=ax[1], bins=20, edgecolor='black', color='red')
    ax[1].set_title('Survived 1')
    x2 = list(range(0, 85, 5))
    ax[1].set_yticks(x2)
    plt.show()
