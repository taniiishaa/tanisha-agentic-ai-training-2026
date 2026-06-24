import httpx
from langchain_core.tools import tool

@tool
async def bio(username):
    """Gets the name, company, location, and bio of a GitHub user."""
    url = f"https://api.github.com/users/{username}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            name = data.get("name", "No Name")
            bio_text = data.get("bio", "No Bio")
            loc = data.get("location", "No Location")
            comp = data.get("company", "No Company")
            return f"User: {name} | Bio: {bio_text} | Location: {loc} | Company: {comp}"
        return "Error: User not found."

@tool
async def stats(username):
    """Gets the number of followers, following, and public repositories for a user."""
    url = f"https://api.github.com/users/{username}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            repos = data.get("public_repos", 0)
            followers = data.get("followers", 0)
            following = data.get("following", 0)
            return f"{username} has {repos} public repos, {followers} followers, and follows {following} users."
        return "Error: Could not get metrics."

@tool
async def gists(username):
    """Lists the descriptions and links of public gists created by a user."""
    url = f"https://api.github.com/users/{username}/gists"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            if len(data) == 0:
                return f"No public gists found for {username}."
            output = "Public Gists:\n"
            for g in data[:5]:
                desc = g.get("description") or "No description"
                output += f"- {desc}: {g.get('html_url')}\n"
            return output.strip()
        return "Error fetching gists."

@tool
async def orgs(username):
    """Lists the organizations that a GitHub user belongs to."""
    url = f"https://api.github.com/users/{username}/orgs"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            if len(data) == 0:
                return f"{username} is not part of any organization."
            names = []
            for o in data:
                names.append(o.get("login"))
            return f"Organizations for {username}: " + ", ".join(names)
        return "Error fetching organizations."


@tool
async def repo_info(owner, repo):
    """Gets description, default branch, and creation date of a repository."""
    url = f"https://api.github.com/repos/{owner}/{repo}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            desc = data.get("description", "No description")
            branch = data.get("default_branch", "main")
            created = data.get("created_at", "")
            return f"Repo: {repo} | Description: {desc} | Default Branch: {branch} | Created at: {created}"
        return "Repository not found."

@tool
async def repo_stats(owner, repo):
    """Gets total stars, watchers, and forks for a repository."""
    url = f"https://api.github.com/repos/{owner}/{repo}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            stars = data.get("stargazers_count", 0)
            watchers = data.get("subscribers_count", 0)
            forks = data.get("forks_count", 0)
            return f"Repository has {stars} stars, {watchers} watchers, and {forks} forks."
        return "Error getting repo stats."

@tool
async def repo_langs(owner, repo):
    """Lists the programming languages used inside a repository with their byte size."""
    url = f"https://api.github.com/repos/{owner}/{repo}/languages"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            if len(data) == 0:
                return "No language data found."
            lang_list = []
            for key, val in data.items():
                lang_list.append(f"{key} ({val} bytes)")
            return "Languages: " + ", ".join(lang_list)
        return "Error getting languages."

@tool
async def repo_license(owner, repo):
    """Checks the open-source license used in a project repository."""
    url = f"https://api.github.com/repos/{owner}/{repo}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            lic = data.get("license")
            if lic:
                return f"License: {lic.get('name')}"
            return "This project does not have a license."
        return "Error checking license."

@tool
async def repo_users(owner, repo):
    """Lists the top 10 contributors who have worked on the repository."""
    url = f"https://api.github.com/repos/{owner}/{repo}/contributors"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            names = []
            for c in data[:10]:
                names.append(c.get("login"))
            return "Top contributors: " + ", ".join(names)
        return "Error getting contributors."

@tool
async def repo_readme(owner, repo):
    """Gets the URL link to read the README.md file of a repository."""
    url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            return f"README link: {data.get('html_url')}"
        return "No README file found."

@tool
async def commits(owner, repo):
    """Gets the last 5 commits with their messages and author names."""
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            output = "Recent Commits:\n"
            for c in data[:5]:
                author = c["commit"]["author"]["name"]
                msg = c["commit"]["message"]
                output += f"- {author}: {msg}\n"
            return output.strip()
        return "Error getting recent commits."

@tool
async def issues(owner, repo):
    """Lists up to 5 open issues or bugs in a repository."""
    url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=open"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            issues_list = []
            for i in data:
                if "pull_request" not in i:
                    issues_list.append(i)
            if len(issues_list) == 0:
                return "No open issues found!"
            output = "Open Issues:\n"
            for i in issues_list[:5]:
                output += f"#{i['number']} {i['title']}\n"
            return output.strip()
        return "Error fetching open issues."

@tool
async def comments(owner, repo, num):
    """Gets up to 3 comments from a specific issue number."""
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{num}/comments"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            if len(data) == 0:
                return f"No comments found on issue #{num}."
            output = f"Comments on issue #{num}:\n"
            for c in data[:3]:
                output += f"[{c['user']['login']}]: {c['body']}\n"
            return output.strip()
        return "Could not get comments."

@tool
async def pulls(owner, repo):
    """Lists up to 5 open pull requests in a repository."""
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls?state=open"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            if len(data) == 0:
                return "No open pull requests found."
            output = "Active Pull Requests:\n"
            for p in data[:5]:
                output += f"PR #{p['number']} - '{p['title']}' by {p['user']['login']}\n"
            return output.strip()
        return "Error checking open pull requests."

@tool
async def tags(owner, repo):
    """Lists up to 5 version tags assigned to a repository."""
    url = f"https://api.github.com/repos/{owner}/{repo}/tags"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            if len(data) == 0:
                return "No version tags found."
            names = []
            for t in data[:5]:
                names.append(t.get("name"))
            return "Version tags: " + ", ".join(names)
        return "Error checking repository tags."

@tool
async def releases(owner, repo):
    """Gets details and notes of the latest official release."""
    url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            body = data.get("body", "No notes provided.")
            return f"Latest Release: {data.get('name')} ({data.get('tag_name')})\nNotes: {body[:200]}..."
        return "No official releases found."

@tool
async def branches(owner, repo):
    """Lists all the branches inside a repository."""
    url = f"https://api.github.com/repos/{owner}/{repo}/branches"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            names = []
            for b in data:
                names.append(b.get("name"))
            return "Available branches: " + ", ".join(names)
        return "Error checking repository branches."

@tool
async def topics(owner, repo):
    """Gets the topics or tags linked to a repository profile."""
    url = f"https://api.github.com/repos/{owner}/{repo}/topics"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json().get("names", [])
            if len(data) == 0:
                return "No topics found."
            return "Topics: " + ", ".join(data)
        return "Error checking repository topics."

@tool
async def wiki(owner, repo):
    """Checks if the repository has a public wiki documentation page enabled."""
    url = f"https://api.github.com/repos/{owner}/{repo}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            return f"Repository has a public wiki enabled: {data.get('has_wiki', False)}"
        return "Error checking wiki parameters."

@tool
async def stars(owner, repo):
    """Lists up to 5 users who recently starred the repository."""
    url = f"https://api.github.com/repos/{owner}/{repo}/stargazers"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            if len(data) == 0:
                return "Nobody has starred this repository yet."
            names = []
            for s in data[:5]:
                names.append(s.get("login"))
            return "Recent stargazers: " + ", ".join(names)
        return "Error checking repository stargazers."


all_github_tools = [
    bio, stats, gists, orgs,
    repo_info, repo_stats, repo_langs, repo_license,
    repo_users, repo_readme, commits, issues,
    comments, pulls, tags, releases,
    branches, topics, wiki, stars
]