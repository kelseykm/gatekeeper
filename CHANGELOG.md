# Changelog

## [0.1.0] - 2024-11-07

- Initial release of the `Gatekeeper` Python script.

### **Features**

- List followers (`--list_followers`)
- List users you're following (`--list_following`)
- List users you're following but aren't following you back (`--list_crooks`)
- Unfollow users who aren't following you back (`--unfollow_crooks`)
- List users following you but you're not following them back (`--list_niceys`)
- Follow users who are following you but you're not following back (`--follow_niceys`)

#### **Configuration**

- `config.toml` file to store your GitHub `API_KEY` and exceptions for `crooks` and `niceys`.
- Example `example.config.toml` included to guide the creation of `config.toml`.

### **Command-Line Interface (CLI)**

- Arguments for each feature with usage examples in the README.
  