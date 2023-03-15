# 0. User model
Creating a SQLAlchemy model named User for a database table named users (by using the mapping declaration of SQLAlchemy).

# 1. create user
Implementing the add_user method, which has two required string arguments: email and hashed_password, and returns a User object.
The method saves the user to the database

# 2. Find user
Implementing the DB.find_user_by method. This method takes in arbitrary keyword arguments and returns the first row found in
the users table as filtered by the method’s input arguments

# 3. update user
Implementing the DB.update_user method that takes as argument a required user_id integer and arbitrary keyword arguments, and returns None.

# 4. Hash password
A _hash_password method that takes in a password string arguments and returns bytes.

# 5. Register user
implementing the Auth.register_user in the Auth class
The method takes mandatory email and password string arguments and return a User object.

# 6. Basic Flask app
Setting up a basic Flask App
