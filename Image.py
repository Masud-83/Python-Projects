# This is for git commit check

#*********************************Image to text**********************

from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
txt = pytesseract.image_to_string(Image.open('job11.png'))
fl = open(r'C:\Users\asrock\Desktop\new2.txt', 'w')
fl.write(txt)
fl.close()


# In[8]:


#*********************************pdf to text**********************************

import tkinter, PyPDF2
from tkinter import filedialog



def openFile():
    filename = filedialog.askopenfilename(title="Open PDF file", 
                                                  initialdir='C:/Users/asrock/Desktop')
    print(filename)
    
    filename_label.configure(text=filename)    
    outputfile_text.delete("1.0", tkinter.END)
    reader = PyPDF2.PdfReader(filename)
    for i in range (len(reader.pages)):
        current_text = reader.pages[i].extract_text()
        outputfile_text.insert(tkinter.END, current_text)


root = tkinter.Tk()
root.title("PDF Text Extractor")


filename_label = tkinter.Label(root, text="No File Selected")
outputfile_text = tkinter.Text(root)
openfile_button = tkinter.Button(root, text="Open PDF File", command=openFile)

filename_label.pack()
outputfile_text.pack()
openfile_button.pack()

root.mainloop()


# In[9]:


#*******************************text to docx***********************************

import aspose.words as aw

file = 'new.txt'

output = aw.Document()
# Remove all content from the destination document before appending.
output.remove_all_children()
tfile = aw.Document(file)
    # Append the source document to the end of the destination document.
output.append_document(tfile, aw.ImportFormatMode.KEEP_SOURCE_FORMATTING)

output.save("C:/Users/asrock/Desktop/Output1.docx");


# In[ ]:


#******************************Best for pdf docs *************************************

import tkinter
import sys, pathlib, fitz
from tkinter import filedialog

root = tkinter.Tk()
fname = filedialog.askopenfilename(title="Open PDF file", 
                                                  initialdir='C:/Users/asrock/Desktop')#sys.argv[1]  # get document filename
with fitz.open(fname) as doc:  # open document
    text = chr(12).join([page.get_text() for page in doc])
# write as a binary file to support non-ASCII characters
pathlib.Path(r"C:\Users\asrock\Desktop\rxt3.txt").write_bytes(text.encode())


root.mainloop()

