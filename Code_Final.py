import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model
from keras.utils import load_img, img_to_array
from keras.utils.image_utils import img_to_array
from tkinter import *
from tkinter.filedialog import *
from PIL import Image, ImageTk

gender = load_model("C:\\Desktop\\AI\\Gender_Detection.h5")
picture = 0
def predict():
    global gender
    global picture
    vat = {1:'Male', 2:'Female'}
    result = np.argmax(gender.predict(picture), axis=1)
    label_1.config(text='{}'.format(vat[result[0]]))

def import_picture():
    global picture
    filename = askopenfilename(initialdir = 'c:\\python31\\', filetypes=[('jpg files', '.jpg')])
    load = Image.open(filename)
    new_size = (300, 285)
    load = load.resize(new_size)
    render = ImageTk.PhotoImage(load)
    picture = load_img(filename, target_size=(30, 40))
    plt.imshow(picture)
    picture = img_to_array(picture)
    picture = picture.reshape(1, 30, 40, 3)
    picture = picture.astype('float32')
    picture = picture/255
    result.configure(image=render)
    result.image = render
    import_picture["state"] = "normal"
    label_1.config(text='')

def delete():
    global result
    result.destroy()
    result = Label()
    result = Label(padx = 150, pady = 135)
    result.place(x = 35, y = 190)
    import_picture["state"] = DISABLED
    label_1.config(text='')

window = Tk()
window.geometry("1000x600")
window.title("Gender Detection")
bg = PhotoImage(file = "C:\\Users\\Admin\\Downloads\\tri-tue-nhan-tao-la-gi.png")
background = Label(window, image = bg)
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

label_1 = Label(font=('Showcard Gothic', 20), bg = "#F9D949", width = 10, height = 2, relief = "sunken")
label_1.place(x = 735, y = 250)

label_2 = Label(text = 'Result', font=('Showcard Gothic', 20), bg = "#F9D949", relief = "sunken")
label_2.place(x = 780, y = 110)

result = Label(padx = 150, pady = 135)
result.place(x = 35, y = 190)

label_3 = Label(text = 'Picture', font=('Showcard Gothic', 20), bg = "#F9D949", relief = "sunken")
label_3.place(x = 125, y = 110)

label_4 = Label(text= 'Gender Detection', font = ('Showcard Gothic', 30), bg = "#F9D949", relief = "sunken")
label_4.place(x = 305, y = 20)

delete = Button(text = 'Delete', font=('Showcard Gothic', 20), bg = "#F9D949",relief = "raised", command = delete)
delete.place(x=430, y=510)

convert = Button(text = 'Choose a picture', font = ('Showcard Gothic', 20), bg = "#F9D949",relief = "raised", command = import_picture)
convert.place(x = 50, y = 510)

import_picture = Button(text = 'Predict', font = ('Showcard Gothic', 20), bg = "#F9D949",relief = "raised", command = predict)
import_picture.place(x = 760, y=510)
import_picture["state"]= DISABLED

mainloop()