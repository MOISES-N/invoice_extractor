import argparse

def parse_args():
    """Parse command-line arguments for the scraper script.

    Returns:
        argparse.Namespace: Parsed arguments including category and config path.
    """
    parser = argparse.ArgumentParser(
        description="Run the BaseScraper for a specific product category."
    )

    parser.add_argument(
        "--data_path",
        type=str,
        required=True,
        help="Extract invoice data from PDFs in this folder path.",
    )

    return parser.parse_args()