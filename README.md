# KwisBot

KwisBot v1.0.0 (Python 3.5)

Chatbot for Twitch

Check the project's [Wiki](https://github.com/Kwistech/KwisBot/wiki) for more info.

## Installation ##

+ Fork the repository and clone it to your local drive.

+ From the program's root directory, double-click `main.py`

## How to Use

Once the repository is cloned to your local drive, there are two variables you need to change in main.py.

1. Change the "channel" variable (found in main() function) to your Twitch channel's name (must be lowercase).
2. Change the "oauth" variable (also found in main() function) to your Twitch channel's OAuth key (can be generated [here](https://twitchapps.com/tmi/)).

Once the above two steps are done, all you have to do is run the script. The bot will be active when the message "KwisBot is now active." appears in the console/terminal.

To test if the bot is working, go to your Twitch channel and type a command associated with the bot (list of commands can be found in the commands.txt file.

## How to Add/Delete Commands

As of right now, commands can be added to the commands.txt file in the below format:

+ user's chat message : KwisBot's response

The leftmost part of the above line is reserved for the user's message. The rightmost part of the line is the bot's response to the user's message. The colon with spaces ( : ) separates the two.

Examples:

+ Hey : Welcome to the stream!
+ ~uptime : Streaming for {time}

If you would like to add commands, just follow the examples above. To delete commands, just delete the command from commands.txt.

*Note: If you want to do special commands (like banning viewers), you need to add both the command in commands.txt and the functionality in main.py (print_commands() method).*
