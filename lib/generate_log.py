from datetime import datetime
import requests

def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}

def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("Input must be a list")
    
    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"
    
    with open(filename, 'w') as file:
        for entry in data:
            file.write(f"{entry}\n")
    
    print(f"Log file created: {filename}")
    return filename

if __name__ == "__main__":
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
    
    log_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(log_data)
