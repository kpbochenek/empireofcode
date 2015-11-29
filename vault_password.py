def golf(p): return len(p)>9 and p!=p.lower() and p!=p.upper() and any('0'<=l and l<='9' for l in p)
