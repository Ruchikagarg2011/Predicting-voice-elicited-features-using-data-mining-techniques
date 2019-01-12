# Predicting voice elicited features using data mining techniques

Objective
The objective of the project is to process user’s audio, to be used for work
process automation. Given a speech input, our aim is to identify the speaker,
detect speaker’s gender, and analyze the speaker’s emotion.

Proposed approach has the following two steps:
1. Feature Extraction: It splits the input signal into short-term windows
(frames) and computes a number of features for each frame. This
process leads to a sequence of short-term feature vectors for the whole
signal.In many cases, the signal is represented by statistics on the
extracted short-term feature sequences and extracts a number of
statistics (e.g. mean and standard deviation) over each short-term
feature sequence.Features include like Energy,entropy of energy,MFCCs
2. Regression and Segmentation: Regression is important in audio
analysis, e.g. in the context of speech emotion recognition, where the
emotional state is not a discrete class but a real-valued measurement
(e.g. arousal or valence). Segmentation is a very important processing
stage for most of audio analysis applications. The goal is to split an
uninterrupted audio signal into homogeneous segments. Segmentation
can either be
        Supervised: in that case some type of supervised knowledge is
        used to classify and segment the input signals. This is either
        achieved through applying a classifier in order to classify
        successive fix-sized segments to a set of predefined classes, or
        using HMM approach to achieve joint segmentation-classification.
        Unsupervised: a supervised model is not available and the
        detected segments are clustered (example: speaker diarization)
        
The project is divided into two phases.
1. Enrolment Phase or Training Phase: The enrolment or training phase is
the initial phase where the input speaker signal is pre-processed and its
features are extracted. Pre-processing is a form of cleansing to make it
suitable to identify and extract characteristic features of the speaker
signal. The process of feature extraction will enable the presentation of
the speaker vocal characteristics to construct a model for that particular
speaker.
2. Matching Phase: The matching phrase is responsible to identity the
voice functionalities by comparing the test voice prints with the existing
models stored in the database during the enrolment phase; the
comparison of unique characteristic features is what defines ’matching’

Algorithm & Actual Process:
➔ Input data set contains the voice signals that are parsed and MFCC
features are extracted using the PyAudioAnalysis library and tagged as
per the respective labels.
➔ Once we have the extracted feature set, we train the model using the
SVM (Simple vector machine) algorithm to classify the voice features as
per the desired label. During the training phase, each and every dataset
item is given as the input to the Simple Vector machine algorithm for
analysis of future data.
➔ We have the model trained with the training data based out of SVM and
other algorithms, we get the model that can actually classify the future
inputs.
➔ Once we have the model ready, we give the test input to check the
accuracy of the model. Depending on the output, we tune various
parameters of the system and consider various features for further dry
runs to optimize the maximum efficiency.
➔ Now any test voice that needs to be checked with the model , is taken
either by recording or by giving a wav file to the system.
➔ Our system converts the wav file into features and runs through the 
model and gives the output to the user
