from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Anu's Kitchen – Avala Murabba</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #fff7e6;
            color: #333;
        }
        header {
            background: #ff9933;
            padding: 20px;
            text-align: center;
            color: white;
            font-size: 32px;
            font-weight: bold;
        }
        .banner {
            width: 100%;
            text-align: center;
            margin-top: 20px;
        }
        .banner img {
            width: 300px;
            border-radius: 15px;
            box-shadow: 0 0 10px #999;
        }
        .section {
            padding: 20px;
            text-align: center;
        }
        .section h2 {
            color: #cc6600;
        }
        .buy {
            background: #cc6600;
            color: white;
            padding: 12px 25px;
            border-radius: 8px;
            text-decoration: none;
            font-size: 18px;
            display: inline-block;
            margin-top: 15px;
        }
        .footer {
            background: #ff9933;
            padding: 10px;
            text-align: center;
            color: white;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <header>
        Anu's Kitchen – Avala Murabba
    </header>

    <div class="banner">
        <img src="WhatsApp Image 2025-11-17 at 21.42.59.jpeg" alt="Amla Murabba">
    </div>

    <div class="section">
        <h2>Pure. Homemade. Healthy.</h2>
        <p>
            Our Avala (Amla) Murabba is made using the best quality amla, jaggery/sugar,
            and traditional recipes from Anu's Kitchen.
            <br><br>
            Boost your immunity naturally!
        </p>

        <h2>Benefits of Amla Murabba</h2>
        <p>
            ✔ Boosts immunity  
            ✔ Improves digestion  
            ✔ Good for hair & skin  
            ✔ Rich in Vitamin C  
        </p>

        <a class="buy" href="https://wa.me/919673443424">Order Now on WhatsApp</a>
    </div>

    <div class="footer">
        © 2025 Anu's Kitchen | Avala Murabba | Pune
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run(debug=True)
