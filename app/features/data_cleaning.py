import pandas as pd

#Загрузка сырых (грязных) данных
def load_dirty_data(path: str = "app/data/employees_dirty.csv") -> pd.DataFrame:
    return pd.read_csv(path)

#Вывод информации о пропусках
def check_missing(df: pd.DataFrame):
    print("\n🔎 Пропуски:\n", df.isna().sum())
    return df

#Заполняем пропуски: age на среднее, salary на медиана
def fill_missing(df: pd.DataFrame) -> pd.DataFrame:
    df['age'].fillna(df['age'].mean(), inplace=True)
    df['salary'].fillna(df['salary'].median(), inplace=True)
    return df

#Удаляем дубликаты строк
def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    print(f"\n✅ Удалено дублей: {before - after}")
    return df

#Удаляем аномалии: age < 0 или salary < 10000
def fix_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    before = len(df)
    df = df[(df["age"] >= 0) & (df["salary"] >= 10000)]
    after = len(df)
    print(f"\n✅ Удалено аномальных строк: {before - after}")
    return df

#Убираем пробелы и приводим имена к нижнему регистру
def clean_names(df: pd.DataFrame) -> pd.DataFrame:
    df["name"] = df["name"].str.strip().str.lower()
    return df

#Преобразуем hire_date в datetime и добавляем колонку year
def convert_dates(df: pd.DataFrame) -> pd.DataFrame:
    df["hire_date"] = pd.to_datetime(df["hire_date"], errors="coerce")
    df["year"] = df["hire_date"].dt.year
    return df

def add_age_group(df: pd.DataFrame) -> pd.DataFrame:
    bins = [0, 25, 40, 100]
    labels = ["молодой", "средний", "старший"]
    df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels, right=False)
    return df

import numpy as np

def add_salary_level(df: pd.DataFrame) -> pd.DataFrame:
    conditions = [
        (df["salary"] < 70000),
        (df["salary"].between(70000, 100000)),
        (df["salary"] > 100000)
    ]
    choices = ["низкая", "средняя", "высокая"]
    df["salary_level"] = np.select(conditions, choices, default="неизвестно")
    return df


def add_name_length(df: pd.DataFrame) -> pd.DataFrame:
    df["name_length"] = df["name"].str.len()
    return df

def add_is_newcomer(df: pd.DataFrame) -> pd.DataFrame:
    df["is_newcomer"] = df["year"] >= 2020
    return df


def data_cleaning():
    df = load_dirty_data()

    print("\n=== Исходные данные ===\n", df.head())

    df = check_missing(df)
    df = fill_missing(df)
    df = remove_duplicates(df)
    df = fix_anomalies(df)
    df = clean_names(df)
    df = convert_dates(df)

    # 🔹 Фичи-инжиниринг
    df = add_age_group(df)
    df = add_salary_level(df)
    df = add_name_length(df)
    df = add_is_newcomer(df)

    print("\n=== Итоговые очищенные данные ===\n", df.head())

    df.to_csv("app/data/employees_clean.csv", index=False)
    print("\n💾 Файл сохранён: app/data/employees_clean.csv")