import os
import requests
from random import randint

# GitHub API authentication token
TOKEN = "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"

# Base URL for GitHub API
BASE_URL = "https://api.github.com"

# Function to create a pull request
def create_pull_request(repo_owner, repo_name, base_branch, head_branch, title, body):
    url = f"{BASE_URL}/repos/{repo_owner}/{repo_name}/pulls"
    headers = {"Authorization": f"token {TOKEN}"}
    data = {
        "title": title,
        "body": body,
        "head": head_branch,
        "base": base_branch
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Function to create an issue
def create_issue(repo_owner, repo_name, title, body):
    url = f"{BASE_URL}/repos/{repo_owner}/{repo_name}/issues"
    headers = {"Authorization": f"token {TOKEN}"}
    data = {
        "title": title,
        "body": body
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Main loop to create commits
for day in range(1, 150):
    for commits in range(0, randint(1, 20)):
        day_str = str(day) + ' days ago'
        with open('file.txt', 'a') as file:
            file.write(day_str + "\n")
        os.system('git add .')
        os.system('git commit --date="' + day_str + '" -m "commit"')

# Customize pull request title and body
pull_request_title = "Feature: Implement new functionality"
pull_request_body = "This pull request adds new features to improve the project.\nPlease review and merge as needed."

# Create pull request
pull_request = create_pull_request("reyewka", "Bot", "main", "main", pull_request_title, pull_request_body)
print("Pull request created:", pull_request)

# Customize issue title and body
issue_title = "Bug: Fix issue with login functionality"
issue_body = "Users are reporting issues with the login process. This issue needs to be investigated and fixed promptly."

# Create issue
issue = create_issue("rewyekha", "Bot", issue_title, issue_body)
print("Issue created:", issue)
