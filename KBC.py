<<<<<<< HEAD
                                #  CHAT GPT CODE

# import time
# import sys

# def kbc_game():
#     questions = [
        # {
        #     "question": "Who is known as the Father of India?",
        #     "options": ["A. Jawaharlal Nehru", "B. Sardar Patel", "C. Mahatma Gandhi", "D. Bhagat Singh"],
        #     "answer": "C"
        # },
        # {
        #     "question": "What is the capital of France?",
        #     "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        #     "answer": "C"
        # },
        # {
        #     "question": "Which is the largest planet in our Solar System?",
        #     "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"],
        #     "answer": "B"
        # },
        # {
        #     "question": "Who wrote the national anthem of India?",
        #     "options": ["A. Rabindranath Tagore", "B. Bankim Chandra Chatterjee", "C. Sarojini Naidu", "D. Subhash Chandra Bose"],
        #     "answer": "A"
        # }
#     ]
    
#     prize_money = [1000, 5000, 10000, 50000]
    
#     print("\n\n\t\t\t\tWelcome to Kaun Banega Crorepati!\n")
#     time.sleep(3)
    
#     try:
#         for i, q in enumerate(questions):
#             print(f"Question {i+1}: {q['question']}")
            
#             for option in q["options"]:
#                 time.sleep(2)
#                 print(option)
            
#             answer = input("Enter your answer (A/B/C/D): ").strip().upper()
            
#             if answer == q["answer"]:
#                 time.sleep(3)
#                 print(f"Correct! You have won Rs. {prize_money[i]}\n")
#             else:
#                 time.sleep(3)
#                 print("Wrong answer! Game Over.")
#                 print(f"You won Rs. {prize_money[i-1] if i > 0 else 0}")
#                 break
#         else:
#             print("Congratulations! You have won the grand prize of Rs. 50,000!")
#     except (KeyboardInterrupt, EOFError):
#         print("\nGame exited unexpectedly. Thank you for playing!")
#         sys.exit(1)

# if __name__ == "__main__":
#     kbc_game()




#                                MY KBC CODE

import time 

quesetionList = [
    {
        'question':'Who was the first President of India ?',

        'options':['A. Dr. Rajendra Prasad','B. Dr. B. R. Ambedkar','C. Jawaharlal Nehru', 'D. Sardar Vallabhbhai Patel']  ,

        'answer':'A'    
    },
    {
        'question':'Which is the longest river in the world?',

        'options':['A. Amazon River',
                       'B. Ganges River',
                        'C. Nile River',
                       'D. Yangtze River']  ,

        'answer':'C'    

    },
    {
            "question": "Who is known as the Father of India?",
            "options": ["A. Jawaharlal Nehru", "B. Sardar Patel", "C. Mahatma Gandhi", "D. Bhagat Singh"],
            "answer": "C"
        },
        {
            "question": "What is the capital of France?",
            "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
            "answer": "C"
        },
        {
            "question": "Which is the largest planet in our Solar System?",
            "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"],
            "answer": "B"
        },
        {
            "question": "Who wrote the national anthem of India?",
            "options": ["A. Rabindranath Tagore", "B. Bankim Chandra Chatterjee", "C. Sarojini Naidu", "D. Subhash Chandra Bose"],
            "answer": "A"
        },
        {
            'question':'Which gas do plants absorb during photosynthesis?',
            'options':['A. Carbon Dioxide','B. Nitrojen','C. Hydogen','D. Oxygen'],
            'answer':"A"
        }
]


level = [1000,2000,5000,10000,25000,50000,1000000]

for i ,q in enumerate(quesetionList):
    print(f"Question {i+1} : {q['question']}")
    
    for option in q['options']:
        print(option)

    result = input("Enter correct option (A/B/C/D):").strip().upper()    

    if result == q['answer']:
        
        print(f"Correct answer ! you won {level[i]}\n ")
    else:
        print("Wrong answer! Game is over now!")
        print(f"Your wining price is {level[i-1] if i>0 else 0}")
        break
else:
=======
                                #  CHAT GPT CODE

# import time
# import sys

# def kbc_game():
#     questions = [
        # {
        #     "question": "Who is known as the Father of India?",
        #     "options": ["A. Jawaharlal Nehru", "B. Sardar Patel", "C. Mahatma Gandhi", "D. Bhagat Singh"],
        #     "answer": "C"
        # },
        # {
        #     "question": "What is the capital of France?",
        #     "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        #     "answer": "C"
        # },
        # {
        #     "question": "Which is the largest planet in our Solar System?",
        #     "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"],
        #     "answer": "B"
        # },
        # {
        #     "question": "Who wrote the national anthem of India?",
        #     "options": ["A. Rabindranath Tagore", "B. Bankim Chandra Chatterjee", "C. Sarojini Naidu", "D. Subhash Chandra Bose"],
        #     "answer": "A"
        # }
#     ]
    
#     prize_money = [1000, 5000, 10000, 50000]
    
#     print("\n\n\t\t\t\tWelcome to Kaun Banega Crorepati!\n")
#     time.sleep(3)
    
#     try:
#         for i, q in enumerate(questions):
#             print(f"Question {i+1}: {q['question']}")
            
#             for option in q["options"]:
#                 time.sleep(2)
#                 print(option)
            
#             answer = input("Enter your answer (A/B/C/D): ").strip().upper()
            
#             if answer == q["answer"]:
#                 time.sleep(3)
#                 print(f"Correct! You have won Rs. {prize_money[i]}\n")
#             else:
#                 time.sleep(3)
#                 print("Wrong answer! Game Over.")
#                 print(f"You won Rs. {prize_money[i-1] if i > 0 else 0}")
#                 break
#         else:
#             print("Congratulations! You have won the grand prize of Rs. 50,000!")
#     except (KeyboardInterrupt, EOFError):
#         print("\nGame exited unexpectedly. Thank you for playing!")
#         sys.exit(1)

# if __name__ == "__main__":
#     kbc_game()




#                                MY KBC CODE

import time 

quesetionList = [
    {
        'question':'Who was the first President of India ?',

        'options':['A. Dr. Rajendra Prasad','B. Dr. B. R. Ambedkar','C. Jawaharlal Nehru', 'D. Sardar Vallabhbhai Patel']  ,

        'answer':'A'    
    },
    {
        'question':'Which is the longest river in the world?',

        'options':['A. Amazon River',
                       'B. Ganges River',
                        'C. Nile River',
                       'D. Yangtze River']  ,

        'answer':'C'    

    },
    {
            "question": "Who is known as the Father of India?",
            "options": ["A. Jawaharlal Nehru", "B. Sardar Patel", "C. Mahatma Gandhi", "D. Bhagat Singh"],
            "answer": "C"
        },
        {
            "question": "What is the capital of France?",
            "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
            "answer": "C"
        },
        {
            "question": "Which is the largest planet in our Solar System?",
            "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"],
            "answer": "B"
        },
        {
            "question": "Who wrote the national anthem of India?",
            "options": ["A. Rabindranath Tagore", "B. Bankim Chandra Chatterjee", "C. Sarojini Naidu", "D. Subhash Chandra Bose"],
            "answer": "A"
        },
        {
            'question':'Which gas do plants absorb during photosynthesis?',
            'options':['A. Carbon Dioxide','B. Nitrojen','C. Hydogen','D. Oxygen'],
            'answer':"A"
        }
]


level = [1000,2000,5000,10000,25000,50000,1000000]

for i ,q in enumerate(quesetionList):
    print(f"Question {i+1} : {q['question']}")
    
    for option in q['options']:
        print(option)

    result = input("Enter correct option (A/B/C/D):").strip().upper()    

    if result == q['answer']:
        
        print(f"Correct answer ! you won {level[i]}\n ")
    else:
        print("Wrong answer! Game is over now!")
        print(f"Your wining price is {level[i-1] if i>0 else 0}")
        break
else:
>>>>>>> 24e997752c4f7a453d885da1e91bcefa948f39e2
    print("Congratulations! You have won the grand prize of Rs. 100000!")