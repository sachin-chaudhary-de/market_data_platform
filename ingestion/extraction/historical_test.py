from ingestion.extraction.nifty50 import get_nifty50_instrument_keys


instrument_keys = get_nifty50_instrument_keys()

print("Matched instruments:", len(instrument_keys))
print(instrument_keys)