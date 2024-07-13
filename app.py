from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Dummy user data for demonstration
valid_username = 'mo'
valid_password = 'moapp'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == valid_username and password == valid_password:
            session['username'] = username
            return redirect(url_for('dashboard'))
        return "<h1>Invalid credentials</h1>"
    return render_template('login.html')

@app.route('/is_logged_in')
def is_logged_in():
    logged_in = 'username' in session
    return jsonify(loggedIn=logged_in)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/accessibility-inclusivity')
def accessibility_inclusivity():
    return render_template('accessibility-inclusivity.html')

@app.route('/color-contrast')
def color_contrast():
    return render_template('color-contrast.html')

@app.route('/guide')
def guide():
    return render_template('guide.html')

@app.route('/image-alt-text')
def image_alt_text():
    return render_template('image-alt-text.html')

@app.route('/visual-impairment-simulator')
def visual_impairment_simulator():
    return render_template('visual-impairment-simulator.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        feedback = request.form['feedback']
        # Process the feedback (e.g., save to a database or send an email)
        return redirect(url_for('thank_you'))
    return render_template('feedback.html')

@app.route('/thank-you')
def thank_you():
    return "<h1>Thank you for your feedback!</h1>"

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
