import requests
import json
from unittest.mock import patch

def fetch_repositories_and_commits(user_id):
    base_url = f"https://api.github.com/users/{user_id}/repos"
    
    try:
        repos = requests.get(base_url).json()
        
        if not repos or "message" in repos:
            print(repos)  
            raise ValueError(f"error in fetching repos for user: {user_id}")

        results = []
        for repo in repos:
            repo_name = repo["name"]
            commits_url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
            commits = requests.get(commits_url).json()
            results.append({"Repo": repo_name, "Number of commits": len(commits)})
            
        return results
    except requests.RequestException as e:
        print(f"Error occurred: {e}")
        return []

def test_fetch_repositories_and_commits():
 
    mock_response = [{"name": "Repo1"}, {"name": "Repo2"}]
    
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        
        results = fetch_repositories_and_commits("richkempinski")
        
        assert type(results) is list
        assert len(results) == 2  
        assert "Repo" in results[0]
        assert "Number of commits" in results[0]
        assert results[0]["Repo"] == "Repo1"  

def main():
    user_id = input("Enter GitHub user ID: ")
    results = fetch_repositories_and_commits(user_id)
    for repo_details in results:
        print(f"Repo: {repo_details['Repo']} Number of commits: {repo_details['Number of commits']}")

if __name__ == "__main__":
    main()
