# PteroPython (no longer maintained)

**PROJECT NO LONGE MAINTAINED**
Pterodactyl v1 API for Python

*This project is no longer maintained, I currently have other things to do and the Pydactyl API has recently updated to 1.x as well which is much better since this project was never completed. Therefor I recommend you to use Pydacttyl instead of PteroPython*

## About this project
I have made this API because it didn't exist for the v1 API, I needed it and I hope some other people will find it useful.

At the moment I only made the Client API but I am working on the Application API and I hope it will be available in a few weeks.
Also I still need to add a few methods to send commands to your server, change the power state and list your API keys, servers and permissions.

A documentation will be available in a few days.

## Getting started

As mentioned above, Pterodactyl has two APIs: Client and Application. Both need a different API key, any user can make an API key for the client API and only admins can make a key for the Application API

### Installation

The project will be uploaded to PyPi (pip) when it is finished, until then you can download PteroPython using this command:

```shell
pip install git+https://github.com/danielrosnl/PteroPython
```

### Example script

```python
from PteroPython import Client

# Create a client to connect to your panel with you API key
client = Client('https://panel.example.com', 'YourAmazingSecretApiKey')

# Get information from your account
username = client.getUsername()
email = client.getEmail()

# Print information
print(f'Hello {username}! Your email adress is {email}.')

# Update user information
client.updatePassword('YourCurrentPassword', 'YourNewPassword', 'YourNewPasswordConfirmation')

# Get server information
serverName = client.getServerName('ServerId')
serverSftpIp = client.getServerSftpIp('ServerId')
```
