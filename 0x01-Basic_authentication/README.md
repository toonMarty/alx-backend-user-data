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
