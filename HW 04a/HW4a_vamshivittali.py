import requests
import json

def fetch_github_repo(user_id):
    base_url = f"https://api.github.com/users/{user_id}/repos"
    try:
        repos = requests.get(base_url).json()
        
        if not repos or "message" in repos:
            print(repos)  
            raise ValueError(f"error in finding repos of : {user_id}")

        results = []
        for repo in repos:
            repo_name = repo["name"]
            commits_url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
            commits = requests.get(commits_url).json()
            results.append({"Repo": repo_name, "Number of commits": len(commits)})
            
        return results
    except requests.RequestException as e:
        print(f"an unexpected error has raised: {e}")
        return []

def test_suite():
    results = fetch_github_repo("vamshivittali76")
    assert type(results) is list
    assert len(results) > 0
    assert "Repo" in results[0]
    assert "Number of commits" in results[0]

def main():
    user_id = input("Enter GitHubID: ")
    results = fetch_github_repo(user_id)
    for repo_details in results:
        print(f"Repo: {repo_details['Repo']} Number of commits: {repo_details['Number of commits']}")

if __name__ == "__main__":
    main()
