import requests


def main():
    while True:
        username = input("github-activity ")
        activities = get_github_activities(username)

        if isinstance(activities, int):
            continue

        for activity in activities:
            activity_type = activity["type"]

            if activity_type == "WatchEvent":
                print(f"- Starred {activity['repo']['name']}")
            elif activity_type == "PushEvent":
                size = activity["payload"]["size"]
                if size == 1:
                    print(
                        f"- Pushed {activity['payload']['size']} commit to {activity['repo']['name']}"
                    )
                else:
                    print(
                        f"- Pushed {activity['payload']['size']} commits to {activity['repo']['name']}"
                    )
            elif activity_type == "CreateEvent":
                print(f"- Created {activity['repo']['name']}")


def get_github_activities(username: str):
    url = f"https://api.github.com/users/{username}/events"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request returned status code {response.status_code}")
        return response.status_code


if __name__ == "__main__":
    main()
