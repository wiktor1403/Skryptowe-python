import json
from datetime import datetime
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os

# Load menu data
def load_menu():
    with open("menu.json", "r") as file:
        data = json.load(file)
    return data["items"]

# Load opening hours data
def load_opening_hours():
    with open("opening_hours.json", "r") as file:
        data = json.load(file)
    return data["items"]

# Action to check if the restaurant is open
class ActionCheckOpeningHours(Action):
    def name(self):
        return "action_check_opening_hours"

    def run(self, dispatcher, tracker, domain):
        opening_hours = load_opening_hours()

        # Get user-provided day or use today
        requested_day = next(tracker.get_latest_entity_values("day"), None)
        if not requested_day:
            requested_day = datetime.today().strftime("%A")  # Get today's name

        if requested_day in opening_hours:
            hours = opening_hours[requested_day]
            open_time = hours["open"]
            close_time = hours["close"]

            if open_time == 0 and close_time == 0:
                dispatcher.utter_message(text=f"Sorry, the restaurant is closed on {requested_day}.")
            else:
                dispatcher.utter_message(text=f"The restaurant is open on {requested_day} from {open_time}:00 to {close_time}:00.")
        else:
            dispatcher.utter_message(text="I couldn't find the opening hours for that day.")

        return []

# Action to list menu items
class ActionShowMenu(Action):
    def name(self):
        return "action_show_menu"

    def run(self, dispatcher, tracker, domain):
        menu_items = load_menu()
        menu_text = "\n".join([f"{item['name']} - ${item['price']}" for item in menu_items])
        
        dispatcher.utter_message(text=f"Here is our menu:\n{menu_text}")
        return []

# Action to send a message to Slack
class ActionSendSlackMessage(Action):
    def name(self) -> str:
        return "action_send_slack_message"

    async def run(self, dispatcher, tracker, domain):
        slack_token = os.getenv("SLACK_TOKEN")  # Ensure this environment variable is set
        client = WebClient(token=slack_token)
        
        message = "Hello from Rasa!"
        channel = "#your-channel"  # Change this to your Slack channel
        
        try:
            response = client.chat_postMessage(channel=channel, text=message)
            dispatcher.utter_message(text="Message sent to Slack!")
        except SlackApiError as e:
            dispatcher.utter_message(text=f"Error sending message to Slack: {e.response['error']}")
        
        return []
