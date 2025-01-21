# GitHub Issues Manager

This is a simple Python application that interacts with the GitHub API to manage issues on repositories. You can:
- Open new issues
- Close existing issues
- List issues in a repository

## Prerequisites

1. Python 3.6+ installed.
2. A **GitHub personal access token** for authentication. You will need to generate this token to interact with the GitHub API.

## Installation

Follow the steps below to set up and run this project on your local machine.

### Step 1: Clone the Repository
If you don't have the project on your local machine, clone it using Git:
```bash
git clone https://github.com/sharon088/IssuesExercise.git
cd IssuesExercise
```

### Step 2: Set Up a Virtual Environment

**On Windows:**
1. Open a Command Prompt or PowerShell window.
2. Create a virtual environment:
```bash
python3 -m venv venv  # or python -m venv venv if python3 is not required
```

3. Activate the virtual environment:
- For Command Prompt ( Windows CMD ):
```bash
venv\Scripts\activate
```
- For PowerShell ( Windows ):
```bash
.\venv\Scripts\Activate.ps1
```

**On Linux/macOS:**
1. Open a Command Prompt or PowerShell window.
2. Create a virtual environment:
```bash
python3 -m venv venv  # or python -m venv venv if python3 is not required
```
3. Activate the virtual environment: 
```bash
source venv/bin/activate
```

### Step 3: Install Required Dependencies
Once the virtual environment is activated, install the required packages using requirements.txt:
```bash
pip install -r requirements.txt
```
### 4: Generate GitHub Personal Access Token
To interact with the GitHub API, you will need a GitHub Personal Access Token (PAT):
1. Go to [GitHub Personal Access Tokens](https://github.com/settings/tokens)
2. Click on Generate new token.
3. Select the necessary scopes:
    - repo (for full repository access)
    - public_repo (for public repositories)
4. Copy the token you generate (you will not be able to view it again).

### Step 5: Set the GitHub Token
#### Method 1: Using .env File (If using Visual studio code)
1. In the project directory, create a file named .env.
2. Inside the .env file, add the following line:
```bash
GITHUB_TOKEN=your_personal_access_token_here
```
Replace your_personal_access_token_here with the token you generated in Step 4.

#### Method 2: Set Token in the Terminal (If Not Using VS Code)
If you're not using Visual Studio Code or an IDE that automatically loads the .env file, you need to manually set the GITHUB_TOKEN environment variable before running the script.
**On Windows (Command Prompt (CMD)):**
```bash
set GITHUB_TOKEN=your_personal_access_token_here
```
**On Windows (PowerShell):**
```bash
$env:GITHUB_TOKEN="your_personal_access_token_here"
```

**On Linux/macOS (Terminal):**
```bash
export GITHUB_TOKEN=your_personal_access_token_here
```

### Step 6: Run the Script
Once the virtual environment is set up and the dependencies are installed, you can run the script:
```bash
python3 -m venv venv  # or python3 app.py if python3 is not required
```

The script will prompt you to enter the repository name. Based on your inputs, it will allow you to:

- Open a new issue
- Close an existing issue
- List issues in the repository

### Troubleshooting
- If the token is not set properly: You will see an error message indicating that the GITHUB_TOKEN environment variable is missing. Double-check that your .env file is correctly formatted or that you’ve set the token in your terminal session.
- If you run into authentication issues: Ensure that the token has the correct permissions (i.e., the repo scope for private repositories or public_repo for public ones).

### Dependencies
This project requires the following Python packages:
- PyGithub: A Python library for interacting with the GitHub API.
- python-dotenv: A library for loading environment variables from a .env file.
You can install the dependencies by running:
```bash
pip install -r requirements.txt
```

#### requirements.txt
Here’s the content of the requirements.txt file:
```bash
PyGithub==2.5.0
python-dotenv==1.0.1
```