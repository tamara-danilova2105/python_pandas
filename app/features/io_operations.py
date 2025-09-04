import pandas as pd


def load_csv(path="app/data/employees_clean.csv"):
    return pd.read_csv(path)


def save_csv(df, path="app/data/exported.csv"):
    df.to_csv(path, index=False)
    print(f"CSV сохранён: {path}")


def load_excel(path="app/data/employees.xlsx"):
    return pd.read_excel(path, sheet_name="Sheet1")


def save_excel(df, path="app/data/report.xlsx"):
    df.to_excel(path, sheet_name="Report", index=False)
    print(f"Excel сохранён: {path}")


def load_json(path="app/data/employees.json"):
    return pd.read_json(path)


def save_json(df, path="app/data/employees_out.json"):
    df.to_json(path, orient="records", force_ascii=False, indent=2)
    print(f"JSON сохранён: {path}")

#Склеиваем несколько CSV в один
def concat_multiple(files: list[str]) -> pd.DataFrame:
    dfs = [pd.read_csv(f) for f in files]
    return pd.concat(dfs, ignore_index=True)


def io_operations():
    df = load_csv()

    # CSV
    save_csv(df)

    # Excel
    save_excel(df)

    # JSON
    save_json(df)

    # Concat нескольких CSV
    combined = concat_multiple([
        "app/data/employees_clean.csv",
        "app/data/employees_clean.csv"
    ])
    print("\n Объединённые данные (2 файла):\n", combined.head())
