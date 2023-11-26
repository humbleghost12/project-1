from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem
import random
from kivy.core.window import Window

Window.size = (310, 580)

KV = '''
MDBoxLayout:
    md_bg_color: 0, 1, 0, 1
    line_color: 0, 0, 1, 1
    orientation: 'vertical'
    spacing: '10dp'
    padding: '10dp'
        
    ScrollView:
        GridLayout:
            id: question_list
            cols: 1
            spacing: '10dp'
            size_hint_y: None
            height: self.minimum_height

    MDRaisedButton:
        text: 'Truth'
        on_press: app.show_random_question()
        pos_hint: {"center_x": .5, "center_y": .5}
        
    
    MDRaisedButton:
        text: 'Dare'
        pos_hint: {"center_x": .5, "center_y": .95}
        on_press: app.show_random_dare()
'''

class RandomQuestionApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def show_random_question(self):
        question = self.get_random_question()
        self.add_question_to_list(question)
        self.show_dialog(question)

    def get_random_question(self):
        questions = [
            "What’s one thing you wish people knew about you?",
            "What’s the worst thing you’ve lied about?",
            "Have you ever cheated on someone?",
            "Where’s the weirdest place you peed?",
            "When was the last time you lied?",
            "When was the last time you cried?",
            "What’s your biggest fear?"
            "Have you followed someone into a restroom with the intention of kissing him / her?",
            "What is the weirdest place that you made love with someone in?",
            "What is your most favorite position for yoga?",
            "What is your most favorite memory of sex?",
            "When was the last time you had a crazy one-night stand and why was it crazy?",
            "What is your most favorite memory of sex?",
            "What is the weirdest thing you have done with your partner?",
            "What is your most favorite foreplay?",
            "What do you do when you think about the person you love?",
            "Which date do you prefer the most, breakfast date or dinner date?",
            "Have you ever dated someone just for sex?",
            "Have you ever taken money from someone for having sex?",
            "Do you prefer to keep the light on or off?",
            "Have you ever made out in a smelly bathroom?",
            "How was your first time dating experience?",
            "Have you ever had it so loud that someone complained about it?",
            "Have you ever talked dirty with someone of the same gender?",
            "Have you ever paid to watch porn?",
            "How frequently do you watch porn?",
            "Have you ever caught someone nude by mistake?",
            "When was the last time you faked an orgasm?",
            "Have you ever kissed your friend’s sibling?",
            "Have you ever dated your best friend?",
            "Have you ever made a video of you making out?",
            "Have you ever tried to recreate a porn scene in bed?",
            "What is the stupidest pickup line someone ever tried on you?",
            "Have you ever made out with your partner’s best friend?",
            "Have you ever made out in front of other people?",
            "Have you ever been caught by someone while making out with someone?",
            "When was the last time you covered for your best friend?",
            "What is the weirdest thing your partner told you?",
            "Have you ever made out with someone for revenge?",
            "When was the first time you watched porn?",
            "To whom did you lose your virginity and when?",
            "Bring a banana from the kitchen and eat that in a seductive way?",
            "Have you ever dated two people at one time to make a final decision?",
            "When was the last time you ghosted someone and why?",
            "Have you ever thought of breaking up with your partner but did not do it?",
            "When was the last time you got dumped? ",
            "Have you ever pretended to love someone?",
            "Have you ever got aroused at the wrong place?",
            "Do you think your partner ever faked an orgasm while doing it with you?",
            "Is there anything weird you do when you go on a date?",
            "What do you hate the most about your partner?",
            "What can turn you on at any time at any place?",
            "Has your partner ever cheated on you?",
            "Have you ever considered having a threesome or foursome?",
            "If you meet your ex all of a sudden how do you think you would react?",
            "What is your most favorite sex toy?",
            "What was your most horror date ever and why?",
            "Would you rather lick someone’s hand or chick?",
            "Which part of your body receives compliments the most?",
            "When was the last time someone complimented any of your actions?",

        ]
        return random.choice(questions)


    def show_dialog(self, question):
        dialog = MDDialog(
            title="Random Question",
            text=question,
            buttons=[
                MDRaisedButton(
                    text="Close", on_release=lambda *x: dialog.dismiss()
                )
            ],
        )
        dialog.open()

    def add_question_to_list(self, question):
        question_list = self.root.ids.question_list
        item = OneLineListItem(text=question)
        question_list.add_widget(item)


#############################################################################################

    def show_random_dare(self):
        question = self.get_random_dare()
        self.add_question_to_list(question)
        self.show_dialog(question)

    def get_random_dare(self):
        questions = [
            "D:Lick a car tire",
            "I dare you to tie your hands to your anklec s for the rest of the game.",
            "Spin around 10 times and try to walk straight.",
            "Eat a raw egg.",
            "Write a letter to your doctor describing an embarrassing rash you have, and post it on Facebook.",
            "Eat a small piece of fruit from someone else’s tongue.",
            "Spank or get spanked.",
            "Do a skit of a celebrity couple passionately kissing each other. You can take help from someone here.",
            "Call your crush and tell him/she you love them so much.",
            "Send a voicemail to your crush.",
            "Give someone in this room a full body massage.",
            "Post a Facebook status saying ‘I am coming’.",
            "Do lap dance on someone in this room.",
            "Share with us the last voicemail you have sent to your ex.",
            "Choose someone in this room to lick whipped cream from your finger.",
            "Blindfold yourself and kiss the first person you can touch.",
            "Choose someone from this room to go skinny dipping in a pool.",
            "Tell us about the things that you think you dislike the most in your life.",
            "Remove one of your underwear without removing your outfit.",
            "Make a video of working out and send it to your crush.",
            "Write about the best sexual encounter on your Facebook.",
            "Do ballet with no music on.",
            "Post a status on your Facebook saying ‘feeling horny’.",
            "Ask someone from this group to post something on your social media.",
            "Kiss someone from this group.",
            "Share your darkest desire with everyone.",
            "Describe your favorite person from this group and let everyone guess it.",
            "Try to lick your elbow.",
            "Dance in the shower with your clothes on and make a video of it.",
            "Share a secret about your most recent ex.",
            "Do pole dance and make a video of it and send it to your partner.",
            "Post a status about your most recent date with your partner in detail.",
            "Call your parents and convince them that you are pregnant.",
            "Shaved your full face now.",
            "Shave your one eyebrow.",
            "Do break dance with someone from this room in a romantic song.",
            "Call your ex and tell them how you really feel about them.",
            "Tell us a secret about your partner.",
            "Keep a piece of fruit on someone’s belly button and eat it in the most sensual way",
            "Lick someone’s ear.",
            "Give your partner or anyone here a lap dance.",
            "Kiss someone of the same gender present here.",
            "Undo your bf/gf shirt with only your teeth and keep eye contact throughout.",
            "Pour wine or champagne/drink on someone’s stomach/chest and lick it, very slowly.",
            "Rate 3 boys and girls you find hot, and want to make out with.",
            "Pinch every guy’s and girl’s butt in this room.",
            "Wear a girl’s lipstick or lip gloss and kiss her entire face",
            "Smooch a guy/girl for 1 minute, without parting your lips",
            "Give your partner or anyone here a lap dance.",
            "Climb on the table, let your hair loose (if a girl), and sing a sexy song, and perform.",
            "Use ketchup to put the mark of Simba on your forehead.",






















        ]
        return random.choice(questions)


    ##########


    def show_dialog(self, question):
        dialog = MDDialog(
            title="Random Question",
            text=question,
            buttons=[
                MDRaisedButton(
                    text="Close", on_release=lambda *x: dialog.dismiss()
                )
            ],
        )
        dialog.open()

    def add_question_to_list(self, question):
        question_list = self.root.ids.question_list
        item = OneLineListItem(text=question)
        question_list.add_widget(item)






if __name__ == '__main__':
    RandomQuestionApp().run()
