from tkinter import *

root = Tk()
root.title("Percentage Calculator")
root.configure(bg="white")
root.geometry("300x400")

class grade_3:
    def __init__(self, english, mathematic):
        self.mathematic = mathematic
        self.english = english
    
    def percentage(self):
        totalMark = self.mathematic + self.english

        percentage = totalMark / 200 * 100
        grade_3_label['text'] = str(percentage) + "%"


class grade_5:
    def __init__(self, english, mathematic, social_studies):
        self.mathematic = mathematic
        self.english = english
        self.social_studies = social_studies
    
    def percentage(self):
        totalMark = self.mathematic + self.english + self.social_studies

        percentage = totalMark / 300 * 100
        grade_5_label['text'] = str(percentage) + "%"


class grade_8:
    def __init__(self, english, mathematic, social_studies, science):
        self.mathematic = mathematic
        self.english = english
        self.science = science
        self.social_studies = social_studies
    
    def percentage(self):
        totalMark = self.mathematic + self.english +self.science + self.social_studies

        percentage = totalMark / 400 * 100
        grade_8_label['text'] = str(percentage) + "%"


Intance_of_class_grade3 = grade_3(99, 97)
Intance_of_class_grade5 = grade_5(99, 97, 100)
Intance_of_class_grade8 = grade_8(99, 97, 100, 98)

grade_3_label = Label(root)
grade_3_label.pack(pady=30)

button = Button(root, text="Grade 3", bg="#818391",foreground= "#ffffff", command=Intance_of_class_grade3.percentage)
button.pack()

grade_5_label = Label(root)
grade_5_label.pack(pady=30)

button = Button(root, text="Grade 5", bg="#818391",foreground= "#ffffff", command=Intance_of_class_grade5.percentage)
button.pack()

grade_8_label = Label(root)
grade_8_label.pack(pady=30)

button = Button(root, text="Grade 8", bg="#818391",foreground= "#ffffff", command=Intance_of_class_grade8.percentage)
button.pack()

root.mainloop()