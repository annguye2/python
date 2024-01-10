def prediction_model(pclass, sex, age, sibsp, parch, fare, enbarked, title):
 import pickle
 x = [[pclass, sex, age, sibsp, parch, fare, enbarked, title]]
 randomforest = pickle.load(open('titanic_model.sav', 'rb'))
 predictions = randomforest.predict(x)
 return predictions
#  print(predictions)