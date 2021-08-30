import platform

import cmdstanpy
import numpy as np

np.set_printoptions(precision=16)

schools_dat = dict(
    J=8, y=[28, 8, -3, 7, -1, 1, 18, 12], sigma=[15, 10, 16, 11, 9, 11, 10, 18]
)

model = cmdstanpy.CmdStanModel(
    stan_file="Stan-models/8schools.stan",
)

fit = model.sample(
    data=schools_dat,
    chains=1,
    iter_warmup=4,
    iter_sampling=4,
    save_warmup=True,
    sig_figs=17,
    seed=123,
)

res = fit.draws_pd(inc_warmup=True)

print(" ")
print(fit.runset.stdout_files)
for i, path in enumerate(fit.runset.stdout_files, 1):
    file_out = f"stdout_{i}_{platform.system()}.txt"
    with open(path) as fin, open(file_out, "w") as fout:
        try:
            fout.write(fin.read(-1))
            print(f"Saved: {file_out}")
        except Exception as err:
            print("ERROR:", err)
print("result:\n", res)
print("\n\n\n", res["lp__"].values[:3])

file_out2 = f"lp_values_{platform.system()}.txt"
with open(file_out2, "w") as f:
    res["lp__"].to_csv(f)