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

    customerAccounts = [
        {
            "username": "statuc",
            "password": "5d146e23ef85601a30ed0481c73cfd40a742a0965005c6cf9429054339bdfc1f",
            "customerFirstName": "Samantha",
            "customerLastName": "Mullen",
            "country": "Myanmar",
            "emailAddress": "uhardin@gmail.com",
            "age": 42,
            "birthDate": datetime(1983, 12, 2),
            "phoneNumber": "+95 65 258 441 3336",
            "walletBalancePeso": 673.09
        },
        {
            "username": "sabcol",
            "password": "e418578c25d64d864ead74876372d055d764974bf0ed1b61dd930f8cf76b1e6d",
            "customerFirstName": "Ricky",
            "customerLastName": "Hall",
            "country": "Thailand",
            "emailAddress": "galvanelizabeth@yahoo.com",
            "age": 53,
            "birthDate": datetime(1972, 8, 7),
            "phoneNumber": "+6630 647 985 5344",
            "walletBalancePeso": 82.09
        },
        {
            "username": "ronwri",
            "password": "6fd21e0be262653a124805783ac5bbf40a46e64085509dc50170b821091f5e9d",
            "customerFirstName": "Ricky",
            "customerLastName": "Anderson",
            "country": "Malaysia",
            "emailAddress": "warnold@yahoo.com",
            "age": 20,
            "birthDate": datetime(2005, 3, 8),
            "phoneNumber": "+60 10 796 894 6850",
            "walletBalancePeso": 628.61
        },
        {
            "username": "bobpar",
            "password": "356babc5c7a38bfa74b1fea184b05bd071fd9565a718a08fc1eb7ba8080d4578",
            "customerFirstName": "Keith",
            "customerLastName": "Hardin",
            "country": "Singapore",
            "emailAddress": "thomas55@yahoo.com",
            "age": 64,
            "birthDate": datetime(1961, 2, 8),
            "phoneNumber": "+65995 331 484 4665",
            "walletBalancePeso": 164.39
        },
        {
            "username": "hanols",
            "password": "c70a93369ed2f536a224611dd998c9b5a8c4bd70ba9ab2387b7f62eaa1d344cd",
            "customerFirstName": "Keith",
            "customerLastName": "Campbell",
            "country": "Singapore",
            "emailAddress": "troybryan@gmail.com",
            "age": 62,
            "birthDate": datetime(1963, 8, 4),
            "phoneNumber": "+65995 331 484 4665",
            "walletBalancePeso": 146.29
        },
        {
            "username": "liswea",
            "password": "2cc684788744307c6f0a2c066e63aed396bfe2115e8144ac6df4a349463b2326",
            "customerFirstName": "Jenny",
            "customerLastName": "Vincent",
            "country": "Laos",
            "emailAddress": "darrencoffey@hotmail.com",
            "age": 62,
            "birthDate": datetime(1963, 8, 23),
            "phoneNumber": "+856970 624 160 2718",
            "walletBalancePeso": 180.73
        },
        {
            "username": "kailam",
            "password": "214e051249c3fa8e4a381b1914cdc8b6066ac1affb188b88f7c0a891a5afe0cd",
            "customerFirstName": "Tony",
            "customerLastName": "Larson",
            "country": "Cambodia",
            "emailAddress": "browndavid@gmail.com",
            "age": 50,
            "birthDate": datetime(1975, 7, 8),
            "phoneNumber": "+855 29 438 9286",
            "walletBalancePeso": 490.25
        },
        {
            "username": "rayjoh",
            "password": "ce95c52a97592c90ce6c20203c2361794123c2f717aa8907c6545e740ebddcc1",
            "customerFirstName": "James",
            "customerLastName": "Mata",
            "country": "Singapore",
            "emailAddress": "vgibson@yahoo.com",
            "age": 40,
            "birthDate": datetime(1985, 6, 13),
            "phoneNumber": "+65995 331 484 4665",
            "walletBalancePeso": 587.36
        },
        {
            "username": "eridaw",
            "password": "c4f84617c92eec18cc0b73a1f2384704dddcaf49a23cfab9441c53849a130fb3",
            "customerFirstName": "Alexander",
            "customerLastName": "Davis",
            "country": "Thailand",
            "emailAddress": "evansgabriel@gmail.com",
            "age": 20,
            "birthDate": datetime(2005, 11, 20),
            "phoneNumber": "+6630 647 985 5344",
            "walletBalancePeso": 454.41
        },
        {
            "username": "samgon",
            "password": "9b8692578e229fe8861706f4942746d917c8d3c9602363cbb065dd3c890d11af",
            "customerFirstName": "Brittany",
            "customerLastName": "George",
            "country": "Vietnam",
            "emailAddress": "caleb25@yahoo.com",
            "age": 54,
            "birthDate": datetime(1971, 9, 1),
            "phoneNumber": "+84974 506 709 2624",
            "walletBalancePeso": 239.61
        },
        {
            "username": "nannel",
            "password": "0651a6ea09f72c76aaea47479b6e63cca805baa78a284d8a79fb8d6369fe5281",
            "customerFirstName": "Connor",
            "customerLastName": "Gaines",
            "country": "Myanmar",
            "emailAddress": "laura38@hotmail.com",
            "age": 63,
            "birthDate": datetime(1962, 3, 13),
            "phoneNumber": "+95 65 258 441 3336",
            "walletBalancePeso": 426.94
        },
        {
            "username": "chrmit",
            "password": "02f9dfa7504c361ec0d9d7e07bb0934b893248b457cc69dd688f082983788a0b",
            "customerFirstName": "Andre",
            "customerLastName": "Delgado",
            "country": "Philippines",
            "emailAddress": "joseph21@gmail.com",
            "age": 54,
            "birthDate": datetime(1971, 12, 12),
            "phoneNumber": "+63910 307 702 7488",
            "walletBalancePeso": 151.37
        },
        {
            "username": "clapen",
            "password": "07285e3aefcc6fa265a3c89a5d72dafac116e497d5c0181a66275446be13e259",
            "customerFirstName": "Michael",
            "customerLastName": "Harmon",
            "country": "Laos",
            "emailAddress": "gomezzachary@gmail.com",
            "age": 36,
            "birthDate": datetime(1989, 3, 4),
            "phoneNumber": "+856970 624 160 2718",
            "walletBalancePeso": 251.53
        },
        {
            "username": "alerom",
            "password": "33f840d53533e38f17211b83cc63304f43edc25ec4c7fd9bf85ccb51a3081895",
            "customerFirstName": "Lauren",
            "customerLastName": "King",
            "country": "Indonesia",
            "emailAddress": "seanleonard@yahoo.com",
            "age": 48,
            "birthDate": datetime(1977, 2, 25),
            "phoneNumber": "+62810 640 720 9408",
            "walletBalancePeso": 462.75
        },
        {
            "username": "paubre",
            "password": "281ecbecc7c454bd519e3d67d1990fe26020337a6807c94ec94c905ea19531b2",
            "customerFirstName": "Jacob",
            "customerLastName": "Johnson",
            "country": "Singapore",
            "emailAddress": "jmeyer@hotmail.com",
            "age": 50,
            "birthDate": datetime(1975, 7, 15),
            "phoneNumber": "+65995 331 484 4665",
            "walletBalancePeso": 789.59
        },
        {
            "username": "karhow",
            "password": "3bfd2266708cfabf451840daa0feb1799e1e2fee43bd94a8a7db450c639d181e",
            "customerFirstName": "Christopher",
            "customerLastName": "Daniels",
            "country": "Malaysia",
            "emailAddress": "mitchellryan@hotmail.com",
            "age": 23,
            "birthDate": datetime(2002, 11, 22),
            "phoneNumber": "+60 10 796 894 6850",
            "walletBalancePeso": 497.31
        },
        {
            "username": "jesfle",
            "password": "a88226a9175fdb47f15d5599dc288f1c6920e67c7878a3428bdf0b333460b285",
            "customerFirstName": "Keith",
            "customerLastName": "Perez",
            "country": "Laos",
            "emailAddress": "woodwardwilliam@hotmail.com",
            "age": 37,
            "birthDate": datetime(1988, 9, 12),
            "phoneNumber": "+856970 624 160 2718",
            "walletBalancePeso": 218.35
        },
        {
            "username": "walwal",
            "password": "6c9da4ac3ab6be538c1ba665d0c1ed9db4c040a84b4aa3a2c00760b53115085f",
            "customerFirstName": "Kelly",
            "customerLastName": "Tucker",
            "country": "Thailand",
            "emailAddress": "freemanmartha@gmail.com",
            "age": 59,
            "birthDate": datetime(1966, 10, 12),
            "phoneNumber": "+6630 647 985 5344",
            "walletBalancePeso": 107.68
        },
        {
            "username": "paujoh",
            "password": "e8a3150c3c9b44171b17178a589a8ce48b3355c25325c490c2bb6764fba61034",
            "customerFirstName": "Juan",
            "customerLastName": "Prince",
            "country": "Philippines",
            "emailAddress": "steven95@yahoo.com",
            "age": 35,
            "birthDate": datetime(1990, 8, 8),
            "phoneNumber": "+63910 307 702 7488",
            "walletBalancePeso": 591.76
        },
        {
            "username": "whimur",
            "password": "cd1551fd5616a5206868714e46f7f66be53935a5332c4f6ddc15fa5eaff849e6",
            "customerFirstName": "Jared",
            "customerLastName": "Hines",
            "country": "Philippines",
            "emailAddress": "elizabeth26@yahoo.com",
            "age": 29,
            "birthDate": datetime(1996, 2, 24),
            "phoneNumber": "+63910 307 702 7488",
            "walletBalancePeso": 884.78
        },
        {
            "username": "rachic",
            "password": "0f1bc49e19267b98a144b729e582f9e59b620a1e186076696e2d91ad23561f8c",
            "customerFirstName": "Kyle",
            "customerLastName": "Hebert",
            "country": "Indonesia",
            "emailAddress": "cranesara@hotmail.com",
            "age": 53,
            "birthDate": datetime(1972, 10, 8),
            "phoneNumber": "+62810 640 720 9408",
            "walletBalancePeso": 578.64
        },
        {
            "username": "alerya",
            "password": "24c57f8f1d073cf9a2dc237b2d82a137154ef4529ca137e17d86e79a1f954541",
            "customerFirstName": "Ian",
            "customerLastName": "Kelly",
            "country": "Myanmar",
            "emailAddress": "daniel77@hotmail.com",
            "age": 34,
            "birthDate": datetime(1991, 12, 30),
            "phoneNumber": "+95 65 258 441 3336",
            "walletBalancePeso": 411.49
        },
        {
            "username": "pauest",
            "password": "d536a905e805b57695d4f6111a7ce70fe06c7bde03c24e83c00fafeea966b80a",
            "customerFirstName": "Andrea",
            "customerLastName": "Blevins",
            "country": "Vietnam",
            "emailAddress": "martinezelizabeth@yahoo.com",
            "age": 23,
            "birthDate": datetime(2002, 10, 21),
            "phoneNumber": "+84974 506 709 2624",
            "walletBalancePeso": 335.05
        },
        {
            "username": "alawil",
            "password": "116e441972899b04af5550f725835e58c6ee20f1c6e5dcbcead416b61610eb67",
            "customerFirstName": "Julie",
            "customerLastName": "Smith",
            "country": "Cambodia",
            "emailAddress": "charlesbuck@gmail.com",
            "age": 62,
            "birthDate": datetime(1963, 7, 8),
            "phoneNumber": "+855 29 438 9286",
            "walletBalancePeso": 355.87
        },
        {
            "username": "benmor",
            "password": "3d01e4d401f344bb89146aa8132d483dcff13dcf3380bb48f2cf166ab5f95bc0",
            "customerFirstName": "Kelly",
            "customerLastName": "Campos",
            "country": "Indonesia",
            "emailAddress": "hwilliams@hotmail.com",
            "age": 48,
            "birthDate": datetime(1977, 11, 19),
            "phoneNumber": "+62810 640 720 9408",
            "walletBalancePeso": 697.28
        },
        {
            "username": "petgil",
            "password": "584b9acc470612e0a5183bb93db44c9110fd7f6030aedacedb76a36a35ec2b1d",
            "customerFirstName": "John",
            "customerLastName": "Martinez",
            "country": "Malaysia",
            "emailAddress": "joshuaalvarado@yahoo.com",
            "age": 65,
            "birthDate": datetime(1960, 1, 31),
            "phoneNumber": "+60 10 796 894 6850",
            "walletBalancePeso": 813.33
        },
        {
            "username": "donspe",
            "password": "8083d2eaa015ea3ba6955df021d87fbf005ad1e06acc175db1fb2c60f5a71e92",
            "customerFirstName": "Tyler",
            "customerLastName": "Johnson",
            "country": "Indonesia",
            "emailAddress": "jguzman@hotmail.com",
            "age": 57,
            "birthDate": datetime(1968, 6, 7),
            "phoneNumber": "+62810 640 720 9408",
            "walletBalancePeso": 929.30
        },
        {
            "username": "sarmad",
            "password": "ef9d19afa70b41a839b971038607ea78c257f6e8f345c19ff08d3a03837b32ad",
            "customerFirstName": "Curtis",
            "customerLastName": "Baker",
            "country": "Thailand",
            "emailAddress": "ostokes@hotmail.com",
            "age": 42,
            "birthDate": datetime(1983, 2, 5),
            "phoneNumber": "+6630 647 985 5344",
            "walletBalancePeso": 401.43
        },
        {
            "username": "aleell",
            "password": "ea4c971894510518c7a17405e9d7fe523eb49c6e8cba33e6f52bad1d34451476",
            "customerFirstName": "Barbara",
            "customerLastName": "Graham",
            "country": "Myanmar",
            "emailAddress": "jodiramirez@hotmail.com",
            "age": 38,
            "birthDate": datetime(1987, 5, 26),
            "phoneNumber": "+95 65 258 441 3336",
            "walletBalancePeso": 528.17
        },
        {
            "username": "darjon",
            "password": "590b10ac866427b2f9b771271a14cfc004d5837c943dffd531249f8c3b8c8d82",
            "customerFirstName": "Mary",
            "customerLastName": "Nunez",
            "country": "Myanmar",
            "emailAddress": "wardvicki@yahoo.com",
            "age": 21,
            "birthDate": datetime(2004, 7, 23),
            "phoneNumber": "+95 65 258 441 3336",
            "walletBalancePeso": 743.86
        },
        {
            "username": "ricgoo",
            "password": "c002f770311ba30f9ee6d18df1ac8c5c8a76d8008a98460cedaf363d6f493ac4",
            "customerFirstName": "Daniel",
            "customerLastName": "Miller",
            "country": "Vietnam",
            "emailAddress": "creed@yahoo.com",
            "age": 57,
            "birthDate": datetime(1968, 10, 18),
            "phoneNumber": "+84974 506 709 2624",
            "walletBalancePeso": 229.74
        },
        {
            "username": "connor",
            "password": "cc0b8a95a883bc0b5f64a536de42349e0ce0673918a3c446255ddc8354887140",
            "customerFirstName": "James",
            "customerLastName": "Harper",
            "country": "Philippines",
            "emailAddress": "ambergriffith@gmail.com",
            "age": 48,
            "birthDate": datetime(1977, 10, 31),
            "phoneNumber": "+63910 307 702 7488",
            "walletBalancePeso": 986.02
        },
        {
            "username": "searog",
            "password": "088f158c8189633e325777cf5612ccf33a67c652235c1a7705e4db73769fd2fd",
            "customerFirstName": "Samantha",
            "customerLastName": "Hall",
            "country": "Singapore",
            "emailAddress": "mendezcolin@gmail.com",
            "age": 38,
            "birthDate": datetime(1987, 1, 15),
            "phoneNumber": "+65995 331 484 4665",
            "walletBalancePeso": 752.67
        },
        {
            "username": "jamcoh",
            "password": "659f49900580eb42da992f9567d2666f2482be63b19fbc11c78b5066e14acc15",
            "customerFirstName": "Christina",
            "customerLastName": "Woods",
            "country": "Indonesia",
            "emailAddress": "arobertson@gmail.com",
            "age": 46,
            "birthDate": datetime(1979, 4, 20),
            "phoneNumber": "+62810 640 720 9408",
            "walletBalancePeso": 708.92
        },
        {
            "username": "brafis",
            "password": "d83b92b0a9f10dc75053b924230c6d3795e79d6d564bb9f41c0833064e2a46b6",
            "customerFirstName": "Eric",
            "customerLastName": "Moore",
            "country": "Malaysia",
            "emailAddress": "buckleykevin@hotmail.com",
            "age": 30,
            "birthDate": datetime(1995, 8, 7),
            "phoneNumber": "+60 10 796 894 6850",
            "walletBalancePeso": 189.48
        },
        {
            "username": "donlow",
            "password": "1160146c15cb6ea3a43a0ea270e923a85e0dd2db70c43a5b08f21a98ddad41f4",
            "customerFirstName": "Ronald",
            "customerLastName": "Lopez",
            "country": "Indonesia",
            "emailAddress": "amanda46@yahoo.com",
            "age": 36,
            "birthDate": datetime(1989, 10, 15),
            "phoneNumber": "+62810 640 720 9408",
            "walletBalancePeso": 886.39
        },
        {
            "username": "johjoh",
            "password": "95fff048381f4693ab3890d470b0170e7c62dbeaec951af72550f56908b958b2",
            "customerFirstName": "April",
            "customerLastName": "Williams",
            "country": "Thailand",
            "emailAddress": "johndavis@hotmail.com",
            "age": 38,
            "birthDate": datetime(1987, 8, 27),
            "phoneNumber": "+6630 647 985 5344",
            "walletBalancePeso": 153.79
        },
        {
            "username": "ricpar",
            "password": "a64b106ca389a675437b1029ebc2a7e35a2a401df71ad3226f62ca59eda8a615",
            "customerFirstName": "Vickie",
            "customerLastName": "Payne",
            "country": "Cambodia",
            "emailAddress": "perrygary@gmail.com",
            "age": 45,
            "birthDate": datetime(1980, 12, 27),
            "phoneNumber": "+855 29 438 9286",
            "walletBalancePeso": 709.20
        },
        {
            "username": "aliglo",
            "password": "7d5ed12aded0c748c1b0e8cf6b53a227af8260bcde1b783cc660baa765363ddf",
            "customerFirstName": "Anna",
            "customerLastName": "Collins",
            "country": "Malaysia",
            "emailAddress": "ejohnson@gmail.com",
            "age": 38,
            "birthDate": datetime(1987, 10, 10),
            "phoneNumber": "+60 10 796 894 6850",
            "walletBalancePeso": 133.22
        },
        {
            "username": "sheper",
            "password": "1471b56d0ce4089d7df7618bb88147964866d424ba4d683557e970fd0bb88efa",
            "customerFirstName": "Billy",
            "customerLastName": "Graham",
            "country": "Myanmar",
            "emailAddress": "kfisher@hotmail.com",
            "age": 21,
            "birthDate": datetime(2004, 12, 18),
            "phoneNumber": "+95 65 258 441 3336",
            "walletBalancePeso": 53.61
        },
        {
            "username": "antsan",
            "password": "48c2be4c6613f5bfe0d9427db11352d9437235785253032e03d28436f08d3f6b",
            "customerFirstName": "Sean",
            "customerLastName": "Clark",
            "country": "Vietnam",
            "emailAddress": "dawnpreston@gmail.com",
            "age": 53,
            "birthDate": datetime(1972, 7, 11),
            "phoneNumber": "+84974 506 709 2624",
            "walletBalancePeso": 603.21
        },
        {
            "username": "micdix",
            "password": "2d488f7f5dcc66231f1c5c3f1816db959863104319bfa9e9b4b6107dd339c3d6",
            "customerFirstName": "Victoria",
            "customerLastName": "Johnson",
            "country": "Malaysia",
            "emailAddress": "keith77@yahoo.com",
            "age": 28,
            "birthDate": datetime(1997, 4, 27),
            "phoneNumber": "+60 10 796 894 6850",
            "walletBalancePeso": 869.55
        },
        {
            "username": "donvaz",
            "password": "965270270671cce474e1f160f9b801497c56f5521e647de84e05c52ffa1e8f95",
            "customerFirstName": "Joanna",
            "customerLastName": "Campbell",
            "country": "Cambodia",
            "emailAddress": "pageangela@hotmail.com",
            "age": 61,
            "birthDate": datetime(1964, 12, 19),
            "phoneNumber": "+855 29 438 9286",
            "walletBalancePeso": 779.18
        },
        {
            "username": "tylmel",
            "password": "34ccb0ba70484297a347cdf10013559dda5343e8983dd9f50ec40cc035e32a57",
            "customerFirstName": "Joshua",
            "customerLastName": "Lawrence",
            "country": "Thailand",
            "emailAddress": "mckinneyteresa@yahoo.com",
            "age": 33,
            "birthDate": datetime(1992, 1, 3),
            "phoneNumber": "+6630 647 985 5344",
            "walletBalancePeso": 568.10
        },
        {
            "username": "eriash",
            "password": "07a92a6628165a031613f069921157693384ea534a0fe9ab8b1556763f87e872",
            "customerFirstName": "Eric",
            "customerLastName": "Wallace",
            "country": "Malaysia",
            "emailAddress": "englishchristopher@gmail.com",
            "age": 57,
            "birthDate": datetime(1968, 12, 30),
            "phoneNumber": "+60 10 796 894 6850",
            "walletBalancePeso": 284.60
        },
        {
            "username": "heacon",
            "password": "7851768caa1121795e52bed12c5b0c8877080f7154ee8b1b202376bb4b9025cb",
            "customerFirstName": "Vanessa",
            "customerLastName": "Williams",
            "country": "Vietnam",
            "emailAddress": "bernardvictor@gmail.com",
            "age": 38,
            "birthDate": datetime(1987, 2, 22),
            "phoneNumber": "+84974 506 709 2624",
            "walletBalancePeso": 589.28
        },
        {
            "username": "judski",
            "password": "8997ac87ade872a6f89f4442f10f09dfcda98117ba4c958e9267805fa76fecaa",
            "customerFirstName": "Ashley",
            "customerLastName": "Palmer",
            "country": "Cambodia",
            "emailAddress": "scarter@yahoo.com",
            "age": 58,
            "birthDate": datetime(1967, 2, 22),
            "phoneNumber": "+855 29 438 9286",
            "walletBalancePeso": 953.19
        },
        {
            "username": "ricfos",
            "password": "f56107e81ba7468db2f873d39aff10929741cb0cbbfcd2d284cda39df5c9b8ee",
            "customerFirstName": "Adam",
            "customerLastName": "Pacheco",
            "country": "Philippines",
            "emailAddress": "ralph34@hotmail.com",
            "age": 70,
            "birthDate": datetime(1955, 1, 7),
            "phoneNumber": "+63910 307 702 7488",
            "walletBalancePeso": 220.23
        },
        {
            "username": "marsim",
            "password": "12502387be6004c67f13bdd881221f68bb201f7bf8b079d8235d5490e9080074",
            "customerFirstName": "Catherine",
            "customerLastName": "Horton",
            "country": "Vietnam",
            "emailAddress": "iosborn@hotmail.com",
            "age": 36,
            "birthDate": datetime(1989, 4, 12),
            "phoneNumber": "+84974 506 709 2624",
            "walletBalancePeso": 344.60
        },
        {
            "username": "katpea",
            "password": "f63d8c92bfef53595e2208bada64fcaf45c53be6e12db08b6674cc1d145dcc04",
            "customerFirstName": "Lance",
            "customerLastName": "Hodge",
            "country": "Vietnam",
            "emailAddress": "schultzbenjamin@gmail.com",
            "age": 38,
            "birthDate": datetime(1987, 4, 11),
            "phoneNumber": "+84974 506 709 2624",
            "walletBalancePeso": 865.48
        }
    ]


    storeGameInfo = [
        {
            "gameTitle": "Battlefield™ 2042",
            "reviewVerdict": "Mostly Negative",
            "averageRating": 25,
            "originalPricePeso": 0,
            "currentPricePeso": 0,
            "isDiscounted": True,
            "isFree": True,
            "isEarlyAccess": True,
            "currentDiscountPercent": 0,
            "releaseDate": datetime(2004, 6, 2),
            "developer": "DICE",
            "categories": [
                "Multi-player",
                "Co-op",
                "Online Co-op"
            ],
            "description": "Battlefield™ 2042 is a first-person shooter that marks the return to the iconic all-out warfare of t...",
        },
        {
            "gameTitle": "THE FINALS",
            "reviewVerdict": "Mixed",
            "averageRating": 63,
            "originalPricePeso": 3242.13,
            "currentPricePeso": 551.16,
            "isDiscounted": True,
            "isFree": False,
            "isEarlyAccess": True,
            "currentDiscountPercent": 83,
            "releaseDate": datetime(1991, 12, 27),
            "developer": "Embark Studios",
            "categories": [
                "Multi-player",
                "PvP",
                "Online PvP",
                "Co-op",
                "Online Co-op",
                "Cross-Platform Multiplayer"
            ],
            "description": "Join THE FINALS, the world-famous, free-to-play, combat-centered game show! Fight alongside your tea...",
        },
        {
            "gameTitle": "Fallout 4",
            "reviewVerdict": "Mixed",
            "averageRating": 41,
            "originalPricePeso": 4687.82,
            "currentPricePeso": 3375.23,
            "isDiscounted": True,
            "isFree": False,
            "isEarlyAccess": True,
            "currentDiscountPercent": 28,
            "releaseDate": datetime(1914, 9, 27),
            "developer": "Bethesda Game Studios",
            "categories": [
                "Single-player",
                "Multi-player",
                "Co-op",
                "Online Co-op"
            ],
            "description": "Bethesda Game Studios, the award-winning creators of Fallout 3 and The Elder Scrolls V: Skyrim, welc...",
        },
        {
            "gameTitle": "Vampire Survivors",
            "reviewVerdict": "Mixed",
            "averageRating": 60,
            "originalPricePeso": 9601.63,
            "currentPricePeso": 5280.90,
            "isDiscounted": True,
            "isFree": False,
            "isEarlyAccess": False,
            "currentDiscountPercent": 45,
            "releaseDate": datetime(1997, 12, 7),
            "developer": "poncle",
            "categories": [
                "Single-player",
                "Multi-player",
                "Co-op",
                "Online Co-op"
            ],
            "description": "Mow down thousands of night creatures and survive until dawn! Vampire Survivors is a gothic horror c...",
        },
        {
            "gameTitle": "Hearts of Iron IV",
            "reviewVerdict": "Mixed",
            "averageRating": 42,
            "originalPricePeso": 0,
            "currentPricePeso": 0,
            "isDiscounted": True,
            "isFree": True,
            "isEarlyAccess": True,
            "currentDiscountPercent": 0,
            "releaseDate": datetime(1982, 12, 21),
            "developer": "Paradox Development Studio",
            "categories": [
                "Single-player",
                "Multi-player",
                "Co-op",
                "Online Co-op"
            ],
            "description": "Victory is at your fingertips! Your ability to lead your nation is your supreme weapon, the strategy...",
        },
        {
            "gameTitle": "DARK SOULS™ III",
            "reviewVerdict": "Mixed",
            "averageRating": 60,
            "originalPricePeso": 0,
            "currentPricePeso": 0,
            "isDiscounted": True,
            "isFree": True,
            "isEarlyAccess": True,
            "currentDiscountPercent": 0,
            "releaseDate": datetime(2007, 9, 20),
            "developer": "FromSoftware, Inc.",
            "categories": [
                "Single-player",
                "Multi-player",
                "Co-op",
                "Online Co-op"
            ],
            "description": "Dark Souls continues to push the boundaries with the latest, ambitious chapter in the critically-acc...",
        },
        {
            "gameTitle": "Marvel Rivals",
            "reviewVerdict": "Mostly Negative",
            "averageRating": 35,
            "originalPricePeso": 8324.51,
            "currentPricePeso": 249.74,
            "isDiscounted": True,
            "isFree": False,
            "isEarlyAccess": True,
            "currentDiscountPercent": 97,
            "releaseDate": datetime(1926, 12, 13),
            "developer": "NetEase Games",
            "categories": [
                "Multi-player",
                "Co-op",
                "Online Co-op"
            ],
            "description": "Marvel Rivals is a Super Hero Team-Based PVP Shooter! Assemble an all-star Marvel squad, devise coun...",
        },
        {
            "gameTitle": "NARAKA: BLADEPOINT",
            "reviewVerdict": "Positive",
            "averageRating": 78,
            "originalPricePeso": 2703.44,
            "currentPricePeso": 540.69,
            "isDiscounted": True,
            "isFree": False,
            "isEarlyAccess": False,
            "currentDiscountPercent": 80,
            "releaseDate": datetime(2018, 12, 3),
            "developer": "24 Entertainment",
            "categories": [
                "Multi-player",
                "Co-op",
                "Online Co-op"
            ],
            "description": "Dive into the legends of the Far East in NARAKA: BLADEPOINT; team up with friends in fast-paced mele...",
        },
        {
            "gameTitle": "Project Zomboid",
            "reviewVerdict": "Mixed",
            "averageRating": 61,
            "originalPricePeso": 0,
            "currentPricePeso": 0,
            "isDiscounted": True,
            "isFree": True,
            "isEarlyAccess": True,
            "currentDiscountPercent": 0,
            "releaseDate": datetime(1943, 5, 1),
            "developer": "The Indie Stone",
            "categories": [
                "Single-player",
                "Multi-player",
                "Co-op",
                "Online Co-op"
            ],
            "description": "Project Zomboid is the ultimate in zombie survival. Alone or in MP: you loot, build, craft, fight, f...",
        },
        {
            "gameTitle": "Path of Exile",
            "reviewVerdict": "Negative",
            "averageRating": 12,
            "originalPricePeso": 12983.94,
            "currentPricePeso": 12983.94,
            "isDiscounted": False,
            "isFree": False,
            "isEarlyAccess": True,
            "currentDiscountPercent": 0,
            "releaseDate": datetime(1990, 8, 3),
            "developer": "Grinding Gear Games",
            "categories": [
                "Single-player",
                "Multi-player",
                "Co-op",
                "Online Co-op"
            ],
            "description": "You are an Exile, struggling to survive on the dark continent of Wraeclast, as you fight to earn pow...",
        },
        {
            "gameTitle": "New World: Aeternum",
            "reviewVerdict": "Mixed",
            "averageRating": 65,
            "originalPricePeso": 0,
            "currentPricePeso": 0,
            "isDiscounted": True,
            "isFree": True,
            "isEarlyAccess": True,
            "currentDiscountPercent": 0,
            "releaseDate": datetime(1924, 7, 10),
            "developer": "Amazon Games",
            "categories": [
                "Multi-player",
                "Co-op",
                "Online Co-op"
            ],
            "description": "Experience a thrilling action RPG set on the supernatural island of Aeternum. Forge your destiny on ...",
        },
        {
            "gameTitle": "Hogwarts Legacy",
            "reviewVerdict": "Mostly Negative",
            "averageRating": 38,
            "originalPricePeso": 2822.77,
            "currentPricePeso": 2822.77,
            "isDiscounted": False,
            "isFree": False,
            "isEarlyAccess": True,
            "currentDiscountPercent": 0,
            "releaseDate": datetime(2020, 8, 21),
            "developer": "Avalanche Software",
            "categories": [
                "Single-player",
                "Multi-player",
                "Co-op",
                "Online Co-op"
            ],
            "description": "Hogwarts Legacy is an immersive, open-world action RPG. Now you can take control of the action and b...",
        },
        {
            "gameTitle": "People Playground",
            "reviewVerdict": "Negative",
            "averageRating": 4,
            "originalPricePeso": 0,
            "currentPricePeso": 0,
            "isDiscounted": True,
            "isFree": True,
            "isEarlyAccess": False,
            "currentDiscountPercent": 0,
            "releaseDate": datetime(1930, 8, 20),
            "developer": "mestiez",
            "categories": [
                "Single-player",
                "Multi-player",
                "Co-op",
                "Online Co-op"
            ],
            "description": "Shoot, stab, burn, poison, tear, vaporise, or crush ragdolls in a large open space.",
        },
        {
            "gameTitle": "Sid Meier’s Civilization® VI",
            "reviewVerdict": "Mixed",
            "averageRating": 51,
            "originalPricePeso": 0,
            "currentPricePeso": 0,
            "isDiscounted": True,
            "isFree": True,
            "isEarlyAccess": False,
            "currentDiscountPercent": 0,
            "releaseDate": datetime(1920, 1, 2),
            "developer": "Firaxis Games",
            "categories": [
                "Single-player",
                "Multi-player",
                "Co-op",
                "Online Co-op"
            ],
            "description": "Expand your empire, advance your culture and go head-to-head against history’s greatest leaders. Wil...",
        },
        {
            "gameTitle": "7 Days to Die",
            "reviewVerdict": "Mixed",
            "averageRating": 49,
            "originalPricePeso": 0,
            "currentPricePeso": 0,
            "isDiscounted": True,
            "isFree": True,
            "isEarlyAccess": True,
            "currentDiscountPercent": 0,
            "releaseDate": datetime(2022, 10, 4),
            "developer": "The Fun Pimps",
            "categories": [
                "Single-player",
                "Multi-player",
                "Co-op",
                "Online Co-op"
            ],
            "description": "7 Days to Die is an open-world game that is a unique combination of first-person shooter, survival h...",
        },
        {
            "gameTitle": "Deep Rock Galactic",
            "reviewVerdict": "Negative",
            "averageRating": 13,
            "originalPricePeso": 11900.91,
            "currentPricePeso": 1309.10,
            "isDiscounted": True,
            "isFree": False,
            "isEarlyAccess": False,
            "currentDiscountPercent": 89,
            "releaseDate": datetime(1971, 4, 13),
            "developer": "Ghost Ship Games",
            "categories": [
                "Single-player",
                "Multi-player",
                "Co-op",
                "Online Co-op",
                "Steam Achievements"
            ],
            "description": "Deep Rock Galactic is a 1-4 player co-op FPS featuring badass space Dwarves, 100 percent destructible envir...",
        },
        {
            "gameTitle": "VRChat",
            "reviewVerdict": "Mixed",
            "averageRating": 62,
            "originalPricePeso": 9209.67,
            "currentPricePeso": 92.10,
            "isDiscounted": True,
            "isFree": False,
            "isEarlyAccess": True,
            "currentDiscountPercent": 99,
            "releaseDate": datetime(2025, 5, 16),
            "developer": "VRChat Inc.",
            "categories": [
                "Multi-player",
                "Co-op",
                "Online Co-op"
            ],
            "description": "Join our growing community as you explore, play, and help craft the future of social VR. Create worl...",
        },
        {
            "gameTitle": "No Mans Sky",
            "reviewVerdict": "Mostly Negative",
            "averageRating": 22,
            "originalPricePeso": 11097.89,
            "currentPricePeso": 11097.89,
            "isDiscounted": False,
            "isFree": False,
            "isEarlyAccess": True,
            "currentDiscountPercent": 0,
            "releaseDate": datetime(1942, 8, 12),
            "developer": "Hello Games",
            "categories": [
                "Single-player",
                "Multi-player",
                "Co-op",
                "Online Co-op"
            ],
            "description": "No Man's Sky is a game about exploration and survival in an infinite procedurally generated universe...",
        },
        {
            "gameTitle": "Sekiro™: Shadows Die Twice - GOTY Edition",
            "reviewVerdict": "Very Positive",
            "averageRating": 82,
            "originalPricePeso": 0,
            "currentPricePeso": 0,
            "isDiscounted": True,
            "isFree": True,
            "isEarlyAccess": False,
            "currentDiscountPercent": 0,
            "releaseDate": datetime(2003, 9, 5),
            "developer": "FromSoftware, Inc.",
            "categories": [
                "Single-player",
                "Multi-player",
                "Co-op",
                "Online Co-op"
            ],
            "description": "Game of the Year - The Game Awards 2019 Best Action Game of 2019 - IGN Carve your own clever path to...",
        },
        {
            "gameTitle": "Undertale",
            "reviewVerdict": "Mixed",
            "averageRating": 54,
            "originalPricePeso": 0,
            "currentPricePeso": 0,
            "isDiscounted": True,
            "isFree": True,
            "isEarlyAccess": True,
            "currentDiscountPercent": 0,
            "releaseDate": datetime(1992, 2, 21),
            "developer": "tobyfox",
            "categories": [
                "Single-player",
                "Multi-player",
                "Co-op",
                "Online Co-op"
            ],
            "description": "UNDERTALE! The RPG game where you don't have to destroy anyone.",
        },
        {
            "gameTitle": "Hades",
            "reviewVerdict": "Negative",
            "averageRating": 17,
            "originalPricePeso": 11751.00,
            "currentPricePeso": 9400.80,
            "isDiscounted": True,
            "isFree": False,
            "isEarlyAccess": True,
            "currentDiscountPercent": 20,
            "releaseDate": datetime(2018, 3, 17),
            "developer": "Supergiant Games",
            "categories": [
                "Single-player",
                "Multi-player",
                "Co-op",
                "Online Co-op"
            ],
            "description": "Defy the god of the dead as you hack and slash out of the Underworld in this rogue-like dungeon craw...",
        }
    ]

    ownedGameInfo = [
        {
            "ownerUsername": "statuc",
            "owner_id": "*****",
            "gameTitle": "Battlefield™ 2042",
            "game_id": "*****",
            "licenseID": "bf2042-key-83749201",
            "hoursPlayed": 12.5,
            "spaceRequiredGB": 92.4,
            "isInstalled": True,
            "datePurchased": datetime(2025, 11, 19)
        },
        {
            "ownerUsername": "statuc",
            "owner_id": "*****",
            "gameTitle": "THE FINALS",
            "game_id": "*****",
            "licenseID": "finals-key-gen-102938",
            "hoursPlayed": 14.2,
            "spaceRequiredGB": 18.5,
            "isInstalled": True,
            "datePurchased": datetime(2025, 11, 19)
        },
        {
            "ownerUsername": "statuc",
            "owner_id": "*****",
            "gameTitle": "Fallout 4",
            "game_id": "*****",
            "licenseID": "fo4-key-gen-47582910",
            "hoursPlayed": 5.5,
            "spaceRequiredGB": 35.8,
            "isInstalled": True,
            "datePurchased": datetime(2025, 11, 19)
        },
        {
            "ownerUsername": "statuc",
            "owner_id": "*****",
            "gameTitle": "Hades",
            "game_id": "*****",
            "licenseID": "hades-key-gen-55667788",
            "hoursPlayed": 32.8,
            "spaceRequiredGB": 15.6,
            "isInstalled": True,
            "datePurchased": datetime(2025, 10, 12)
        },
        {
            "ownerUsername": "statuc",
            "owner_id": "*****",
            "gameTitle": "Undertale",
            "game_id": "*****",
            "licenseID": "und-key-gen-99887766",
            "hoursPlayed": 8.9,
            "spaceRequiredGB": 0.3,
            "isInstalled": True,
            "datePurchased": datetime(2025, 10, 12)
        },
        {
            "ownerUsername": "sabcol",
            "owner_id": "*****",
            "gameTitle": "THE FINALS",
            "game_id": "*****",
            "licenseID": "finals-lic-29384756",
            "hoursPlayed": 64.2,
            "spaceRequiredGB": 18.5,
            "isInstalled": True,
            "datePurchased": datetime(2025, 12, 10)
        },
        {
            "ownerUsername": "sabcol",
            "owner_id": "*****",
            "gameTitle": "Battlefield™ 2042",
            "game_id": "*****",
            "licenseID": "bf2042-key-gen-44332211",
            "hoursPlayed": 1.2,
            "spaceRequiredGB": 92.4,
            "isInstalled": True,
            "datePurchased": datetime(2025, 12, 10)
        },
        {
            "ownerUsername": "sabcol",
            "owner_id": "*****",
            "gameTitle": "Hearts of Iron IV",
            "game_id": "*****",
            "licenseID": "hoi4-key-gen-55661122",
            "hoursPlayed": 150.5,
            "spaceRequiredGB": 4.5,
            "isInstalled": True,
            "datePurchased": datetime(2025, 12, 10)
        },
        {
            "ownerUsername": "ronwri",
            "owner_id": "*****",
            "gameTitle": "Fallout 4",
            "game_id": "*****",
            "licenseID": "fo4-goty-10293847",
            "hoursPlayed": 240.5,
            "spaceRequiredGB": 35.8,
            "isInstalled": True,
            "datePurchased": datetime(2025, 10, 6)
        },
        {
            "ownerUsername": "ronwri",
            "owner_id": "*****",
            "gameTitle": "NARAKA: BLADEPOINT",
            "game_id": "*****",
            "licenseID": "narak-key-gen-77889900",
            "hoursPlayed": 45.6,
            "spaceRequiredGB": 32.1,
            "isInstalled": True,
            "datePurchased": datetime(2025, 10, 6)
        },
        {
            "ownerUsername": "ronwri",
            "owner_id": "*****",
            "gameTitle": "Path of Exile",
            "game_id": "*****",
            "licenseID": "poe-key-gen-11223344",
            "hoursPlayed": 210.4,
            "spaceRequiredGB": 40.0,
            "isInstalled": True,
            "datePurchased": datetime(2025, 10, 6)
        },
        {
            "ownerUsername": "bobpar",
            "owner_id": "*****",
            "gameTitle": "Hearts of Iron IV",
            "game_id": "*****",
            "licenseID": "hoi4-gen-56473829",
            "hoursPlayed": 512.9,
            "spaceRequiredGB": 4.5,
            "isInstalled": True,
            "datePurchased": datetime(2025, 6, 6)
        },
        {
            "ownerUsername": "bobpar",
            "owner_id": "*****",
            "gameTitle": "Marvel Rivals",
            "game_id": "*****",
            "licenseID": "mr-key-gen-66554433",
            "hoursPlayed": 5.5,
            "spaceRequiredGB": 25.0,
            "isInstalled": True,
            "datePurchased": datetime(2025, 6, 6)
        },
        {
            "ownerUsername": "bobpar",
            "owner_id": "*****",
            "gameTitle": "NARAKA: BLADEPOINT",
            "game_id": "*****",
            "licenseID": "narak-key-gen-99887711",
            "hoursPlayed": 22.1,
            "spaceRequiredGB": 32.1,
            "isInstalled": True,
            "datePurchased": datetime(2025, 6, 6)
        },
        {
            "ownerUsername": "hanols",
            "owner_id": "*****",
            "gameTitle": "Marvel Rivals",
            "game_id": "*****",
            "licenseID": "mr-beta-99887766",
            "hoursPlayed": 8.1,
            "spaceRequiredGB": 25.0,
            "isInstalled": True,
            "datePurchased": datetime(2025, 1, 15)
        },
        {
            "ownerUsername": "hanols",
            "owner_id": "*****",
            "gameTitle": "Sid Meier’s Civilization® VI",
            "game_id": "*****",
            "licenseID": "civ6-key-gen-22334455",
            "hoursPlayed": 88.2,
            "spaceRequiredGB": 12.0,
            "isInstalled": True,
            "datePurchased": datetime(2025, 1, 15)
        },
        {
            "ownerUsername": "hanols",
            "owner_id": "*****",
            "gameTitle": "7 Days to Die",
            "game_id": "*****",
            "licenseID": "7dtd-key-gen-11223344",
            "hoursPlayed": 14.3,
            "spaceRequiredGB": 15.0,
            "isInstalled": True,
            "datePurchased": datetime(2025, 1, 15)
        },
        {
            "ownerUsername": "liswea",
            "owner_id": "*****",
            "gameTitle": "Project Zomboid",
            "game_id": "*****",
            "licenseID": "pz-surv-11223344",
            "hoursPlayed": 150.3,
            "spaceRequiredGB": 3.2,
            "isInstalled": True,
            "datePurchased": datetime(2022, 3, 14)
        },
        {
            "ownerUsername": "liswea",
            "owner_id": "*****",
            "gameTitle": "No Mans Sky",
            "game_id": "*****",
            "licenseID": "nms-key-gen-88776655",
            "hoursPlayed": 66.7,
            "spaceRequiredGB": 14.3,
            "isInstalled": True,
            "datePurchased": datetime(2022, 3, 14)
        },
        {
            "ownerUsername": "kailam",
            "owner_id": "*****",
            "gameTitle": "Deep Rock Galactic",
            "game_id": "*****",
            "licenseID": "drg-rock-55667788",
            "hoursPlayed": 13.0,
            "spaceRequiredGB": 3.5,
            "isInstalled": True,
            "datePurchased": datetime(2021, 9, 9)
        },
        {
            "ownerUsername": "kailam",
            "owner_id": "*****",
            "gameTitle": "Sekiro™: Shadows Die Twice - GOTY Edition",
            "game_id": "*****",
            "licenseID": "sek-key-gen-99001122",
            "hoursPlayed": 2.5,
            "spaceRequiredGB": 25.0,
            "isInstalled": True,
            "datePurchased": datetime(2021, 9, 9)
        },
        {
            "ownerUsername": "eridaw",
            "owner_id": "*****",
            "gameTitle": "Path of Exile",
            "game_id": "*****",
            "licenseID": "poe-free-00000001",
            "hoursPlayed": 4.2,
            "spaceRequiredGB": 40.0,
            "isInstalled": True,
            "datePurchased": datetime(2020, 8, 20)
        },
        {
            "ownerUsername": "eridaw",
            "owner_id": "*****",
            "gameTitle": "Deep Rock Galactic",
            "game_id": "*****",
            "licenseID": "drg-key-gen-44556677",
            "hoursPlayed": 105.0,
            "spaceRequiredGB": 3.5,
            "isInstalled": True,
            "datePurchased": datetime(2020, 8, 20)
        },
        {
            "ownerUsername": "samgon",
            "owner_id": "*****",
            "gameTitle": "Hogwarts Legacy",
            "game_id": "*****",
            "licenseID": "hl-wiza-44332211",
            "hoursPlayed": 25.6,
            "spaceRequiredGB": 85.0,
            "isInstalled": True,
            "datePurchased": datetime(2023, 2, 10)
        },
        {
            "ownerUsername": "samgon",
            "owner_id": "*****",
            "gameTitle": "Sid Meier’s Civilization® VI",
            "game_id": "*****",
            "licenseID": "civ6-key-gen-11223399",
            "hoursPlayed": 30.0,
            "spaceRequiredGB": 12.0,
            "isInstalled": True,
            "datePurchased": datetime(2023, 2, 10)
        },
        {
            "ownerUsername": "nannel",
            "owner_id": "*****",
            "gameTitle": "People Playground",
            "game_id": "*****",
            "licenseID": "pp-doll-77665544",
            "hoursPlayed": 2.1,
            "spaceRequiredGB": 0.8,
            "isInstalled": True,
            "datePurchased": datetime(2021, 5, 5)
        },
        {
            "ownerUsername": "nannel",
            "owner_id": "*****",
            "gameTitle": "New World: Aeternum",
            "game_id": "*****",
            "licenseID": "nw-key-gen-88552233",
            "hoursPlayed": 0.4,
            "spaceRequiredGB": 50.5,
            "isInstalled": True,
            "datePurchased": datetime(2021, 5, 5)
        },
        {
            "ownerUsername": "chrmit",
            "owner_id": "*****",
            "gameTitle": "Sid Meier’s Civilization® VI",
            "game_id": "*****",
            "licenseID": "civ6-gold-22114433",
            "hoursPlayed": 340.9,
            "spaceRequiredGB": 12.0,
            "isInstalled": True,
            "datePurchased": datetime(2017, 12, 25)
        },
        {
            "ownerUsername": "chrmit",
            "owner_id": "*****",
            "gameTitle": "Hogwarts Legacy",
            "game_id": "*****",
            "licenseID": "hl-key-gen-55443322",
            "hoursPlayed": 42.0,
            "spaceRequiredGB": 85.0,
            "isInstalled": True,
            "datePurchased": datetime(2017, 12, 25)
        },
        {
            "ownerUsername": "clapen",
            "owner_id": "*****",
            "gameTitle": "7 Days to Die",
            "game_id": "*****",
            "licenseID": "7dtd-key-99882233",
            "hoursPlayed": 99.5,
            "spaceRequiredGB": 15.0,
            "isInstalled": True,
            "datePurchased": datetime(2019, 10, 11)
        },
        {
            "ownerUsername": "clapen",
            "owner_id": "*****",
            "gameTitle": "NARAKA: BLADEPOINT",
            "game_id": "*****",
            "licenseID": "narak-key-gen-11559900",
            "hoursPlayed": 18.9,
            "spaceRequiredGB": 32.1,
            "isInstalled": True,
            "datePurchased": datetime(2019, 10, 11)
        },
        {
            "ownerUsername": "alerom",
            "owner_id": "*****",
            "gameTitle": "VRChat",
            "game_id": "*****",
            "licenseID": "vrc-meta-55443322",
            "hoursPlayed": 1200.2,
            "spaceRequiredGB": 20.5,
            "isInstalled": True,
            "datePurchased": datetime(2020, 3, 20)
        },
        {
            "ownerUsername": "alerom",
            "owner_id": "*****",
            "gameTitle": "Sid Meier’s Civilization® VI",
            "game_id": "*****",
            "licenseID": "civ6-key-gen-77441122",
            "hoursPlayed": 400.1,
            "spaceRequiredGB": 12.0,
            "isInstalled": True,
            "datePurchased": datetime(2020, 3, 20)
        },
        {
            "ownerUsername": "paubre",
            "owner_id": "*****",
            "gameTitle": "No Mans Sky",
            "game_id": "*****",
            "licenseID": "nms-space-11992288",
            "hoursPlayed": 18.4,
            "spaceRequiredGB": 14.3,
            "isInstalled": True,
            "datePurchased": datetime(2016, 8, 12)
        },
        {
            "ownerUsername": "karhow",
            "owner_id": "*****",
            "gameTitle": "Sekiro™: Shadows Die Twice - GOTY Edition",
            "game_id": "*****",
            "licenseID": "sek-goty-77338822",
            "hoursPlayed": 75.0,
            "spaceRequiredGB": 25.0,
            "isInstalled": True,
            "datePurchased": datetime(2020, 11, 28)
        },
        {
            "ownerUsername": "jesfle",
            "owner_id": "*****",
            "gameTitle": "Undertale",
            "game_id": "*****",
            "licenseID": "und-soul-44556677",
            "hoursPlayed": 10.5,
            "spaceRequiredGB": 0.3,
            "isInstalled": True,
            "datePurchased": datetime(2016, 1, 15)
        },
        {
            "ownerUsername": "walwal",
            "owner_id": "*****",
            "gameTitle": "Hades",
            "game_id": "*****",
            "licenseID": "hades-hell-99118822",
            "hoursPlayed": 5.2,
            "spaceRequiredGB": 15.6,
            "isInstalled": True,
            "datePurchased": datetime(2021, 6, 20)
        },
        {
            "ownerUsername": "paujoh",
            "owner_id": "*****",
            "gameTitle": "Vampire Survivors",
            "game_id": "*****",
            "licenseID": "vs-garlic-33221100",
            "hoursPlayed": 80.1,
            "spaceRequiredGB": 0.6,
            "isInstalled": True,
            "datePurchased": datetime(2025, 10, 17)
        },
        {
            "ownerUsername": "whimur",
            "owner_id": "*****",
            "gameTitle": "DARK SOULS™ III",
            "game_id": "*****",
            "licenseID": "ds3-fire-55005500",
            "hoursPlayed": 110.8,
            "spaceRequiredGB": 25.0,
            "isInstalled": True,
            "datePurchased": datetime(2017, 4, 15)
        },
        {
            "ownerUsername": "rachic",
            "owner_id": "*****",
            "gameTitle": "New World: Aeternum",
            "game_id": "*****",
            "licenseID": "nw-mmo-22883377",
            "hoursPlayed": 45.0,
            "spaceRequiredGB": 50.5,
            "isInstalled": True,
            "datePurchased": datetime(2021, 9, 28)
        },
        {
            "ownerUsername": "alerya",
            "owner_id": "*****",
            "gameTitle": "Battlefield™ 2042",
            "game_id": "*****",
            "licenseID": "bf2042-key-11229988",
            "hoursPlayed": 20.2,
            "spaceRequiredGB": 92.4,
            "isInstalled": True,
            "datePurchased": datetime(2022, 12, 25)
        },
        {
            "ownerUsername": "pauest",
            "owner_id": "*****",
            "gameTitle": "THE FINALS",
            "game_id": "*****",
            "licenseID": "finals-lic-77441122",
            "hoursPlayed": 150.9,
            "spaceRequiredGB": 18.5,
            "isInstalled": True,
            "datePurchased": datetime(2024, 1, 1)
        },
        {
            "ownerUsername": "alawil",
            "owner_id": "*****",
            "gameTitle": "Fallout 4",
            "game_id": "*****",
            "licenseID": "fo4-key-33669922",
            "hoursPlayed": 60.5,
            "spaceRequiredGB": 35.8,
            "isInstalled": True,
            "datePurchased": datetime(2019, 2, 14)
        },
        {
            "ownerUsername": "benmor",
            "owner_id": "*****",
            "gameTitle": "Marvel Rivals",
            "game_id": "*****",
            "licenseID": "mr-key-44885522",
            "hoursPlayed": 6.0,
            "spaceRequiredGB": 25.0,
            "isInstalled": True,
            "datePurchased": datetime(2025, 2, 20)
        },
        {
            "ownerUsername": "petgil",
            "owner_id": "*****",
            "gameTitle": "Project Zomboid",
            "game_id": "*****",
            "licenseID": "pz-key-11002299",
            "hoursPlayed": 300.2,
            "spaceRequiredGB": 3.2,
            "isInstalled": True,
            "datePurchased": datetime(2021, 8, 15)
        },
        {
            "ownerUsername": "donspe",
            "owner_id": "*****",
            "gameTitle": "Deep Rock Galactic",
            "game_id": "*****",
            "licenseID": "drg-key-55884411",
            "hoursPlayed": 3.5,
            "spaceRequiredGB": 3.5,
            "isInstalled": True,
            "datePurchased": datetime(2023, 5, 5)
        },
        {
            "ownerUsername": "aleell",
            "owner_id": "*****",
            "gameTitle": "Path of Exile",
            "game_id": "*****",
            "licenseID": "poe-key-77441155",
            "hoursPlayed": 15.0,
            "spaceRequiredGB": 40.0,
            "isInstalled": True,
            "datePurchased": datetime(2025, 10, 14)
        },
        {
            "ownerUsername": "darjon",
            "owner_id": "*****",
            "gameTitle": "Path of Exile",
            "game_id": "*****",
            "licenseID": "poe-key-gen-55663322",
            "hoursPlayed": 12.8,
            "spaceRequiredGB": 40.0,
            "isInstalled": True,
            "datePurchased": datetime(2025, 4, 22)
        },
        {
            "ownerUsername": "ricgoo",
            "owner_id": "*****",
            "gameTitle": "Hearts of Iron IV",
            "game_id": "*****",
            "licenseID": "hoi4-key-11447788",
            "hoursPlayed": 40.5,
            "spaceRequiredGB": 4.5,
            "isInstalled": True,
            "datePurchased": datetime(2020, 5, 9)
        },
        {
            "ownerUsername": "connor",
            "owner_id": "*****",
            "gameTitle": "Hogwarts Legacy",
            "game_id": "*****",
            "licenseID": "hl-key-22558899",
            "hoursPlayed": 60.0,
            "spaceRequiredGB": 85.0,
            "isInstalled": True,
            "datePurchased": datetime(2025, 3, 15)
        }
    ]

    gameReviews = [
        {
            "gameTitle": "Battlefield™ 2042",
            "game_id": "*****",
            "authorUsername": "statuc",
            "author_id": "*****",
            "isRecommended": False,
            "reviewDescription": "DICE really dropped the ball here. The maps feel empty and the specialist system ruins the class identity Battlefield is known for. Even after updates, it just doesn't feel right.",
            "reviewVisibility": "Public",
            "datePosted": datetime(2025, 11, 25),
            "userPlaytimeHours": 12.5
        },
        {
            "gameTitle": "THE FINALS",
            "game_id": "*****",
            "authorUsername": "sabcol",
            "author_id": "*****",
            "isRecommended": True,
            "reviewDescription": "Chaotic fun! The destruction mechanics are insane. Playing with friends in Thailand servers is smooth, but solo queue can be frustrating.",
            "reviewVisibility": "Public",
            "datePosted": datetime(2025, 12, 20),
            "userPlaytimeHours": 64.2
        },
        {
            "gameTitle": "Fallout 4",
            "game_id": "*****",
            "authorUsername": "ronwri",
            "author_id": "*****",
            "isRecommended": True,
            "reviewDescription": "The base game is okay, but the modding community carries this title. Settlement building is addictive once you get the hang of it.",
            "reviewVisibility": "Public",
            "datePosted": datetime(2025, 10, 20),
            "userPlaytimeHours": 240.5
        },
        {
            "gameTitle": "Hearts of Iron IV",
            "game_id": "*****",
            "authorUsername": "bobpar",
            "author_id": "*****",
            "isRecommended": True,
            "reviewDescription": "Steep learning curve but incredibly rewarding. I've spent 500 hours just trying to conquer Asia as a minor nation.",
            "reviewVisibility": "Public",
            "datePosted": datetime(2025, 7, 10),
            "userPlaytimeHours": 512.9
        },
        {
            "gameTitle": "Marvel Rivals",
            "game_id": "*****",
            "authorUsername": "hanols",
            "author_id": "*****",
            "isRecommended": False,
            "reviewDescription": "NetEase needs to fix the balancing. Some heroes are instant wins while others are useless. Not worth the grind in its current state.",
            "reviewVisibility": "Public",
            "datePosted": datetime(2025, 11, 5),
            "userPlaytimeHours": 8.1
        },
        {
            "gameTitle": "Project Zomboid",
            "game_id": "*****",
            "authorUsername": "liswea",
            "author_id": "*****",
            "isRecommended": True,
            "reviewDescription": "This is how you died. Best zombie survival simulator ever made. I died because I ate burnt toast. 10/10.",
            "reviewVisibility": "Public",
            "datePosted": datetime(2025, 6, 22),
            "userPlaytimeHours": 150.3
        },
        {
            "gameTitle": "Deep Rock Galactic",
            "game_id": "*****",
            "authorUsername": "kailam",
            "author_id": "*****",
            "isRecommended": False,
            "reviewDescription": "The grind is too repetitive for me. I wanted to like the dwarves, but the mission variety just isn't there after the first 10 hours.",
            "reviewVisibility": "Public",
            "datePosted": datetime(2025, 2, 18),
            "userPlaytimeHours": 13.0
        },
        {
            "gameTitle": "NARAKA: BLADEPOINT",
            "game_id": "*****",
            "authorUsername": "ronwri",
            "author_id": "*****",
            "isRecommended": True,
            "reviewDescription": "Combat is fluid and fast. The grappling hook mechanics add so much verticality to the fights. Ping is great in Singapore region.",
            "reviewVisibility": "Public",
            "datePosted": datetime(2025, 11, 7),
            "userPlaytimeHours": 45.6
        },
        {
            "gameTitle": "Path of Exile",
            "game_id": "*****",
            "authorUsername": "eridaw",
            "author_id": "*****",
            "isRecommended": False,
            "reviewDescription": "Too complex for a casual player. The skill tree gives me a headache and the trading system is archaic.",
            "reviewVisibility": "Public",
            "datePosted": datetime(2025, 10, 12),
            "userPlaytimeHours": 4.2
        },
        {
            "gameTitle": "Hogwarts Legacy",
            "game_id": "*****",
            "authorUsername": "samgon",
            "author_id": "*****",
            "isRecommended": False,
            "reviewDescription": "Beautiful world, boring gameplay. Once you explore the castle, the open world feels generic and repetitive.",
            "reviewVisibility": "Public",
            "datePosted": datetime(2025, 4, 30),
            "userPlaytimeHours": 25.6
        },
        {
            "gameTitle": "People Playground",
            "game_id": "*****",
            "authorUsername": "nannel",
            "author_id": "*****",
            "isRecommended": False,
            "reviewDescription": "It's just a gore sandbox. Gets boring after you've blown up a ragdoll for the 50th time.",
            "reviewVisibility": "Public",
            "datePosted": datetime(2025, 1, 5),
            "userPlaytimeHours": 2.1
        },
        {
            "gameTitle": "Sid Meier’s Civilization® VI",
            "game_id": "*****",
            "authorUsername": "chrmit",
            "author_id": "*****",
            "isRecommended": True,
            "reviewDescription": "Just one more turn... and suddenly it's 4 AM. playing as the Philippines mod adds nice flavor.",
            "reviewVisibility": "Public",
            "datePosted": datetime(2025, 11, 20),
            "userPlaytimeHours": 340.9
        },
        {
            "gameTitle": "7 Days to Die",
            "game_id": "*****",
            "authorUsername": "clapen",
            "author_id": "*****",
            "isRecommended": True,
            "reviewDescription": "Janky as hell but incredibly fun with friends. Building a base to survive the horde night is a rush.",
            "reviewVisibility": "Public",
            "datePosted": datetime(2025, 8, 8),
            "userPlaytimeHours": 99.5
        },
        {
            "gameTitle": "VRChat",
            "game_id": "*****",
            "authorUsername": "alerom",
            "author_id": "*****",
            "isRecommended": True,
            "reviewDescription": "I don't even have a VR headset and I've met some of my best friends here. The community creates amazing worlds.",
            "reviewVisibility": "Public",
            "datePosted": datetime(2025, 9, 15),
            "userPlaytimeHours": 1200.2
        },
        {
            "gameTitle": "No Mans Sky",
            "game_id": "*****",
            "authorUsername": "paubre",
            "author_id": "*****",
            "isRecommended": False,
            "reviewDescription": "Wide as an ocean, deep as a puddle. Procedural generation makes everything look the same after a while.",
            "reviewVisibility": "Public",
            "datePosted": datetime(2025, 5, 22),
            "userPlaytimeHours": 18.4
        },
        {
            "gameTitle": "Sekiro™: Shadows Die Twice - GOTY Edition",
            "game_id": "*****",
            "authorUsername": "karhow",
            "author_id": "*****",
            "isRecommended": True,
            "reviewDescription": "Hesitation is defeat. Best combat system FromSoftware has ever made. Hard, but fair.",
            "reviewVisibility": "Public",
            "datePosted": datetime(2025, 12, 1),
            "userPlaytimeHours": 75.0
        },
        {
            "gameTitle": "Undertale",
            "game_id": "*****",
            "authorUsername": "jesfle",
            "author_id": "*****",
            "isRecommended": True,
            "reviewDescription": "A masterpiece. The music, the story, the characters—everything is perfect. Stay filled with determination!",
            "reviewVisibility": "Public",
            "datePosted": datetime(2025, 2, 14),
            "userPlaytimeHours": 10.5
        },
        {
            "gameTitle": "Hades",
            "game_id": "*****",
            "authorUsername": "walwal",
            "author_id": "*****",
            "isRecommended": False,
            "reviewDescription": "Too much button mashing for my taste. My hands hurt after an hour of playing this.",
            "reviewVisibility": "Public",
            "datePosted": datetime(2025, 7, 19),
            "userPlaytimeHours": 5.2
        },
        {
            "gameTitle": "Vampire Survivors",
            "game_id": "*****",
            "authorUsername": "paujoh",
            "author_id": "*****",
            "isRecommended": True,
            "reviewDescription": "Cheap price for hundreds of hours of dopamine hits. It runs great on my laptop too.",
            "reviewVisibility": "Public",
            "datePosted": datetime(2025, 10, 31),
            "userPlaytimeHours": 80.1
        },
        {
            "gameTitle": "DARK SOULS™ III",
            "game_id": "*****",
            "authorUsername": "whimur",
            "author_id": "*****",
            "isRecommended": True,
            "reviewDescription": "The atmosphere in this game is unmatched. The boss fights are epic, though the swamp area is annoying.",
            "reviewVisibility": "Public",
            "datePosted": datetime(2025, 6, 5),
            "userPlaytimeHours": 110.8
        },
        {
            "gameTitle": "New World: Aeternum",
            "game_id": "*****",
            "authorUsername": "rachic",
            "author_id": "*****",
            "isRecommended": False,
            "reviewDescription": "Amazon needs to fix the economy. Crafting feels useless and the quests are just fetch quests.",
            "reviewVisibility": "Public",
            "datePosted": datetime(2025, 3, 28),
            "userPlaytimeHours": 45.0
        },
        {
            "gameTitle": "Battlefield™ 2042",
            "game_id": "*****",
            "authorUsername": "alerya",
            "author_id": "*****",
            "isRecommended": False,
            "reviewDescription": "Still buggy in 2025? Come on DICE. The hit registration is awful on Asian servers.",
            "reviewVisibility": "Public",
            "datePosted": datetime(2025, 9, 2),
            "userPlaytimeHours": 20.2
        },
        {
            "gameTitle": "THE FINALS",
            "game_id": "*****",
            "authorUsername": "pauest",
            "author_id": "*****",
            "isRecommended": True,
            "reviewDescription": "Best FPS out right now. The movement speed and strategy required make every match feel unique.",
            "reviewVisibility": "Public",
            "datePosted": datetime(2025, 11, 15),
            "userPlaytimeHours": 150.9
        },
        {
            "gameTitle": "Fallout 4",
            "game_id": "*****",
            "authorUsername": "alawil",
            "author_id": "*****",
            "isRecommended": False,
            "reviewDescription": "Story is weak compared to New Vegas. The dialogue options are too limited—basically just Yes, No, Sarcastic, Later.",
            "reviewVisibility": "Public",
            "datePosted": datetime(2025, 4, 12),
            "userPlaytimeHours": 60.5
        },
        {
            "gameTitle": "Marvel Rivals",
            "game_id": "*****",
            "authorUsername": "benmor",
            "author_id": "*****",
            "isRecommended": False,
            "reviewDescription": "Feels like an Overwatch clone but with worse optimization. FPS drops constantly.",
            "reviewVisibility": "Public",
            "datePosted": datetime(2025, 10, 25),
            "userPlaytimeHours": 6.0
        },
        {
            "gameTitle": "Project Zomboid",
            "game_id": "*****",
            "authorUsername": "petgil",
            "author_id": "*****",
            "isRecommended": True,
            "reviewDescription": "Hardcore survival at its finest. Playing multiplayer with friends in Malaysia is a blast.",
            "reviewVisibility": "Public",
            "datePosted": datetime(2025, 1, 20),
            "userPlaytimeHours": 300.2
        },
        {
            "gameTitle": "Deep Rock Galactic",
            "game_id": "*****",
            "authorUsername": "donspe",
            "author_id": "*****",
            "isRecommended": False,
            "reviewDescription": "The community is toxic. Got kicked from a lobby just for being a new player.",
            "reviewVisibility": "Public",
            "datePosted": datetime(2025, 8, 30),
            "userPlaytimeHours": 3.5
        },
        {
            "gameTitle": "NARAKA: BLADEPOINT",
            "game_id": "*****",
            "authorUsername": "clapen",
            "author_id": "*****",
            "isRecommended": True,
            "reviewDescription": "Finally a Battle Royale that focuses on melee! The character customization is top tier.",
            "reviewVisibility": "Public",
            "datePosted": datetime(2025, 7, 22),
            "userPlaytimeHours": 18.9
        },
        {
            "gameTitle": "Path of Exile",
            "game_id": "*****",
            "authorUsername": "aleell",
            "author_id": "*****",
            "isRecommended": False,
            "reviewDescription": "Desync issues make this unplayable on my connection in Myanmar. Rubberbanding everywhere.",
            "reviewVisibility": "Public",
            "datePosted": datetime(2025, 11, 5),
            "userPlaytimeHours": 15.0
        },
        {
            "gameTitle": "Hades",
            "game_id": "*****",
            "authorUsername": "statuc",
            "author_id": "*****",
            "isRecommended": False,
            "reviewDescription": "Rogue-likes aren't for me. I hate losing progress every time I die. The art is nice though.",
            "reviewVisibility": "Public",
            "datePosted": datetime(2025, 11, 18),
            "userPlaytimeHours": 32.8
        }
    ]

    transactionsBuy = [
        {
            "customerUsername" : "statuc",
            "customer_id" : "*****",
            "transactionDate" : datetime(2025,11,19),
            "isRefund" : False,
            "subtotal" : 3926.39,
            "lineItems" : [
                {
                    "gameTitle" : "Battlefield™ 2042",
                    "game_id" : "*****",
                    "purchasePricePeso" : 0,
                    "isDiscounted" : True
                },
                {
                    "gameTitle" : "THE FINALS",
                    "game_id" : "*****",
                    "purchasePricePeso" : 551.16,
                    "isDiscounted" : True
                },
                {
                    "gameTitle" : "Fallout 4",
                    "game_id" : "*****",
                    "purchasePricePeso" : 3375.23,
                    "isDiscounted" : True
                }
            ]
        },
        {
            "customerUsername" : "sabcol",
            "customer_id" : "*****",
            "transactionDate" : datetime(2025,12,10),
            "isRefund" : False,
            "subtotal" : 551.16,
            "lineItems" : [
                {
                    "gameTitle" : "Battlefield™ 2042",
                    "game_id" : "*****",
                    "purchasePricePeso" : 0,
                    "isDiscounted" : True
                },
                {
                    "gameTitle" : "THE FINALS",
                    "game_id" : "*****",
                    "purchasePricePeso" : 551.16,
                    "isDiscounted" : True
                },
                {
                    "gameTitle" : "Hearts of Iron IV",
                    "game_id" : "*****",
                    "purchasePricePeso" : 0,
                    "isDiscounted" : True
                }
            ]
        },
        {
            "customerUsername" : "ronwri",
            "customer_id" : "*****",
            "transactionDate" : datetime(2025,10,6),
            "isRefund" : False,
            "subtotal" : 16899.86,
            "lineItems" : [
                {
                    "gameTitle" : "NARAKA: BLADEPOINT",
                    "game_id" : "*****",
                    "purchasePricePeso" : 540.69,
                    "isDiscounted" : True
                },
                {
                    "gameTitle" : "Fallout 4",
                    "game_id" : "*****",
                    "purchasePricePeso" : 3375.23,
                    "isDiscounted" : True
                },
                {
                    "gameTitle" : "Path of Exile",
                    "game_id" : "*****",
                    "purchasePricePeso" : 12983.94,
                    "isDiscounted" : False
                }
            ]
        },
        {
            "customerUsername" : "bobpar",
            "customer_id" : "*****",
            "transactionDate" : datetime(2025,6, 6),
            "isRefund" : False,
            "subtotal" : 790.42,
            "lineItems" : [
                {
                    "gameTitle" : "Marvel Rivals",
                    "game_id" : "*****",
                    "purchasePricePeso" : 249.74,
                    "isDiscounted" : True
                },
                {
                    "gameTitle" : "Hearts of Iron IV",
                    "game_id" : "*****",
                    "purchasePricePeso" : 0,
                    "isDiscounted" : True
                },
                {
                    "gameTitle" : "NARAKA: BLADEPOINT",
                    "game_id" : "*****",
                    "purchasePricePeso" : 540.69,
                    "isDiscounted" : False
                }
            ]
        },
        {
            "customerUsername" : "hanols",
            "customer_id" : "*****",
            "transactionDate" : datetime(2025,1, 15),
            "isRefund" : False,
            "subtotal" : 249.74,
            "lineItems" : [
                {
                    "gameTitle" : "Marvel Rivals",
                    "game_id" : "*****",
                    "purchasePricePeso" : 249.74,
                    "isDiscounted" : True
                },
                {
                    "gameTitle" : "Sid Meier’s Civilization® VI",
                    "game_id" : "*****",
                    "purchasePricePeso" : 0,
                    "isDiscounted" : True
                },
                {
                    "gameTitle" : "7 Days to Die",
                    "game_id" : "*****",
                    "purchasePricePeso" : 0,
                    "isDiscounted" : False
                }
            ]
        },
        {
            "customerUsername" : "liswea",
            "customer_id" : "*****",
            "transactionDate" : datetime(2022,3, 14),
            "isRefund" : False,
            "subtotal" : 11097.89,
            "lineItems" : [
                {
                    "gameTitle" : "No Mans Sky",
                    "game_id" : "*****",
                    "purchasePricePeso" : 11097.89,
                    "isDiscounted" : False
                },
                {
                    "gameTitle" : "Project Zomboid",
                    "game_id" : "*****",
                    "purchasePricePeso" : 0,
                    "isDiscounted" : True
                },
            ]
        },
        {
            "customerUsername" : "kailam",
            "customer_id" : "*****",
            "transactionDate" : datetime(2021,9,9),
            "isRefund" : False,
            "subtotal" : 1309.10,
            "lineItems" : [
                {
                    "gameTitle" : "Sekiro™: Shadows Die Twice - GOTY Edition",
                    "game_id" : "*****",
                    "purchasePricePeso" : 0,
                    "isDiscounted" : True
                },
                {
                    "gameTitle" : "Deep Rock Galactic",
                    "game_id" : "*****",
                    "purchasePricePeso" : 1309.10,
                    "isDiscounted" : True
                },
            ]
        },
        {
            "customerUsername" : "statuc",
            "customer_id" : "*****",
            "transactionDate" : datetime(2025,10,12),
            "isRefund" : False,
            "subtotal" : 9400.80,
            "lineItems" : [
                {
                    "gameTitle" : "Hades",
                    "game_id" : "*****",
                    "purchasePricePeso" : 9400.80,
                    "isDiscounted" : True
                },
                {
                    "gameTitle" : "Undertale",
                    "game_id" : "*****",
                    "purchasePricePeso" : 0,
                    "isDiscounted" : True
                },
            ]
        },
        {
            "customerUsername" : "rayjoh",
            "customer_id" : "*****",
            "transactionDate" : datetime(2022, 1, 5),
            "isRefund" : True,
            "subtotal" : 540.69,
            "lineItems" : [
                {
                    "gameTitle" : "NARAKA: BLADEPOINT",
                    "game_id" : "*****",
                    "purchasePricePeso" : 540.69,
                    "isDiscounted" : True
                },
                {
                    "gameTitle" : "Sekiro™: Shadows Die Twice - GOTY Edition",
                    "game_id" : "*****",
                    "purchasePricePeso" : 0,
                    "isDiscounted" : True
                },
            ]
        },
        {
            "customerUsername" : "eridaw",
            "customer_id" : "*****",
            "transactionDate" : datetime(2020,8,20),
            "isRefund" : False,
            "subtotal" : 14293.04,
            "lineItems" : [
                {
                    "gameTitle" : "Path of Exile",
                    "game_id" : "*****",
                    "purchasePricePeso" : 12983.9405435028,
                    "isDiscounted" : False
                },
                {
                    "gameTitle" : "Deep Rock Galactic",
                    "game_id" : "*****",
                    "purchasePricePeso" : 1309.099902308662,
                    "isDiscounted" : True
                },
            ]
        },
        {
            "customerUsername" : "samgon",
            "customer_id" : "*****",
            "transactionDate" : datetime(2023,2,10),
            "isRefund" : False,
            "subtotal" : 2822.77,
            "lineItems" : [
                {
                    "gameTitle" : "Hogwarts Legacy",
                    "game_id" : "*****",
                    "purchasePricePeso" : 2822.769455639357,
                    "isDiscounted" : True
                },
                {
                    "gameTitle" : "Sid Meier’s Civilization® VI",
                    "game_id" : "*****",
                    "purchasePricePeso" : 0,
                    "isDiscounted" : True
                },
            ]
        },
        {
            "customerUsername" : "nannel",
            "customer_id" : "*****",
            "transactionDate" : datetime(2021,5,5),
            "isRefund" : False,
            "subtotal" : 0,
            "lineItems" : [
                {
                    "gameTitle" : "People Playground",
                    "game_id" : "*****",
                    "purchasePricePeso" : 0,
                    "isDiscounted" : True
                },
                {
                    "gameTitle" : "New World: Aeternum",
                    "game_id" : "*****",
                    "purchasePricePeso" : 0,
                    "isDiscounted" : True
                },
            ]
        },
        {
            "customerUsername" : "chrmit",
            "customer_id" : "*****",
            "transactionDate" : datetime(2017,12,25),
            "isRefund" : False,
            "subtotal" : 2822.77,
            "lineItems" : [
                {
                    "gameTitle" : "Hogwarts Legacy",
                    "game_id" : "*****",
                    "purchasePricePeso" : 2822.769455639357,
                    "isDiscounted" : True
                },
                {
                    "gameTitle" : "Sid Meier’s Civilization® VI",
                    "game_id" : "*****",
                    "purchasePricePeso" : 0,
                    "isDiscounted" : True
                },
            ]
        },
        {
            "customerUsername" : "clapen",
            "customer_id" : "*****",
            "transactionDate" : datetime(2019,10,11),
            "isRefund" : False,
            "subtotal" : 540.69,
            "lineItems" : [
                {
                    "gameTitle" : "NARAKA: BLADEPOINT",
                    "game_id" : "*****",
                    "purchasePricePeso" : 540.6875814837028,
                    "isDiscounted" : True
                },
                {
                    "gameTitle" : "7 Days to Die",
                    "game_id" : "*****",
                    "purchasePricePeso" : 0,
                    "isDiscounted" : True
                },
            ]
        },
        {
            "customerUsername" : "alerom",
            "customer_id" : "*****",
            "transactionDate" : datetime(2020,3,20),
            "isRefund" : False,
            "subtotal" : 92.10,
            "lineItems" : [
                {
                    "gameTitle" : "VRChat",
                    "game_id" : "*****",
                    "purchasePricePeso" : 92.10,
                    "isDiscounted" : True
                },
                {
                    "gameTitle" : "Sid Meier’s Civilization® VI",
                    "game_id" : "*****",
                    "purchasePricePeso" : 0,
                    "isDiscounted" : True
                },
            ]
        },
        {
            "customerUsername" : "paubre",
            "customer_id" : "*****",
            "transactionDate" : datetime(2016, 8, 12),
            "isRefund" : False,
            "subtotal" : 11097.89,
            "lineItems" : [
                {
                    "gameTitle" : "No Mans Sky",
                    "game_id" : "*****",
                    "purchasePricePeso" : 11097.89,
                    "isDiscounted" : False
                }
            ]
        },
        {
            "customerUsername" : "karhow",
            "customer_id" : "*****",
            "transactionDate" : datetime(2020, 11, 28),
            "isRefund" : False,
            "subtotal" : 0,
            "lineItems" : [
                {
                    "gameTitle" : "Sekiro™: Shadows Die Twice - GOTY Edition",
                    "game_id" : "*****",
                    "purchasePricePeso" : 0,
                    "isDiscounted" : True
                }
            ]
        },
        {
            "customerUsername" : "jesfle",
            "customer_id" : "*****",
            "transactionDate" : datetime(2016,1,15),
            "isRefund" : False,
            "subtotal" : 0,
            "lineItems" : [
                {
                    "gameTitle" : "Undertale",
                    "game_id" : "*****",
                    "purchasePricePeso" : 0,
                    "isDiscounted" : True
                }
            ]
        },
        {
            "customerUsername" : "walwal",
            "customer_id" : "*****",
            "transactionDate" : datetime(2021, 6, 20),
            "isRefund" : False,
            "subtotal" : 9400.80,
            "lineItems" : [
                {
                    "gameTitle" : "Hades",
                    "game_id" : "*****",
                    "purchasePricePeso" : 9400.80,
                    "isDiscounted" : True
                }
            ]
        },
        {
            "customerUsername" : "paujoh",
            "customer_id" : "*****",
            "transactionDate" : datetime(2025,10,17),
            "isRefund" : False,
            "subtotal" : 5280.90,
            "lineItems" : [
                {
                    "gameTitle" : "Vampire Survivors",
                    "game_id" : "*****",
                    "purchasePricePeso" : 5280.896863946048,
                    "isDiscounted" : True
                }
            ]
        },
        {
            "customerUsername" : "whimur",
            "customer_id" : "*****",
            "transactionDate" : datetime(2017, 4, 15),
            "isRefund" : False,
            "subtotal" : 0,
            "lineItems" : [
                {
                    "gameTitle" : "DARK SOULS™ III",
                    "game_id" : "*****",
                    "purchasePricePeso" : 0,
                    "isDiscounted" : True
                }
            ]
        },
        {
            "customerUsername" : "rachic",
            "customer_id" : "*****",
            "transactionDate" : datetime(2021, 9, 28),
            "isRefund" : False,
            "subtotal" : 0,
            "lineItems" : [
                {
                    "gameTitle" : "New World: Aeternum",
                    "game_id" : "*****",
                    "purchasePricePeso" : 0,
                    "isDiscounted" : True
                }
            ]
        },
        {
            "customerUsername" : "alerya",
            "customer_id" : "*****",
            "transactionDate" : datetime(2022, 12, 25),
            "isRefund" : False,
            "subtotal" : 0,
            "lineItems" : [
                {
                    "gameTitle" : "Battlefield™ 2042",
                    "game_id" : "*****",
                    "purchasePricePeso" : 0,
                    "isDiscounted" : True
                }
            ]
        },
        {
            "customerUsername" : "pauest",
            "customer_id" : "*****",
            "transactionDate" : datetime(2024, 1, 1),
            "isRefund" : False,
            "subtotal" : 551.16,
            "lineItems" : [
                {
                    "gameTitle" : "THE FINALS",
                    "game_id" : "*****",
                    "purchasePricePeso" : 551.16,
                    "isDiscounted" : True
                }
            ]
        },
        {
            "customerUsername" : "alawil",
            "customer_id" : "*****",
            "transactionDate" : datetime(2019, 2, 14),
            "isRefund" : False,
            "subtotal" : 3375.23,
            "lineItems" : [
                {
                    "gameTitle" : "Fallout 4",
                    "game_id" : "*****",
                    "purchasePricePeso" : 3375.23,
                    "isDiscounted" : True
                }
            ]
        },
        {
            "customerUsername" : "benmor",
            "customer_id" : "*****",
            "transactionDate" : datetime(2025, 2, 20),
            "isRefund" : False,
            "subtotal" : 249.74,
            "lineItems" : [
                {
                    "gameTitle" : "Marvel Rivals",
                    "game_id" : "*****",
                    "purchasePricePeso" : 249.74,
                    "isDiscounted" : True
                }
            ]
        },
        {
            "customerUsername" : "petgil",
            "customer_id" : "*****",
            "transactionDate" : datetime(2021, 8, 15),
            "isRefund" : False,
            "subtotal" : 0,
            "lineItems" : [
                {
                    "gameTitle" : "Project Zomboid",
                    "game_id" : "*****",
                    "purchasePricePeso" : 0,
                    "isDiscounted" : True
                }
            ]
        },
        {
            "customerUsername" : "donspe",
            "customer_id" : "*****",
            "transactionDate" : datetime(2023, 5, 5),
            "isRefund" : False,
            "subtotal" : 1309.10,
            "lineItems" : [
                {
                    "gameTitle" : "Deep Rock Galactic",
                    "game_id" : "*****",
                    "purchasePricePeso" : 1309.10,
                    "isDiscounted" : True
                }
            ]
        },
        {
            "customerUsername" : "aleell",
            "customer_id" : "*****",
            "transactionDate" : datetime(2025,10,14),
            "isRefund" : False,
            "subtotal" : 11097.89,
            "lineItems" : [
                {
                    "gameTitle" : "Path of Exile",
                    "game_id" : "*****",
                    "purchasePricePeso" : 11097.89,
                    "isDiscounted" : True
                }
            ]
        },
        {
            "customerUsername" : "darjon",
            "customer_id" : "*****",
            "transactionDate" : datetime(2025, 4, 22),
            "isRefund" : False,
            "subtotal" : 9400.80,
            "lineItems" : [
                {
                    "gameTitle" : "Path of Exile",
                    "game_id" : "*****",
                    "purchasePricePeso" : 9400.80,
                    "isDiscounted" : True
                }
            ]
        },
        {
            "customerUsername" : "ricgoo",
            "customer_id" : "*****",
            "transactionDate" : datetime(2020, 5, 9),
            "isRefund" : False,
            "subtotal" : 0,
            "lineItems" : [
                {
                    "gameTitle" : "Hearts of Iron IV",
                    "game_id" : "*****",
                    "purchasePricePeso" : 0,
                    "isDiscounted" : True
                }
            ]
        },
        {
            "customerUsername" : "connor",
            "customer_id" : "*****",
            "transactionDate" : datetime(2025, 3, 15),
            "isRefund" : False,
            "subtotal" : 2822.77,
            "lineItems" : [
                {
                    "gameTitle" : "Hogwarts Legacy",
                    "game_id" : "*****",
                    "purchasePricePeso" : 2822.77,
                    "isDiscounted" : False
                }
            ]
        },
    ]

    transactionsRefund = [
        {
            "customerUsername" : "rayjoh",
            "customer_id" : "*****",
            "refundedGameTitle" : "NARAKA: BLADEPOINT",
            "refundedGameStore_id" : "*****",
            "refundedGameLibrary_id" : "*****",
            "transactionDate" : datetime(2025,11,23),
            "isRefund" : True,
            "balanceRefunded" : 540.68
        },
        {
            "customerUsername" : "rayjoh",
            "customer_id" : "*****",
            "refundedGameTitle" : "Sekiro™: Shadows Die Twice - GOTY Edition",
            "refundedGameStore_id" : "*****",
            "refundedGameLibrary_id" : "*****",
            "transactionDate" : datetime(2025,11,23),
            "isRefund" : True,
            "balanceRefunded" : 0
        },
        {
            "customerUsername" : "chrmit",
            "customer_id" : "*****",
            "refundedGameTitle" : "Hogwarts Legacy",
            "refundedGameStore_id" : "*****",
            "refundedGameLibrary_id" : "*****",
            "transactionDate" : datetime(2025,11,26),
            "isRefund" : True,
            "balanceRefunded" : 2822.76
        },
        {
            "customerUsername" : "clapen",
            "customer_id" : "*****",
            "refundedGameTitle" : "NARAKA: BLADEPOINT",
            "refundedGameStore_id" : "*****",
            "refundedGameLibrary_id" : "*****",
            "transactionDate" : datetime(2025,11,23),
            "isRefund" : True,
            "balanceRefunded" : 540.68
        },
        {
            "customerUsername" : "karhow",
            "customer_id" : "*****",
            "refundedGameTitle" : "Sekiro™: Shadows Die Twice - GOTY Edition",
            "refundedGameStore_id" : "*****",
            "refundedGameLibrary_id" : "*****",
            "transactionDate" : datetime(2025,11,23),
            "isRefund" : True,
            "balanceRefunded" : 540.68
        },
        {
            "customerUsername" : "hanols",
            "customer_id" : "*****",
            "refundedGameTitle" : "Marvel Rivals",
            "refundedGameStore_id" : "*****",
            "refundedGameLibrary_id" : "*****",
            "transactionDate" : datetime(2025,11,26),
            "isRefund" : True,
            "balanceRefunded" : 540.68
        },
        {
            "customerUsername" : "samgon",
            "customer_id" : "*****",
            "refundedGameTitle" : "Hogwarts LegacyT",
            "refundedGameStore_id" : "*****",
            "refundedGameLibrary_id" : "*****",
            "transactionDate" : datetime(2025,11,29),
            "isRefund" : True,
            "balanceRefunded" : 2822.76
        },
        {
            "customerUsername" : "nannel",
            "customer_id" : "*****",
            "refundedGameTitle" : "People Playground",
            "refundedGameStore_id" : "*****",
            "refundedGameLibrary_id" : "*****",
            "transactionDate" : datetime(2025,11,23),
            "isRefund" : True,
            "balanceRefunded" : 0
        },
        {
            "customerUsername" : "statuc",
            "customer_id" : "*****",
            "refundedGameTitle" : "THE FINALS",
            "refundedGameStore_id" : "*****",
            "refundedGameLibrary_id" : "*****",
            "transactionDate" : datetime(2025,11,30),
            "isRefund" : True,
            "balanceRefunded" : 551.16
        },
        {
            "customerUsername" : "statuc",
            "customer_id" : "*****",
            "refundedGameTitle" : "Fallout 4",
            "refundedGameStore_id" : "*****",
            "refundedGameLibrary_id" : "*****",
            "transactionDate" : datetime(2025,11,25),
            "isRefund" : True,
            "balanceRefunded" : 3375.22
        }
    ]

    db['customerAccounts'].insert_many(customerAccounts)
    db['storeGameInfo'].insert_many(storeGameInfo)
    db['ownedGameInfo'].insert_many(ownedGameInfo)
    db['gameReviews'].insert_many(gameReviews)
    db['transactions'].insert_many(transactionsBuy)
    db['transactions'].insert_many(transactionsRefund)

    closeConnection(conn) 