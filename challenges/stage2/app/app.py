

from flask import Flask, request, render_template_string

app = Flask(__name__)

HOME_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>CyberVault Teller Portal</title>
</head>
<body>
    <h1>CyberVault Teller Portal</h1>
    <p>Welcome to the internal teller system.</p>
    <p>The login system is currently unavailable.</p>

    <!-- TODO: restore the forgotten login page -->
    <!-- Developers: the old login route is /login -->

    <p>System status: Operational</p>
</body>
</html>
"""

LOGIN_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Forgotten Login</title>
  <script src="/static/script.js"></script>
</head>
<body>
    <h1>Forgotten Login</h1>

    <form method="POST">
        <label>Username:</label>
        <input type="text" name="username">

        <br><br>

        <label>Password:</label>
        <input type="password" name="password">

        <br><br>

        <button type="submit">Login</button>
    </form>

    {% if message %}
        <p>{{ message }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HOME_PAGE)

@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "teller" and password == "ledger2026":
            return """
            <h1>Login Successful</h1>
            <p>Welcome, teller.</p>
            <p>Flag: <strong>CTF{the_forgotten_login}</strong></p>
            """

        message = "Invalid credentials."

    return render_template_string(LOGIN_PAGE, message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
