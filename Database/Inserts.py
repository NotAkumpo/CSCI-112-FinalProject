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
            "phoneNumber": "'+95 65 258 441 3336",
            "walletBalancePeso": 673.0896245821835
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
            "phoneNumber": "'+6630 647 985 5344",
            "walletBalancePeso": 82.08713139715081
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
            "phoneNumber": "'+60 10 796 894 6850",
            "walletBalancePeso": 628.612929114156
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
            "phoneNumber": "'+65995 331 484 4665",
            "walletBalancePeso": 164.3911703768176
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
            "phoneNumber": "'+65995 331 484 4665",
            "walletBalancePeso": 146.28708335860142
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
            "phoneNumber": "'+856970 624 160 2718",
            "walletBalancePeso": 180.73489078523355
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
            "phoneNumber": "'+855 29 438 9286",
            "walletBalancePeso": 490.2473713833288
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
            "phoneNumber": "'+65995 331 484 4665",
            "walletBalancePeso": 587.3624597984689
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
            "phoneNumber": "'+6630 647 985 5344",
            "walletBalancePeso": 454.40586093712994
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
            "phoneNumber": "'+84974 506 709 2624",
            "walletBalancePeso": 239.60806929024386
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
            "phoneNumber": "'+95 65 258 441 3336",
            "walletBalancePeso": 426.9386057394909
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
            "phoneNumber": "'+63910 307 702 7488",
            "walletBalancePeso": 151.3650352925619
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
            "phoneNumber": "'+856970 624 160 2718",
            "walletBalancePeso": 251.5291012310439
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
            "phoneNumber": "'+62810 640 720 9408",
            "walletBalancePeso": 462.7483197208195
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
            "phoneNumber": "'+65995 331 484 4665",
            "walletBalancePeso": 789.5851920019587
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
            "phoneNumber": "'+60 10 796 894 6850",
            "walletBalancePeso": 497.31001868394895
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
            "phoneNumber": "'+856970 624 160 2718",
            "walletBalancePeso": 218.35447969441182
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
            "phoneNumber": "'+6630 647 985 5344",
            "walletBalancePeso": 107.67901458868741
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
            "phoneNumber": "'+63910 307 702 7488",
            "walletBalancePeso": 591.7588716148557
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
            "phoneNumber": "'+63910 307 702 7488",
            "walletBalancePeso": 884.7848778244477
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
            "phoneNumber": "'+62810 640 720 9408",
            "walletBalancePeso": 578.6396046346415
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
            "phoneNumber": "'+95 65 258 441 3336",
            "walletBalancePeso": 411.4867884208052
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
            "phoneNumber": "'+84974 506 709 2624",
            "walletBalancePeso": 335.0513502370871
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
            "phoneNumber": "'+855 29 438 9286",
            "walletBalancePeso": 355.87120627532784
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
            "phoneNumber": "'+62810 640 720 9408",
            "walletBalancePeso": 697.2790696669086
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
            "phoneNumber": "'+60 10 796 894 6850",
            "walletBalancePeso": 813.3258386271077
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
            "phoneNumber": "'+62810 640 720 9408",
            "walletBalancePeso": 929.3025585675663
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
            "phoneNumber": "'+6630 647 985 5344",
            "walletBalancePeso": 401.42743330972144
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
            "phoneNumber": "'+95 65 258 441 3336",
            "walletBalancePeso": 528.1736884399741
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
            "phoneNumber": "'+95 65 258 441 3336",
            "walletBalancePeso": 743.8643954446442
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
            "phoneNumber": "'+84974 506 709 2624",
            "walletBalancePeso": 229.74349181958863
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
            "phoneNumber": "'+63910 307 702 7488",
            "walletBalancePeso": 986.0223434057023
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
            "phoneNumber": "'+65995 331 484 4665",
            "walletBalancePeso": 752.6729491456148
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
            "phoneNumber": "'+62810 640 720 9408",
            "walletBalancePeso": 708.9169798828582
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
            "phoneNumber": "'+60 10 796 894 6850",
            "walletBalancePeso": 189.48462743944586
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
            "phoneNumber": "'+62810 640 720 9408",
            "walletBalancePeso": 886.3938238344557
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
            "phoneNumber": "'+6630 647 985 5344",
            "walletBalancePeso": 153.78598656859515
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
            "phoneNumber": "'+855 29 438 9286",
            "walletBalancePeso": 709.2047994209119
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
            "phoneNumber": "'+60 10 796 894 6850",
            "walletBalancePeso": 133.2176592658391
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
            "phoneNumber": "'+95 65 258 441 3336",
            "walletBalancePeso": 53.612058753713846
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
            "phoneNumber": "'+84974 506 709 2624",
            "walletBalancePeso": 603.2053842629031
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
            "phoneNumber": "'+60 10 796 894 6850",
            "walletBalancePeso": 869.5491095600768
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
            "phoneNumber": "'+855 29 438 9286",
            "walletBalancePeso": 779.1797905630443
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
            "phoneNumber": "'+6630 647 985 5344",
            "walletBalancePeso": 568.0979029582904
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
            "phoneNumber": "'+60 10 796 894 6850",
            "walletBalancePeso": 284.597375675467
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
            "phoneNumber": "'+84974 506 709 2624",
            "walletBalancePeso": 589.284767753526
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
            "phoneNumber": "'+855 29 438 9286",
            "walletBalancePeso": 953.1916320307228
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
            "phoneNumber": "'+63910 307 702 7488",
            "walletBalancePeso": 220.23308580322978
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
            "phoneNumber": "'+84974 506 709 2624",
            "walletBalancePeso": 344.5960688760814
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
            "phoneNumber": "'+84974 506 709 2624",
            "walletBalancePeso": 865.4827897076999
        }
    ]
    
    db.customerAccounts.insert_many(customerAccounts)

    closeConnection(conn) 