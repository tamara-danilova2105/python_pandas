# Advanced Pandas

## Объединения таблиц

``` python
# Объединение по ключу
pd.merge(df1, df2, on="key", how="left")   # left join
pd.merge(df1, df2, on="key", how="inner")  # inner join

# Склеивание
pd.concat([df1, df2])            # по строкам
pd.concat([df1, df2], axis=1)    # по колонкам
```

------------------------------------------------------------------------

## Сводные таблицы (Pivot)

``` python
pd.pivot_table(
    df,
    values="salary",              # что считаем
    index="region",               # строки
    columns="department_name",    # колонки
    aggfunc="mean"                # функция агрегации
)
```

------------------------------------------------------------------------

## Работа с датами

``` python
df["hire_date"] = pd.to_datetime(df["hire_date"])  # строку → дату
df["year"] = df["hire_date"].dt.year               # год
df["month"] = df["hire_date"].dt.month             # месяц
df.groupby("year")["id"].count()                   # количество по годам
```

------------------------------------------------------------------------

## Продвинутые методы

-   `df.query("age > 30 and city == 'Moscow'")` --- фильтрация через
    строку\
-   `df.apply(func, axis=1)` --- применить функцию к строкам\
-   `df["col"].map(func)` --- применить функцию к значениям колонки\
-   `df.value_counts()` --- количество уникальных значений
