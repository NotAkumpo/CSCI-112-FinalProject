import pymongo
from datetime import datetime
from bson.int64 import Int64
from bson.decimal128 import Decimal128
from decimal import Decimal

def establishConnection(host='localhost'):
    conn = pymongo.MongoClient(host, 27017)
    return conn

def closeConnection(conn):
    conn.close()

if __name__ == "__main__":
    """
    In this main function, we need to uncomment the lines one by one in order to avoid errors
    and also see the code executions step by step. Follow the sequence provided in the comments. Make sure to
    comment the previous line before uncommenting and running the next line.
    """

    # Establish MongoDB connection. Make sure to replace localhost accordingly
    conn = establishConnection('localhost') # Never comment this line as this establishes the connection to MongoDB

    db = conn['finalProjectTest'] 

    # __________________________________________________________________________________________
    # ---------------------------------customerAccounts Schema----------------------------------
    # The collection containing the accounts of the customers/users of the digital game store.
    # SCHEMA
    customerAccounts = {
        "username" : "String",
        "password" : "StringEncrypted", 
        "customerFirstName" : "String",
        "customerLastName" : "String",
        "country" : "String",
        "emailAddress" : "String",
        "age" : 0,
        "birthDate" : datetime(2025,1,1),
        "phoneNumber" : "String",
        "walletBalancePeso" : 0,
    }
    # SAMPLE DOCUMENT
    customerAccountsSample = {
        "username" : "Akumpo",
        "password" : "4676424d5f805a7579abd1236287be2abf24f39b8a622ef587edd7d91b8e2952",
        "customerFirstName" : "Abdiel",
        "customerLastName" : "Evangelista",
        "country" : "Philippines",
        "emailAddress" : "abdiel.evangelista@student.ateneo.edu",
        "age" : 23,
        "birthDate" : datetime(2002,12,31),
        "phoneNumber" : "+63 905 271 9062",
        "walletBalancePeso" : 2480.79,
    }
    # FIELD DESCRIPTIONS
    customerAccountsFieldDescriptions = {
        "username" : "The customer account's unique username",
        "password" : "The customer account's password (this will be encrypted)",
        "customerFirstName" : "The customer's first name",
        "customerLastName" : "The customer's last name",
        "country" : "The country that the customer account is bound to",
        "emailAddress" : "The email address that the customer account is bound to",
        "age" : "The customer's age",
        "birthDate" : "The customer's birth date",
        "phoneNumber" : "The phone number that the customer account is bound to",
        "walletBalancePeso" : "The customer account's money balance that can be used to purchase games",
    }
    # __________________________________________________________________________________________
    

    db['customerAccounts'].insert_one(customerAccounts)
    db['customerAccounts'].insert_one(customerAccountsSample)
    db['customerAccounts'].insert_one(customerAccountsFieldDescriptions)

    
    # __________________________________________________________________________________________
    # ---------------------------------storeGameInfo Schema-------------------------------------
    # The collection containing the data of the games as displayed on the store itself for browsing or purchase.
    # SCHEMA
    storeGameInfo = {
        "gameTitle" : "String",
        "reviewVerdict" : "String",
        "averageRating" : 0,
        "originalPricePeso" : 0,
        "currentPricePeso" : 0,
        "isDiscounted" : True,
        "isFree" : True,
        "isEarlyAccess" : True,
        "currentDiscountPercent" : 0,
        "releaseDate" : datetime(2025,1,1),
        "developer" : "String",
        "categories" : [
            "String"
        ],
        "description" : "String",
    }
    # SAMPLE DOCUMENT
    storeGameInfoSample = {
        "gameTitle" : "Clover Pit",
        "reviewVerdict" : "Very Positive",
        "averageRating" : 90,
        "originalPricePeso" : 335,
        "currentPricePeso" : 301.5,
        "isDiscounted" : True,
        "isFree" : False,
        "isEarlyAccess" : False,
        "currentDiscountPercent" : 20,
        "releaseDate" : datetime(2025,9,27),
        "developer" : "Panik Arcade",
        "categories" : [
            "Gambling",
            "Roguelite",
            "Strategy",
            "3D"
        ],
        "description" : "A rogue-lite slot machine nightmare. Gamble for your life in a never-ending debt simulator!",
    }
    # FIELD DESCRIPTIONS
    storeGameInfoFieldDescriptions = {
        "gameTitle" : "The title of the game",
        "reviewVerdict" : "The overall verdict based on all the reviews of the game",
        "averageRating" : "The overall rating based on all the reviews of the game",
        "originalPricePeso" : "The game's original price in peso",
        "currentPricePeso" : "The game's current price in peso",
        "isDiscounted" : "True if the game is currently discounted",
        "isFree" : "True if the game is free",
        "isEarlyAccess" : "True if the game is in early access",
        "currentDiscountPercent" : "The percentage of the game's current discount",
        "releaseDate" : "The game's release date",
        "developer" : "The game's developer",
        "categories" : "A list of the game's categories",
        "description" : "The game's description",
    }
    # __________________________________________________________________________________________
    

    db['storeGameInfo'].insert_one(storeGameInfo)
    db['storeGameInfo'].insert_one(storeGameInfoSample)
    db['storeGameInfo'].insert_one(storeGameInfoFieldDescriptions)


    # __________________________________________________________________________________________
    # ---------------------------------ownedGameInfo Schema-------------------------------------
    # The collection containing the data of the already purchased games as displayed in the user's library.
    # SCHEMA
    ownedGameInfo = {
        "ownerUsername" : "String",
        "owner_id" : "String (indexed)",
        "gameTitle" : "String",
        "game_id" : "String (indexed)",
        "licenseID" : "String",
        "hoursPlayed" : 0,
        "spaceRequiredGB" : 0,
        "isInstalled" : True,
        "datePurchased" : datetime(2025,1,1),
    }

    # SAMPLE DOCUMENT
    ownedGameInfoSample = {
        "ownerUsername" : "Akumpo",
        "owner_id" : "*****",
        "gameTitle" : "Path of Exile 2",
        "game_id" : "*****",
        "licenseID" : "hajsdbhasbdhbk12312312",
        "hoursPlayed" : 299.8,
        "spaceRequiredGB" : 112.9,
        "isInstalled" : False,
        "datePurchased" : datetime(2024,12,9),
    }
    # FIELD DESCRIPTIONS
    ownedGameInfoFieldDescriptions = {
        "ownerUsername" : "The username of the game's owner",
        "owner_id" : "A foreign key to the customerAccount that the owned game is bound to",
        "gameTitle" : "The title of the game",
        "game_id" : "A foreign key to the storeGameInfo that corresponds to the same game",
        "licenseID" : "The license ID serving as proof that the game has been purchased by the owner",
        "hoursPlayed" : "The total playtime of the game in hours",
        "spaceRequiredGB" : "The total required space to download the game in GB",
        "isInstalled" : "True if the game is installed to user's desktop",
        "datePurchased" : "The date that the game was purchased",
    }
    # __________________________________________________________________________________________


    db['ownedGameInfo'].insert_one(ownedGameInfo)
    db['ownedGameInfo'].insert_one(ownedGameInfoSample)
    db['ownedGameInfo'].insert_one(ownedGameInfoFieldDescriptions)


    # __________________________________________________________________________________________
    # ---------------------------------gameReviews Schema---------------------------------------
    # The collection containing the users' reviews of the games in the store.
    # SCHEMA
    gameReviews = {
        "gameTitle" : "String",
        "game_id" : "String (indexed)",
        "authorUsername" : "String",
        "author_id" : "String (indexed)",
        "isRecommended" : True,
        "reviewDescription" : "String",
        "reviewVisibility" : "String",
        "datePosted" : datetime(2025,1,1),
        "userPlaytimeHours" : 0,
    }
    # SAMPLE DOCUMENT
    gameReviewsSample = {
        "gameTitle" : "NBA 2K26",
        "game_id" : "*****",
        "authorUsername" : "m14mumphrey2003",
        "author_id" : "*****",
        "isRecommended" : True,
        "reviewDescription" : "Since the last NBA 2K26 update (v1.4 on Sept 18, 2025), the game has started stuttering badly on my PC, even though I’m running an i7-14700KF, RTX 4070, and 64GB RAM. FPS looks stable, but offline modes like Play Now and MyNBA feel really choppy. Oddly, if I swap to an older modded exe, the game runs perfectly smooth. Online with the official exe also feels smoother, so it seems like the new patch broke offline frame pacing or presentation. I’ve tried everything — shader cache reset, reinstall, file verify, clean drivers — nothing fixes it. Looks like this started only with the latest update. Anyone else seeing this?",
        "reviewVisibility" : "Public",
        "datePosted" : datetime(2025,10,2),
        "userPlaytimeHours" : 50,
    }
    # FIELD DESCRIPTIONS
    gameReviewsFieldDescriptions = {
        "gameTitle" : "The title of the game being reviewed",
        "game_id" : "A foreign key to the ownedGameInfo being reviewed",
        "authorUsername" : "The username of the customer reviewing the game",
        "author_id" : "A foreign key to the customerAccount reviewing the game",
        "isRecommended" : "True if the user recommends the game",
        "reviewDescription" : "The detailed review of the game",
        "reviewVisibility" : "The visibility of the review to other users",
        "datePosted" : "The date that the review was posted",
        "userPlaytimeHours" : "The author's playtime of the game in hours",
    }
    # __________________________________________________________________________________________


    db['gameReviews'].insert_one(gameReviews)
    db['gameReviews'].insert_one(gameReviewsSample)
    db['gameReviews'].insert_one(gameReviewsFieldDescriptions)


    # __________________________________________________________________________________________
    # ---------------------------------transactions Schema--------------------------------------
    # The collection containing the data of all the transactions of games in the digital game store. Documents can be one of two types: purchase or refund. The schema of the document is different depending on the type.
    # SCHEMA
    transactionsBuy = {
        "customerUsername" : "String",
        "customer_id" : "String (indexed)",
        "transactionDate" : datetime(2025,1,1),
        "isRefund" : False,
        "subtotal" : 0,
        "lineItems" : [
            {
                "gameTitle" : "String",
                "game_id" : "String (indexed)",
                "purchasePricePeso" : 0,
                "isDiscounted" : True
            }
        ]
    }
    # SAMPLE DOCUMENT
    transactionsBuySample = {
        "customerUsername" : "Akumpo",
        "customer_id" : "*****",
        "transactionDate" : datetime(2025,10,23),
        "isRefund" : False,
        "subtotal" : 1023.50,
        "lineItems" : [
            {
                "gameTitle" : "Megabonk",
                "game_id" : "*****",
                "purchasePricePeso" : 335,
                "isDiscounted" : False
            },
            {
                "gameTitle" : "Fellowship",
                "game_id" : "*****",
                "purchasePricePeso" : 688.50,
                "isDiscounted" : True
            },
            {
                "gameTitle" : "Destiny 2",
                "game_id" : "*****",
                "purchasePricePeso" : 0,
                "isDiscounted" : False
            },
        ]
    }
    transactionsBuyFieldDescriptions = {
        "customerUsername" : "The username of the customer buying the game/s",
        "customer_id" : "A foreign key to the customerAccount making the purchase",
        "transactionDate" : "The date of purchase",
        "isRefund" : "True if the transaction is a refund, false if purchase",
        "subtotal" : "The total cost of all the games in the transaction",
        "lineItems" : "A list of documents containing the games being purchased in the transaction"
    }

    db['transactions'].insert_one(transactionsBuy)
    db['transactions'].insert_one(transactionsBuySample)
    db['transactions'].insert_one(transactionsBuyFieldDescriptions)

    # SCHEMA
    transactionsRefund = {
        "customerUsername" : "String",
        "customer_id" : "String (indexed)",
        "refundedGameTitle" : "String",
        "refundedGameStore_id" : "String",
        "refundedGameLibrary_id" : "String",
        "transactionDate" : datetime(2025,1,1),
        "isRefund" : True,
        "balanceRefunded" : 0,
    }
    # SAMPLE DOCUMENT
    transactionsRefundSample = {
        "customerUsername" : "Akumpo",
        "customer_id" : "String (indexed)",
        "refundedGameTitle" : "V Rising",
        "refundedGameStore_id" : "*****",
        "refundedGameLibrary_id" : "*****",
        "transactionDate" : datetime(2025,11,2),
        "isRefund" : True,
        "balanceRefunded" : 449.50,
    }
    # FIELD DESCRIPTIONS
    transactionsRefundFieldDescriptions = {
        "customerUsername" : "The username of the customer buying the game/s",
        "customer_id" : "A foreign key to the customerAccount making the purchase",
        "refundedGameTitle" : "The title of the game being refunded",
        "refundedGameStore_id" : "A foreign key to the storeGameInfo of the game being refunded",
        "refundedGameLibrary_id" : "A foreign key to the ownedGameInfo of the game being refunded",
        "transactionDate" : "The date of purchase",
        "isRefund" : "True if the transaction is a refund, false if purchase",
        "balanceRefunded" : "The total amount refunded to the customerAccount for refund of the game",
    }
    # __________________________________________________________________________________________

    db['transactions'].insert_one(transactionsRefund)
    db['transactions'].insert_one(transactionsRefundSample)
    db['transactions'].insert_one(transactionsRefundFieldDescriptions)


    closeConnection(conn)