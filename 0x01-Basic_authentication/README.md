# 0. Simple-basic-API
Downloading, configuring and starting the project.

# 1. Error handler: Unauthorized
Adding a new error handler for an unauthorized request code 401.

# 2. Error handler: Forbidden
Adding a new error handler for the status code 403, Forbidden.

# 3. Auth class
A class to manage the API authentication.

# 4. Define which routes don't need authentication
Updating the method require in Auth that returns True if the path is not in the list
of strings excluded_paths

# 5. Request validation!
validating all requests to secure the API

# 6. Basic auth
A class BasicAuth that inherits from Auth

# 7. Basic - Base64 part
A method def extract in the class BasicAuth that returns the Base64 part of the Authorization header for a Basic Authentication

# 8. Basic - Base64 decode
A method def decode_base64_authorization_header that returns the decoded value of a Base64 string base64_authorization_header.

# 9. Basic - User credentials
A method def extract_user_credentials in the class BasicAuth that returns the user email and password from the Base64 decoded value.

# 10. Basic - User object
A method def user_object_from_credentials in the class BasicAuth that returns the User instance based on his email and password.

# 11. Basic - Overload current_user - and BOOM!
the method def current_user in the class BasicAuth that overloads Auth and retrieves the User instance for a request.

# 12. Basic - Allow password with ":"
Improving the method def extract_user_credentials to allow password with :.

# 13. Require auth with stars
Improving def require_auth by allowing * at the end of excluded paths.
