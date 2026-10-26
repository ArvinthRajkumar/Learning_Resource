def cost_seq_scan(pages, cpu_per_row=0.01, rows=0): return pages * 1.0 + rows * cpu_per_row
def cost_index(selected_rows, tree_height=3): return tree_height + selected_rows * 1.0 + selected_rows * 0.01   # about one random page per row
table_pages, table_rows = 10_000, 1_000_000
for pct in (0.001, 0.01, 0.1, 1, 5, 20):
    sel = int(table_rows * pct / 100)
    seq, idx = cost_seq_scan(table_pages, rows=table_rows), cost_index(sel)
    print(f"keeps {pct:>6}% of rows ({sel:>7,}): scan cost {seq:>9,.0f} vs index cost {idx:>9,.0f} -> {'index' if idx < seq else 'scan'}")
