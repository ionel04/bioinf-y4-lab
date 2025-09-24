# Lab 2 — Sequence Alignment (NW, SW, MSA/BLAST)

## Obiective & competențe
- Explici și implementezi aliniere **globală (Needleman–Wunsch)** și **locală (Smith–Waterman)**.
- Înțelegi **scoring** (match/mismatch, gap liniar; noțiuni despre PAM/BLOSUM).
- Rulezi **MSA** (Clustal Omega / orice echivalent) și verifici similaritatea cu **BLAST**.
- Reproductibilitate: Docker/Codespaces, PR cu CI verde.

## Date folosite
Folosim **aceleași fișiere** din `data/sample/` (ex.: `tp53_dna_multi.fasta`, `tp53_protein_multi.fasta`).  
*Nu introducem FASTA-uri “toy” separate; pentru exemple scurte folosim subsecvențe extrase în script (ex. `[:7]`).*

## Structură
labs/02_alignment/
README.md
assignment.md
demo01_pairwise_biopython.py
demo02_distance_matrix.py
ex01_global_needleman_wunsch.py
ex02_local_smith_waterman.py

bash
Copy code

## Rulare rapidă (în container/Codespaces)
```bash
# Demos
python labs/02_alignment/demo01_pairwise_biopython.py \
  --fasta data/sample/tp53_dna_multi.fasta

python labs/02_alignment/demo02_distance_matrix.py \
  --fasta data/sample/tp53_dna_multi.fasta

# Exercitii (completați TODO-urile înainte)
python labs/02_alignment/ex01_global_needleman_wunsch.py --a ACTG --b ACAG
python labs/02_alignment/ex02_local_smith_waterman.py --a TGTTACGG --b GGTTGACTA
Livrabile (PR)
Folder: labs/02_alignment/solutions/<username>/

nw.py, sw.py (sau redenumirile voastre)

fișier MSA (.aln sau .txt) + notițe BLAST (blast_notes.txt)

NOTES.md (≤1 pag. cu explicații și capturi mici)

CI (syntax) trebuie să fie verde.

Timp estimat
~90 min în lab + 60–90 min pentru finalizare.

Resurse
Needleman–Wunsch, Smith–Waterman (articole clasice)

Matrici PAM/BLOSUM (intro): EBI

markdown
Copy code

---

### `labs/02_alignment/assignment.md`
```markdown
# Assignment — Lab 2 (Pachete A–D)

## Pachet A — Distanțe simple (obligatoriu)
1) Calculează **p-distance** și **Hamming distance** pentru toate perechile din `data/sample/tp53_dna_multi.fasta`.
   - Dacă lungimile diferă, **trunchiază** la lungimea minimă (doar pentru acest exercițiu) și menționează în `NOTES.md`.
   - Exportă matricea (CSV sau tabel în `NOTES.md`).

## Pachet B — Alinieri pereche (obligatoriu)
2) **Global (NW, gap liniar)**: completează `ex01_global_needleman_wunsch.py` (TODO).
3) **Local (SW, gap liniar)**: completează `ex02_local_smith_waterman.py` (TODO).
   - Testează cu două perechi scurte (poți folosi secvențe hardcodate).
   - Explică scorurile în `NOTES.md` (1–2 paragrafe).

## Pachet C — MSA + BLAST (obligatoriu)
4) Rulează un **MSA** mic pe 3 secvențe din `tp53_*multi.fasta` (poți selecta primele 3 în editor sau script).
5) Verifică cu **BLAST** una dintre secvențe și notează primele 2 hit-uri (ID + scor pe scurt).

## Pachet D — Bonus (opțional)
6) **Semiglobal** pentru o pereche scurtă (gap gratuit la capete). Comentează diferența de scor vs. NW.
7) **Counting**: pentru două șiruri (≤5), câte alinieri globale distincte există (gap liniar)? Explică metoda.

---

## Predare (PR)
- `labs/02_alignment/solutions/<username>/`
  - `nw.py`, `sw.py`, `msa.aln`/`msa.txt`, `blast_notes.txt`, `NOTES.md` (≤1 pag.)
- CI syntax verde obligatoriu.

## Rubrică (10p)
- A: distanțe corecte + raportare clară (2p)
- B: NW funcțional + teste (3p); SW funcțional + teste (3p)
- C: MSA + BLAST documentate (2p)
- D: +1p bonus (semiglobal / counting)

## Onestitate academică
Lucru în perechi permis; ambii trebuie să înțeleagă codul. Includeți sursele.