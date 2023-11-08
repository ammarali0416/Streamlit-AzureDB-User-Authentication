# Streamlit-AzureDB-User-Authentication
A Streamlit app with a Azure SQL Database Back-end for User Authentication
> This readme was written with the help of AI
## Introduction
---------------
This repo is a simple proof of concept that showcases the integration of a Streamlit-powered frontend with an Azure SQL Database backend. This project serves as a demonstration of how a Python-based web app can effectively manage user authentication and data handling in a multi-page application environment.

Streamlit is an open-source app framework that turns data scripts into shareable web apps in minutes. Coupled with an Azure SQL Database, this POC showcases the ease and efficiency with which developers can build and deploy full-stack applications.

The core functionality allows users to create new accounts or log in to existing ones, with each action interacting directly with the Azure SQL DB to insert new records or verify existing user credentials.
## How it Works
---------------
- Azure SQL Database Connection:
  -```pyodbc``` to establish a connection with Azure SQL Database.
  - Connection parameters are securely fetched from a .env file using ```python-dotenv```.
- User Authentication:
  - When a user attempts to log in, the authenticate_user function is called.
  - It queries the Users table in the database to verify if the username exists and if the provided password matches the one stored in the database.
- Account Creation:
  - For new users, the create_new_user function allows them to sign up.
  - It checks if the username or email is already in use and, if not, inserts a new user record into the Users table.
- Streamlit Frontend:
  - The login.py script uses Streamlit to create a web interface.
  - It provides two main functionalities: "Sign Up" for new account creation and "Log In" for existing users.
  - User inputs are gathered through text inputs and buttons on the Streamlit interface.
- Session Management:
  - After successful login, user details such as user ID and role are stored in ```st.session_state``` for session management.
- Role-Based Access:
  - The dashboard page checks the logged-in user's role and customizes the displayed message accordingly.
  - It also ensures that no content is displayed unless the user is logged in.
- Modular Design:
  - The code is structured in a modular fashion, with database operations encapsulated in azsqldb.py and Streamlit pages managed separately.
- Security Practices:
  - Passwords and sensitive information are not stored in the code but are retrieved from environment variables for better security practices.
## Dependencies and Installation
---------------
To install the app, please follow these steps:
1. Clone the repository to your local machine.
2. Install the required dependencies
   ```
   pip install -r requirements.txt
   ```
4. Create a free [Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/free-offer?view=azuresql)
5. Configure the `.env` file in the project directory (rename `.env.example`):
    ```
    AZURE_SERVER=<<database URL>>.database.windows.net
    AZURE_DATABASE=<<database>>
    AZURE_USERNAME=<<username>>
    AZURE_PASSWORD=<<user password>>
    ```
6. Create a USERS table by executing `Objects.sql` in your free database.
## Usage
--------------
To use the app, follow these steps:
1. Ensure you have installed the required dependencies and executed `Objects.sql` in your database
2. In Command Prompt / Poweshell, run `LOGIN.py` file using the following command:
   ```
   streamlit run LOGIN.py
   ```
## Contributing
------------
This repository is intended for educational purposes. Feel free to utilize and enhance the app based on your own requirements. Any similarity to other apps is purely coincidental and not intended to infringe on any intelectual property rights or private data.

## License
-------
This app is released under the [MIT License](https://opensource.org/licenses/MIT).
