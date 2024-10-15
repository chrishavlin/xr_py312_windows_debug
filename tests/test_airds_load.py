import xarray as xr

def test_air_temp_load():
    _ = xr.tutorial.open_dataset("air_temperature")