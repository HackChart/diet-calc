def to_txt(diet: str):
    file_name = "Meal Plan.txt"
    with open(file_name, "w") as f:
        print(diet, file= f)
    print(f"The file '{file_name}' has been created!")

def email():
    pass

if __name__ == "__main__":
    to_txt("This is a test")