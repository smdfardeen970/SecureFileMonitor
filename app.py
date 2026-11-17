from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Secure File Monitor</title>
        <style>
            body {
                background: #101827;
                color: white;
                font-family: Arial;
                text-align: center;
                padding: 80px;
            }
            h1 { color: #38bdf8; }
            .card {
                background: #1e293b;
                padding: 30px;
                border-radius: 12px;
                display: inline-block;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Secure File Monitor</h1>
            <h2>Security Dashboard</h2>
            <p>File Monitoring Project</p>
            <p>Integrity Checking System</p>
            <p>Security Alert System</p>
            <h3>Website Deployed Successfully!</h3>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
