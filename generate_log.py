from datetime import datetime
import requests

def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}

def generate_log(log_data):
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")
    print(f"Log written to {filename}")
    return filename

if __name__ == "__main__":
    post = fetch_data()
    title = post.get("title", "No title found")
    print(f"Fetched Post Title: {title}")

    sample_logs = [
        "User logged in",
        "User updated profile",
        "Report exported",
        f"Fetched API Post Title: {title}"
    ]
    generate_log(sample_logs)