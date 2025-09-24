#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Schelet: Smith–Waterman (local, gap liniar).
Rulare:
  python labs/02_alignment/ex02_local_smith_waterman.py --a TGTTACGG --b GGTTGACTA
"""
import argparse

def sw_local(a, b, match=2, mismatch=-1, gap=-2):
    n, m = len(a), len(b)
    # 1) matrice S zero-init (condiție locală)
    S = [[0] * (m + 1) for _ in range(n + 1)]
    best = (0, 0, 0)  # (score, i, j)

    # 2) umplere
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            diag = S[i - 1][j - 1] + (match if a[i - 1] == b[j - 1] else mismatch)
            up = S[i - 1][j] + gap
            left = S[i][j - 1] + gap
            S[i][j] = max(0, diag, up, left)
            if S[i][j] > best[0]:
                best = (S[i][j], i, j)

    # 3) backtrack până la valoare zero
    score, i, j = best
    al_a, al_b = [], []
    while i > 0 and j > 0 and S[i][j] > 0:
        if S[i][j] == S[i - 1][j - 1] + (match if a[i - 1] == b[j - 1] else mismatch):
            al_a.append(a[i - 1]); al_b.append(b[j - 1]); i -= 1; j -= 1
        elif S[i][j] == S[i - 1][j] + gap:
            al_a.append(a[i - 1]); al_b.append('-'); i -= 1
        else:
            al_a.append('-'); al_b.append(b[j - 1]); j -= 1

    return score, ''.join(reversed(al_a)), ''.join(reversed(al_b))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True)
    ap.add_argument("--b", required=True)
    args = ap.parse_args()
    score, aa, bb = sw_local(args.a, args.b)
    print("Score:", score)
    print(aa)
    print(bb)

if __name__ == "__main__":
    main()
