# OEIS A280537: no four coplanar points in a cube

<!-- oeis-status:begin -->
**OEIS status** (lab registry, 13 Nov 2026):

- [A280537](https://oeis.org/A280537), a(12) >= 31 and a(n) <= 3n (comment of 23 Aug 2026): **approved** (2026-08-23: approved). Certificate: complete.
- [A280537](https://oeis.org/A280537), link to the repository; a(21) >= 47, a(22) >= 49, a(27) >= 56: **queued** (2026-11-13: queued). Certificate: complete.

Rules and the full registry: [athanor-oeis](https://github.com/iwasborninbali/athanor-oeis/blob/main/REGISTRY.md).
<!-- oeis-status:end -->

[A280537](https://oeis.org/A280537) gives the maximum number of points in an n × n × n grid with no four in a plane. The sequence, beginning at n=2, is 5, 8, 10, 13, 16, 18, 20. The OEIS says terms through a(6) were found by exhaustive search, while a(7) and a(8) rest on extensive numerical evidence.

Aleksei Kudriashov's 23 August 2026 OEIS comment gives a(12) ≥ 31 and a(n) ≤ 3n, since every coordinate plane contains at most three points. The [attached file](https://oeis.org/A280537/a280537_4.txt) on the OEIS, credited to Moritz Franckenstein, Aleksei Kudriashov, and Hugo Pfoertner, contains 13 configurations for nonprime sizes between 8 and 18; it states individual credit for n=12, 14, 15, 16 and 18. In particular the n=18 configurations have 43 points; a later 41-point witness is not an improvement.

Later witnesses in `witnesses/` establish a(21) ≥ 47, a(22) ≥ 49 and a(27) ≥ 56, alongside the 31-point n=12 witness; the research note compares them with the 2017 OEIS bounds and with the results of Al Zimmermann's 2016 contest, and these four are the improvements. `A280537_no4coplanar_cube.txt` holds configurations for every n = 9..25, 27, 29; the others confirm or fall below known bounds. The full research note and other bounds are in [paper/a280537_note.tex](paper/a280537_note.tex), archived at [Zenodo 10.5281/zenodo.22023079](https://doi.org/10.5281/zenodo.22023079). These witnesses establish lower bounds, not optimality. The earlier sequence author is Hugo Pfoertner; Walter Möhres is credited for the exhaustive n=6 search.

## Rechecking

[Verification certificate](CERTIFICATE.md) and [prior-art record](PRIOR-ART.md).

```sh
curl -s -o witnesses/oeis-a280537_4.txt https://oeis.org/A280537/a280537_4.txt   # the OEIS file is not redistributed here
python3 -B check_oeis.py
python3 -B witnesses/verify_witness.py 12 witnesses/witness_n12_31_record.txt 31
python3 -B witnesses/verify_witness_2.py --all witnesses
```

The first checks all 13 OEIS-file configurations using exact integer determinants, point counts, distinctness and range. The independent second verifier checks every individual `witness_n*.txt` file for collinear triples and coplanar quadruples. The combined `A280537_no4coplanar_cube.txt` records additional lower-bound configurations; not every one is an improvement over the earlier OEIS file.

## Licence

Aleksei Kudriashov (ORCID 0009-0006-8885-5338), Athanor lab, with AI assistance. Code: MIT; original data and text: CC BY 4.0; see [LICENSE.md](LICENSE.md). The OEIS attachment (with Franckenstein's and Pfoertner's configurations) is not redistributed here; it is downloaded from the OEIS for the check.
