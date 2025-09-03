# ⏱ Time Series (Урок 5)

## Подготовка дат

``` python
df["hire_date"] = pd.to_datetime(df["hire_date"])
df = df.set_index("hire_date").sort_index()
```

## Resample (агрегация по периодам)

``` python
df.resample("M")["salary"].mean()   # средняя зарплата по месяцам
df.resample("Y")["id"].count()      # количество сотрудников по годам
```

## Rolling (скользящее среднее)

``` python
df["salary"].resample("M").mean().rolling(window=3).mean()
```

## Срезы по датам

``` python
df.loc["2020"]                # все строки за 2020 год
df.loc["2020-01":"2020-06"]   # январь–июнь 2020
```