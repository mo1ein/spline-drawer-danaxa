
import os
from typing import List, Union, Tuple
from spline_drawer import spline
from flask import Flask, request, render_template, send_file

app = Flask(
    __name__,
    static_folder='static'
)
app.config['UPLOAD_FOLDER'] = 'upload'

# redirect to main endpoint


@app.route('/', methods=['POST', 'GET'])
def root() -> str:
    return "hello to root :)"


@app.route('/s', methods=['POST', 'GET'])
def draw():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        form_data = request.form.to_dict(flat=False)
        image = request.files['image']
        if is_data_valid(form_data) and image.filename != '':
            xs, ys, k = is_data_valid(form_data)
            image_path = os.path.join(
                app.config['UPLOAD_FOLDER'],
                image.filename
            )
            image.save(image_path)
            result = spline.draw(xs, ys, k, image_path)
            return send_file(result, mimetype='image/jpeg')
        else:
            message = 'input data is not correct!'
            return render_template('index.html', message=message)

    return "nice"


def is_data_valid(data: dict) -> Union[Tuple[List[int], List[int], int], bool]:
    # print(data)
    xs = data['xs'][0].split(',')
    for i, v in enumerate(xs):
        if not v.isnumeric():
            return False
        xs[i] = int(v)

    ys = data['ys'][0].split(',')
    for i, v in enumerate(ys):
        if not v.isnumeric():
            return False
        ys[i] = int(v)

    k = data['k'][0]
    if not k.isnumeric():
        return False
    # TODO: have limit?
    k = int(k)

    return xs, ys, k


if __name__ == '__main__':
    app.run(debug=True)
