# I/O Operations (Урок 6)

## CSV

``` python
df = pd.read_csv("file.csv")
df.to_csv("out.csv", index=False)
```

## Excel

``` python
df = pd.read_excel("file.xlsx", sheet_name="Sheet1")
df.to_excel("out.xlsx", sheet_name="Report", index=False)
```

## JSON

``` python
df = pd.read_json("file.json")
df.to_json("out.json", orient="records", force_ascii=False, indent=2)
```

## Объединение нескольких файлов

``` python
df1 = pd.read_csv("jan.csv")
df2 = pd.read_csv("feb.csv")
df_all = pd.concat([df1, df2], ignore_index=True)
```