"""الملف 1: توليد بيانات مصروفات تجريبية باستخدام numpy + pandas"""
import numpy as np
import pandas as pd


def generate_data(n=300, seed=42):
    rng = np.random.default_rng(seed)

    categories = ["Food", "Transport", "Bills", "Entertainment", "Shopping", "Health"]
    probabilities = [0.35, 0.20, 0.10, 0.15, 0.15, 0.05]
    amount_ranges = {
        "Food": (30, 300),
        "Transport": (10, 150),
        "Bills": (200, 900),
        "Entertainment": (50, 500),
        "Shopping": (100, 1500),
        "Health": (80, 800),
    }

    # تواريخ عشوائية على مدار 9 شهور
    days = rng.integers(0, 270, n)
    dates = pd.to_datetime("2026-01-01") + pd.to_timedelta(days, unit="D")

    cats = rng.choice(categories, size=n, p=probabilities)
    amounts = [round(rng.uniform(*amount_ranges[c]), 2) for c in cats]

    df = pd.DataFrame({"date": dates, "category": cats, "amount": amounts})
    return df.sort_values("date").reset_index(drop=True)


if __name__ == "__main__":
    df = generate_data()
    df.to_csv("expenses.csv", index=False)
    print("تم إنشاء expenses.csv")
    print(df.head())