

def generate_id_script():
    input_string = "abdc"
    ids = sorted([input_string[i:j+1] for i in range(len(input_string)) for j in range(i, len(input_string)) if len(input_string[i:j+1]) <= 10^9])
    return ids[-1]

print(generate_id_script())