"""Converts the full APOGEE dr17 allStarLite table to a smaller .parquet file with
just a few columns.
"""

import numpy as np
from astropy import table as at


apogee_full = at.Table.read("allStarLite-dr17-synspec_rev1.fits")
apogee_full.remove_columns(
    [
        "PARAMFLAG",
        "X_H",
        "X_H_ERR",
        "X_M",
        "X_M_ERR",
        "ELEM_CHI2",
        "ELEMFRAC",
        "X_H_SPEC",
        "X_M_SPEC",
    ]
)
apogee_full = at.unique(apogee_full, "APOGEE_ID")
apogee_full = apogee_full.to_pandas()
apogee_full = apogee_full.loc[
    np.logical_and(apogee_full["M_H"].notna(), apogee_full["ALPHA_M"].notna())
]
apogee_full["APOGEE_ID"] = apogee_full["APOGEE_ID"].astype(str)
apogee_full[["APOGEE_ID", "GLON", "GLAT", "M_H", "ALPHA_M"]].to_parquet(
    "apogee-dr17-metallicites-and-alphas-cut.parquet"
)
