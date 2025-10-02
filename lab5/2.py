# requirements: pandas, numpy
# pip install pandas numpy openpyxl

import numpy as np
import pandas as pd
import sys

def process_dataset(path, column, sample_size=1000, replace=False, out_name="surname.csv"):
    # 1) Загрузка (поддержка csv и xlsx)
    if path.lower().endswith(('.xls', '.xlsx')):
        df = pd.read_excel(path)
    else:
        df = pd.read_csv(path)
    print(f"Исходный датасет: {df.shape[0]} строк, {df.shape[1]} колонок")

    # 2) Выбор колонки (если None - возьмём весь датасет и будем работать по первой числовой колонке)
    if column is None:
        # находим первую числовую колонку
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) == 0:
            raise ValueError("В датасете нет числовых колонок. Укажите колонку вручную.")
        column = numeric_cols[0]
        print(f"Колонка не указана — выбрана первая числовая колонка: '{column}'")

    if isinstance(column, int):
        colname = df.columns[column]
    else:
        colname = column

    if colname not in df.columns:
        raise ValueError(f"Колонка '{colname}' не найдена в датасете.")

    series = df[colname]
    print(f"Работаем с колонкой: {colname}")

    # 2.2) Взять 1000 значений (случайная выборка)
    n = sample_size
    if len(series) < n and not replace:
        print(f"В колонке только {len(series)} значений, а sample_size={n} и replace=False — будут взяты все значения.")
        sampled = series.copy()
    else:
        sampled = series.sample(n=n, replace=replace, random_state=42).reset_index(drop=True)

    # 2.3) Проверить данные на пропуски
    missing_count = sampled.isna().sum()
    print(f"Пропущенных значений в выборке: {missing_count}")

    # 2.4) Заполнить пропуски и обработать аномалии.
    # Стратегия: заполнить медианой (для чисел). Для немедленных аномалий — отбросить значения, выходящие за границы z-score>3
    # Переведём в числовой тип, где возможно
    sampled_numeric = pd.to_numeric(sampled, errors='coerce')

    # Заполнение пропусков медианой
    med = sampled_numeric.median()
    sampled_filled = sampled_numeric.fillna(med)
    print(f"Медиана для заполнения пропусков: {med}")

    # Обработка аномалий — z-score
    arr = sampled_filled.to_numpy(dtype=float)
    mean = arr.mean()
    std = arr.std(ddof=0)
    if std == 0:
        z = np.zeros_like(arr)
    else:
        z = (arr - mean) / std
    mask = np.abs(z) <= 3  # True — нормальные
    outliers_count = np.sum(~mask)
    print(f"Найдены аномалий (|z|>3): {outliers_count}")

    # Стратегия: заменить аномалии на ближайшую допустимую границу (mean +/- 3*std) или на медиану
    upper = mean + 3*std
    lower = mean - 3*std
    arr_clipped = np.clip(arr, lower, upper)

    # Собираем финальный массив
    final = arr_clipped

    # 2.5) Провести полный анализ — базовая статистика
    stats = {
        "count": int(len(final)),
        "mean": float(np.mean(final)),
        "median": float(np.median(final)),
        "std": float(np.std(final)),
        "min": float(np.min(final)),
        "25%": float(np.percentile(final, 25)),
        "75%": float(np.percentile(final, 75)),
        "max": float(np.max(final)),
        "outliers_detected": int(outliers_count),
        "missing_before": int(missing_count)
    }
    print("Статистика по обработанной выборке:")
    for k, v in stats.items():
        print(f"  {k}: {v}")

    # 2.6) Сохранить итоговый обработанный массив без выбросов и пропусков в файл
    df_out = pd.DataFrame({colname: final})
    df_out.to_csv(out_name, index=False, float_format="%.6f")
    print(f"Итоговый обработанный файл сохранён как: {out_name}")

    return df_out, stats

if __name__ == "__main__":
    # Пример использования:
    # python process.py data.csv column_name 1000 False Ivanov.csv
    if len(sys.argv) >= 3:
        path = sys.argv[1]
        column = sys.argv[2]
        if column.lower() == "none":
            column = None
    else:
        # тестовые значения, замените при запуске
        path = "data.csv"
        column = None

    # можно изменить параметры
    out_df, stats = process_dataset(path=path, column=column, sample_size=1000, replace=False, out_name="surname.csv")
