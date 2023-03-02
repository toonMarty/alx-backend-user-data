# 0. Regex-ing
A function called filter_datum that uses a regex to replace occurrences of certain field values.

# 1. Log formatter
Implementing the format method to filter values in incoming log records using filter_datum.
Values for fields in fields are be filtered.

# 2. Create logger
A get_logger function that takes no arguments and returns a logging.Logger object.

# 3. Connect to secure database
A get_db function that returns a connector to the database

# 4. Read and filter data
A main function that takes no arguments and returns nothing.
The function obtains a database connection using get_db and retrieves
all rows in the users table and displays each row under a filtered format.

# 5. Encrypting passwords
A hash_password function that expects one string argument name password and returns a salted, hashed password, which is a byte string.

# 6. Check valid password
An is_valid function that expects 2 arguments and returns a boolean.

