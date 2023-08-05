import firebase_admin
from firebase_admin import credentials, firestore, storage


serviceAccountKey = {
  "type": "service_account",
  "project_id": "musverse-784e4",
  "private_key_id": "c4fcd75cc1678595a495dd91fe556b5f11b0e6c9",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCojRY/DSuJ1KtI\n2oSZtZLxEKIWXpDiGjttmDUTjy4ISYWlv8DyIW6cVg9ICRAn2WJcE4PW6lWm8YUp\nlkvbW5XTCAoiofiYWysR/yezdFGgCFa55fd9lgIrg+6PmHItj6lsFXoji5B/aMQa\nha+RP1R7QYZB0Lpqn5kPWzbHJIIdjl5KZIbvButRJQe14vvJx9plqjzAmI5/ia3U\nXQ+oPwloqvEn0RjTxp5699wZGixnb8Q3CGDjiRhKwoaytXERj35APGoIjymuCCkA\nnEdWHx4+vcRX0URYh1N5YFPkz1kS87nh687zeYDGmhG7AHaFeK6u5pAh13rsAGAk\nnppOjKOhAgMBAAECggEAAS8YBtkl0GqaidOzSp/eFHnKygQlKa8YMlBx/3/yCXp9\nkQeY5a6EJWlHQ1OWeKbavYrgzO68QNS5nBbyCUGnqqntMHdMLML3rraTecu1cChc\n1m0/TOiucwMtduEMkhsRgZNgoQfVAT3GzQj56IKYuk1VwcgN64EGXoduz00XfvkE\nYZKXPZPqHv1oVaU57CfGCTmC/wbWr6AA5j+cfdaYvqwIa0wuptF8Oe4DJFHvNH97\nfS8/V27eyDxK0KvkMYx7V7bb48GF1asijltaoOV2Nw1KD/zNJ/1U1uk6+Waq6uXq\nibkmlpEm8OBO+YURK5N3cqNbcuf+0zphvLdspjl9MQKBgQDk3iHQEerXCe4JtNz6\nNhlrFEcnbEZ9qBngktIs0EUV7Oi91o0nVJtysmphoAcvm1aMlflC9Xv8CRqQjcKQ\nN5eVs8fzCQQLP5bTKTY3qTxpdLFpZcJxubGcJU2pX4df1kmSJKeaWRFM2isWzGPY\nSvn/Kivl1nKVy5EFRB67thB6EQKBgQC8iGq3yhrMa+atJ9XJA4tLZJeRu+RlpJOB\ncNnSeoDrd7YlvbeAAcw0cER/ZbInwiKbzpLWsiRM3g/4HGBsOI6xfZhDcwciooAt\nueIOGXtuVN9OVmGN7oOCY0q4uHqNMNjy7+qm4Ao95PMipjQm9aMPza+TecExmrT0\nne7raD+AkQKBgBQXL86tE/lmhL/TYaaRQy/0Kr7aMWHsdMETAmIusjHXhyLLB78R\nHUg3Q0Foo9jZAQL8U1I+bHDWd7+CwjaYurTIgF/kRbebEGle78R5FbWIKd6/sQ78\npwu29pdMrHyMOg8bKp9Q/ETLzgaFUKp3AnUUxZ+6cHqX0RYuQahmthGRAoGATIVy\nCzbUubPx5MYOV5BAsVEa0+PXSAoMdLVBM9TVDr2ACMGAAUy5fW8z3iGAtfJt6Z9m\nqg2T/j8DbEjYOhSalh/L9VRyyPP74pNX1TEykA2StVEKN3lfl0SFx4PY+gWhiLko\nHKNChOywYpfjAw0gKgHqCYmZiHCqkb6ogpPFcoECgYEAtWqX1TAnaIG/+6nG4j5i\nO9CHS3puZ3oMCkMvwAqSJNoJV5GdqP3yumCtn9P7jWGS4h8dfMVsO/u/taikcb5T\n64OEFM6xqPakBGGex2ahh7H7dz/0ad4PgydRf/gKjO70i0AZ16nyZrk0cp4qCcWS\nHlWJFheuolpe3HBFEtLK+CA=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-bvxpp@musverse-784e4.iam.gserviceaccount.com",
  "client_id": "115347137708460813022",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-bvxpp%40musverse-784e4.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

cred = credentials.Certificate(serviceAccountKey)

config = {
    "apiKey": "AIzaSyA0FjpJuSmEuXXKGfcRUQ2YQv_B3ShPsSw",
    "authDomain": "musverse-784e4.firebaseapp.com",
    "projectId": "musverse-784e4",
    "storageBucket": "musverse-784e4.appspot.com",
    "messagingSenderId": "681171328905",
    "appId": "1:681171328905:web:421eed50799c026ec58b58",
    "measurementId": "G-M7LN6BW495",
    "serviceAccount": cred,
}


def increment(type:str, id:int):
    app = firebase_admin.initialize_app(cred,config)
    db = firestore.client()
    db.collection("Next").document(type).set({'ID':id+1})
    firebase_admin.delete_app(app)


def getNextId(type:str)->int:
    app = firebase_admin.initialize_app(cred,config)
    db = firestore.client()
    result = db.collection("Next").document(type).get().to_dict()
    firebase_admin.delete_app(app)
    return result["ID"]


def getUserData(id:str)->dict:
    app = firebase_admin.initialize_app(cred,config)
    db = firestore.client()
    result = db.collection("User Data").document(id).get().to_dict()
    firebase_admin.delete_app(app)

    return result


def getMusicData(id:str)->dict:
    app = firebase_admin.initialize_app(cred,config)
    db = firestore.client()
    result = db.collection("Music").document(id).get().to_dict()
    firebase_admin.delete_app(app)

    return result


def songUpload(filename):
    app = firebase_admin.initialize_app(cred, config)
    bucket = storage.bucket()
    blob = bucket.blob(filename)
    blob.upload_from_filename(filename)
    blob.make_public()
    url = blob.public_url
    firebase_admin.delete_app(app)
    return url
        


def addSong(data:dict, filename:str):
    data['url'] = songUpload(filename)
    id = getNextId('Song')
    increment(type, id)
    app = firebase_admin.initialize_app(cred, config)
    db = firestore.client()
    db.collection('Music').document(str(id)).set(data)
    print("Done")
    firebase_admin.delete_app(app)


def addUser(data:dict):
    
    id = getNextId("User")
    increment(type, id)
    app = firebase_admin.initialize_app(cred, config)
    db = firestore.client()
    db.collection("User Data").document(str(id)).set(data)
    firebase_admin.delete_app(app)
    return True
        


def searchSong(name:str)->list:
    n = getNextId("Song")
    app = firebase_admin.initialize_app(cred, config)
    db = firestore.client()
    data = []
    for i in range(1, n):
        result = db.collection('Music').document(str(i)).get().to_dict()
        if (len(result)!=0) and (name in result['Name']):
            data.append(result)
            
    firebase_admin.delete_app(app)
    return data
