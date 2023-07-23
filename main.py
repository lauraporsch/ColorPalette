from flask import Flask, render_template, flash, request, redirect, url_for
from flask_bootstrap import Bootstrap
import os
from werkzeug.utils import secure_filename
from PIL import Image
import numpy as np

SECRET_KEY = "sjdbfjksdbfjkwesf"
UPLOAD_FOLDER = 'static/img/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
WORKING_WIDTH = 900
img_path = ""

# ---------------------------- START FLASK FRAMEWORK ------------------------------- #
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = SECRET_KEY
Bootstrap(app)


# ---------------------------- DEFINE FUNCTIONS ------------------------------- #
def allowed_file(filename):
    """ takes the last part of the filename (extension) and checks if it is part of ALLOWED_EXTENSIONS"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def process_colors(amount):
    global img_path
    img = Image.open(img_path)
    og_width = img.size[0]
    og_height = img.size[1]
    # resize image to lower processing times
    width_percentage = WORKING_WIDTH / og_width
    new_height = int(og_height * width_percentage)
    img = img.resize((WORKING_WIDTH, new_height))
    # convert image to NumPy arrays
    img_data = np.asarray(img)
    # reshape 3D array to 2D array
    # -1 means unknown number of rows, 3 means there's 3 columns (RGB)
    img_data = img_data.reshape(-1, 3)
    # find all unique RGB codes and their counts in the array
    unique, counts = np.unique(img_data, axis=0, return_counts=True)
    # get indices of the x (=amount) highest counts
    index = np.argpartition(counts, -amount)[-amount:]
    # find RGB codes with the index
    top_colors = unique[index]
    top_colors = top_colors.tolist()
    return top_colors



# ---------------------------- SET UP ROUTES ------------------------------- #
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    global img_path
    if request.method == 'POST':
        image_file = request.files['file']
        # If user does not select a file, the browser submits an empty file
        if image_file.filename == '':
            flash('Please select a file!')
            return render_template('index.html')
        if not allowed_file(image_file.filename):
            flash('Your image has to be a ".png", ".jpg", ".jpeg" or ".gif" file')
            return render_template('index.html')
        if image_file and allowed_file(image_file.filename):
            # use secure_filename to prevent saving fraud files to the os
            filename = secure_filename(image_file.filename)
            image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            img_path = f"static/img/uploads/{filename}"
            return redirect(url_for('show_image')), img_path
    else:
        return render_template('index.html')


@app.route('/show-image', methods=['GET', 'POST'])
def show_image():
    global img_path
    if request.method == 'POST':
        amount_of_colors = int(request.form.get('amount'))
        return redirect(url_for('show_colors', amount=amount_of_colors))
    else:
        return render_template('show-image.html', image_path=img_path)


@app.route('/show-colors/<int:amount>')
def show_colors(amount):
    top_colors = process_colors(amount)
    colors = []
    for color in top_colors:
        colors.append(tuple(color))
    print(colors)
    return render_template('colors.html', colors=colors)


if __name__ == "__main__":
    app.run(debug=True)