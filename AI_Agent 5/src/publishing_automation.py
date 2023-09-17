
import requests
import json
from config import wordpress_api_config

class PublishingAutomation:
    def __init__(self):
        self.api_url = wordpress_api_config['api_url']
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {wordpress_api_config['api_token']}"
        }

    def publish_post(self, post_data):
        response = requests.post(
            url=f"{self.api_url}/posts",
            headers=self.headers,
            data=json.dumps(post_data)
        )

        if response.status_code == 201:
            print("Post published successfully.")
        else:
            print(f"Failed to publish post. Status code: {response.status_code}")

if __name__ == "__main__":
    publishing_automation = PublishingAutomation()
    post_data = {
        "title": "AI Generated News Title",
        "content": "This is an AI generated news content.",
        "status": "publish"
    }
    publishing_automation.publish_post(post_data)
