# Generate PDF file of your 3rd Semester Mark-sheet

# importing necessary libraries
import img2pdf
from PIL import Image
import os

import img2pdf

with open("E:/Athu/Degree Engg/Sem 4/Python/Practicals/converted_img.pdf",'wb') as f:
    f.write(img2pdf.convert('E:/Athu/Degree Engg/Sem 4/Python/Practicals/img.jpg'))
# output
print("Successfully made pdf file")

# D21CS105
# Atharva Joshi