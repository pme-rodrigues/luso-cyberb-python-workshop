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
    correct_sentence = f"Hello, my name is {name}. I am {age} years old, and I live in {city}, {country}."
    if sentence == correct_sentence:
        return "Correct Solution"
    else:
        return "Incorrect Solution"


def check_solution_n1_lab3(expression_1, expression_2, expression_3, expression_4, expression_5, expression_6, expression_7, expression_8, expression_9, expression_10,expression_11, expression_12, expression_13, expression_14):
    # Check if all results are True
    if expression_1:
        print("✅ Expression 1 is correct.")
    else:
        print("❌ Expression 1 is incorrect.")

    if expression_2:
        print("✅ Expression 2 is correct.")
    else:
        print("❌ Expression 2 is incorrect.")

    if expression_3: 
        print("✅ Expression 3 is correct.")
    else:
        print("❌ Expression 3 is incorrect.")

    if expression_4:
        print("✅ Expression 4 is correct.")
    else:
        print("❌ Expression 4 is incorrect.")

    if expression_5:
        print("✅ Expression 5 is correct.")
    else:
        print("❌ Expression 5 is incorrect.")

    if expression_6:
        print("✅ Expression 6 is correct.")
    else:
        print("❌ Expression 6 is incorrect.")

    if not expression_7:
        print("✅ Expression 7 is correct.")
    else:
        print("❌ Expression 7 is incorrect.")

    if expression_8:
        print("✅ Expression 8 is correct.")
    else:
        print("❌ Expression 8 is incorrect.")

    if expression_9:
        print("✅ Expression 9 is correct.")
    else:
        print("❌ Expression 9 is incorrect.")

    if not expression_10:
        print("✅ Expression 9 is correct.")
    else:
        print("❌ Expression 9 is incorrect.")

    if expression_11:
        print("✅ Expression 9 is correct.")
    else:
        print("❌ Expression 9 is incorrect.")

    if not expression_12:
        print("✅ Expression 9 is correct.")
    else:
        print("❌ Expression 9 is incorrect.")

    if expression_13:
        print("✅ Expression 9 is correct.")
    else:
        print("❌ Expression 9 is incorrect.")

    if expression_14:
        print("✅ Expression 9 is correct.")
    else:
        print("❌ Expression 9 is incorrect.")


def check_solution_n2_lab3(expression_1, expression_2, expression_3, expression_4, expression_5, expression_6, expression_7, expression_8, expression_9):
    # Check if all results are True
    if expression_1 == -3.5:
        print("✅ Expression 1 is correct.")
    else:
        print("❌ Expression 1 is incorrect.")

    if expression_2 == 1.75:
        print("✅ Expression 2 is correct.")
    else:
        print("❌ Expression 2 is incorrect.")

    if expression_3 == -2: 
        print("✅ Expression 3 is correct.")
    else:
        print("❌ Expression 3 is incorrect.")

    if expression_4 == -14:
        print("✅ Expression 4 is correct.")
    else:
        print("❌ Expression 4 is incorrect.")

    if expression_5 == 32:
        print("✅ Expression 5 is correct.")
    else:
        print("❌ Expression 5 is incorrect.")

    if expression_6 == -504:
        print("✅ Expression 6 is correct.")
    else:
        print("❌ Expression 6 is incorrect.")

    if expression_7 == -30.25:
        print("✅ Expression 7 is correct.")
    else:
        print("❌ Expression 7 is incorrect.")

    if expression_8 == 6:
        print("✅ Expression 8 is correct.")
    else:
        print("❌ Expression 8 is incorrect.")

    if expression_9 == -194.5:
        print("✅ Expression 9 is correct.")
    else:
        print("❌ Expression 9 is incorrect.")





def check_solution_n3_lab3(result_1, result_2, result_3, result_4, result_5, result_6, result_7, result_8, result_9):
    # Check if all results are True
    if result_1:
        print("✅ Expression 1 is correct.")
    else:
        print("❌ Expression 1 is incorrect.")

    if result_2:
        print("✅ Expression 2 is correct.")
    else:
        print("❌ Expression 2 is incorrect.")

    if result_3:
        print("✅ Expression 3 is correct.")
    else:
        print("❌ Expression 3 is incorrect.")

    if result_4:
        print("✅ Expression 4 is correct.")
    else:
        print("❌ Expression 4 is incorrect.")

    if result_5:
        print("✅ Expression 5 is correct.")
    else:
        print("❌ Expression 5 is incorrect.")

    if result_6:
        print("✅ Expression 6 is correct.")
    else:
        print("❌ Expression 6 is incorrect.")

    if result_7:
        print("✅ Expression 7 is correct.")
    else:
        print("❌ Expression 7 is incorrect.")

    if result_8:
        print("✅ Expression 8 is correct.")
    else:
        print("❌ Expression 8 is incorrect.")

    if result_9:
        print("✅ Expression 9 is correct.")
    else:
        print("❌ Expression 9 is incorrect.")




def check_solution_n4_lab3(text, fourth_letter, last_letter, first_word, last_word, speak_louder, middle_text, reversed_text):
    # Expected values
    expected_fourth_letter = text[3]  # Fourth letter (index 3)
    expected_last_letter = text[-1]  # Last letter (index -1)
    expected_first_word = text[:7]  # First 7 characters
    expected_last_word = text[-6:-1]  # Last 5 characters before the period
    expected_speak_louder = text[8:20]  # Slice of 'speak louder'
    expected_middle_text = text[1:-1]  # All characters except first and last
    expected_reversed_text = text[::-1]  # Reverse the entire string
    
    # Check 4th letter
    if fourth_letter == expected_fourth_letter:
        print(f"✅ The 4th letter is correct: {fourth_letter}")
    else:
        print(f"❌ The 4th letter is incorrect. Expected {expected_fourth_letter}, but got {fourth_letter}")
    
    # Check last letter
    if last_letter == expected_last_letter:
        print(f"✅ The last letter is correct: {last_letter}")
    else:
        print(f"❌ The last letter is incorrect. Expected {expected_last_letter}, but got {last_letter}")
    
    # Check first word
    if first_word == expected_first_word:
        print(f"✅ The first word is correct: {first_word}")
    else:
        print(f"❌ The first word is incorrect. Expected '{expected_first_word}', but got '{first_word}'")
    
    # Check last word
    if last_word == expected_last_word:
        print(f"✅ The last word is correct: {last_word}")
    else:
        print(f"❌ The last word is incorrect. Expected '{expected_last_word}', but got '{last_word}'")
    
    # Check slice 'speak louder'
    if speak_louder == expected_speak_louder:
        print(f"✅ The slice 'speak louder' is correct: {speak_louder}")
    else:
        print(f"❌ The slice 'speak louder' is incorrect. Expected '{expected_speak_louder}', but got '{speak_louder}'")
    
    # Check middle text
    if middle_text == expected_middle_text:
        print(f"✅ The text without first and last characters is correct: {middle_text}")
    else:
        print(f"❌ The text without first and last characters is incorrect. Expected '{expected_middle_text}', but got '{middle_text}'")
    
    # Check reversed text
    if reversed_text == expected_reversed_text:
        print(f"✅ The reversed text is correct: {reversed_text}")
    else:
        print(f"❌ The reversed text is incorrect. Expected '{expected_reversed_text}', but got '{reversed_text}'")



def check_solution_n5_lab3(text, starts_with_practice, ends_with_perfect, count_e, index_makes, new_text, words_list, joined_text, uppercase_text, number_vowels):
    # Expected values
    expected_starts_with_practice = text.startswith("Practice")
    expected_ends_with_perfect = text.endswith("perfect")
    expected_count_e = text.count("e")
    expected_index_makes = text.find("makes")
    expected_new_text = text.replace("makes", "creates")
    expected_words_list = text.split()
    expected_joined_text = ", ".join(expected_words_list)
    expected_uppercase_text = text.upper()
    
    expected_number_a = text.lower().count('a')
    expected_number_e = text.lower().count('e')
    expected_number_i = text.lower().count('i')
    expected_number_o = text.lower().count('o')
    expected_number_u = text.lower().count('u')
    expected_number_vowels = expected_number_a + expected_number_e + expected_number_i + expected_number_o + expected_number_u

    # Check starts with 'Practice'
    if starts_with_practice == expected_starts_with_practice:
        print("✅ 'Starts with Practice' is correct.")
    else:
        print("❌ 'Starts with Practice' is incorrect.")
    
    # Check ends with 'perfect'
    if ends_with_perfect == expected_ends_with_perfect:
        print("✅ 'Ends with perfect' is correct.")
    else:
        print("❌ 'Ends with perfect' is incorrect.")
    
    # Check number of 'e's
    if count_e == expected_count_e:
        print(f"✅ The count of 'e' is correct: {count_e}.")
    else:
        print(f"❌ The count of 'e' is incorrect. Expected {expected_count_e}, but got {count_e}.")
    
    # Check index of 'makes'
    if index_makes == expected_index_makes:
        print(f"✅ The index of 'makes' is correct: {index_makes}.")
    else:
        print(f"❌ The index of 'makes' is incorrect. Expected {expected_index_makes}, but got {index_makes}.")
    
    # Check replaced text
    if new_text == expected_new_text:
        print("✅ The replaced text is correct.")
    else:
        print(f"❌ The replaced text is incorrect. Expected '{expected_new_text}', but got '{new_text}'.")
    
    # Check word list
    if words_list == expected_words_list:
        print(f"✅ The list of words is correct: {words_list}.")
    else:
        print(f"❌ The list of words is incorrect. Expected {expected_words_list}, but got {words_list}.")
    
    # Check joined text
    if joined_text == expected_joined_text:
        print(f"✅ The joined text is correct: {joined_text}.")
    else:
        print(f"❌ The joined text is incorrect. Expected '{expected_joined_text}', but got '{joined_text}'.")
    
    # Check uppercase text
    if uppercase_text == expected_uppercase_text:
        print(f"✅ The uppercase text is correct: {uppercase_text}.")
    else:
        print(f"❌ The uppercase text is incorrect. Expected '{expected_uppercase_text}', but got '{uppercase_text}'.")
    
    # Check number of vowels
    if number_vowels == expected_number_vowels:
        print(f"✅ The number of vowels is correct: {number_vowels}.")
    else:
        print(f"❌ The number of vowels is incorrect. Expected {expected_number_vowels}, but got {number_vowels}.")



def check_solution_n6_lab3(sentence_1, sentence_2, sentence_3, actions_count):
    # Define the expected values
    expected_sentence_1 = "actions speak louder than words."
    expected_sentence_2 = "it is not how you say, but how you do."
    expected_sentence_3 = "actions matter more than words."
    expected_actions_count = 2
    
    # Check the sentences
    if sentence_1 == expected_sentence_1:
        print("✅ Sentence 1 is correct.")
    else:
        print("❌ Sentence 1 is incorrect.")
    
    if sentence_2 == expected_sentence_2:
        print("✅ Sentence 2 is correct.")
    else:
        print("❌ Sentence 2 is incorrect.")
    
    if sentence_3 == expected_sentence_3:
        print("✅ Sentence 3 is correct.")
    else:
        print("❌ Sentence 3 is incorrect.")
    
    # Check the number of occurrences of "actions"
    if actions_count == expected_actions_count:
        print(f"✅ The number of counts of the word 'actions' is correct.")
    else:
        print(f"❌ The number of counts of the word 'actions' is incorrect.")



    