## GUI - RUN THIS FILE

# DEPENDENCIES
# pip install -r requirements.txt

import customtkinter as ctk
from PIL import Image
from tkinter import messagebox
import time
from pathlib import Path

def resize(images, saveDirectory, x:int, y:int):
    global win
    workingDia = messagebox.showinfo("Working", "Resizing...")
    if images:
        imageAccumulator: int = 0
        startTime = time.perf_counter()
        
        
        for image in images:
            try:
                fileName = image.split('/')
            
                currentPath = Path(image)
                pic = Image.open(currentPath)
                resizedPic = pic.resize((x, y))
                resizedPic.save(f"{saveDirectory}\{fileName[-1]}")
                
            except:
                dia = messagebox.showerror(title="ERROR", message="Something went wrong when resizing your images!")
            
            imageAccumulator+=1
        endTime = time.perf_counter()
        totalTime = endTime - startTime
        
        dia = messagebox.showinfo(title="Complete", message=f"Resized {imageAccumulator} Image file(s) ({images}) in {round(totalTime, 2)} seconds!")
    else:
        print("there are no images in this directory")



def chooseDirectory(label: ctk.CTkLabel):
    global selectedFiles
    selectedFiles = ctk.filedialog.askopenfilenames(title="Select Files To Resize", filetypes=[("Images", "*.png")])
    files: str = ''
    for file in selectedFiles:
        files+=file
    label.configure(text=files)
    
def chooseSaveDirectory(label: ctk.CTkLabel):
    global saveDirectory
    saveDirectory = ctk.filedialog.askdirectory(title="Select a directory to save images to")
    label.configure(text=saveDirectory)

def main():
    global selectedFiles
    global saveDirectory
    selectedFiles = ''
    saveDirectory = ''
    
    global win
    win = ctk.ctk_tk.CTk()
    win.wm_title("Image Resizer")
    win.geometry('370x380')
    win.resizable(False, False)
    
    
    saveFrame = ctk.CTkScrollableFrame(win, width=130)
    imagesFrame = ctk.CTkScrollableFrame(win, width=130)
    
    chooseDirectoryLabel = ctk.CTkLabel(imagesFrame, text=selectedFiles, wraplength=130)
    chooseDirectoryButton = ctk.CTkButton(win, text="Choose Images to Resize", command=lambda: chooseDirectory(chooseDirectoryLabel))
    
    chooseSaveDirectoryLabel = ctk.CTkLabel(saveFrame, text=saveDirectory, wraplength=130)
    chooseSaveDirectoryButton = ctk.CTkButton(win, text="Choose Save Directory", command=lambda: chooseSaveDirectory(chooseSaveDirectoryLabel))
    
    inputFrame = ctk.CTkFrame(win, width=500)
    inputLabelX = ctk.CTkLabel(inputFrame, text="X:")
    inputX = ctk.CTkEntry(inputFrame)
    inputLabelY = ctk.CTkLabel(inputFrame, text="Y:")
    inputY = ctk.CTkEntry(inputFrame)
    
    resizeButton = ctk.CTkButton(win, text="Resize!", command=lambda:resize(selectedFiles, saveDirectory, int(inputX.get()), int(inputY.get())))
    
    
    chooseDirectoryButton.place(x=20, y=20)
    chooseDirectoryLabel.pack()
    
    chooseSaveDirectoryButton.place(x=205, y=20)
    
    chooseSaveDirectoryLabel.pack()
    saveFrame.place(x=200, y=60)
    imagesFrame.place(x=25, y=60)
    
    inputLabelX.grid(row=0, column=0, padx=5)
    inputX.grid(row=0, column=1)
    
    inputLabelY.grid(row=0, column=2, padx=5)
    inputY.grid(row=0, column=3)
    inputFrame.place(x=20, y=285)
    
    resizeButton.place(x=120, y=330)
    
    win.mainloop()
    
main()