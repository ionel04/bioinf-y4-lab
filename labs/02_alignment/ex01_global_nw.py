#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Schelet: Needleman–Wunsch (global, gap liniar).
Rulare:
  python labs/02_alignment/ex01_global_needleman_wunsch.py --a ACTG --b ACAG
"""
import argparse

def nw_global(a, b, match=1, mismatch=-1, gap=-1):
    n, m = len(a), len(b)
    # 1) TODO: alocați și inițializați matricea de scoruri S (dim (n+1)x(m+1))
    S = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        S[i][0] = i * gap
    for j in range(1, m + 1):
        S[0][j] = j * gap

    # 2) TODO: completați umplerea matricei (diag / sus+gap / stg+gap)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            diag = S[i - 1][j - 1] + (match if a[i - 1] == b[j - 1] else mismatch)
            up = S[i - 1][j] + gap
            left = S[i][j - 1] + gap
            S[i][j] = max(diag, up, left)

    # 3) TODO: backtrack (de la S[n][m]) pentru aliniamentele finale
    i, j = n, m
    al_a, al_b = [], []
    while i > 0 or j > 0:
        current = S[i][j]
        if i > 0 and j > 0 and current == S[i - 1][j - 1] + (match if a[i - 1] == b[j - 1] else mismatch):
            al_a.append(a[i - 1]); al_b.append(b[j - 1]); i -= 1; j -= 1
        elif i > 0 and current == S[i - 1][j] + gap:
            al_a.append(a[i - 1]); al_b.append('-'); i -= 1
        else:
            al_a.append('-'); al_b.append(b[j - 1]); j -= 1

    score = S[n][m]
    return score, ''.join(reversed(al_a)), ''.join(reversed(al_b))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True)
    ap.add_argument("--b", required=True)
    args = ap.parse_args()
    score, aa, bb = nw_global(args.a, args.b)
    print("Score:", score)
    print(aa)
    print(bb)

if __name__ == "__main__":
    main()
