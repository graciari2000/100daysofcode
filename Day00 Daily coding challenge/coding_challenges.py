import random

def daily_challenge():
    with open("./projects.txt") as projects_file:
        project_lines = projects_file.readlines()
        # choose a random line from the file
        project_line = random.choice(project_lines)
    
    with open("./languages.txt") as languages_file:
        language_lines = languages_file.readlines()
        language_line = random.choice(language_lines)
    
    print(f"Hello Kafui! Today's project is '{project_line.strip()}' in {language_line.strip()}.")


daily_challenge()
