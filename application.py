import numpy as np
from flask import Flask, request, render_template
from skimage.feature import greycomatrix

application = Flask(__name__)
inputmatrix = np.random.randint(0, 5, size=(4, 4))
levels=inputmatrix.max()+1
sol = greycomatrix(inputmatrix, [1], [0., np.pi / 4., np.pi / 2., 3. * np.pi / 4.], levels= levels)
matrixGlcm = sol[:, :, 0, 0]
@application.route('/')
def hello_world():
    return render_template('ViewGLCM.html', Matrix1=inputmatrix, GlcmMatrix=matrixGlcm, Distance=1, Angle=0)
@application.route('/', methods=['POST'])
def my_form_post():
    distance = int(request.form['disttvall'])
    angle = request.form['anggvall']
    valang = 0
    if angle == "45":
        valang = 3*np.pi/4
    elif angle == "90":
        valang = np.pi/2
    elif angle == "135":
        valang = np.pi/4
    res = greycomatrix(inputmatrix, [distance], [valang], levels=levels)
    matrixres = np.transpose(res[:, :, 0, 0])
    return render_template('ViewGLCM.html', Matrix1=inputmatrix, GlcmMatrix=matrixres, Distance=distance, Angle=angle)

if __name__ == '__main__':
    application.run()

