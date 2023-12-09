import requests

username = "gadamico"
url = f"https://api.github.com/users/{username}/events"


def get_repositories(username):
    # Get repositories where the user has committed
    commits_url = f"https://api.github.com/users/{username}/events"
    response = requests.get(commits_url)
    events = response.json()

    repositories = set()

    # Extract repository names from commit events
    for event in events:
        if "repo" in event and "name" in event["repo"]:
            repositories.add(event["repo"]["name"])

    # Get repositories where the user has pushed
    push_url = f"https://api.github.com/users/{username}/repos?type=owner"
    response = requests.get(push_url)
    owned_repos = response.json()

    for repo in owned_repos:
        repositories.add(repo["name"])

    return list(repositories)


# ----------------------------------------------------------------------------------------------------
repos = get_repositories("gadamico")
print(repos)
