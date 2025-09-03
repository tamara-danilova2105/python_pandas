# 📊 Visualization (Урок 4)

## Гистограмма (распределение)

``` python
df["age"].plot(kind="hist", bins=10, title="Распределение возраста")
```

## Столбчатая диаграмма

``` python
df.groupby("city")["salary"].mean().plot(kind="bar", title="Средняя зарплата по городам")
```

## Линейный график

``` python
df.groupby("year")["id"].count().plot(kind="line", marker="o", title="Найм по годам")
```

## Круговая диаграмма

``` python
df["salary_level"].value_counts().plot(kind="pie", autopct="%1.1f%%", title="Распределение уровней зарплаты")
```

## Boxplot (ящик с усами)

``` python
df["salary"].plot(kind="box", title="Boxplot зарплат")
```
