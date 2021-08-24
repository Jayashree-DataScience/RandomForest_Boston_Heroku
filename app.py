
# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
import flask_cors
from flask_cors import CORS,cross_origin
import pickle

application = Flask(__name__) # initializing a flask app
app=application
@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            CRIM = float(request.form['CRIM'])
            INDUS = float(request.form['INDUS'])
            NOX = float(request.form['NOX'])
            RM = float(request.form['RM'])
            AGE = float(request.form['AGE'])
            DIS = float(request.form['DIS'])
            RAD = float(request.form['RAD'])
            TAX = float(request.form['TAX'])
            PTRATIO = float(request.form['PTRATIO'])
            B = float(request.form['B'])
            LSTAT = float(request.form['LSTAT'])
            filename = 'boston_RF_model.pickle'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            file_scaler = 'scaler.pkl'
            load_scaler = pickle.load(open(file_scaler, 'rb'))
            prediction = loaded_model.predict(load_scaler.transform([[CRIM,INDUS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT]]))
            print('prediction is', prediction[0])
            # showing the prediction results in a UI
            return render_template('results.html',prediction=prediction[0])
        except Exception as e:
            print('The Exception message is: ',e)
            #return 'something is wrong'
            return e

        #return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	#app.run(host="0.0.0.0",port=8080) # running the app
    app.run(debug=True)
