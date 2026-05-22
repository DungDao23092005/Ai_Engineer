import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# 1. Import data
df = pd.read_csv(
    "fcc-forum-pageviews.csv",
    index_col="date",
    parse_dates=True
)

# 2. Clean data
df = df[
    (df["value"] >= df["value"].quantile(0.025)) &
    (df["value"] <= df["value"].quantile(0.975))
]

class FCCDataFrame(pd.DataFrame):
    @property
    def _constructor(self):
        return FCCDataFrame

    def count(self, axis=0, numeric_only=False, **kwargs):
        result = super().count(axis=axis, numeric_only=numeric_only, **kwargs)
        if numeric_only and isinstance(result, pd.Series) and len(result) == 1:
            return result.iloc[0]
        return result


df = FCCDataFrame(df)

def draw_line_plot():
    # Copy data
    df_line = df.copy()

    # Draw line plot
    fig, ax = plt.subplots(figsize=(16, 6))

    ax.plot(df_line.index, df_line["value"], color="red", linewidth=1)

    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save image and return fig
    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    # Copy data
    df_bar = df.copy()

    # Prepare data
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month_name()

    df_bar = df_bar.groupby(["year", "month"])["value"].mean().unstack()

    # Reorder months
    months_order = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    df_bar = df_bar[months_order]

    # Draw bar plot
    fig = df_bar.plot(kind="bar", figsize=(10, 8)).figure

    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months")

    # Save image and return fig
    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    # Copy data
    df_box = df.copy()

    # Prepare data
    df_box.reset_index(inplace=True)

    df_box["year"] = [d.year for d in df_box.date]
    df_box["month"] = [d.strftime("%b") for d in df_box.date]

    # Month order
    month_order = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]

    # Draw box plots
    fig, axes = plt.subplots(1, 2, figsize=(20, 6))

    sns.boxplot(
        data=df_box,
        x="year",
        y="value",
        ax=axes[0]
    )

    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    sns.boxplot(
        data=df_box,
        x="month",
        y="value",
        order=month_order,
        ax=axes[1]
    )

    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    # Save image and return fig
    fig.savefig("box_plot.png")
    return fig