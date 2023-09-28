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
url = f"https://api.github.com/repos/{github_username}/{repository_name}/contents/{readme_path}"
headers = {"Authorization": f"token {access_token}"}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Decode the content from base64
    content = response.json()
    current_readme_content = content["content"]
    current_readme_content = base64.b64decode(current_readme_content).decode("utf-8")

    # Update the README content
    updated_readme_content = progress_entry + "\n" + current_readme_content

    # Encode the updated content to base64
    updated_readme_content_base64 = base64.b64encode(updated_readme_content.encode("utf-8")).decode("utf-8")

    # Create a commit to update the README
    update_data = {
        "message": f"Update progress for Day {current_day}",
        "content": updated_readme_content_base64,
        "sha": content["sha"]
    }

    update_url = f"https://api.github.com/repos/{github_username}/{repository_name}/contents/{readme_path}"
    update_response = requests.put(update_url, headers=headers, json=update_data)

    if update_response.status_code == 200:
        print(f"Updated README for Day {current_day}")
    else:
        print(f"Failed to update README for Day {current_day}")
else:
    print("Failed to fetch README content from the repository.")
