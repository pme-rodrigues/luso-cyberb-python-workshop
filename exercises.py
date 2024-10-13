import random

random_words = ["whisper", "galaxy", "wander", "crystal", "star", "ocean", "cascade", "ember", "velocity", "eclipse"]

def mistery_box(n = 3):
    
    types = list(['float', 'int', 'bool', 'str'])
    
    output = []

    for i in range(n):
        var_type = random.choice(types)
        if var_type == 'float':
            output.append(random.random() * 100)
        elif var_type == 'int':
            output.append(random.randint(1, 100))
        elif var_type == 'str':
            output.append(random.choice(random_words))
        else:
            output.append(bool(random.randint(0, 2)))

    return output

def check_solution_n1(mistery_x, mistery_y, mistery_z, mistery_x_type, mistery_y_type, mistery_z_type):
    if (type(mistery_x) == mistery_x_type) \
        and (type(mistery_y) == mistery_y_type) \
            and (type(mistery_z) == mistery_z_type):
        return 'Correct Solution'
    return 'Incorrect Solution'


def check_solution_n2(question_1, question_2, question_3, question_4, question_5, 
                      question_6, question_7, question_8, question_9, question_10):
    # Correct answers
    correct_answers = [False, True, True, True, True, True, False, True, False, True]
    
    # User's answers
    user_answers = [question_1, question_2, question_3, question_4, question_5,
                    question_6, question_7, question_8, question_9, question_10]
    
    if user_answers == correct_answers:
        return 'Correct Solution'
    else:
        return 'Incorrect Solution'


def check_solution_n3(name, age, city, country, sentence):
    correct_sentence = f"Hello, my name is {name}. I am {age} years old, I live in {city}, {country}."
    if sentence == correct_sentence:
        return "Correct Solution"
    else:
        return "Incorrect Solution"