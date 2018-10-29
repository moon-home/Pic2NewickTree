import glob, os
import fitz
from shutil import copyfile

def rename(oldfolder_dir, old_pattern, newfolder_dir, new_pattern=None):
    n = 0
    for pathAndFilename in glob.iglob(os.path.join(oldfolder_dir, old_pattern)):
        n += 1
        doc = fitz.open(pathAndFilename)
        metainfo = '' 
        #metainfo = '_'+doc.metadata['creationDate'][2:10]
        #choose whether to add extra information for new name
        doc.close()
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        copyfile(pathAndFilename, os.path.join(newfolder_dir, str(n)+metainfo+'.pdf'))
        #os.rename(pathAndFilename, os.path.join(newfolder_dir, str(n)+'.pdf'))
        #choose to move or copy
		
oldfolder = "PDFS"
current_dir = os.getcwd()
oldfolder_dir = os.path.join(current_dir, oldfolder)
newfolder_dir = os.path.join(current_dir, "Rename_output")
if os.path.exists(newfolder_dir):
    print("oldfolder_dir: ", newfolder_dir)
    print("foler already existed, please create a new folder！")
    raise SystemExit
else:
    os.makedirs(newfolder_dir)
old_pattern = '*.pdf'
rename(oldfolder_dir, old_pattern, newfolder_dir)

# [os.rename(f, f.replace('_', '-')) for f in os.listdir('.') if not f.startswith('.')]