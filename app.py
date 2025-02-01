from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

os.makedirs("static/output", exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    username = request.form['username'].upper()  

    base_img_path = "static/template.png"
    img = Image.open(base_img_path)
    
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("static/fonts/TimesNewRoman.ttf", size=128)

    except IOError:
        font = ImageFont.load_default()  

    text = username if username else "NO NAME"

    bbox = draw.textbbox((0, 0), text, font=font) if text else (0, 0, 100, 50)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]  
    W, H = img.size
    position = ((W - w) // 2, (H - h) // 2)

    draw.text(position, text, fill="black", font=font)

    new_filename = f"output_{username}.png"
    new_filepath = os.path.join("static/output", new_filename)
    img.save(new_filepath)

    return redirect(url_for('download_page', filename=new_filename))

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory("static/output", filename, as_attachment=True)

@app.route('/download_page/<filename>')
def download_page(filename):
    return render_template('download.html', filename=filename)

if __name__ == "__main__":
    app.run(debug=True)
