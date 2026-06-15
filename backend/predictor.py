import pickle

model = pickle.load(
    open("models/ShipmentSure_Model.pkl","rb")
)

scaler = pickle.load(
    open("models/Scaler.pkl","rb")
)

def predict(data):

    scaled = scaler.transform(data)

    prediction = model.predict(scaled)[0]

    probability = model.predict_proba(
        scaled
    )[0]

    return prediction, probability