import csv as csv
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def save_test_result(td, op):
    result_file = open("E:/data_mining/project/titanic/data/result.csv", "w", newline ='')
    result_writer = csv.writer(result_file)
    result_writer.writerow(["PassengerId", "Survived"])
    size = len(op);
    for i in range(size):
        print([td.PassengerId[i], int(op[i])])
        result_writer.writerow([td.PassengerId[i],int(op[i])])
    result_file.close()

def clean_and_fill_df(df):
    df['Sex'] = df['Sex'].map({'female':0, 'male':1}).astype(int)
    df['EmbarkedFill'] = df['Embarked']
    df.loc[df.Embarked.isnull(), 'EmbarkedFill'] = 'C'
    df['EmbarkedFill'] = df['EmbarkedFill'].map({'C':0, 'Q':1, 'S':2}).astype(int)

    #fill age data
    median_ages = np.zeros((2, 3))

    for i in range(0, 2):
        for j in range(0, 3):
            median_ages[i, j] = df[(df['Sex'] == i) & (df['Pclass'] == j+1)]['Age'].dropna().median()

    df['AgeFill'] = df['Age']

    for i in range(0, 2):
        for j in range(0, 3):
            df.loc[(df.Age.isnull()) & (df.Sex == i) & (df.Pclass == j + 1), 'AgeFill'] = median_ages[i, j]

    #fare
    df['FareFill'] = df['Fare']
    df.loc[df.Fare.isnull(), 'FareFill'] = df.Fare.dropna().mean()

    df=df.drop(['Name', 'PassengerId', 'Cabin', 'Embarked', 'Ticket', 'Age', 'Fare'], axis=1)

    print(df.head(10))
    return df.values;


train_df = pd.read_csv('E:/data_mining/project/titanic/data/train.csv', header=0)
train_data = clean_and_fill_df(train_df)

test_df = pd.read_csv('E:/data_mining/project/titanic/data/test.csv', header=0)
test_data = clean_and_fill_df(test_df)

forest = RandomForestClassifier()
forest = forest.fit(train_data[0::, 1::], train_data[0::, 0])
output = forest.predict(test_data)
print(output)
save_test_result(test_df, output)

