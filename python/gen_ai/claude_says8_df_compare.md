# Prompt
is there a python library that compares two dataframes and returns a simple data structure with the differences? can you generate an example that shows its usage?

# Response

There are two great options here — one built into pandas, and one dedicated library. Here's a rundown:

**1. `pandas.DataFrame.compare()`** — built-in, no extra install needed. Introduced in pandas 1.1.0, it performs element-wise comparison of two DataFrames and returns a new DataFrame highlighting the differences. It requires both DataFrames to have the same shape and index.

**2. `datacompy`** — a dedicated library worth knowing about. It was originally created as a replacement for SAS's `PROC COMPARE` for pandas DataFrames, with more functionality than just `DataFrame.equals()`, including stats and match tolerance. It supports pandas, Spark, Polars, and even Snowflake.

Here's a practical example of both:

```python
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
```

**Key differences between the two:**

| | `df.compare()` | `datacompy` |
|---|---|---|
| Install | Built-in | `pip install datacompy` |
| Join on key column | ❌ (index-based only) | ✅ |
| Human-readable report | ❌ | ✅ |
| Numeric tolerance | ❌ | ✅ |
| Returns plain DataFrame | ✅ | ✅ (via `.all_mismatch()`) |

**Recommendation:** use `df.compare()` for quick checks when both DataFrames share the same index. Use `datacompy` when you need to match on a key column (like an `id`), want a readable summary report, or are working with non-pandas backends like Spark or Polars.