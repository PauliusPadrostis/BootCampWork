import pickle

with open('fish_prediction.pkl', 'rb') as file:
    model = pickle.load(file)

while True:

    print('WELCOME THE THE GRAND FISH PREDICTOR\n')
    print('Please enter the following details to get your fish prediction\n')

    weight = float(input('Enter the weight of the fish: '))
    length1 = float(input('Enter the length of the fish: '))
    length2 = float(input('Enter the length of the fish: '))
    length3 = float(input('Enter the length of the fish: '))
    height = float(input('Enter the height of the fish: '))
    width = float(input('Enter the width of the fish: '))

    print("THE FISH PREDICTOR IS WORKING THINKING...")
    prediction = model.predict([[weight, length1, length2, length3, height, width]])

    print("THE GREAT FISH PREDICTOR HAS SPOKEN!")
    print(f'The fish is of type {prediction[0]}!')