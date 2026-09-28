from ingestion.extraction.instruments import extract_instruments
from ingestion.validation.validation import validate_instruments
from ingestion.loading.instruments_loader import load_instruments


def run():

    instruments = extract_instruments()

    validation_result = validate_instruments(instruments)

    print(validation_result)

    load_instruments(instruments)

    print("Instrument ingestion completed")


if __name__ == "__main__":
    run()