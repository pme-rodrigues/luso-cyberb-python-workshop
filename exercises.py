import random

random_words = ["whisper", "galaxy", "wander", "crystal", "star", "ocean", "cascade", "ember", "velocity", "eclipse"]

mystery_groceries_list = ["apple", "banana", "milk", "apple", "eggs", "banana", "orange", "bread", "milk", "chair", "car"]

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

def get_bookstore_inventory():
    return {
    "Brave New World": {
        "author": "Aldous Huxley",
        "publisher": "Chatto & Windus",
        "price": 9.49
    },
    "War and Peace": {
        "author": "Leo Tolstoy",
        "publisher": "The Russian Messenger",
        "price": 14.99
    },
    "Ulysses": {
        "author": "James Joyce",
        "publisher": "Sylvia Beach",
        "price": 13.49
    },
    "The Odyssey": {
        "author": "Homer",
        "publisher": "Ancient Greek Publication",
        "price": 11.99
    },
    "Crime and Punishment": {
        "author": "Fyodor Dostoevsky",
        "publisher": "The Russian Messenger",
        "price": 10.49
    },
    "The Catcher in the Rye": {
        "author": "J.D. Salinger",
        "publisher": "Little, Brown and Company",
        "price": 8.79
    },
    "The Lord of the Rings": {
        "author": "J.R.R. Tolkien",
        "publisher": "Allen & Unwin",
        "price": 20.99
    },
    "The Hobbit": {
        "author": "J.R.R. Tolkien",
        "publisher": "Allen & Unwin",
        "price": 7.49
    },
    "Harry Potter and the Philosopher's Stone": {
        "author": "J.K. Rowling",
        "publisher": "Bloomsbury",
        "price": 6.99
    },
    "Harry Potter and the Chamber of Secrets": {
        "author": "J.K. Rowling",
        "publisher": "Bloomsbury",
        "price": 7.99
    },
    "Frankenstein": {
        "author": "Mary Shelley",
        "publisher": "Lackington, Hughes, Harding, Mavor & Jones",
        "price": 8.29
    },
    "Dracula": {
        "author": "Bram Stoker",
        "publisher": "Archibald Constable and Company",
        "price": 9.79
    },
    "The Brothers Karamazov": {
        "author": "Fyodor Dostoevsky",
        "publisher": "The Russian Messenger",
        "price": 15.49
    },
    "Anna Karenina": {
        "author": "Leo Tolstoy",
        "publisher": "The Russian Messenger",
        "price": 12.49
    },
    "The Picture of Dorian Gray": {
        "author": "Oscar Wilde",
        "publisher": "Ward, Lock & Co.",
        "price": 8.59
    },
    "Les Misérables": {
        "author": "Victor Hugo",
        "publisher": "A. Lacroix, Verboeckhoven & Cie",
        "price": 18.99
    },
    "Don Quixote": {
        "author": "Miguel de Cervantes",
        "publisher": "Francisco de Robles",
        "price": 11.49
    },
    "Jane Eyre": {
        "author": "Charlotte Brontë",
        "publisher": "Smith, Elder & Co.",
        "price": 7.89
    },
    "Wuthering Heights": {
        "author": "Emily Brontë",
        "publisher": "Thomas Cautley Newby",
        "price": 9.19
    },
    "Fahrenheit 451": {
        "author": "Ray Bradbury",
        "publisher": "Ballantine Books",
        "price": 10.29
    }
    }

def mistery_numbers(n):
    return [random.randint(0, 10) for i in range(n)]

def mistery_employee():
    employees = {
    "Alice": {"base_salary": 80000, "sales": 45},
    "Bob": {"base_salary": 60000, "sales": 78},
    "Charlie": {"base_salary": 50000, "sales": 120},
    "David": {"base_salary": 30000, "sales": 155}
    }
    return employees[random.choice(list(employees.keys()))]

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
        print("✅ Expression 10 is correct.")
    else:
        print("❌ Expression 10 is incorrect.")

    if expression_11:
        print("✅ Expression 11 is correct.")
    else:
        print("❌ Expression 11 is incorrect.")

    if not expression_12:
        print("✅ Expression 12 is correct.")
    else:
        print("❌ Expression 12 is incorrect.")

    if expression_13:
        print("✅ Expression 13 is correct.")
    else:
        print("❌ Expression 13 is incorrect.")

    if expression_14:
        print("✅ Expression 14 is correct.")
    else:
        print("❌ Expression 14 is incorrect.")


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

    if expression_9 == -192.5:
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



def check_solution_n1_lab4(mystery_list, groceries_list, groceries_string):
    # Step 1: Check the original list and length
    if len(mystery_list) != 11:
        print("❌ Step 1: Incorrect number of elements in the original list.")
    else:
        print("✅ Step 1: Original list and length are correct.")
    
    # Step 2: Check that non-grocery items have been removed (length should be reduced by 2)
    if len(groceries_list) != len(mystery_list) - 2:
        print("❌ Step 2: Non-grocery items not correctly removed.")
    else:
        print("✅ Step 2: Non-grocery items removed correctly.")
    
    # Step 4: Check if duplicates have been removed
    if len(set(groceries_list)) != len(groceries_list):
        print("❌ Step 4: Duplicates not removed correctly.")
    else:
        print("✅ Step 4: Duplicates removed correctly.")
    
    # Step 5: Check if vegetables have been added to the list
    if not all(veg in groceries_list for veg in ["carrot", "broccoli", "spinach"]):
        print("❌ Step 5: Vegetables not added correctly.")
    else:
        print("✅ Step 5: Vegetables added correctly.")
    
    # Step 6: Check if the items are joined correctly into a single string
    expected_string = ", ".join(groceries_list)
    if groceries_string != expected_string:
        print("❌ Step 6: Final inventory string is incorrect.")
    else:
        print("✅ Step 6: Final inventory string is correct.")


def check_solution_n2_lab4(even_list, odd_list, even_middle_elements, odd_middle_element):
    # Step 1: Check lengths
    if len(even_list) % 2 != 0 or len(odd_list) % 2 == 0:
        print("❌ Step 1: Lengths are incorrect. `even_list` should have an even length and `odd_list` an odd length.")
    else:
        print("✅ Step 1: Lengths are correct.")
    
    # Step 2: Check if the lists are sorted
    if even_list != sorted(even_list):
        print("❌ Step 2: `even_list` is not sorted correctly.")
    else:
        print("✅ Step 2: `even_list` is sorted correctly.")
    
    if odd_list != sorted(odd_list):
        print("❌ Step 2: `odd_list` is not sorted correctly.")
    else:
        print("✅ Step 2: `odd_list` is sorted correctly.")
    
    # Step 3: Check even list middle elements
    correct_even_middle_elements = sorted(even_list)[(len(even_list) // 2) - 1:(len(even_list) // 2) + 1]
    if even_middle_elements != correct_even_middle_elements:
        print("❌ Step 3: Middle elements of `even_list` are incorrect.")
    else:
        print("✅ Step 3: Middle elements of `even_list` are correct.")
    
    # Step 4: Check odd list middle element
    correct_odd_middle_element = [sorted(odd_list)[len(odd_list) // 2]]
    if odd_middle_element != correct_odd_middle_element:
        print("❌ Step 4: Middle element of `odd_list` is incorrect.")
    else:
        print("✅ Step 4: Middle element of `odd_list` is correct.")


def check_solution_n3_lab4(bookstore_inventory, detailed_inventory, full_inventory, book_order_mary_jane, book_order_peter_parker):
    
    # Step 1: Check discounted prices in `bookstore_inventory`
    expected_prices = {
        "The Great Gatsby": round(10.99 * 0.75, 2),
        "1984": round(6.99 * 0.75, 2),
        "To Kill a Mockingbird": round(8.99 * 0.75, 2),
        "Pride and Prejudice": round(5.99 * 0.75, 2)
    }
    
    for book, price in expected_prices.items():
        if bookstore_inventory.get(book) != price:
            print(f"❌ Step 1: Price for '{book}' is incorrect.")
        else:
            print(f"✅ Step 1: Price for '{book}' is correct.")
    
    # Step 2: Check that "Moby Dick" has been added to `bookstore_inventory`
    if bookstore_inventory.get("Moby Dick") != 12.99:
        print("❌ Step 2: 'Moby Dick' was not added correctly to bookstore_inventory.")
    else:
        print("✅ Step 2: 'Moby Dick' added correctly to bookstore_inventory.")
    
    # Step 3: Check `detailed_inventory` includes prices for each book
    for book in expected_prices:
        if detailed_inventory.get(book, {}).get("price") != expected_prices[book]:
            print(f"❌ Step 3: Price for '{book}' in `detailed_inventory` is incorrect.")
        else:
            print(f"✅ Step 3: Price for '{book}' in `detailed_inventory` is correct.")
    
    # Step 4: Check "Moby Dick" was added to `detailed_inventory` with correct details
    moby_dick_details = {"author": "Herman Melville", "publisher": "Harper & Brothers", "price": 12.99}
    if detailed_inventory.get("Moby Dick") != moby_dick_details:
        print("❌ Step 4: 'Moby Dick' details in `detailed_inventory` are incorrect.")
    else:
        print("✅ Step 4: 'Moby Dick' details in `detailed_inventory` are correct.")
    
    # Step 5: Check `full_inventory` for merged details and specific checks using `.get()`
    if full_inventory.get("The Great Gatsby", {}).get("publisher") != "Scribner":
        print("❌ Step 5: Publisher for 'The Great Gatsby' in `full_inventory` is incorrect.")
    else:
        print("✅ Step 5: Publisher for 'The Great Gatsby' in `full_inventory` is correct.")
    
    checks = {
        "Moby Dick": "Herman Melville",
        "Brave New World": "Aldous Huxley",
        "The Metamorphosis": "The Metamorphosis is not available in the inventory.",
        "The Lusiads": "The Lusiads is not available in the inventory."
    }
    
    for title, expected in checks.items():
        result = full_inventory.get(title, f"{title} is not available in the inventory.")
        if result == expected or result.get("author") == expected:
            print(f"✅ Step 5: '{title}' check is correct.")
        else:
            print(f"❌ Step 5: '{title}' check is incorrect.")
    
    # Step 6: Check `book_order_mary_jane`
    mary_jane_titles = ["The Great Gatsby", "Pride and Prejudice"]
    mary_jane_total_price = sum(full_inventory[title]["price"] for title in mary_jane_titles)
    if book_order_mary_jane["titles"] == mary_jane_titles and book_order_mary_jane["total_price"] == mary_jane_total_price:
        print("✅ Step 6: `book_order_mary_jane` is correct.")
    else:
        print("❌ Step 6: `book_order_mary_jane` is incorrect.")
    
    # Step 8: Check updated `book_order_peter_parker`
    updated_peter_parker_titles = ["1984", "The Hobbit"]
    updated_peter_parker_total_price = sum(full_inventory[title]["price"] for title in updated_peter_parker_titles)
    if book_order_peter_parker["titles"] == updated_peter_parker_titles and book_order_peter_parker["total_price"] == updated_peter_parker_total_price:
        print("✅ Step 8: Updated `book_order_peter_parker` is correct.")
    else:
        print("❌ Step 8: Updated `book_order_peter_parker` is incorrect.")


def check_solution_n1_lab5(employee, ubonus_percentage, utotal_bonus):
    sales = employee['sales']
    if 0 <= sales <= 50:
        bonus_percentage = 0.05
    elif 51 <= sales <= 100:
        bonus_percentage = 0.10
    elif 101 <= sales <= 150:
        bonus_percentage = 0.15
    elif sales > 150:
        bonus_percentage = 0.20

    if ubonus_percentage != bonus_percentage:
        print("❌: The `bonus_percentage` is incorrect.")
        return
    
    if utotal_bonus != bonus_percentage * employee["base_salary"]:
        print("❌: The `total_bonus` is incorrect.")
        return
    print('✅ Correct Solution')


def check_solution_n2_lab5(even_sum):
    print('✅ Correct Solution')  if even_sum == sum([num if num % 2 == 0 else 0 for num in range(51)]) else print('❌: The `even_sum` is incorrect.')

def check_solution_n3_lab5(items, reversed_list):
    
    print('✅ Correct Solution') if reversed_list == [[], 3.14, 'apple', True, 1] else print('❌: The `reversed_list` is incorrect.')

def check_solution_n4_lab5(available_books, missing_books):
    if available_books != ['War and Peace', 'The Odyssey', 'Ulysses']:
        print("❌: The `available_books` is incorrect.")
        return
    
    if missing_books != ['The Idiot']:
        print("❌: The `missing_books` is incorrect.")
        return
    
    print('✅ Correct Solution')

def check_solution_n5_lab5(total_price):
    if total_price != 38.45:
        print("❌: The `total_price` is incorrect. Expected $38.45")
    else:
        print('✅ Correct Solution')


def check_solution_n6_lab5(time):
    if time != 5:
        print("❌: The `time` is incorrect. Expected 5 days")
    else:
        print('✅ Correct Solution')

def check_solution_n7_lab5(publishers, recommendations):
    if sorted(publishers) != sorted(['The Russian Messenger', 'Ancient Greek Publication', 'Sylvia Beach']):
        print("❌: The `publishers` is incorrect.")
        return
    
    if sorted(recommendations) != sorted(['Crime and Punishment', 'The Brothers Karamazov', 'Anna Karenina']):
        print("❌: The `recommendations` is incorrect.")
        return
    
    print('✅ Correct Solution')

