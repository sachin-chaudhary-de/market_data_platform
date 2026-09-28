REQUIRED_FIELDS = {
    "instrument_key",
    "exchange",
    "segment",
    "trading_symbol",
}


def validate_instruments(instruments):

    if not isinstance(instruments, list):
        raise TypeError("Instrument data must be a list")

    if not instruments:
        raise ValueError("Instrument data is empty")

    seen_instrument_keys = set()

    for index, instrument in enumerate(instruments):

        if not isinstance(instrument, dict):
            raise TypeError(
                f"Record {index} is not a dictionary"
            )

        missing_fields = REQUIRED_FIELDS - instrument.keys()

        if missing_fields:
            raise ValueError(
                f"Record {index} is missing fields: "
                f"{missing_fields}"
            )

        for field in REQUIRED_FIELDS:

            if instrument[field] is None or instrument[field] == "":
                raise ValueError(
                    f"Record {index} has empty {field}"
                )

        instrument_key = instrument["instrument_key"]

        if instrument_key in seen_instrument_keys:
            raise ValueError(
                f"Duplicate instrument_key: {instrument_key}"
            )

        seen_instrument_keys.add(instrument_key)

    return {
        "record_count": len(instruments),
        "unique_instrument_keys": len(seen_instrument_keys),
    }