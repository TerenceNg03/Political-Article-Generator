from flask import Flask, render_template, make_response, request
import webbrowser
from generator import gen_text

app = Flask(__name__, template_folder='./')

@app.route("/index.html", methods=['GET', 'POST'])
def index():
    init = None
    version = None
    gen_len = None
    temperature = None
    if request.method == 'POST':
        try:
            data = request.form.to_dict(flat=True)
            print(data)
            init = data['init_text']
            if len(init) == 0:
                raise ValueError('Input can not be empty!')
            gen_len = int(data['gen_len'])
            temperature = float(data['temp_submit'])
            if 'version' in data:
                version = data['version']
            else:
                raise ValueError('Need to select a version!')
            text = gen_text(version, init, gen_len, temperature)
            return text
        except Exception as e:
            return str(e)
    return render_template("index.html", text="")

@app.route('/index.css')
def css():
    resp = make_response(render_template("index.css"))
    return resp

webbrowser.open("http://127.0.0.1:5000/index.html")
app.run()
