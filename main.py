from PyPDF2 import PdfReader, PdfWriter
import os

def split_and_rename_certificates(input_pdf, output_dir):
   if not os.path.exists(output_dir):
       os.makedirs(output_dir)
   
   reader = PdfReader(input_pdf)
   
   for i in range(len(reader.pages)):
       writer = PdfWriter()
       writer.add_page(reader.pages[i])
       
       # Extract name from text
       text = reader.pages[i].extract_text()
       name_end = text.find("Priscilla Bakalian")
       text_before = text[:name_end].strip()
       name = text_before.split("scaling")[-1].strip()
       
       # Save certificate with name
       output_path = os.path.join(output_dir, f"Certificate_{name}.pdf")
       with open(output_path, "wb") as output_file:
           writer.write(output_file)
       print(f"Created certificate for: {name}")

input_pdf = "AGO Cohort 6 Cert of Excellence.pdf"
output_dir = "individual_certificates"
split_and_rename_certificates(input_pdf, output_dir)