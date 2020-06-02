#!/usr/bin/env python
import sys
from pathlib import Path

import pandas as pd

if len(sys.argv) != 3:
    print("Usage: topickle.py IN_FILEPATH OUT_DIR")
    sys.exit(1)

infile = Path(sys.argv[1])
assert infile.is_file() and infile.exists()

outdir = Path(sys.argv[2])
assert outdir.is_dir() and outdir.exists()

print(f"Input file : {infile}")

outfile = outdir / (infile.name + ".pkl")
assert not outfile.exists()

print(f"Output file: {outfile}")

dtype = {
    "coduf": "Int64",
    "codmun": "Int64",
    "codRegiaoSaude": "Int64",
    "semanaEpi": "Int64",
    "populacaoTCU2019": "Int64",
    "casosAcumulado": "Int64",
    "obitosAcumulado": "Int64",
    "Recuperadosnovos": "Int64",
    "emAcompanhamentoNovos": "Int64",
}

df = pd.read_excel(infile, dtype=dtype)
df["data"] = pd.to_datetime(df["data"], format="%Y-%m-%d")
df["coduf"] = df["coduf"].astype("Int64")

df.to_pickle(outfile)
