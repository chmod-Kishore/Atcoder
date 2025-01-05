import os
import subprocess
import argparse

# Configuration
LOCAL_REPO_PATH = "/home/kishore/Atcoder"  # Replace with your local Atcoder repo path

def create_and_setup_contest(contest_name, problems):
    # Navigate to the local repo
    os.chdir(LOCAL_REPO_PATH)

    # Create a new folder for the contest if it doesn't exist
    contest_folder = os.path.join(LOCAL_REPO_PATH, contest_name)
    if not os.path.exists(contest_folder):
        os.makedirs(contest_folder)
        print(f"Folder '{contest_name}' created.")
    else:
        print(f"Folder '{contest_name}' already exists.")

    # Create empty problem files (e.g., A.cpp, B.cpp, etc.)
    for problem in problems:
        problem_file = os.path.join(contest_folder, f"{problem}.cpp")
        if not os.path.exists(problem_file):
            with open(problem_file, "w") as f:
                f.write(f"// Solution for problem {problem} in {contest_name}\n")
            print(f"Created file: {problem_file}")
        else:
            print(f"File {problem_file} already exists.")

def main():
    # Argument parser for the contest name and problem identifiers
    parser = argparse.ArgumentParser(description="Automate setting up Atcoder solutions.")
    parser.add_argument("contest_name", type=str, help="Name of the contest (e.g., abc190).")
    parser.add_argument(
        "-p", "--problems", nargs="+", default=["A", "B", "C", "D", "E", "F"],
        help="List of problem identifiers to create files for (default: A, B, C, D, E, F)."
    )
    args = parser.parse_args()

    # Call the function to set up the contest
    create_and_setup_contest(args.contest_name, args.problems)

if __name__ == "__main__":
    main()
