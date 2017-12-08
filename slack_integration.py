from slackclient import SlackClient
import requests, json

import argparse

parser = argparse.ArgumentParser(description='Launch integration')
parser.add_argument('--name', default='westebot', help='The name of our bot')
parser.add_argument('--token', help='Slack API token', required=True)
parser.add_argument('--url', help='backend url', default='http://ndi.eliott.tech/api/answer/')
args = parser.parse_args()

BOT_NAME  = args.name
BOT_TOKEN = args.token
API_URL   = args.url

slack_client = SlackClient(BOT_TOKEN)

if __name__ == "__main__":
    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        # retrieve all users so we can find our bot
        users = api_call.get('members')
        user = None
        for u in users:
            if 'name' in u and u.get('name') == BOT_NAME:
                print("Bot ID for '" + u['name'] + "' is " + u.get('id'))
                user = u
                # Get every channels"""
        for i in slack_client.api_call(
            "conversations.list",
            types="public_channel, private_channel"
        )['channels']:
            if i['name'] == 'general':
                while True:
                    u = slack_client.api_call("channels.info", channel=i['id'])
                    if 'channel' in u:
                        message = u['channel']['latest']
                        if message['type'] == 'message':
                            # If the message was sent by a humain
                            if 'user' in message:
                                print(message)
                                question = message['text']
                                answer = requests.post(
                                    API_URL,
                                    data = dict(question=question)
                                ).text
                                print(answer)
                                answer = json.loads(answer)['answer']
                                slack_client.api_call(
                                    "chat.postMessage",
                                    channel="#general",
                                    text=answer,
                                    user=user.get('id')
                                )

    else:
        print("could not find bot user with the name " + BOT_NAME)
