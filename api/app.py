import os
import subprocess
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/Users/pramod/Documents/MachineLearning/AudioMining/api/data'
ALLOWED_EXTENSIONS = set(['wav', 'webm'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/jquery")
def js():
   return render_template("./jquery.js")

@app.route('/emotion', methods=['GET', 'POST'])
def doEmotion():
   wavfileinput = request.args.get('wavfile')
   output = executeEmotion(wavfileinput)
   return output

@app.route('/predictdata', methods=['GET', 'POST'])
def do_processing():
   if request.method == 'POST':
      if request.method == 'POST':
          # check if the post request has the file part
          if 'recordfile' not in request.files:
              print 'no file'
              print request.files
              return redirect(request.url)
          file = request.files['recordfile']
          # if user does not select file, browser also
          # submit a empty part without filename
          if file.filename == '':
              print 'no filename'
              return 'no filename'
          if file:
              print 'filename found'
              print file.filename
              filename = secure_filename(file.filename)
              print file.filename
              print os.path
              wavefilepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
              file.save(wavefilepath)
              #return redirect(url_for('uploaded_file',
               #                       filename=filename))
              output = executeFeatures(wavefilepath)
              return output
      return '''
             processing file
             '''


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    return render_template('./index.html')
    # with open('./index.html', 'r') as myfile:
    #   data=myfile.read().replace('\n', '')
    # return data

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

def executeEmotion(wavfile):
    print 'wfile:'+wavfile
    outputlist = {}
    proc = subprocess.Popen(['python /Users/pramod/Documents/MachineLearning/AudioMining/pyAudioAnalysis/emotion.py /Users/pramod/Documents/MachineLearning/AudioMining/pyAudioAnalysis/' + wavfile],  stdout=subprocess.PIPE, shell=True, bufsize=1)
    out =  proc.communicate()
    jsonresult = '{"gender":"-", "speaker": "-", "emotion" : "'+out[0]+'"}'
    return jsonresult

def executeFeatures(wavfile):
    genderGmm = '/Users/pramod/Documents/MachineLearning/AudioMining/AppliedGender/PyGender-Voice/test_gender.py'
    genderLogistic = '/Users/pramod/Documents/MachineLearning/AudioMining/AppliedGender/PyGender-Voice/test_gender.py'
    speakerGmm = '/Users/pramod/Documents/MachineLearning/AudioMining/AppliedGender/PyGender-Voice/test_gender.py'
    emotionSvm = '/Users/pramod/Documents/MachineLearning/AudioMining/AppliedGender/PyGender-Voice/test_gender.py'
    outputlist = {}
    proc = subprocess.Popen(["python /Users/pramod/Documents/MachineLearning/AudioMining/AppliedGender/PyGender-Voice/test_gender.py"],  stdout=subprocess.PIPE, shell=True, bufsize=1)
    out =  proc.communicate()
    #print '>>>'+out
    outputlist['gender-gmm'] = out[0].strip()
    proc = subprocess.Popen(["python /Users/pramod/Documents/MachineLearning/AudioMining/AppliedGender/PyGender-Voice/test_gender.py"],  stdout=subprocess.PIPE, shell=True, bufsize=1)
    (out,err) = proc.communicate()
    outputlist['gender-logistic'] = out
    proc = subprocess.Popen(["python /Users/pramod/Documents/MachineLearning/AudioMining/AppliedGender/PyGender-Voice/test_gender.py"],  stdout=subprocess.PIPE, shell=True, bufsize=1)
    (out,err) = proc.communicate()
    outputlist['speaker-gmm'] = out
    proc = subprocess.Popen(["python /Users/pramod/Documents/MachineLearning/AudioMining/AppliedGender/PyGender-Voice/test_gender.py"],  stdout=subprocess.PIPE, shell=True, bufsize=1)
    (out,err) = proc.communicate()
    outputlist['emotion-svm'] = out
    jsonresult = '{"gender":"'+outputlist['gender-gmm']+'", "speaker": "-", "emotion" : "-"}'
    return jsonresult

if __name__ == "__main__":
    app.run(debug=True)
