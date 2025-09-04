import pandas as pd

def load_data():
    employees = pd.read_csv("app/data/employees.csv")
    departments = pd.read_csv("app/data/departments.csv")
    cities = pd.read_csv("app/data/cities.csv")
    return employees, departments, cities

#Объединение сотрудников с названиями департаментов
def merge_with_departments(employees: pd.DataFrame, departments: pd.DataFrame) -> pd.DataFrame:
    return employees.merge(departments, on="department_id", how="left")

#Объединение сотрудников с регионами
def merge_with_cities(employees, cities):
    return employees.merge(cities, on="city", how="left")

#Средняя зарплата по департаментам
def avg_salary_by_department(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("department_name")["salary"].mean()

#Количество сотрудников по регионам
def count_employees_by_region(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("region")["id"].count()

#Департамент с максимальной средней зарплатой
def department_with_max_salary(df: pd.DataFrame) -> pd.DataFrame:
    avg_salary = df.groupby("department_name")["salary"].mean()
    return avg_salary.idxmax(), avg_salary.max()

#Количество сотрудников по годам найма
def employees_by_hire_year(df: pd.DataFrame) -> pd.DataFrame:
    df["hire_date"] = pd.to_datetime(df["hire_date"])
    return df.groupby(df["hire_date"].dt.year)["id"].count()

#Сводная таблица: средняя зарплата по регионам и департаментам
def pivot_salary_by_region_department(df: pd.DataFrame) -> pd.DataFrame:
    return pd.pivot_table(
        df,
        values="salary",
        index="region",
        columns="department_name",
        aggfunc="mean",
    )

#Сводная таблица: количество сотрудников по годам и департаментам
def pivot_count_by_year_department(df: pd.DataFrame) -> pd.DataFrame:
    df["hire_date"] = pd.to_datetime(df["hire_date"])
    df["year"] = df["hire_date"].dt.year
    return pd.pivot_table(
        df,
        values="id",
        index="year",
        columns="department_name",
        aggfunc="count",
    )

def company_analysis():
    employees, departments, cities = load_data()

    # Объединение данных
    df = merge_with_departments(employees, departments)
    df = merge_with_cities(df, cities)

    # 1. Средняя зарплата по департаментам
    avg_salary = avg_salary_by_department(df)
    print("\nСредняя зарплата по департаментам:\n", avg_salary)

    # 2. Количество сотрудников по регионам
    count_region = count_employees_by_region(df)
    print("\nКоличество сотрудников по регионам:\n", count_region)

    # 3. Департамент с самой высокой средней зарплатой
    dep, salary = department_with_max_salary(df)
    print(f"\n Департамент с самой высокой средней зарплатой: {dep} ({salary})")

    # 4. Количество сотрудников по годам найма
    hire_years = employees_by_hire_year(df)
    print("\nКоличество сотрудников по годам найма:\n", hire_years)

    # 5. Pivot: средняя зарплата по регионам и департаментам
    pivot_salary = pivot_salary_by_region_department(df)
    print("\nPivot: средняя зарплата по регионам и департаментам:\n", pivot_salary)
    pivot_salary.to_csv("app/data/pivot_salary.csv")

    # 6. Pivot: количество сотрудников по годам и департаментам
    pivot_count = pivot_count_by_year_department(df)
    print("\nPivot: количество сотрудников по годам и департаментам:\n", pivot_count)
    pivot_count.to_csv("app/data/pivot_count.csv")

    return df
