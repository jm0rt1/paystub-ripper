from pathlib import Path
import PyPDF2


class PDFSplitter:
    def __init__(self, input_pdf_path: Path, output_pdf_base_path: Path):
        self.input_pdf_path = input_pdf_path
        self.output_pdf_base_path = output_pdf_base_path

    def split(self):
        pdf_file = open(self.input_pdf_path, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        total_pages = len(pdf_reader.pages)
        for page in range(total_pages):
            pdf_writer = PyPDF2.PdfWriter()
            page_content = pdf_reader.pages[page].extract_text()
            page_content = page_content.split("\n")
            pay_date_str = ""
            for line in page_content:
                line_content = line.replace(" ", "").lower().strip()
                if "paydate" in line_content:
                    pay_date_str = line_content.replace(
                        "paydate", "").replace("\\", "-").replace("/", "-")
                    break
            else:
                print(f"Pay date not found in page {page} pdf")

            pdf_writer.add_page(pdf_reader.pages[page])

            output_pdf_path = self.output_pdf_base_path / \
                f"pay_date_{pay_date_str}.pdf"
            with open(output_pdf_path, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)

        pdf_file.close()
