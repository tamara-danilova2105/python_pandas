import pandas as pd

#Series = колонка (или одна строка).
#DataFrame = таблица (строки + колонки).

def load_data(path="app/data/people.csv"):
    return pd.read_csv(path) #pd.read_csv один из способов загрузить данные.

def add_is_adult(df):
    df["is_adult"] = df["age"] >= 18 #возвращает Series (колонку из True/False) и создаёт новый столбец в таблице
    return df

def get_info_lesson_one(df):
    print('первые 5 строк', df.head())
    print('типы колонок', df.info())
    print('статистика по числовым колонкам', df.describe())
    print('уникальные города', df["city"].unique())
    print('фильтрация только взрослых', df[df["is_adult"]])
    print('Средний возраст', df["age"].mean())
    print('Максимальная зарплата', df["salary"].max())
    return df

def save_data(df, path="app/data/people_processed.csv"): #df.to_csv сохраняет DataFrame обратно в CSV.
    df.to_csv(path, index=False) #index=False убирает индекс (0,1,2) из файла, чтобы CSV выглядел чисто.

def add_salary_in_k(df: pd.DataFrame) -> pd.DataFrame:
    df["salary_in_k"] = df["salary"] / 1000 #Добавляем колонку salary_in_k = зарплата в тысячах
    return df

def group_by_city(df: pd.DataFrame) -> pd.DataFrame:
    print('Средняя зарплата по городам', df.groupby("city")["salary"].mean())
    return df

def sort_by_age(df: pd.DataFrame) -> pd.DataFrame:
    print('Сортировка по возраст (убывание):', df.sort_values("age", ascending=False))
    return df

def filter_age_30_plus(df: pd.DataFrame) -> pd.DataFrame:
    print('Люди старше 30 лет', df[df["age"] >= 30])
    return df

def filter_moscow(df: pd.DataFrame) -> pd.DataFrame:
    print('Живут в Москве', df[df["city"] == 'Moscow'])
    return df

def count_people_by_city(df: pd.DataFrame) -> pd.DataFrame:
    print("Количество людей по городам", df['city'].value_counts())
    return df

def city_with_max_avg_salary(df: pd.DataFrame) -> pd.DataFrame:
    avg_salary = df.groupby("city")["salary"].mean()
    print("Город с максимальной зарплатой", avg_salary.idxmax())
    return df

def names_to_lower(df: pd.DataFrame) -> pd.DataFrame:
    df['name_lower'] = df['name'].str.lower() #Перевод имен в нижний регистр
    return df

def add_has_a(df: pd.DataFrame) -> pd.DataFrame:
    df['has_a'] = df['name'].str.contains('a', case=False) #Добавляем колонку содержит ли имя букву a
    return df

def add_name_length(df: pd.DataFrame) -> pd.DataFrame:
    df['name_length'] = df["name"].str.len() #Добавляем колонку длина имени
    return df

def filter_adults_novosib(df: pd.DataFrame) -> pd.DataFrame:
    print("Взрослые из Новосибирска", df[(df['is_adult']) & (df['city'] == 'Novosibirsk')])
    return df

def top_2_by_salary(df: pd.DataFrame) -> pd.DataFrame:
    print("Топ 2 по зп", df.sort_values('salary', ascending=False).head(2))
    return df

def stats_by_city(df: pd.DataFrame) -> pd.DataFrame:
    stats = df.groupby('city').agg(
        avg_age=('age', 'mean'),
        avg_salary=('salary', 'mean'),
        adults=('is_adult', 'sum')
    )
    print('Средний возраст, зарплата и количество взрослых по каждому городу', stats)
    return df

def build_features():
    df = load_data()
    df = add_is_adult(df)
    df = get_info_lesson_one(df)
    df = add_salary_in_k(df)
    df = group_by_city(df)
    df = sort_by_age(df)
    df = filter_age_30_plus(df)
    df = filter_moscow(df)
    df = count_people_by_city(df)
    df = city_with_max_avg_salary(df)
    df = names_to_lower(df)
    df = add_has_a(df)
    df = add_name_length(df)
    df = filter_adults_novosib(df)
    df = top_2_by_salary(df)
    df = stats_by_city(df)
    save_data(df)
    print("✅ Обработка завершена")