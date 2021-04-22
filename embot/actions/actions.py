# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3
import pandas as pd
import datetime


class ActionShowHotelDetails(Action):

    def name(self) -> Text:
        return "show_hotel_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn = sqlite3.connect('hoteldata.sqlite')
        query = "SELECT name, url, rating, address FROM hoteldata WHERE img!=\"\" AND facility!=\"\" AND city=\"Bangalore\" ORDER BY rating desc LIMIT 5 "
        df = pd.read_sql(query, conn)

        if df.shape[0] > 0:
            values = list(df.values)

            content = 'Below are the options:\n\n'

            for data in values:
                hotelname = data[0]
                link = data[1]
                rating = data[2]
                address = data[3]

                content = content + "\n\nHotelname: " + hotelname + "\nBook Now: " + link + "\nRatting: " + rating + "\nAddress: " + address + "\n\n"
                print(content)
        else:
            content: "No hotels found"

        dispatcher.utter_message(text=content)

        return []


class ActionShowTicketsDetails(Action):

    def name(self) -> Text:
        return "show_tickets_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_tickets_details")

        return []


class ActionShowEventsDetails(Action):

    def name(self) -> Text:
        return "show_event_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_event_details")

        return []
