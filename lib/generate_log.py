from datetime import datetime
import requests

def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}

if __name__ == "__main__":
    post = fetch_data()
    title = post.get("title", "No title found")
    print(f"Fetched Post Title: {title}")

    log_data = [
        "User logged in",
        "User updated profile",
        "Report exported",
        f"Fetched API Post Title: {title}"
    ]
    
    filename = f"log_{datetime.now().strftime('%Y%m%m')}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")