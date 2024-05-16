import os
import xml.etree.ElementTree as ET

students = []
languages = []
path_to_program = "D:/Projects/My-Labs/Yarik/Course2/SEM_2/POIS/lab2(pois)/"
data_directory = "DATA"


def get_student_from_xml(xml_path):
    students.clear()
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        students_in_xml = root.find('students')
        students_in_xml = students_in_xml.findall('student')
        for student in students_in_xml:
            row = []
            row.append(student.get('name'))
            row.append(int(student.get('course')))
            row.append(int(student.get('group')))
            row.append(int(student.get('total_number_of_works')))
            row.append(int(student.get('number_of_completed_works')))
            row.append(student.get('programming_language'))
            students.append(row)
    except IOError as error:
        print(error)

def get_languages_from_xml(xml_path):
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        language_in_xml = root.find('languages')
        language_in_xml = language_in_xml.findall('language')
        for language in language_in_xml:
            languages.append(language.get('name'))
    except IOError as error:
        print(error)


def set_student_to_xml(name,course,group,total_number_of_works,number_of_completed_works,programming_language, path):
    path_to_XML = path_to_program + data_directory + path
    tree = ET.parse(path_to_XML)
    root = tree.getroot()
    print(name,course,group,total_number_of_works,number_of_completed_works,programming_language)
    student = ET.Element('student',
                         attrib={'name': name,
                                 'course': str(course),
                                 'group': str(group),
                                 'total_number_of_works': str(total_number_of_works),
                                 'number_of_completed_works': str(number_of_completed_works),
                                 'programming_language': programming_language})
    root.find('students').append(student)
    tree.write(path_to_XML)


def add_student_to_memory_list(file_path):
    path_to_XML = path_to_program + data_directory
    get_student_from_xml(path_to_XML + file_path)
    return students


def add_language_to_memory_list():
    path_to_XML = path_to_program + data_directory + "/LANGUAGES/"
    files_list = os.listdir(path_to_XML)
    for file in files_list:
        get_languages_from_xml(path_to_XML + file)
    return languages

def find_student_in_memory_list(name,course,group,total_number_of_works,number_of_completed_works,programming_language):
    clear_xml("/INFO/info.xml")
    for student in students:
        number = 0
        check = check_student(name, number, student)
        if check == False:
            continue
        number += 1
        check = check_student(course, number, student)
        if check == False:
            continue
        number += 1
        check = check_student(group, number, student)
        if check == False:
            continue
        number += 1
        check = check_student(total_number_of_works, number, student)
        if check == False:
            continue
        number += 1
        check = check_student(number_of_completed_works, number, student)
        if check == False:
            continue
        number += 1
        check = check_student(programming_language, number, student)
        if check == True:
            set_student_to_xml(student[0],student[1],student[2],student[3],student[4],student[5],"/INFO/info.xml")

def dell_student_in_memory_list(name,course,group,total_number_of_works,number_of_completed_works,programming_language):
    clear_xml("/INFO/info.xml")
    del_stud = students
    for student in students:
        number = 0
        check = check_student(name, number, student)
        if check == False:
            continue
        number += 1
        check = check_student(course, number, student)
        if check == False:
            continue
        number += 1
        check = check_student(group, number, student)
        if check == False:
            continue
        number += 1
        check = check_student(total_number_of_works, number, student)
        if check == False:
            continue
        number += 1
        check = check_student(number_of_completed_works, number, student)
        if check == False:
            continue
        number += 1
        check = check_student(programming_language, number, student)
        if check == True:
            set_student_to_xml(student[0],student[1],student[2],student[3],student[4],student[5],"/INFO/info.xml")
            delete = student
            del_stud.remove(delete)
    clear_xml("/EXAMPLE/example.xml")
    for stud in del_stud:
        set_student_to_xml(stud[0], stud[1], stud[2], stud[3], stud[4], stud[5]
                           , "/EXAMPLE/example.xml")

def check_student(parament, number, student):
    if parament != '':
        if parament == str(student[number]):
            return True
        else:
            return False
    else:
        return True

def clear_xml(path):
    tree = ET.parse(path_to_program + data_directory + path)
    root = tree.getroot()
    studs = root.find('students')
    for student in studs.findall('student'):
        studs.remove(student)
    tree.write(path_to_program + data_directory + path)




