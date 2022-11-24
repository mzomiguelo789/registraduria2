import pymongo
import certifi

ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://ciclo4:ciclo4@cluster0.kzfcwiy.mongodb.net/escuela?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.test
print(db)

baseDatos = client["escuela"]
print(baseDatos.list_collection_names())