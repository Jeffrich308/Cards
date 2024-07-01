# -------------------------------------------------------------------------------
# Name:             Card.py
# Purpose:          Create a deck of cards.  Shuffle and deal.
#
# Author:           Jeffreaux
#
# Created:          24June24
#
# Required Packages:    PyQt5, PyQt5-Tools
# -------------------------------------------------------------------------------

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QAction, QLabel
from PyQt5 import uic
from PyQt5.QtGui import QPixmap

import sys
import random


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the UI file
        uic.loadUi("Cards.ui", self)
        self.setWindowTitle("Deal Cards")

        # define Widgets
        self.btnShuffle = self.findChild(QPushButton, "btnShuffle")
        self.btnDeal = self.findChild(QPushButton, "btnDeal")

        self.lblDealerCard = self.findChild(QLabel, "lblDealerCard")
        self.lblPlayerCard = self.findChild(QLabel, "lblPlayerCard")
        self.lblDealer = self.findChild(QLabel, "lblDealer")
        self.lblPlayer = self.findChild(QLabel, "lblPlayer")

        # Define the actions
        self.btnShuffle.clicked.connect(self.shuffle)
        self.btnDeal.clicked.connect(self.dealCards)

        # Shuffle Cards at Startup
        self.shuffle()

        # Show the app
        self.show()

    def shuffle(self):
        self.setWindowTitle("Deck Shuffled")
        print("Shuffle Button Pressed")
        suites = ["diamonds", "clubs", "hearts", "spades"]
        values = range(2, 15)  # 11=Jack, 12=Queen, 13=King, 14=Ace

        #Create Deck
        global deck
        deck = []

        for suit in suites:
            for value in values:
                deck.append(f"{value}_of_{suit}")

        print(deck)
        print(len(deck))

        # Create Players
        global dealer, player
        dealer = []
        player = []

        # Grab a card from the deck
        card = random.choice(deck)
        print(card)

        # Remove card from the deck
        deck.remove(card)
        
        # Add Card to dealer list
        dealer.append(card)
        
        # Output card to a screen
        pixmap = QPixmap(f'cards/{card}.png')
        self.lblDealerCard.setPixmap(pixmap)

         # Grab a card from the deck
        card = random.choice(deck)
        print(card)

        # Remove card from the deck
        deck.remove(card)
        
        # Add Card to dealer list
        player.append(card)
        
        # Output card to a screen
        pixmap = QPixmap(f'cards/{card}.png')
        self.lblPlayerCard.setPixmap(pixmap)

        self.setWindowTitle(f"{len(deck)} Cards left in the deck....")


    
    def dealCards(self):
        try:
            # Grab a card from the deck
            card = random.choice(deck)
            print(card)

            # Remove card from the deck
            deck.remove(card)
            
            # Add Card to dealer list
            dealer.append(card)
            
            # Output card to a screen
            pixmap = QPixmap(f'cards/{card}.png')
            self.lblDealerCard.setPixmap(pixmap)

            # Grab a card from the deck
            card = random.choice(deck)
            print(card)

            # Remove card from the deck
            deck.remove(card)
            
            # Add Card to dealer list
            player.append(card)
            
            # Output card to a screen
            pixmap = QPixmap(f'cards/{card}.png')
            self.lblPlayerCard.setPixmap(pixmap)

            self.setWindowTitle(f"{len(deck)} Cards left in the deck....")



        except:
            self.setWindowTitle("Game Over!!")


    def closeEvent(self, *args, **kwargs):
        # print("Program closed Successfully!")
        self.close()


# Initialize the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
