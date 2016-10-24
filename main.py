# KwisBot - Chat Bot for Twitch
from datetime import datetime
from socket import socket


class KwisBot(object):

    def __init__(self, host, port, channel, oauth):
        # Initializes parameters
        self.host = host
        self.port = port
        self.channel = channel
        self.oauth = oauth

        # Creates socket and connection
        self.socket = socket()
        self.socket.connect((self.host, self.port))

        # Sends information through socket
        self.socket.send(bytes("PASS " + self.oauth + "\r\n", "UTF-8"))
        self.socket.send(bytes("NICK " + self.channel + "\r\n", "UTF-8"))
        self.socket.send(bytes("JOIN #" + self.channel + " \r\n", "UTF-8"))

        # Program variables
        self.start_time = datetime.now()
        self.emote = ":O "
        self.filename = "commands.txt"
        self.statements = ["QUIT", "JOIN", "PART"]

        # Calls connection method
        self.commands = self.get_commands()
        self.connection()

    def get_commands(self):
        with open(self.filename, "r") as commands:
            commands = commands.readlines()
        return commands

    def connection(self):
        # Filters through initializing connection messages
        while True:
            conn_str = str(self.socket.recv(1024))
            if "End of /NAMES list" in conn_str:
                break

        print("KwisBot is now active.")

        # Main program loop
        while True:
            conn_str = str(self.socket.recv(1024)).split("\\r\\n")
            for line in conn_str:
                parts = line.split(":")
                if len(parts) < 3:
                    continue

                for statement in self.statements:
                    if statement not in parts[1]:
                        user_message = parts[2]

                username_split = parts[1].split("!")
                username = username_split[0]
                print(username + ": " + user_message)

                self.print_commands(username, user_message)

    def print_commands(self, username, user_message):
        for line in self.commands:
            line = line.split(" : ")

            # Handles username input into username response message
            if line[0] in user_message and "{username}" in line[1]:
                self.send_message(line[1].format(username=username))

            # Handles time input for time response message
            elif line[0] in user_message and "{time}" in line[1]:
                streaming_time = datetime.now() - self.start_time
                stream_str = str(streaming_time).split(".")
                self.send_message(line[1].format(time=stream_str[0]))

            # Handles other responses
            elif line[0] in user_message:
                self.send_message(line[1])

    def send_message(self, message):
        string = "PRIVMSG #" + self.channel + " :" + self.emote + message + \
                 "\r\n"
        self.socket.send(bytes(string, "UTF-8"))


def main():
    # Twitch Host and Port
    HOST = "irc.chat.twitch.tv"
    PORT = 6667

    # Channel and Oauth of Channel (Change these per user!)
    channel = "kwisart"  # All lowercase
    oauth = "oauth:examplekey"  # Include "oauth:"

    # Initiates Bot
    KwisBot(HOST, PORT, channel, oauth)

if __name__ == "__main__":
    main()
