import pathlib
from pypdf import PdfReader
import re
import pandas as pd
from invoice_extractor.config.config import ProjectConfig

class Extractor:
    """Extract text and structured fields from invoice PDF files.

    Attributes:
        config (ProjectConfig): Configuration containing field extraction
            patterns under the attribute `field_extractors`.
        pdf_list (list[pathlib.WindowsPath]): List of PDF file paths to process.
    """
    
    def __init__(self, config: ProjectConfig, pdf_list: list[pathlib.WindowsPath]) -> None:
        """Initialize the Extractor.

        Args:
            config: ProjectConfig instance that provides `field_extractors`,
                a mapping of field names to regex patterns.
            pdf_list: List of pathlib.WindowsPath objects pointing to PDFs to process.
        """
        self.config = config
        self.pdf_list = pdf_list

    def run_pipeline(self, excel_path: str) -> None:
        """Run the full extraction pipeline and save results to Excel.

        This method runs extraction of raw text, field extraction, and saves
        the extracted results to the provided Excel path.

        Args:
            excel_path: Destination file path for the Excel output.

        Returns:
            None.
        """
        (
            self
            .extract_raw_text()
            .extract_fields()
            .save_to_excel(excel_path)
        )
        
        
    def extract_raw_text(self) -> 'Extractor':
        """Extract raw text from all PDFs and store it on the instance.

        The method reads each PDF in self.pdf_list, concatenates text from all
        pages (separated by newlines) and stores the resulting strings in
        self.pdf_text_list. Errors encountered while reading a PDF are printed.

        Returns:
            Extractor: self, to allow method chaining.
        """
        self.pdf_text_list: list[str] = []

        for pdf in self.pdf_list:
            
            try:
                reader = PdfReader(pdf)
                complete_text = ""
                for pagina in reader.pages:
                    complete_text += pagina.extract_text() + "\n"

                self.pdf_text_list.append(complete_text)  
                
            except Exception as e:
                print(f"❌ Error en {pdf.name}: {e}")

        return self
    
    def extract_fields(self) -> 'Extractor':
        """Extract structured fields from the previously extracted raw text.

        Uses regex patterns from self.config.field_extractors to search each
        document's text. For each pattern, the first capture group is taken,
        trimmed and newlines replaced with spaces. Results per document are
        stored in self.extracted_fields as a list of dicts.

        Returns:
            Extractor: self, to allow method chaining.
        """
        patterns = self.config.field_extractors
        
        self.extracted_fields = []
        for pdf_text in self.pdf_text_list:

            results = {}
            for campo, patron in patterns.items():
                
                match = re.search(patron, pdf_text, re.DOTALL | re.MULTILINE)
                if match:
                    results[campo] = match.group(1).strip().replace('\n', ' ')

            self.extracted_fields.append(results)

        return self

    def save_to_excel(self, excel_path: str) -> None:
        """Save extracted fields to an Excel file.

        Creates a pandas DataFrame from self.extracted_fields, drops rows that
        are missing the 'invoice_number' field, and writes the DataFrame to
        the given excel_path.

        Args:
            excel_path: Destination path for the Excel file to write.

        Returns:
            None
        """
        results = pd.DataFrame(self.extracted_fields).dropna(subset=['invoice_number'])
        results.to_excel(excel_path, index=False)
    
