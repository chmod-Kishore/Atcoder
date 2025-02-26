import os
import subprocess
from datetime import datetime

# Configuration
LOCAL_REPO_PATH = "/home/kishore/kishore/Atcoder"  # Replace with your local Atcoder repo path

def commit_and_push_changes(contest_name):
    # Navigate to the local repo
    os.chdir(LOCAL_REPO_PATH)

    # Check if the contest folder exists
    contest_folder = os.path.join(LOCAL_REPO_PATH, contest_name)
    if not os.path.exists(contest_folder):
        print(f"Folder '{contest_name}' does not exist!")
        return

    # Navigate to the contest folder
    os.chdir(contest_folder)

    # Git commands to commit and push changes
    try:
        subprocess.run(["git", "add", "."], check=True)
        commit_message = f"Completed solutions for {contest_name} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Change to `master` or `main` depending on your branch
        subprocess.run(["git", "push", "origin", "master"], check=True)  # Replace 'master' with 'main' if needed
        print("Changes committed and pushed to GitHub successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def main():
    # Get the contest name from user input
    contest_name = input("Enter the contest name (e.g., abc190): ")
    
    # Call the function to commit and push changes
    commit_and_push_changes(contest_name)

if __name__ == "__main__":
    main()

