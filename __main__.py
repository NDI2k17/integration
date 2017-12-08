from slackclient import SlackClient


BOT_NAME = 'bobot'
BOT_KEY = 'xoxb-283548997155-U0hxkV8BdvQCRslWpdaiz4jy'

slack_client = SlackClient(BOT_KEY)


if __name__ == "__main__":
    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        # retrieve all users so we can find our bot
        users = api_call.get('members')
        for user in users:
            if 'name' in user and user.get('name') == BOT_NAME:
                print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
                '''slack_client.api_call(
                    "chat.postMessage",
                    channel="#general",
                    text="caca #maturité",
                    user=user.get('id')
                )'''
                # Get every channels
                '''for i in slack_client.api_call(
                    "conversations.list",
                    types="public_channel, private_channel"
                )['channels']:
                    if i['name'] == 'general':'''
                print(slack_client.api_call(
                    method='chat.message',
                    channel='#general'
                ))

    else:
        print("could not find bot user with the name " + BOT_NAME)
