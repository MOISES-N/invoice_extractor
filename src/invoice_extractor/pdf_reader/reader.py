import pathlib

class InvoiceReader:
    """Reader for invoice PDF files stored in a directory.

    Parameters
    ----------
    folder_path : str
        Path to the directory that contains invoice PDF files.
    """

    def __init__(self, folder_path: str) -> None:
        """Initialize the InvoiceReader with a folder path.

        Args:
            folder_path: Path to the directory containing PDF invoices.
        """
        self.folder_path = folder_path

    def read_invoice(self):
        """Find and return PDF files in the configured folder.

        Returns:
            list[pathlib.WindowsPath]: A list of pathlib WindowsPath objects
            for files matching the pattern '*.pdf' in self.folder_path.
        """
        pdf_list: list[pathlib.WindowsPath] = list(pathlib.Path(self.folder_path).glob("*.pdf"))
        return pdf_list