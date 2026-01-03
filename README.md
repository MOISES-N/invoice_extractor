# Invoice Extractor

A robust data extraction tool designed to automate the processing of invoice documents. This project utilizes **PyPDF** for reading PDF documents and **Pydantic** for strict configuration validation, ensuring reliable data extraction using customizable Regex patterns.

## 📋 Project Overview

* **Project Name:** `invoice-extractor`
* **Description:** Automated pipeline for extracting structured data from invoice PDF files.
* **Python Version:** Requires Python 3.11 or higher.
* **Key Libraries:** `pypdf`, `pandas`, `pydantic`, `openpyxl`.

## 🛠️ Prerequisites

Before running the project, ensure you have the following installed:

* **Python 3.11+**
* **uv** (Recommended for efficient dependency management)

## 🚀 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/MOISES-N/invoice_extractor.git](https://github.com/MOISES-N/invoice_extractor.git)
    cd invoice_extractor
    ```

2.  **Set up the environment:**
    This project is configured to use `uv` for fast package management.

    ```bash
    # Create virtual environment
    uv venv

    # Activate environment
    # Windows:
    .venv\Scripts\activate
    # macOS/Linux:
    source .venv/bin/activate

    # Install dependencies
    uv sync
    ```

## ⚙️ Configuration

The project behavior is controlled by `config_file.yaml`. This file defines the Regex patterns used to locate and extract specific fields from the invoice text.

**File:** `config_file.yaml`
```yaml
field_extractors:
  invoice_number: "INVOICE\\s*\\n\\s*#\\s*(\\d+)"
  order_id: "Order ID\\s*:\\s*([A-Za-z0-9-]+)"
  customer_name: "Bill To\\s*\\n\\s*:\\s*\\n\\s*(.*)\\nShip To"
  date: "([A-Z][a-z]{2}\\s\\d{2}\\s\\d{4})"
  shipping_address: "Ship To\\s*\\n\\s*:\\s*\\n\\s*(.*?)(?=\\n\\s*[A-Z][a-z]{2}\\s\\d{2})"
  total_amount: "(\\$[\\d,\\.]+)\\nDate"
```

## 💻 Usage

You can run the extractor via the command-line interface by pointing it to your data directory.

**Running via Script**
Run the entry point script scripts/run_extractor.py and pass the required data_path argument.

```bash
uv run scripts/run_extractor.py --data_path data/
```

**Arguments:**

* --data_path: (Required) The directory path containing the PDF invoices you want to process.

## 📂 Project Structure

The project is organized as follows:

```bash
invoice_extractor/
├── data/                     # Directory for input invoice files
├── notebooks/                # Jupyter notebooks for exploration
├── output/                   # Destination for extracted Excel files
├── scripts/
│   └── run_extractor.py      # Main entry point script
├── src/
│   └── invoice_extractor/    # Main package source code
│       ├── config/
│       │   └── config.py     # Pydantic configuration models
│       ├── pdf_reader/
│       │   └── reader.py     # PDF file discovery and reading
│       └── text_extractor/
│           └── extractor.py  # Core extraction logic
├── config_file.yaml          # Regex configuration file
├── pyproject.toml            # Project metadata and dependencies
└── README.md                 # Project documentation
```

## 📤 Output

The extractor processes the documents and saves the results as an Excel file in the output/ directory.

* **Output Path:** output/output.xlsx

* **Columns:** The resulting file contains the fields defined in your configuration, such as:

  * invoice_number

  * order_id

  * customer_name

  * product_review

  * date

  * shipping_address

  * total_amount

## 🔧 Key Dependencies

**PyPDF:** For reading and parsing PDF documents.

**Pandas & OpenPyXL:** For structuring extracted data and exporting to Excel.

**Pydantic:** For strict validation of configuration settings.

**PyYAML:** For parsing the YAML configuration file.

**Loguru:** For robust logging of the extraction progress.

For a complete list of dependencies, refer to pyproject.toml or uv.lock.