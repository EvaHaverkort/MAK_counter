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

if __name__ == '__main__':
    app.run(debug=True)
