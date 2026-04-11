import pandas as pd
import datacompy  # pip install datacompy

# --- Sample DataFrames ---
df1 = pd.DataFrame({
    "id":     [1,    2,       3,    4],
    "name":   ["Alice", "Bob", "Carol", "Dave"],
    "score":  [88,   95,      70,   60],
    "grade":  ["B",  "A",     "C",  "D"],
})

df2 = pd.DataFrame({
    "id":     [1,    2,       3,    4],
    "name":   ["Alice", "Bob", "Carol", "Dave"],
    "score":  [88,   91,      70,   65],   # Bob and Dave changed
    "grade":  ["B",  "A+",    "C",  "D"],  # Bob's grade changed
})

# ── Option 1: pandas built-in ──────────────────────────────────────────────
diff = df1.compare(df2)
print("=== pandas .compare() ===")
print(diff)
# Output: multi-level columns showing (self / other) for each changed cell
#        score       grade
#         self other  self other
# 1       95.0  91.0     A    A+
# 3       60.0  65.0   NaN   NaN

# Tip: align_axis=0 stacks rows instead of columns (often easier to read)
diff_rows = df1.compare(df2, align_axis=0)
print("\n=== .compare(align_axis=0) ===")
print(diff_rows)

# ── Option 2: datacompy ────────────────────────────────────────────────────
compare = datacompy.Compare(
    df1, df2,
    join_columns="id",       # key column to match rows on
    abs_tol=0,               # absolute tolerance for numeric comparisons
    rel_tol=0,
    df1_name="original",
    df2_name="updated",
)

print("\n=== datacompy report ===")
print(compare.report())

# Programmatic access to the differences as plain DataFrames:
print("Rows only in df1:\n", compare.df1_unq_rows)
print("Rows only in df2:\n", compare.df2_unq_rows)
print("Rows with differences:\n", compare.all_mismatch())