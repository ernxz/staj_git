import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector

titanic_data = pd.read_csv("D:/titanic.csv")
#print(titanic_data)

def degiskenler(variable):
    cat = titanic_data[variable]
    sayi = cat.value_counts()
    plt.figure(figsize=(9,3))
    plt.bar(sayi.index,sayi)
    plt.xticks(sayi.index,sayi.index.values)
    plt.ylabel("freakans")
    plt.title(variable)
    plt.show()
    print(variable,sayi)

kategori1 = ["Survived", "Pclass", "Embarked","SibSp","Parch"]

for i in kategori1:
    degiskenler(i)
def hayattakalma():
    connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="kutuphane_yerel"
)
    cursor = connection.cursor()
    titanic_data.fillna({'Cabin':'Bilinmiyor'}, inplace=True)
    titanic_data['Survival Rate'] = 0
    for index, row in titanic_data.iterrows():
       age = row['Age']
       pclass = row['Pclass']
       cabin = row["Cabin"]
       score = 0
       if 20 < age < 40:
           score = 40 + score
       elif 40 < age:
           score = 20 + score
       elif 0 < age < 20: 
           score = 30 + score
       if pclass > 0:
           score = 20 + score
       elif pclass == 0:
           score = 40 + score
       if cabin == "Bilinmiyor":
           score = 100
       survival_percentage = score
       titanic_data.at[index, 'Survival Rate'] = survival_percentage
       cursor.execute("""
        INSERT INTO titanic (survival_rate)
        VALUES (%s)
       """, (survival_percentage,))
    connection.commit()
    cursor.close()
    connection.close()   
    print (titanic_data['Survival Rate'])
    titanic_data.to_csv('D:/titanic.csv', index=False)
    cat1 = titanic_data['Survival Rate']
    sayi = cat1.value_counts()
    plt.figure(figsize=(9, 3))
    plt.bar(sayi.index, sayi)
    plt.xticks(sayi.index, sayi.index.values, rotation=45)
    plt.ylabel("Frekans")
    plt.title('Survival Rate')
    plt.show()
hayattakalma()
