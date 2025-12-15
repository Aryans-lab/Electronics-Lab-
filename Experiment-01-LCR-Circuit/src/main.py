from analysis import (
    load_table_1,
    load_table_2,
    load_table_3,
    fit_rlc,
    plot_magnitude,
    plot_phase
)

# -------------------- TABLE 1 (R = 98.2 Ω) --------------------

f1, ratio1, phi1 = load_table_1("data/table1_R98.csv")

params1, _ = fit_rlc(
    f1,
    ratio1,
    initial_guess=[100, 1e-2, 80e-9]
)

plot_magnitude(
    f1,
    ratio1,
    params1,
    title="R = 98.2 Ω : V_R / V_i vs Frequency",
    ylabel="V_R / V_i"
)

plot_phase(
    f1,
    phi1,
    params1,
    title="R = 98.2 Ω : Phase vs Frequency"
)

# -------------------- TABLE 2 (R = 46.2 Ω) --------------------

f2, ratio2 = load_table_2("data/table2_R46.csv")

params2, _ = fit_rlc(
    f2,
    ratio2,
    initial_guess=[50, 1e-2, 90e-9]
)

plot_magnitude(
    f2,
    ratio2,
    params2,
    title="R = 46.2 Ω : V_R / V_i vs Frequency",
    ylabel="V_R / V_i"
)

# -------------------- TABLE 3 (LC BRANCH) --------------------

f3, ratio3, phi3 = load_table_3("data/table3_LC_branch.csv")

plot_magnitude(
    f3,
    ratio3,
    params2,
    title="LC Branch (R = 46.2 Ω) : V_LC / V_i vs Frequency",
    ylabel="V_LC / V_i"
)

plot_phase(
    f3,
    phi3,
    params2,
    title="LC Branch : Phase vs Frequency"
)
