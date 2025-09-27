from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]

def validate_post_title(data):
    if "title" not in data:
        return False
    return True


def validate_post_content(data):
    if "content" not in data:
        return False
    return True



@app.route('/api/posts', methods=['GET'])
def get_posts():
    return jsonify(POSTS)


@app.route('/api/posts', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        # Get the new post data from the client
        new_post = request.get_json()
        if not validate_post_title(new_post) or new_post["title"] == "":
            return jsonify({"error": "Incorrect Post Data, the title "
                                     "is missing from the post"}), 400
        elif not validate_post_content(new_post) or new_post["content"] == "":
            return jsonify({"error": "Incorrect Post Data, the content "
                                     "is missing from the post"}), 400
        else:
            # Generate a new ID for the post
            new_id = max(post['id'] for post in POSTS) + 1
            new_post['id'] = new_id

            # Add the new post to our list POSTS
            POSTS.append(new_post)

            # Return the new post data to the client
            return jsonify(new_post), 201
    else:
        # Handle the GET request
        return jsonify(POSTS)


@app.errorhandler(400)
def not_found_error(error):
    return jsonify({"error": "Bad Request"}), 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
