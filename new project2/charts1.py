"""الملف 3: الرسومات باستخدام matplotlib"""
import os
import matplotlib.pyplot as plt

OUTPUT_DIR = "output"


def _save(fig, name):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    fig.savefig(os.path.join(OUTPUT_DIR, name), dpi=150, bbox_inches="tight")


def plot_category_bar(by_category):
    fig, ax = plt.subplots(figsize=(8, 5))
    by_category.plot(kind="bar", ax=ax, color="#4c9be8")
    ax.set_title("Total Spending by Category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Amount (EGP)")
    plt.xticks(rotation=45)
    _save(fig, "category_bar.png")
    return fig


def plot_monthly_line(by_month):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(by_month.index, by_month.values, marker="o", color="#e8744c")
    ax.set_title("Monthly Spending")
    ax.set_xlabel("Month")
    ax.set_ylabel("Amount (EGP)")
    ax.grid(alpha=0.3)
    plt.xticks(rotation=45)
    _save(fig, "monthly_line.png")
    return fig


def plot_category_pie(by_category):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(by_category.values, labels=by_category.index, autopct="%1.1f%%")
    ax.set_title("Spending Share by Category")
    _save(fig, "category_pie.png")
    return fig


def plot_amount_hist(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df["amount"], bins=20, color="#6bbf59", edgecolor="white")
    ax.set_title("Distribution of Expense Amounts")
    ax.set_xlabel("Amount (EGP)")
    ax.set_ylabel("Count")
    _save(fig, "amount_hist.png")
    return fig