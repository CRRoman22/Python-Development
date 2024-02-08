while True:
    name = input("Enter Student name? ")
    cat = int(input("Enter CAT Score? "))
    gpa = float(input("Enter GPA? "))
    activity = int(input("Enter no.on extra-curricular activities? "))

    if cat>=1600 and gpa>=3.0 and activity>=3:
        print(name, "should be admitted!")
    elif cat>=1400 and gpa>=2.8 and activity>=5:
        print(name, "should be admitted!")
    else:
        print(name, "should not be admitted!")


    student = input("Another student? (yes/no) ")

    if student == 'yes':
        continue
    else:
        break
