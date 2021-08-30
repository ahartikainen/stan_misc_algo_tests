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
    iter_warmup=2,
    iter_sampling=1,
    save_warmup=True,
    sig_figs=17,
    seed=123,
)

res = fit.draws_pd()

print(" ")
print("result:\n", res)
