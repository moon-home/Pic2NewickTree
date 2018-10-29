import fitz
import time
import re
import os
import sys
from PIL import Image

def recoverpix(doc, item):
    x = item[0]  # xref of PDF image
    s = item[1]  # xref of its /SMask
    pix1 = fitz.Pixmap(doc, x)
    if s == 0:                    # has no /SMask
        return pix1               # no special handling
    pix2 = fitz.Pixmap(doc, s)    # create pixmap of /SMask entry
    # check that we are safe
    if not (pix1.irect == pix2.irect and \
            pix1.alpha == pix2.alpha == 0 and \
            pix2.n == 1):
        print("pix1", pix1, "pix2", pix2)
        raise ValueError("unexpected situation")
    pix = fitz.Pixmap(pix1)       # copy of pix1, alpha channel added
    pix.setAlpha(pix2.samples)    # treat pix2.samples as alpha value
    pix1 = pix2 = None            # free temp pixmaps
    return pix
	
	
def pdf2pic(prefix, pdf_path, outputfolder_path):
    xreflist = [] 
    imgcount = 0 
    pdf = fitz.open(pdf_path)
    for i in range(len(pdf)):
        imglist = pdf.getPageImageList(i)
        for img in imglist:
            if img[0] in xreflist:         # this image has been processed
                continue 
            xreflist.append(img[0])        # take note of the xref
            pix = recoverpix(pdf, img[:2]) # make pixmap from image
            if pix.n - pix.alpha < 4:      # can be saved as PNG
                pass
            else:                          # must convert CMYK first
                pix0 = fitz.Pixmap(fitz.csRGB, pix)
                pix = pix0

            pic_name = prefix+"_p"+str(i)+img[7]+".png"
            pix.writePNG(pic_name)
            current_dir = os.path.join(os.getcwd(), pic_name)
            destination_dir = os.path.join(outputfolder_path, pic_name)
            os.rename(current_dir, destination_dir)
            imgcount += 1
            pix = None    
    pdf.close()

def pdfs2pics(pdffolder_path, outputfolder_path):
    pdfs= os.listdir(pdffolder_path)
    for pdf in pdfs: 
        if not os.path.isdir(pdf): #only open when it's not a folder
            prefix = pdf[0:40]
            pdf_path = os.path.join(pdffolder_path, pdf)
            pdf2pic(prefix, pdf_path, outputfolder_path)
		
current_path = os.getcwd()
pdf_folder = sys.argv[1]
pdffolder_path = os.path.join(current_path, pdf_folder)
outputfolder_path = os.path.join(current_path, "Pdf2Pic_output")
if os.path.exists(outputfolder_path):
    print("folder already existed, please create a new folder！")
    raise SystemExit
else:
    os.makedirs(outputfolder_path)
pdfs2pics(pdffolder_path, outputfolder_path)