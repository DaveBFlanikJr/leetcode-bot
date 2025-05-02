# Leetcode Slack Bot

A Slack bot that fetches solutions to Leetcode problems directly from the GitHub repository. Use the `/leetcode` command to retrieve code solutions for any given problem.

## Features

- Fetch Leetcode problem solutions by number.
- Use the `/leetcode <problem_number>` command in Slack.
- Supports the lookup of problems in multiple Langagues
- Easy to set up and run locally or deploy to cloud platforms like Render, Heroku, etc.

## Installation

### Prerequisites

- Python 3.7+
- [ngrok](https://ngrok.com/) (for local development to expose your server to the internet)
- [Slack App](https://api.slack.com/apps) (to create a Slack bot and generate tokens)

### 1. Clone the Repository

```bash
git clone https://github.com/DaveBFlanikJr/leetcode-bot.git
cd leetcode-bot
```

### 2. Set Up a Virtual Environment
```python3 -m venv venv```

```source venv/bin/activate ``` # Mac/Linux

```venv\Scripts\activate ``` # Windows

### 3.Install Dependencies
```pip install -r requirements.txt```

### 4. Configure Your Environment Variables
Create a .env file and add your Slack bot token and signing secret:
```lack_bot_token=your-bot-token-here
slack_signing_secret=your-signing-secret-here
ngrok_authtoken=your-ngrok-auth-token-here
```

### 5. Start the Application
Run the bot server:
```bash
python3 main.py
```

Start ngrok to expose your server to the internet:
```bash
ngrok http 3000
```
Update your Slash Command's Request URL in Slack to the ngrok URL (https://<random-id>.ngrok.io/slack/events).

### 6. Install the Slack App
Go to the Install App section of your Slack App settings, click Install to Workspace, and complete the installation.

### 7. Test the Bot
Once the bot is installed, go to any Slack channel and type:
```
/leetcode 1
```

Usage
Command: /leetcode <problem_number>

Example: /leetcode 1 will fetch the solution for Leetcode problem 1.

### Contributing
If you'd like to contribute, feel free to fork the repository, make changes, and submit a pull request.
