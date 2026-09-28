from ingestion.extraction.instruments import extract_instruments
from ingestion.validation.validation import validate_instruments
from ingestion.loading.instruments_loader import load_instruments

from ingestion.logger import logger

def run():

    logger.info("Instrument ingestion started")

    logger.info("Starting extraction")
    instruments = extract_instruments()
    logger.info(
        "Extraction completed | records=%s",
        len(instruments),
    )

    logger.info("Starting validation")
    validation_result = validate_instruments(instruments)
    logger.info(
        "Validation completed | result=%s",
        validation_result,
    )

    logger.info("Starting loading")
    load_result = load_instruments(instruments)

    if load_result:
        logger.info("Loading completed | data loaded")
    else:
        logger.info("Loading skipped | object already exists")

    logger.info("Instrument ingestion completed")


if __name__ == "__main__":
    run()