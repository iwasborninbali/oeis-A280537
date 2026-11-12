import re
from pathlib import Path
from witnesses.verify_witness import check
lines = (Path(__file__).parent/'witnesses/oeis-a280537_4.txt').read_text().splitlines()
count=0
for line in lines:
    m = re.match(r'\s*(\d+)\s+\[(\d+)\]:',line)
    if not m: continue
    n,k=map(int,m.groups())
    points=[tuple(map(int,p)) for p in re.findall(r'\((\d+),(\d+),(\d+)\)',line)]
    assert check(n,points,k)
    count+=1
assert count == 13, count
print(f'{count} OEIS configurations checked')
