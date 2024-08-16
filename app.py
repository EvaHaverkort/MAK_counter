import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory store for donations (reset when the server restarts)
total_donations = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/donations', methods=['GET', 'POST'])
def donations():
    global total_donations
    if request.method == 'POST':
        amount = int(request.form['amount'])
        total_donations += amount
        return jsonify({"status": "success", "new_total": total_donations})
    return render_template('donations.html', total_donations=total_donations)

@app.route('/get_total_donations')
def get_total_donations():
    return jsonify({"total_donations": total_donations})


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/mdt')
def mdt():
    return render_template('mdt.html')

@app.route('/redcross')
def redcross():
    return render_template('redcross.html')

@app.route('/servethecity')
def servethecity():
    return render_template('servethecity.html')

@app.route('/zerohunger')
def zerohunger():
    return render_template('zerohunger.html')

@app.route('/end_round_one')
def end_round_one():
    return render_template('end_round_one.html')

@app.route('/end_round_two')
def end_round_two():
    return render_template('end_round_two.html')

@app.route('/end_round_three')
def end_round_three():
    return render_template('end_round_three.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
