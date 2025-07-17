from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) #Route for the home page

def home():
    name = ''
    score = 0
    result = ''
    if request.method == 'POST':
        name = request.form.get('Your_name')
        init_name = name.replace(' ', '').lower()

        crush = request.form.get('Crush')
        init_crush = crush.replace(' ', '').lower()

        print(f'name: {name}')
        print(f'crush: {crush}')

        flames = 'FLAMES'

        for i in init_name:
            if i in init_crush:
                init_name = init_name.replace(i, "")
                init_crush = init_crush.replace(i, "")

        score = len(init_name + init_crush)


        flames = flames * score
        result = flames[score-1]

        match(result):
            case 'F':
                result = 'FRIEND'
            case 'L':
                result = 'LOVER'
            case 'A':
                result = 'AFFECTIONATE'
            case 'M':
                result = 'MARRIAGE'
            case 'E':
                result = 'ENEMY'
            case 'S':
                result = 'SEX'
            case _:
                result = 'Cant Identify'
                    
    return render_template('structure.html', name=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=False)