import pandas as pd
import matplotlib.pyplot as plt


def load_clean_data(path: str = "app/data/employees_clean.csv") -> pd.DataFrame:
    return pd.read_csv(path)

#Гистограмма возраста сотрудников
def plot_age_distribution(df: pd.DataFrame):
    df["age"].plot(kind="hist", bins=10, title="Распределение возраста")
    plt.xlabel("Возраст")
    plt.ylabel("Количество сотрудников")
    plt.show()

#Средняя зарплата по городам
def plot_avg_salary_by_city(df: pd.DataFrame):
    avg_salary = df.groupby("city")["salary"].mean()
    avg_salary.plot(kind="bar", title="Средняя зарплата по городам")
    plt.ylabel("Зарплата")
    plt.show()

#Динамика найма по годам
def plot_hiring_trend(df: pd.DataFrame):
    hires = df.groupby("year")["id"].count()
    hires.plot(kind="line", marker="o", title="Количество сотрудников по годам")
    plt.ylabel("Сотрудников")
    plt.show()

#Круговая диаграмма распределения зарплатных уровней
def plot_salary_level_distribution(df: pd.DataFrame):
    df["salary_level"].value_counts().plot(
        kind="pie", autopct="%1.1f%%", title="Распределение уровней зарплаты"
    )
    plt.ylabel("")
    plt.show()

#Boxplot зарплат
def plot_salary_boxplot(df: pd.DataFrame):
    df["salary"].plot(kind="box", title="Boxplot зарплат")
    plt.ylabel("Зарплата")
    plt.show()


def visualization():
    df = load_clean_data()

    plot_age_distribution(df)
    plot_avg_salary_by_city(df)
    plot_hiring_trend(df)
    plot_salary_level_distribution(df)
    plot_salary_boxplot(df)

