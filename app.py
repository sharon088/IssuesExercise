from github import Github
import os
from github.Repository import Repository
from github.GithubException import GithubException
from typing import Optional

# Authentication is defined via github.Auth
from github import Auth

# Get the GitHub token from the environment
TOKEN = os.getenv("GITHUB_TOKEN")

# Creates a new issue in the given repository
def open_issue(repo: Repository, title: str, body: str) -> None:
    try:
        issue = repo.create_issue(title=title, body=body)
        print(f"Issue created: {issue.title} (#{issue.number})")
    except GithubException as e:
        print(f"Error opening issue: {e}")

# Lists issues in the repository by their state (open, closed, all)
def list_issues(repo: Repository, state: str) -> None:
    try:
        if state not in ['open', 'closed', 'all']:
            print("Invalid state. Please use 'open', 'closed', or 'all'.")
            return
        
        issues = repo.get_issues(state=state)
        if issues.totalCount == 0:
            print(f"No {state} issues found.")
        else:
            for issue in issues:
                print(f"Issue #{issue.number}: {issue.title} - {issue.state}")
    except GithubException as e:
        print(f"Error retrieving issues: {e}")

 # Closes an existing issue by its issue number
def close_issue(repo: Repository, issue_number: int) -> None:
    try:
        issue = repo.get_issue(issue_number)
        issue.edit(state='closed')
        print(f"Issue #{issue_number} has been closed.")
    except GithubException as e:
        print(f"Error closing issue: {e}")


# Function to authenticate and get the repository object
def authenticate_and_get_repo(repo_name: str) -> Optional[Repository]:
    try:
        auth = Auth.Token(TOKEN)
        g = Github(auth=auth)  # Authenticate with GitHub
        for repox in g.get_user().get_repos():
            if repo_name == repox.name:
                return g.get_repo(repox.full_name)  
        print("Couldn't find the repository. Please try again.")
        return None
    except GithubException as e:
        print(f"Error authenticating or accessing repository: {e}")
        return None
    finally:
        if g:
            g.close()

# Main program that interacts with the user
def main() -> None:
    while True:
        repo_name = input("Enter the repository name: ")
        repo = authenticate_and_get_repo(repo_name)
        if repo is None:
            continue  # If repo is not found , try again
        break  # Exit the loop if repository is found and accessible

    while True:
        print("\nSelect an option:")
        print("1. Open a new issue")
        print("2. Close an existing issue")
        print("3. List issues")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            title = input("Enter the issue title: ")
            body = input("Enter the issue description: ")
            open_issue(repo, title, body)

        elif choice == "2":
            issue_number = int(input("Enter the issue number to close: "))
            close_issue(repo, issue_number)

        elif choice == "3":
            state = input("Enter the issue state (open/closed/all): ").lower()
            list_issues(repo, state)

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()