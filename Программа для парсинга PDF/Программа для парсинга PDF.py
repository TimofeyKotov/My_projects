from PyPDF2 import PdfReader 
def parse(path):
    """    Принимает путь к файлу пдф, создает файл csv в текущей директории"""
    pdf = PdfReader(path)
    with open('output.txt', 'w', encoding="utf-8") as out:
        for i in range(len(pdf.pages)):
            page = pdf.pages[i]
            str = page.extract_text()
            k_od = str.find('Ka=')
            k_k = str.rfind('Ka=')
            depth = str.find('Глубина,')
            print(str[k_od+4:k_od+8],str[k_k+4:k_k+8],str[depth-5:depth-1].replace(':',''), file=out)
            
parse('pdf_file_name')