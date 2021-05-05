def calper():
    exam_name = input('Enter Your Name: ')
    marks_obtained_math = int(input('Enter the Marks you have obtained in math: '))
    marks_obtained_sci = int(input('Enter the Marks you have obtained in sci: '))
    marks_obtained_eng = int(input('Enter the Marks you have obtained in eng: '))
    marks_obtained_soc = int(input('Enter the Marks you have obtained in soc: '))
    marks_obtained_lan = int(input('Enter the Marks you have obtained in 2nd Language: '))
    max_marks = int(input('Enter the Maximum Marks: '))*5
    percenatge = (marks_obtained_math+marks_obtained_sci+marks_obtained_soc+marks_obtained_eng+marks_obtained_lan)/max_marks*100
    print('The Percentage you have obtained in ' + exam_name + ' is '+ str(percenatge)+'%')
calper()    