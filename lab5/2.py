import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import kagglehub

def copy_dataset(name):
    path = kagglehub.dataset_download("miadul/lifestyle-and-health-risk-prediction")
    file_path = path + name
    df = pd.read_csv(file_path)
    print("Датасет успешно загружен!\n")
    print(df.head(), "\n")
    return df

def clean(df):

    print("Проверка пропусков:")
    print(df_sample.isnull().sum(), "\n")

    for column in df.columns:
        if df[column].dtype in [np.float64, np.int64]:
            df[column] = df[column].fillna(df[column].median())
        else:
            df[column] = df[column].fillna(df[column].mode()[0])



    cols = df.select_dtypes(include=[np.number]).columns
    Q1 = df[cols].quantile(0.25)
    Q3 = df[cols].quantile(0.75)
    IQR = Q3 - Q1
    df_clean = df[~((df[cols] < (Q1 - 1.5 * IQR)) | 
                        (df[cols] > (Q3 + 1.5 * IQR))).any(axis=1)]
    
    print("Пропуски заполнены, аномалии обработаны. Осталось строк:", len(df), "\n")

    return cols,df_clean

def show_corel(df):
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.select_dtypes(include=[np.number]).corr(), annot=True, cmap="coolwarm")
    plt.title("Корреляция числовых признаков")
    plt.show()

def show_gist(df):
    num_col = numeric_cols[0]
    plt.figure(figsize=(8, 4))
    sns.histplot(df[num_col], bins=20, kde=True)
    plt.title(f"Распределение признака: {num_col}")
    plt.show()

if __name__ == "__main__":

    df = copy_dataset("/Lifestyle_and_Health_Risk_Prediction_Synthetic_Dataset.csv")
    df_sample = df.sample(1000, random_state=42)
    print("Выборка из 1000 строк:")
    print(df_sample.head(), "\n")

  
    numeric_cols, df_clean = clean(df_sample)
    

    print("Анализ данных:")
    print(df_clean.describe(), "\n")

    show_corel(df_clean)
    show_gist(df_clean)
    

    df_clean.to_csv("lab5/Результаты.csv", index=False, encoding='utf-8')
    print("Файл 'Результаты.csv' успешно сохранён!")
