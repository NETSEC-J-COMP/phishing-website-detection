# Importing libraries
import joblib
import Inputscript

# Load the pickle file
classifier = joblib.load("final_model/rf_final.pkl")

# Input url
print("Welcome to the phishing website detection software!\n\n")
url = input("Enter url: ")

# Checking and Predicting
checkprediction = Inputscript.main(url)
prediction = classifier.predict(checkprediction)
print(prediction)

if(prediction == 1):
    print("The site is a phishing site")
else:
    print("The site is not a phishing site")
    