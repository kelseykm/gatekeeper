# Gatekeeper

`Gatekeeper` is a Python script for managing followers and following users on GitHub. The script allows you to list, follow, or unfollow users based on whether they follow you back or not. You can also define exceptions in the configuration file to exclude certain users from being included in these lists.

## Features

- List all your followers
- List all users you're following
- List users you're following but aren't following you back
- Unfollow users who aren't following you back
- List users following you but you're not following them back
- Follow users who are following you but you're not following back
- Supports user-defined exceptions for certain categories (crooks and niceys)

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/gatekeeper.git
    ```

2. Navigate into the project directory:

    ```bash
    cd gatekeeper
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Ensure you have created a `config.toml` file based on the provided `example.config.toml`.

## Configuration

You’ll need to configure the `API_KEY` in the `config.toml` file for the script to work with GitHub's API. You can use the provided `example.config.toml` file as a template for creating your own `config.toml`.

### Example Configuration File

1. Copy the `example.config.toml` file and rename it to `config.toml` (it’s just a template).
2. Fill in your GitHub Personal Access Token for `API_KEY` and adjust the `crooks` and `niceys` lists as needed.

Here's the structure you should follow:

```toml
[security]
API_KEY = ""  # Replace with your GitHub API Key

[users.exceptions]
crooks = []  # List of users you're following but aren't following you back
niceys = []  # List of users following you but you aren't following back
```

- The `API_KEY` field should be filled with your GitHub Personal Access Token. You can create one on GitHub [here](https://github.com/settings/tokens).
- The `crooks` and `niceys` fields are optional and can be used to maintain a list of users that fit these categories, which you can use in your program’s logic.

### How Exceptions Are Used

The `crooks` and `niceys` lists in the `config.toml` file are used to manage exceptions when filtering your followers and followings:

- **Crooks**: This list is used to exclude users you're following who aren't following you back. For example, the function `get_crooks_logins` calculates users you follow but removes those listed in the `crooks` exception list.
  
- **Niceys**: This list is used to exclude users who are following you but you aren't following them back. The function `get_niceys_logins` identifies such users and removes those listed in the `niceys` exception list.

### Example

```toml
[security]
API_KEY = "your_github_api_key_here"

[users.exceptions]
crooks = ["user1", "user2"]
niceys = ["user3", "user4"]
```

In the above example:

- "user1" and "user2" are considered exceptions and won't be included in the list of "crooks."
- "user3" and "user4" are exceptions and won't be included in the list of "niceys."

## Usage

After configuring the `config.toml` file, you can run the script directly from the command line with different options.

### Command-Line Arguments

```bash
usage: gatekeeper [-h] [-v] (--list_followers | --list_following | --list_crooks | --unfollow_crooks | --list_niceys | --follow_niceys)

Manage followers and following users on Github

options:
  -h, --help         show this help message and exit
  -v, --version      show program's version number and exit
  --list_followers   List all your followers
  --list_following   List all users you're following
  --list_crooks      List all users you're following but aren't following you back
  --unfollow_crooks  Unfollow all users who aren't following you back
  --list_niceys      List all users that are following you but you aren't following them back
  --follow_niceys    Follow all users that you are following you but you aren't following them
```

### Example Usage

1. **List all followers**:

    ```bash
    python run.py --list_followers
    ```

2. **List all users you're following**:

    ```bash
    python run.py --list_following
    ```

3. **List all users you're following but aren't following you back**:

    ```bash
    python run.py --list_crooks
    ```

4. **Unfollow all users who aren't following you back**:

    ```bash
    python run.py --unfollow_crooks
    ```

5. **List all users following you but you aren't following them back**:

    ```bash
    python run.py --list_niceys
    ```

6. **Follow all users that you are following but aren't following you back**:

    ```bash
    python run.py --follow_niceys
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.
