import pandas as pd
import matplotlib.pyplot as plt

#Загружаем данные и готовим hire_date
def load_clean_data(path: str = "app/data/employees_clean.csv") -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["hire_date"])
    df = df.dropna(subset=["hire_date"])       # убираем пустые даты
    df = df.set_index("hire_date").sort_index()
    return df

#Количество сотрудников по годам
def resample_by_year(df: pd.DataFrame):
    hires = df.resample("Y")["id"].count()
    print("\n✅ Количество сотрудников по годам:\n", hires)
    hires.plot(title="Найм сотрудников по годам", marker="o")
    plt.ylabel("Сотрудников")
    plt.show()

#Средняя зарплата по месяцам
def resample_by_month(df: pd.DataFrame):
    avg_salary = df.resample("M")["salary"].mean()
    print("\n✅ Средняя зарплата по месяцам:\n", avg_salary)
    avg_salary.plot(title="Средняя зарплата по месяцам")
    plt.ylabel("Зарплата")
    plt.show()

#Скользящее среднее зарплаты (3 месяца)
def rolling_avg_salary(df: pd.DataFrame):
    rolling_salary = df["salary"].resample("M").mean().rolling(window=3).mean()
    print("\n✅ Скользящее среднее зарплаты (3 месяца):\n", rolling_salary)
    rolling_salary.plot(title="Скользящее среднее зарплаты (3 месяца)")
    plt.ylabel("Зарплата")
    plt.show()

#Срез данных по датам
def slice_by_date(df: pd.DataFrame):
    try:
        print("\n✅ Все за 2020 год:\n", df.loc["2020"])
    except KeyError:
        print("\n⚠️ Нет данных за 2020 год")

    try:
        print("\n✅ Январь–Июнь 2020:\n", df.loc["2020-01":"2020-06"])
    except KeyError:
        print("\n⚠️ Нет данных за Январь–Июнь 2020")


def time_series():
    df = load_clean_data()

    resample_by_year(df)
    resample_by_month(df)
    rolling_avg_salary(df)
    slice_by_date(df)

