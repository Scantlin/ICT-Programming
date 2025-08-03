from flask import Flask, render_template, request #importing the needed libraries first
import random

app = Flask(__name__) #create the app

@app.route('/', methods=['GET', 'POST']) #Decorator
def home(): #function for how the backend render to frontend
    num = '' #initialize the value of name first or any variable
    number = ''
    result = ''

    if request.method == 'POST': #to check the backend if it has a form
        num = request.form.get('your_num') #to get the input from the user in the web
        number = str(random.randint(1, 10))

        if num == number:
            result = 'CONGRATULATIONS🎉'
        else:
            result = "You Lost 😔"

    return render_template('frontend.html', result=num, correct=number, message = result) #render the template and to give back the inputted value of user in the name

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=False) #run the app program