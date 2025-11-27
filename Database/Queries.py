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

    conn = establishConnection('localhost') # Never comment this line as this establishes the connection to MongoDB

    db = conn['finalProjectTest'] 

    # __________________________________________________________________________________________
    # ------------------------------------------Query 1-----------------------------------------   
    # The FIND query for logging in the customerAccount
    # QUERY
    queryLogin = {
        "username" : "String",
        "password" : "String"
    }
    resultQueryLogin = db['customerAccounts'].find_one(queryLogin)
    # This document will be cached in the App

    # SAMPLE QUERY
    queryLoginSample = {
        "username" : "Akumpo",
        "password" : "4676424d5f805a7579abd1236287be2abf24f39b8a622ef587edd7d91b8e2952"
    }
    resultQueryLoginSample = db['customerAccounts'].find_one(queryLoginSample)
    # __________________________________________________________________________________________



    # __________________________________________________________________________________________
    # ------------------------------------------Query 2-----------------------------------------   
    # The FIND query for fetching the user's owned games to be displayed in their library
    # QUERY
    queryShowLibrary = {
        "_id" : "String" # This will be the _id of the currently cached customerAccount
    }
    resultQueryShowLibrary = db['ownedGameInfo'].find(queryShowLibrary)
    # These documents will be cached in the App
    
    # SAMPLE QUERY
    queryShowLibrarySample = {
        "_id" : "6906eff058154850e616ba4b" # This will be the _id of the currently cached customerAccount
    }
    resultQueryShowLibrarySample = db['ownedGameInfo'].find(queryShowLibrarySample)
    # __________________________________________________________________________________________



    # __________________________________________________________________________________________
    # ------------------------------------------Query 3----------------------------------------- 
    # The query for fetching documents of games to be displayed in the user's browse section
    # QUERY
    someQuery = {
        # This query will be filled up using a script in the demo depending on the criteria the user specifies
    }
    pipelineBrowseGames = [
        {
            '$match': someQuery,
        },
        {
            '$sort': {
                'String': 0
            }
        },
        {
            '$project' : {
                'gameTitle' : 1,
                'originalPricePeso' : 1,
                'currentPricePeso' : 1,
                'currentDiscountPercent' : 1,
                'releaseDate' : 1,
            }
        }
    ]
    resultPipelineBrowseGames = db['storeGameInfo'].aggregate(pipelineBrowseGames)

    # SAMPLE QUERY
    someQuerySample = {
        'reviewVerdict' : 'Very Positive',
        'averageRating' : { '$gte': 85},
        'currentPricePeso' : { '$Lte': 400},
        'isDiscounted' : True,
        'categories': { '$all': ['Gambling', '3D'] }
    }
    pipelineBrowseGamesSample = [
        {
            '$match': someQuery,
        },
        {
            '$sort': {
                'String': 0
            }
        },
        {
            '$project' : {
                'gameTitle' : 1,
                'originalPricePeso' : 1,
                'currentPricePeso' : 1,
                'currentDiscountPercent' : 1,
                'releaseDate' : 1,
            }
        }
    ]
    resultPipelineBrowseGames = db['storeGameInfo'].aggregate(pipelineBrowseGamesSample)
    # __________________________________________________________________________________________


    # __________________________________________________________________________________________
    # ------------------------------------------Query 4----------------------------------------- 
    # The FIND query for fetching the full document of a selected game to view its full page
    # QUERY
    queryViewGame = {
        "_id" : "String"
    }
    resultQueryViewGame = db['storeGameInfo'].find_one(queryViewGame)

    # SAMPLE QUERY
    queryViewGameSample = {
        "_id" : "6909faaff56de748af83fad9"
    }
    resultQueryViewGameSample = db['storeGameInfo'].find_one(queryViewGameSample)
    # __________________________________________________________________________________________



    # __________________________________________________________________________________________
    # ------------------------------------------Query 5----------------------------------------- 
    # The AGGREGATION PIPELINE Query for fetching the most recent reviews of a specific game
    # QUERY
    pipelineTopReviews = [
        {
            '$match': {
                'game_id': 'String',
            },
        },
        {
            '$sort': {
                'datePosted': 1
            }
        },
        {
            '$limit': 10
        }
    ]
    resultPipelineTopReviews = db['gameReviews'].aggregate(PipelineTopReviews)

    # SAMPLE QUERY
    pipelineTopReviewsSample = [
        {
            '$match': {
                'game_id': '6909faaff56de748af83fad9',
            },
        },
        {
            '$sort': {
                'datePosted': 1
            }
        },
        {
            '$limit': 10
        }
    ]
    resultPipelineTopReviewsSample = db['gameReviews'].aggregate(PipelineTopReviewsSample)
    # __________________________________________________________________________________________



    # __________________________________________________________________________________________
    # ------------------------------------------Query 6----------------------------------------- 
    # The FIND Query for checking if a particular game is in the user's library
    # QUERY
    queryCheckLibrary = {
        "owner_id" : "String",
        "game_id" : "String"
    }
    resultQueryCheckLibrary = db['storeGameInfo'].find_one(queryCheckLibrary)

    # SAMPLE QUERY
    queryCheckLibrary = {
        "owner_id" : "6909faaff56de748af83fad6",
        "game_id" : "6909faaff56de748af83fad9"
    }
    resultQueryCheckLibrary = db['storeGameInfo'].find_one(queryCheckLibrary)
    # __________________________________________________________________________________________



    # __________________________________________________________________________________________
    # ------------------------------------------Query 7-----------------------------------------
    # The CREATE Query for creating the transaction document of a purchase
    # QUERY
    insertTransactionDocument = {
        "customerUsername" : "String",
        "customer_id" : "String",
        "transactionDate" : datetime(2025,1,1),
        "isRefund" : False,
        "subtotal" : 0,
        "lineItems" : [
            {
                "gameTitle" : "String",
                "game_id" : "String",
                "purchasePricePeso" : 0,
                "isDiscounted" : False
            },
            {
                "gameTitle" : "String",
                "game_id" : "String",
                "purchasePricePeso" : 0,
                "isDiscounted" : True
            },
            {
                "gameTitle" : "String",
                "game_id" : "String",
                "purchasePricePeso" : 0,
                "isDiscounted" : False
            },
        ]
    }
    db['transactions'].insert_one(insertTransactionDocument)

    # SAMPLE QUERY
    transactionDocumentSample = {
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
    db['transactions'].insert_one(transactionDocumentSample)
    # __________________________________________________________________________________________



    # __________________________________________________________________________________________
    # ------------------------------------------Query 8-----------------------------------------
    # The UPDATE Query for updating the user's balance
    # QUERY
    balanceUpdateParameter = {
        "_id" : "String"
    }
    balanceUpdateIncrement = {
        '$inc': { 'walletBalancePeso': 0 }
    }
    db['customerAccounts'].update_one(balanceUpdateParameter, balanceUpdateIncrement)

    # SAMPLE QUERY
    balanceUpdateParameterSample = {
        "_id" : "6909faaff56de748af83fad6"
    }
    balanceUpdateIncrementSample = {
        '$inc': { 'walletBalancePeso': 500 }
    }
    db['customerAccounts'].update_one(balanceUpdateParameterSample, balanceUpdateIncrementSample)
    # __________________________________________________________________________________________



    # __________________________________________________________________________________________
    # ------------------------------------------Query 9-----------------------------------------
    # The CREATE Query for inserting a bought game to the user's library
    # QUERY
    insertLibraryDocument = {
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
    db['ownedGameInfo'].insert_one(insertLibraryDocument)

    # SAMPLE QUERY
    insertLibraryDocumentSample = {
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
    db['ownedGameInfo'].insert_one(insertLibraryDocumentSample)
    # __________________________________________________________________________________________



    # __________________________________________________________________________________________
    # ------------------------------------------Query 9-----------------------------------------
    # The FIND Query for fetching transaction documents made by a user
    # QUERY
    queryGetPurchases = {
        "customer_id" : "String",
        "isRefund" : False
    }
    resultQueryGetPurchases = db['storeGameInfo'].find(queryGetPurchases)

    # SAMPLE QUERY
    queryGetPurchasesSample = {
        "customer_id" : "6909faaff56de748af83fadc",
        "isRefund" : False
    }
    resultQueryGetPurchases = db['storeGameInfo'].find(queryGetPurchasesSample)
    # __________________________________________________________________________________________



    # __________________________________________________________________________________________
    # ------------------------------------------Query 10-----------------------------------------
    # The DELETE Query for removing a game from a user's library after a refund
    # QUERY
    queryRemoveGame = {
        'owner_id': "String",
        "game_id" : "String"
    }
    db['ownedGameInfo'].delete_one(queryRemoveGame)

    # SAMPLE QUERY
    queryRemoveGame = {
        'owner_id': "6909faaff56de748af83fad6",
        "game_id" : "6909faaff56de748af83fad9"
    }
    db['ownedGameInfo'].delete_one(queryRemoveGame)
    # __________________________________________________________________________________________



    # __________________________________________________________________________________________
    # ------------------------------------------Query 10-----------------------------------------
    # The CREATE Query for inserting a review to a game
    # QUERY
    insertReviewDocument = {
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
    db['gameReviews'].insert_one(insertReviewDocument)

    # SAMPLE QUERY
    insertReviewDocumentSample = {
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
    db['gameReviews'].insert_one(insertReviewDocumentSample)
    # __________________________________________________________________________________________



    closeConnection(conn)