#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Create a calendar heatmap of daily lifting totals."""

from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd
import july
from july.utils import date_range
import matplotlib.pyplot as plt


script_dir = Path(__file__).resolve().parent
filename = script_dir.parent / "data_csv" / "fitness_lifting.csv"
outfilename = 'C:\\Users\\User\\ownCloud\\Documents\\fitness\\lifting_latest.png'

df = pd.read_csv(filename)
df["date"] = pd.to_datetime(df["date"], format="%d.%m.%Y", errors="coerce")
df["sum"] = pd.to_numeric(df["sum"], errors="coerce").fillna(0)

valid_dates = df["date"].dropna()
if valid_dates.empty:
    raise ValueError(f"No valid dates found in {filename}")

year = int(valid_dates.dt.year.max())
dates = date_range(f"{year}-01-01", f"{year}-12-31")
data = np.zeros(len(dates), dtype=int)
year_start = datetime(year, 1, 1)

for _, row in df.dropna(subset=["date"]).iterrows():
    date = row["date"].to_pydatetime()
    if date.year == year:
        data[(date - year_start).days] += int(row["sum"])

july.heatmap(dates, data, title="Fitness Lifting", cmap="github")
plt.savefig(outfilename)
