# 0. Et moi et moi et moi!
Adding a new endpoint: GET /users/me to retrieve the authenticated User object.

# 1. Empty session
A class SessionAuth that inherits from Auth

# 2. Create a session
Updating SessionAuth class by:
    * Creating a class attribute user_id_by_session_id initialized by an empty dictionary
    * Creating an instance method def create_session that creates a Session ID for a user_id

# 3. User ID for Session ID
An instance method def user_id_for_session_id that returns a User ID based on a Session ID

# 4. Session cookie
The method def session_cookie that returns a cookie value from a request
