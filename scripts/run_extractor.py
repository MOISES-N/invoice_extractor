from invoice_extractor.utils.utils import parse_args
from invoice_extractor import PROJECT_ROOT
from invoice_extractor.config.config import ProjectConfig

from invoice_extractor.pdf_reader.reader import InvoiceReader
from invoice_extractor.text_extractor.extractor import Extractor

from loguru import logger

args = parse_args()

data_path: str = args.data_path
config_path: str = PROJECT_ROOT / 'config_file.yaml'
excel_path: str = PROJECT_ROOT / 'output' / 'output.xlsx'

config: ProjectConfig = ProjectConfig.from_yaml(config_path=config_path)

invoice_reader = InvoiceReader(folder_path=data_path)
pdf_list = invoice_reader.read_invoice()
logger.info(f"✅ {len(pdf_list)} PDF files found in {data_path}.")

pdf_extractor = Extractor(config=config, pdf_list=pdf_list)
resultado = pdf_extractor.run_pipeline(excel_path)
logger.info(f"✅ Results saved to {excel_path}.")