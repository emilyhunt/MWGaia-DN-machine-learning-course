"""Sorts spectra from the Gaia archive into the correct formatting.

Query used on Gaia archive:

SELECT TOP 100 g.source_id, g.has_xp_sampled, g.teff_gspphot, g.logg_gspphot, g.mh_gspphot, g.distance_gspphot, g.azero_gspphot, g.ag_gspphot
FROM gaiadr3.gaia_source as g
WHERE g.has_xp_sampled = 'True'
AND g.teff_gspphot IS NOT NULL
AND g.phot_g_mean_mag > 7
AND g.phot_g_mean_mag < 9
ORDER BY g.random_index ASC
"""

import numpy as np
import pandas as pd
from astropy.table import Table
from pathlib import Path


# First off, handle all spectra
spectra = Path("./raw_xp_spectra").glob("*.xml")

# Extract spectra into a big 2D numpy array, also grabbing source ids as we go
spectra_list = []
source_ids = []
for spec in spectra:
    source_ids.append(int(spec.stem.split(" ")[-1]))
    df = Table.read(spec).to_pandas()
    spectra_list.append(np.append(df["flux"].to_numpy(), df["flux_error"].to_numpy()))
spectra_array = np.vstack(spectra_list)

# Now turn it into a dataframe (the pain of getting to .parquet...)
wavelengths = df["wavelength"].astype(int).to_numpy()
column_names = (
    # ["source_id"]
    [f"flux_{w}" for w in wavelengths] + [f"flux_{w}_error" for w in wavelengths]
)

spectra_df = pd.DataFrame(spectra_array, columns=column_names)
spectra_df["source_id"] = source_ids

# Next off, read in the Gaia information on these sources
gaia_parameters = Table.read(
    "./raw_xp_spectra/Gaia spectra candidates-result.vot.gz"
).to_pandas()
gaia_parameters = gaia_parameters.rename(columns={"SOURCE_ID": "source_id"})

# ... and join it with the spectra:
gaia_parameters = gaia_parameters.merge(spectra_df, on="source_id")

# ... and save!
gaia_parameters.to_parquet("100_gaia_xp_spectra.parquet")
