from my_package.model import ImageCaptioningModel
from my_package.model import ImageClassificationModel
from tkinter import *
from functools import partial
from PIL import ImageTk, Image
from tkinter import filedialog as fd


def fileClick(clicked):
    # Define the function you want to call when the filebrowser button (Open) is clicked.
    # This function should pop-up a dialog for the user to select an input image file.
    # To have a better clarity, please check out the sample video.
    global the_file
    the_file = fd.askopenfilename(title = "Select a file of any type", initialdir = 'data/imgs', filetypes = [("Images", "*.jpg")])

    output.destroy()
    
    image_name_display.config(state = NORMAL)
    image_name_display.delete(0, END)
    image_name_display.insert(0, the_file)
    image_name_display.config(state = DISABLED)
    
    global temp_img
    temp_img = ImageTk.PhotoImage(Image.open(the_file))
    global img_label
    img_label = Label()
    img_label.grid(row = 1, column = 0, columnspan = 3)
    img_label.config(image = temp_img)
    img_label.image = temp_img


def process(clicked, captioner, classifier):
    # This function will produce the required output when 'Process' button is clicked.
    # Note: This should handle the case if the user clicks on the `Process` button without selecting any image file.
    captions = captioner(the_file, 3)
    classification = classifier(the_file, 3)
    global output
    if operation.get() == "Caption":
        insertion = StringVar()
        insertion = "Top-3 Captions : \n\n\n"
        for index, val in enumerate(captions):
            insertion += ("\n" +val)
        output = Label(root, height = 30, text = insertion, bg = "#FFFFFF")
        output.text = insertion
        output.grid(row = 1, column = 3)
    if operation.get() == "Classification":
        insertion = StringVar()
        insertion = "Top-3 Classification : \n\n\n"
        for index, val in enumerate(captions):
            insertion += ("\n" +val)
        output = Label(root, height = 30, text = insertion, bg = "#FFFFFF")
        output.text = insertion
        output.grid(row = 1, column = 3)


def main():


    global root
    root = Tk()
    classifier = ImageClassificationModel()
    captioner = ImageCaptioningModel()


    global image_name_display
    image_name_display = Entry(root, state = DISABLED, bg = "#FFFFFF", text = "", width = 40)
    image_name_display.grid(row = 0, column = 0)
    image_name_display.config(state = DISABLED)


    global button_open
    button_open = Button(root, text = "Open", command = lambda : fileClick(clicked = "yes"))
    button_open.grid(row = 0, column = 1, padx = 10)


    global options
    global operation
    global drop
    options = ["Classification", "Caption"]
    operation = StringVar()
    operation.set("Classification")
    drop = OptionMenu(root, operation, *options)
    drop.grid(row = 0, column = 2, padx = 10)


    global button_process
    button_process = Button(root, text = "Process", command = lambda : process(clicked = "yes", captioner = captioner, classifier = classifier))
    button_process.grid(row = 0, column = 3, padx = 10)


    global output 
    output = Label()


    root.mainloop()


if __name__ == '__main__':
    # Complete the main function preferably in this order:  
    # Instantiate the root window.
    # Provide a title to the root window.
    # Instantiate the captioner, classifier models.
    # Declare the file browsing button.
    # Declare the drop-down button.
    # Declare the process button.
    # Declare the output label.
    main()