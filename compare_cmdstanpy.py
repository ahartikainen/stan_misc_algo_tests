import os
from glob import glob
import pandas as pd
import numpy as np

np.set_printoptions(precision=16)

files = glob("./*.txt")

results = {}
for path in files:
    with open(path) as f:
        res = pd.read_csv(f, float_precision="round_trip", index=None)
        _, fname = os.path.split(os.path.splitext(path)[0])
        *_, seed, platform = fname.split("_")
        if seed not in results:
            results[seed] = {}
        results[seed][platform] = res


for seed, sub_dict in results.items():
    if (sub_dict["Windows"].iloc[:, 0] == sub_dict["Linux"].iloc[:, 0]).all():
        print(f"Seed: {seed}, same value in all values")
    else:
        print(
            f"Seed: {seed}, same value in ",
            (
                (sub_dict["Windows"].iloc[:, 0] == sub_dict["Linux"].iloc[:, 0])
                == False
            ).idxmax()
            + 1,
        )
