# 13 Nested Lists
# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    # Store all student records in a nested list
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    
    # Extract unique grades and sort them to find the second lowest
    grades = sorted(set(score for name, score in records))
    second_lowest = grades[1]
    
    # Find all student names with the second lowest grade and sort them alphabetically
    second_lowest_students = sorted([name for name, score in records if score == second_lowest])
    
    # Print each name on a new line
    for name in second_lowest_students:
        print(name)
solutoin for this code s
