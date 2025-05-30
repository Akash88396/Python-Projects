if __name__ == '__main__':
    students = []
    
    for _ in range(int(input("Enter range:"))):
        name = input("Enter name:")
        score = float(input("Enter Score:"))
        students.append([name, score])
        
    
    print(students)
    
    scores = sorted(set([score for _, score in students]))
    second_lowest_score = scores[1]  
    
    second_lowest_students = sorted([name for name, score in students if score == second_lowest_score])
    
    print(second_lowest_students)
    for student in second_lowest_students:
        print(student)
