
import json
from wordpress_json import WordpressJsonWrapper

# Load WordPress API configuration
with open("../config/wordpress_api_config.json") as config_file:
    config = json.load(config_file)

# Initialize WordPress API wrapper
wp_api = WordpressJsonWrapper(config["url"], config["username"], config["password"])

def get_user_comments(post_id):
    """
    Fetches all comments for a given post.
    """
    return wp_api.get_comments(post_id)

def post_user_comment(post_id, user_id, content):
    """
    Posts a comment on a given post as a specific user.
    """
    data = {
        "post": post_id,
        "author": user_id,
        "content": content
    }
    return wp_api.post_comment(data)

def get_user_data(user_id):
    """
    Fetches data for a specific user.
    """
    return wp_api.get_user(user_id)
