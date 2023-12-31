import os
import requests
from datetime import datetime

# Define your GitHub username, repository name, and personal access token
github_username = "graciari2000"
repository_name = "100daysofcode"
access_token = "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"  # Replace with your access token

# Define the path to your README.md file
readme_path = "README.md"

# Get the current date and day number (you may need to adjust this depending on your timezone)
current_date = datetime.now().strftime("%Y-%m-%d")
current_day = (datetime.now() - datetime(2023, 9, 27)).days + 1  # Adjust the start date as needed

# Create the progress entry template
progress_entry = f"### Day {current_day} ({current_date}):\n\n- [Link to Day {current_day}](Day{current_day}/Day{current_day}.md)\n"

# Fetch the list of repository contents using the GitHub API
url = f"https://api.github.com/repos/graciari2000/100daysofcode/"
response = requests.get(url, headers={"Authorization": f"token {access_token}"})

# Check if the request was successful
if response.status_code == 200:
    contents = response.json()
    
    # Check if the Day{current_day} directory already exists in the repository
    day_directory_exists = any(content["name"] == f"Day{current_day}" for content in contents)
    
    if not day_directory_exists:
        # Create the Day{current_day} directory
        create_day_directory_url = f"https://api.github.com/repos/{github_username}/{repository_name}/contents/Day{current_day}"
        create_day_directory_data = {
        "message": f"Create Day{current_day} directory",
        "content": "",
        }
        create_day_directory_response = requests.put(
            create_day_directory_url,
            headers={"Authorization": f"token {access_token}"},
            json=create_day_directory_data,
        )
        
        # Check if the directory creation was successful
    if create_day_directory_response.status_code == 201:
        print(f"Created Day{current_day} directory.")
    else:
        print(f"Failed to create Day{current_day} directory.")
    
    # Read the existing README content
    with open(readme_path, "r") as f:
        readme_content = f.read()

    # Append the progress entry to the README content
    updated_readme_content = progress_entry + "\n" + readme_content

    # Write the updated content back to the README
    with open(readme_path, "w") as f:
        f.write(updated_readme_content)

    # Commit and push the changes
    os.system("git config --global user.name 'Your Name'")
    os.system("git config --global user.email 'youremail@example.com'")
    os.system(f"git add {readme_path}")
    os.system(f"git commit -m 'Add progress update for Day {current_day}'")
    os.system("git push")
else:
    print("Failed to fetch repository contents.")
    
with open(readme_path, "r") as f:
    readme_content = f.read()
    updated_readme_content = progress_entry + "\n" + readme_content

with open(readme_path, "w") as f:
    f.write(updated_readme_content)

os.system("git config --global user.name 'graciari2000'")
os.system("git config --global user.email 'youremail@example.com'")
os.system(f"git add {readme_path}")
os.system(f"git commit -m 'Add progress update for Day {current_day}'")
os.system("git push")

    else:
        print("Failed to fetch repository contents.")