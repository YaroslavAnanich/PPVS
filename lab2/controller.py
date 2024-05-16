import model

def open_student_file(path):
    students = model.add_student_to_memory_list(path)
    return students


def open_languages_file():
    languages = model.add_language_to_memory_list()
    return languages


def save_student_file(name,course,group,total_number_of_works,number_of_completed_works,programming_language):
    model.set_student_to_xml(name,course,group,total_number_of_works,number_of_completed_works,programming_language,
                             "/EXAMPLE/example.xml")

def find_student_in_file(name, course, group, total_number_of_works, number_of_completed_works, programming_language):
    model.find_student_in_memory_list(name, course, group, total_number_of_works,
                                      number_of_completed_works, programming_language)

def dell_student_in_file(name, course, group, total_number_of_works, number_of_completed_works, programming_language):
    model.dell_student_in_memory_list(name, course, group, total_number_of_works,
                                      number_of_completed_works, programming_language)


