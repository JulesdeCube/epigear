# EpiGear

## About

EpiGear is a discord bot for server creation, and includes several points.
- Creation of permission groups
- Creation of roles based on permissions
- Creation of a channel and category according to these permissions
- Synchronization of roles and salons even after their creation
- All based on a configuration file

## How to install it ?

1. First, you will have to clone the project.

```shell
git clone https://github.com/gastbob40/epigear
```

2. Consider creating a `virtual environment`, in order to install dependencies locally.

```shell
python -m venv venv
```

3. You need to activate the virtual environment now

```shell
# If you are on Linux or Mac ?
source venv/bin/activate 

# If you are on Windows
./venv/Scripts/activate
``` 

4. Finally, install the dependencies

````shell
pip install requirements.txt
````

## How it works ?

The `run` folder contains all the data of the program configuration.

### config_bot

This folder contain a single file, `default.config.yml`. This file looks like this:
 
```yaml
# General information
discord_server_id: ~
current_promo: ~
token: ~

# Clear information
clear: false
channels_to_ignore: ~ 
roles_to_ignore:   
    - '@everyone' 
```

You will therefore have to modify in this file the `discord_server_id` by the one of the server where you want to run the bot.
Also remember to put the `token` of your bot discord.

You can also choose to delete the roles and channels of the server in question before creating the new roles and channels.
The `channels_to_ignore` and `roles_to_ignore` are lists of name of role / channel

> The `current_promo` line is only used for EPITA, it is not to be filled in for other uses

### config_server

This folder contains the configuration of permissions groups, roles and channels.

#### `perms_groups.yml`

This file contains the names of the permission groups and their correspondence to Discord.
You can therefore add or remove groups.

For example:

```yaml
READ_ONLY: #the name of the group
  read_messages: true     # One permission (read_messages) and its value (true)
  send_messages: false    # One permission (send_messages) and its value (false)
```

#### `roles.yml`

This file contains the list of roles and their specificity.

For example:

```yaml
EXTERNE:  # The name of the role object, used in channel definition
  name: Externe             # The name of the role (on discord)
  color: 0xc0ff00           # The color of the role
  permissions: DEFAULT      # The permission group of the role (link to perms_groups.yml)
  hoist: true               # If the role is hoist or not
  mentionable: false        # If the mentionable is hoist or not
```

#### `server_channels.yml`

The file contains the list of categories and channels for the server

For example:

```yaml
epita_promo:                    # The name of the object
  name: EPITA/PROMO             # The name of the category
  overwrites:                   # The general permission of the category
    PROMO_N: READ_AND_WRITE     # Role (from roles.yml): perms group (from perms_group.yml)
  default_perm: HIDDEN          # Default perm (for everyone role)

  channels:                     # The list of texts channel
    promo:                      # The name of the object
      name: PROMO               # The name of the channel (in discord)
      overwrites:               # The overwrited permission
        STAFF_EPILOGIN: SERVER_ADMIN_PERM   # Role (from roles.yml): perms group (from perms_group.yml)
        ADMIN: ADMIN_PERM
      default_perm: HIDDEN      # Default perm (for everyone role)

  vocal_channels:               # The list of voice channel
    general:                    # The name of the object
      name: General             # The name of the voice channel (in discord)
      overwrites: ~             # The overwrited permissions
      default_perm: HIDDEN      # The default perm
```

To start the bot, just start the `index.py` file in the `run` folder.