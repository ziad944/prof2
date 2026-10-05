"""الملف 4: الملف الرئيسي - شغّله وهو يعمل كل حاجة"""
import os
import matplotlib.pyplot as plt

from data_generator import generate_data
from analysis import (load_data, total_by_category, total_by_month,
                      basic_stats, top_expenses, unusual_expenses)
from charts1 import (plot_category_bar, plot_monthly_line,
                    plot_category_pie, plot_amount_hist)


def main():
    # 1) أنشئ البيانات لو مش موجودة
    if not os.path.exists("expenses.csv"):
        generate_data().to_csv("expenses.csv", index=False)

    # 2) حمّل وحلّل
    df = load_data()
    by_cat = total_by_category(df)
    by_month = total_by_month(df)

    print("=== Basic Stats ===")
    for k, v in basic_stats(df).items():
        print(f"{k}: {v:,.2f}")

    print("\n=== Total by Category ===")
    print(by_cat)

    print("\n=== Top 5 Expenses ===")
    print(top_expenses(df))

    print("\n=== Unusual Expenses ===")
    print(unusual_expenses(df))

    # 3) ارسم
    plot_category_bar(by_cat)
    plot_monthly_line(by_month)
    plot_category_pie(by_cat)
    plot_amount_hist(df)
    print("\nتم حفظ الرسومات في فولدر output")
    plt.show()


if __name__ == "__main__":
    main()