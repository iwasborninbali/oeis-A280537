# Verification certificate

## Claim

- a(12) >= 31.
- a(n) <= 3n, since each of n coordinate planes contains at most three points.
- a(21) >= 47.
- a(22) >= 49.
- a(27) >= 56.
- Link to this repository (queued).

## Evidence

| What | Repository path | Author and date | Coverage | Result | Independence / shared code or data |
|---|---|---|---|---|---|
| Witness check | `witnesses/verify_witness_2.py`, `witnesses/witness_n{12,21,22,27}_*_record.txt` | Athanor lab, individual authors and exact dates not stated | Four stated lower bounds; exact integer tests | All four pass, among 16 clean witnesses | Separate verifier according to README; same producer witness data; code independence beyond that statement not established |
| Producer / human proof | `paper/a280537_note.tex`, `witnesses/A280537_no4coplanar_cube.txt` | Aleksei Kudriashov / Athanor lab, AI assisted; exact dates of individual artifacts not stated | Witnesses and coordinate-plane bound | Claimed lower bounds and elementary upper bound | Uses same witness data; upper-bound argument is human-checkable |

## Replayed for this repository

Executed on 13 Nov 2026 WITA, locally. Commands use the logged working directory; logs contain the full outputs. Wall times include process startup.

- `python3 -B witnesses/verify_witness_2.py --selftest` — exit 0, 0.037 s; output: six checks PASS, including rejection of planted defects. [`logs/certificate-2026-11-13/selftest.log`](logs/certificate-2026-11-13/selftest.log) (SHA-256 `cfc3b95f07f905955505aec995c97eecc220db178de37941e8db750f070f111c`).
- `python3 -B witnesses/verify_witness_2.py --all witnesses` — exit 0, 0.197 s; output: 16 witnesses, 16 clean; includes n=12/21/22/27. [`logs/certificate-2026-11-13/witnesses.log`](logs/certificate-2026-11-13/witnesses.log) (SHA-256 `75f2b43f469d0f5a0a882a13a2479451ae8d970fe797bcdd83bf3b3b112c5b3d`).

The named individual witnesses fit the time limit. Replaying the combined file and downloading the OEIS attachment were not required to check the four contributed individual witnesses; their runtime has not been measured.

## Not covered

The combined witness file and the third-party OEIS attachment were not replayed; the four named individual witnesses were checked. No optimality follows from a lower-bound witness. The upper bound is an elementary human-checkable argument, not machine-checked. Link availability was not checked.

## Guide's independent check

pending

## Verdict

partial — The evidence and replay leave the gaps above, and the Guide's independent check is pending.
