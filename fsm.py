from transitions.extensions import GraphMachine
import random
from utils import send_text_message

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        self.a=random.randrange(0, 3, 1)

    def is_going_to_state1(self, event):
        text = event.message.text
        if self.a == 0:
            return text.lower() == "發財"
        else :
            return text.lower() == ""

    def is_going_to_state2(self, event):
        text = event.message.text
        if self.a == 1:
            return text.lower() == "發財"
        else :
            return text.lower() == ""
    def is_going_to_state3(self, event):
        text = event.message.text
        if self.a == 2:
            return text.lower() == "發財"
        else :
            return text.lower() == ""

    def on_enter_state1(self, event):
        print("I'm entering state1")
        reply_token = event.reply_token
        send_text_message(reply_token, "高雄發大財")
        self.go_back()
        self.a=random.randrange(0, 3, 1)

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "總目標是高雄要發財")
        self.go_back()
        self.a=random.randrange(0, 3, 1)
        

    def on_exit_state2(self):
        print("Leaving state2")
        
    def on_enter_state3(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token
        send_text_message(reply_token, "太平島 開石油")
        self.go_back()
        self.a=random.randrange(0, 3, 1)

    def on_exit_state3(self):
        print("Leaving state3")