# import random
# file_loc = "classCode.py"
# with open(file_loc, 'r') as f:
#         code = f.read()

# content_list = list(code)
# operators = ['+','-','==','*','/','%','**','!=','<','>','<=','>=','+=','-=']

# for i in range(len(operators)):
#        count = content_list.count(operators[i])
#        print(str(operators[i]) + " appears " + str(count) )
# # Modify specific indices
# for index, char in enumerate(content_list):
#      select = random.randint(0,11)
#      if char == operators[select]:
#          count = content_list.count(operators[select])
        
#         #  content_list[index] = replace_char  

# # # Join back into a string
# # modified_content = ''.join(content_list)

# # # Write back to the file
# # with open(file_path, "w") as file:
# #     file.write(modified_content)


# # modified_content = content.replace(search_char, replace_char, 1)

import re
import random

# Define the file paths
input_file_path = "code_1.py"  # Original file

# Define the regex pattern for the operators
operator_pattern = r"(\+=|-=|\*\*=|==|!=|<=|>=|<|>|\+|-|\*|/|%)"

# List of all possible operators for mutation
all_operators = ["+=", "-=", "**", "==", "!=", "<=", ">=", "<", ">", "+", "-", "*", "/", "%"]

def mutate_operator(content):
    # Find all operators in the file content
    file_ops = list(re.finditer(operator_pattern, content))

    selected_op = random.choice(file_ops)
    start, end = selected_op.span()
    original_op = selected_op.group(0)
    
    new_op = random.choice([op for op in all_operators if op != original_op])
    
    # Replace the selected operator
    mutated_content = content[:start] + new_op + content[end:]
    print(f"Replaced '{original_op}' with '{new_op}' at position {start}-{end}")
    
    return mutated_content

# Read the content of the input file
with open(input_file_path, "r") as file:
    content = file.read()


# Mutate the content
for i in range(30):
    mutated_content = mutate_operator(content)
    # Write the mutated content to the output file
    with open(f"mutant{i}.py", "w") as file:
        file.write(mutated_content)