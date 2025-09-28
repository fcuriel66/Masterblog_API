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


def find_post_by_id(post_id):
    """ Find the post with the id `post_id`.
    If there is no post with this id, return None. """
    for post in POSTS:
        if int(post_id) == post["id"]:
            return post
    return None


@app.route('/api/posts', methods=['GET'])
def get_posts():
    # Get query parameters sort and direction
    sort_field = request.args.get("sort")
    direction = request.args.get("direction", "asc")  # asc is default

    # Validate sort_field
    if sort_field and sort_field not in ("title", "content"):
        return jsonify({"error": "Invalid sort field. Use 'title' or 'content'."}), 400

    # Validate direction
    if direction and direction not in ("asc", "desc"):
        return jsonify({"error": "Invalid direction. Use 'asc' or 'desc'."}), 400

    # If sorting requested, apply sorting
    sorted_posts = POSTS
    if sort_field:
        reverse = direction == "desc"
        sorted_posts = sorted(POSTS, key=lambda post: post[sort_field].lower(), reverse=reverse)

    return jsonify(sorted_posts)


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


@app.route('/api/posts/<int:id>', methods=['PUT'])
def update_post(id):
    # Find the post with the given ID
    blog_post = find_post_by_id(id)

    # If the post with provided id wasn't found, return a 404 error
    if blog_post is None:
        return f'The Post with id {id} was not found', 404

    # Update the updated or unchanged post
    updated_post = request.get_json()
    blog_post.update(updated_post)

    # Return the updated post
    return jsonify(blog_post), 200


@app.route('/api/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    # Find the post with the given ID
    post = find_post_by_id(id)

    # If the post wasn't found, return a 404 error
    if post is None:
        return f'Post with id {id} not found', 404

    # Remove the post from the list
    POSTS.remove(post)

    # logic for confirmation of the deletion (not implemented,
                                        # not working with interface
    # user_confirm = input("Are you sure you want to delete this post? (y/n)")
    # if user_confirm.strip().lower() == 'y':
    #     POSTS.remove(post)
    # else:
    #     abort_message = {
    #         "message": "No post deleted."
    #     }
    #     return jsonify(abort_message), 200

    # Return the deleted book successful message
    deleted_message = {
    "message": f"Post with id {id} has been deleted successfully."
}
    return jsonify(deleted_message), 200


@app.route("/api/posts/search", methods=["GET"])
def search_posts():
    title_query = request.args.get("title", "").strip().lower()
    content_query = request.args.get("content", "").strip().lower()

    # Filter posts for provided strings if any
    results = []
    for post in POSTS:
        match_title = title_query in post["title"].lower() if title_query else True
        match_content = content_query in post["content"].lower() if content_query else True

        if match_title and match_content:
            results.append(post)

    return jsonify(results), 200


@app.errorhandler(400)
def not_found_error(error):
    return jsonify({"error": "Bad Request"}), 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
