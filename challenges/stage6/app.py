
from flask import Flask, request, jsonify, make_response, render_template_string
import os
import jwt
from datetime import datetime, timedelta, timezone

app = Flask(__name__)

# Deliberately vulnerable TEST configuration for this CTF only.
TEST_SECRET = "CyberVault-Dev-JWT-Secret-2026"
FLAG = "CYBERVAULT{VAULT_BACKDOOR_UNLOCKED}"

HOME_HTML = """
<!DOCTYPE html>
<html>
<head>
<title>CyberVault | Transfer Authorization</title>
<style>
body {font-family:Arial;background:#0b1220;color:#e5e7eb;margin:0}
header {background:#14213a;padding:24px 40px;font-size:25px;font-weight:bold}
main {max-width:760px;margin:65px auto;padding:35px;background:#18263e;border-radius:12px}
button {padding:12px 20px;background:#22c55e;border:0;border-radius:6px;cursor:pointer}
a {color:#93c5fd}
small {color:#9ca3af}
</style>
</head>
<body>
<header>CyberVault Bank — Internal Portal</header>
<main>
<h1>Transfer Authorization System</h1>
<p>Restricted internal transaction review portal.</p>
<p>Investigators may obtain a temporary viewer session.</p>
<form action="/login" method="post">
<button type="submit">Start Investigator Session</button>
</form>
<p><a href="/transactions">View Protected Transactions</a></p>
<small>CyberVault internal systems | Build 2026.09</small>
</main>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HOME_HTML)

@app.route("/login", methods=["POST"])
def login():
    payload = {
        "sub": "investigator",
        "role": "user",
        "exp": datetime.now(timezone.utc) + timedelta(hours=2)
    }

    token = jwt.encode(payload, TEST_SECRET, algorithm="HS256")

    response = make_response("""
    <h2>Investigator session created</h2>
    <p>Your role is <b>user</b>.</p>
    <p>Try accessing the protected transaction page.</p>
    <p><a href="/transactions">Open transactions</a></p>
    <p><a href="/">Back to homepage</a></p>
    """)

    response.set_cookie(
        "session_token",
        token,
        httponly=True,
        samesite="Lax"
    )
    return response

@app.route("/internal/debug/config")
def debug_config():
    # Intentional information disclosure vulnerability.
    return jsonify({
        "application": "CyberVault Transfer Authorization",
        "environment": "development",
        "jwt_algorithm": "HS256",
        "jwt_signing_secret": TEST_SECRET,
        "required_role": "admin",
        "message": "Legacy debug configuration endpoint"
    })

@app.route("/transactions")
def transactions():
    token = request.cookies.get("session_token")

    if not token:
        return "Access denied: no session token.", 401

    try:
        claims = jwt.decode(
            token,
            TEST_SECRET,
            algorithms=["HS256"]
        )
    except jwt.ExpiredSignatureError:
        return "Access denied: session expired.", 401
    except jwt.InvalidTokenError:
        return "Access denied: invalid session token.", 401

    if claims.get("role") != "admin":
        return "Access denied: administrator role required.", 403

    return f"""
    <h1>CyberVault — Protected Transaction Record</h1>
    <p>Authorization level: Administrator</p>
    <p>Transaction reference: CV-2026-2347</p>
    <p>Status: Suspicious transfer under investigation</p>
    <h2>Investigation Flag</h2>
    <code>{FLAG}</code>
    """

@app.route("/robots.txt")
def robots():
    return (
        "User-agent: *\n"
        "Disallow: /internal/\n",
        200,
        {"Content-Type": "text/plain"}
    )

if __name__ == "__main__":
    app.run(host=os.environ.get("HOST", "127.0.0.1"),
    port=5000,
    debug=False)
