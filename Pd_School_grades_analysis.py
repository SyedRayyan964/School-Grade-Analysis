students = {
    "Name": [
        "Abubakar", "Ahmed", "Sara", "Zain", "Ali",
        "Hassan", "Fatima", "Usman", "Ayesha", "Bilal",
        "Hamza", "Haleema", "Saad", "Iqra", "Talha",
        "Noor", "Daniyal", "Laiba", "Huzaifa", "Sana"
    ],

    "English": [
        118, 95, 135, 110, 45,
        72, 128, 88, 60, 52,
        100, 140, 76, 125, 69,
        132, 84, 119, 57, 137
    ],

    "Urdu": [
        120, 98, 140, 112, 50,
        68, 132, 90, 58, 49,
        102, 145, 80, 130, 65,
        138, 87, 122, 60, 141
    ],

    "Math": [
        130, 85, 145, 120, 25,
        55, 138, 75, 42, 30,
        110, 148, 66, 140, 58,
        142, 79, 126, 45, 144
    ],

    "Physics": [
        110, 75, 138, 102, 20,
        60, 130, 70, 40, 35,
        98, 142, 64, 128, 55,
        135, 74, 115, 39, 140
    ],

    "Chemistry": [
        105, 70, 132, 98, 18,
        58, 126, 68, 39, 32,
        95, 139, 61, 124, 53,
        130, 72, 112, 36, 136
    ],

    "Computer Science": [
        115, 90, 140, 125, 35,
        66, 135, 80, 50, 45,
        108, 144, 70, 136, 60,
        139, 82, 120, 48, 142
    ],

    "Islamiyat": [
        82, 68, 91, 74, 40,
        55, 85, 62, 48, 44,
        70, 92, 58, 88, 52,
        90, 64, 80, 46, 94
    ],

    "Pakistan Studies": [
        78, 65, 88, 72, 38,
        52, 84, 60, 45, 40,
        68, 90, 55, 86, 50,
        89, 62, 76, 42, 93
    ]
}
import pandas as pd
class SchoolGradesAnalysis:
    def __init__(self):
        self.students=students
        self.pd_total=[]
        self.pd_percentage=[]
        self.pd_status=[]
        self.pd_grade=[]
    def Percentage_Analysis(self):    
      self.df = pd.DataFrame(students)
      for Students in range(0,len(self.df)):
        self.Total = self.df["Math"][Students] + self.df["Chemistry"][Students] + self.df["English"][Students]+ self.df["Physics"][Students] + self.df["Islamiyat"][Students] + self.df["Pakistan Studies"][Students] + self.df["Computer Science"][Students] + self.df["Urdu"][Students]
        self.pd_total.append(self.Total)
        Percentage = (self.Total / 1100) * 100
        self.pd_percentage.append(Percentage)
      self.pass_fail_analysis()
    def pass_fail_analysis(self):    
       for stu in range(0,len(self.df["Name"])):
            if self.pd_percentage[stu] >= 40.0 :
                self.pd_status.append("Pass")
            else:
                self.pd_status.append("Fail")
       self.Grade_Analysis()
    def Grade_Analysis(self):
       for stu in range(0,len(self.df["Name"])):
        if self.pd_percentage[stu] >= 80 :
            self.pd_grade.append("A+")
        elif self.pd_percentage[stu] >= 70 and self.pd_percentage[stu]< 80:
            self.pd_grade.append("A")
        elif self.pd_percentage[stu] >= 60 and self.pd_percentage[stu]< 70:
            self.pd_grade.append("B")
        elif self.pd_percentage[stu] >= 50 and self.pd_percentage[stu]< 60:
            self.pd_grade.append("C")
        elif self.pd_percentage[stu]>=40 and self.pd_percentage[stu] < 50:
            self.pd_grade.append("D")
        else:
            self.pd_grade.append("F")
       self.Output_Generator()
    def Output_Generator(self):
        self.df.insert(9,"Total",self.pd_total)
        self.df.insert(10,"Percentage",self.pd_percentage)
        self.df.insert(11,"Status",self.pd_status)
        self.df.insert(12,"Grade",self.pd_grade)
        d= self.df
        d.to_csv("School_Grades_Analysis.csv",index=False)   
        print(d)
Run=SchoolGradesAnalysis()
Run.Percentage_Analysis()