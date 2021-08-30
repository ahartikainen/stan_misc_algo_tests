import os
from glob import glob
import pandas as pd
import numpy as np

np.set_printoptions(precision=16)

files = glob("./Upload stdout files/*.txt")

print("\nStarting file processing")
results = {}
i = -1
for i, path in enumerate(files):
    with open(path) as f:
        res = pd.read_csv(f, float_precision="round_trip", index=None)
        _, fname = os.path.split(os.path.splitext(path)[0])
        *_, seed, platform = fname.split("_")
        if seed not in results:
            results[seed] = {}
        results[seed][platform] = res
print(f"Processed total of {i + 1} files.")

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
print("\nScript finished")
