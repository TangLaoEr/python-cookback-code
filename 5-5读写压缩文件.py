import gzip
import bz2

a = 1
with gzip.open('text.zip','rt') as f:
    f.read()
