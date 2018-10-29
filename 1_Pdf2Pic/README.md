## Extracts all pictures from pdf files. 

You can use either Pdf2Pic.py or Pdf2Pic.ipynb for this

#### Step 1(Optional): rename all pdf files

1. Put all pdf files into a folder called "PDFS" which is in the same directory of Rename.ipynb.
2. Run Rename.ipynb or Rename.py

#### Step 2: extract pictures from pdf files

#### option 1 is to use Pdf2Pic.py

1. Have a folder of your pdf files

2. : download Pdf2Pic.py

3: run below code in your command line console
```
python Pdf2Pic.py [your folder name]
```

#### option 2 is to use Pdf2Pic.ipynb

1: Create a folder called "PDFS" in the same directory where you will put Pdf2Pic.ipynb. 

2: Put all pdf files into this folder.

3: download and run Pdf2Pic.ipynb. 


**Result**: All extracted pictures are saved as png files in a folder called "Pdf2Pic_output". Each picture is named in the form of pdfname_pagenumber_imagename.png.

python 3 and the libraries in the header of Pdf2Pic.ipynb are used.
