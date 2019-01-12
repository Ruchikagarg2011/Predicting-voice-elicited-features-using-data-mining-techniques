import soundfile as sf

data, samplerate = sf.read('/Users/pramod/Documents/MachineLearning/AudioMining/AppliedGender/dataset/test_data/samples/recorded.webm')
sf.write('/Users/pramod/Documents/MachineLearning/AudioMining/AppliedGender/dataset/test_data/samples/recorded_wav.wav', data, samplerate)
