import subprocess,sys
filename=sys.argv[1]
proc = subprocess.Popen(["pythonw /Users/pramod/Documents/MachineLearning/AudioMining/pyAudioAnalysis/audioAnalysis.py regressionFile -i "+filename+" --model svm --regression /Users/pramod/Documents/MachineLearning/AudioMining/pyAudioAnalysis/data/svmSpeechEmotion"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
#print "program output:", out
#print out
arr=out.split()

arr[1]=float(arr[1])
arr[3]=float(arr[3])

if arr[1]>0 and arr[3]>0:
    print "happy"
elif arr[1]>0 and arr[3]<0:
    print "angry"
elif arr[1]<0 and arr[3]>0:
    print "calm"
else:
    print "sad"
