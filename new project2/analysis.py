"""الملف 2: تحليل البيانات باستخدام pandas + numpy"""
import numpy as np
import pandas as pd


def load_data(path="expenses.csv"):
    df = pd.read_csv(path, parse_dates=["date"])
    df["month"] = df["date"].dt.to_period("M").astype(str)
    return df


def total_by_category(df):
    return df.groupby("category")["amount"].sum().sort_values(ascending=False)


def total_by_month(df):
    return df.groupby("month")["amount"].sum()


def basic_stats(df):
    amounts = df["amount"].to_numpy()
    return {
        "Total": np.sum(amounts),
        "Average": np.mean(amounts),
        "Median": np.median(amounts),
        "Std": np.std(amounts),
        "Max": np.max(amounts),
        "Min": np.min(amounts),
    }


def top_expenses(df, n=5):
    return df.nlargest(n, "amount")


def unusual_expenses(df):
    """المصروفات الغريبة: أكبر من المتوسط + 2 انحراف معياري"""
    limit = df["amount"].mean() + 2 * df["amount"].std()
    return df[df["amount"] > limit]