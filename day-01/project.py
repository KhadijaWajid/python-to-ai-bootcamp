# def analyze(marks):
#     total = sum(marks)
#     avg = total / len(marks)
    
#     if avg > 90:
#         print("Excellent")
#     elif avg>70:
#         print("Normal")
#     elif avg > 50:
#         print("Needs improvement")
#     else:
#         print("Bad Result")
        
    
#     for i in range(0,4):
#         print(marks[i])
    
#     print("Total :", total)
#     print("Avg: ", round(avg, 2))
    

# student_marks = [40, 80, 90, 100, 50]

# analyze(student_marks)



#Practice
def track_budget(expenses):
    total = sum(expenses)
    avg = total / len(expenses)

    if total > 500:
        print("Status: Over Budget!")
    elif total > 300:
        print("Status: Moderate spending.")
    elif total > 100:
        print("Status: Within normal budget limits.")
    else:
        print("Status: Low spending! Great savings.")
        
    for i in range(len(expenses)):
        print(f"Expense {i + 1}: ${expenses[i]}")
        
    highest_expense = max(expenses)
    lowest_expense = min(expenses)
    
    print("Total Spent:   $", round(total, 2))
    print("Daily Average: $", round(avg, 2))
    print("Peak Expense:  $", round(highest_expense, 2))
    print("Lowest Spend:  $", round(lowest_expense, 2))

weekly_expenses = [45.50, 120.00, 15.00, 85.20, 210.00]
track_budget(weekly_expenses)
