from flask import Flask, render_template, send_file, jsonify, request
import os

app = Flask(__name__)

CAT_DOG = "catDog"
MAN_WOMAN = "manWoman"
BIKE_MOTORBIKE = "bikeMotorbike"

datasets_dir = "../tmp/" + MAN_WOMAN

@app.route("/deleteImages", methods=["POST"])
def deleteImages():
    path = request.args.get('p').replace("/", os.sep)

    imagesRemoved = []
    if request.is_json:
        images = request.get_json()

        if not images is None:
            for image in images:
                fileToDelete = os.path.join(
                    os.path.join(datasets_dir, path), image)
                print(fileToDelete)

                if os.path.exists(fileToDelete):
                    os.remove(fileToDelete)
                    imagesRemoved.append(os.path.basename(fileToDelete))
    
    return jsonify(imagesRemoved)

@app.route('/image')
def get_image():
    path = request.args.get('p').replace("/", os.sep)
    img = request.args.get('i')
    return send_file(os.path.join(os.path.join(datasets_dir, path), img), mimetype='image/jpeg')

@app.route('/getFolders')
def getDatasets():
    dirtree = {}
    dirs = [root for root, _, _ in os.walk(datasets_dir)]
    
    for item in dirs:
        p = dirtree
        for x in item.split(os.sep):
            p = p.setdefault(x, {})

    return jsonify({".": dirtree[datasets_dir]})

@app.route('/getImages')
def getImages():
    path = request.args.get('p').replace("/", os.sep)
    directory = os.path.join(datasets_dir, path)
    images = []

    if os.path.exists(directory):
        images = os.listdir(directory)

    return jsonify(images)


@app.route('/')
def listDatasets():
    return render_template('index.html')

@app.route('/check')
def listImages():
    path = request.args.get('p')
    return render_template('check.html', path=path)

app.run(host="0.0.0.0", port=8080)
