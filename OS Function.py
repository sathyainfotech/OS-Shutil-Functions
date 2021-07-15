"""
    1)Rename
    2)Move
    3)Replace
    4)Copyfile
    5)Join
"""
import os
import shutil

# original="C:/Users/Sathya/Desktop/PDF/python.pdf"
# rename="C:/Users/Sathya/Desktop/PDF/sathya.pdf"
# os.rename(rename,original)
# print("File Rename Successfully")

# source="C:/Users/Sathya/Desktop/PDF/python.pdf"
# destination="C:/Users/Sathya/Desktop/Files/python.pdf"
# shutil.move(source,destination)
# print("File Moved Successfully")

# actualfile="C:/Users/Sathya/Desktop/PDF/HTML.pdf"
# replacefile="C:/Users/Sathya/Desktop/Files/HTML.pdf"
# os.replace(actualfile,replacefile)
# print("File Replaced Successfully")

# original="C:/Users/Sathya/Desktop/PDF/Cshorp.pdf"
# # target="C:/Users/Sathya/Desktop/Files/Cshorp.pdf"
# # shutil.copyfile(original,target)
# # print("File Copied Successfully")

filename="sathya.jpg"
filepath="C:/Users/Sathya/Desktop/Image\\"
joinpath=os.path.join(filepath,filename).replace("\\","/")
print(joinpath)