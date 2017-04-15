# Measuring attention using cross-brain correlations in a real setting

### Introduction
In this lab, we will measure correlations across brains, as a measure of
attention.  The idea is that, the more people pay attention to a stimulus, the
more their brain is driven by a stimulus and not their internal thoughts. If it
is driven by the stimulus, then brain signals across different sessions should be similar.

### Setup

First, install the libraries (there are new python dependencies this time!):
``` bash
cd recording
npm install
pip install -r requirements.txt
```

(If you don't have `npm`, you can install by running `brew install node`. You can get `brew` from https://brew.sh/)

### Stimulus Presentation + Recording

- Attach electrodes to participant's head, 2 on the frontal cortex (on forehead) and 2 on temporal lobe (right above the ears).
- Connect to the ganglion and stream data: `cd recording; node ganglion-lsl.js`
- Run lsl-viewer to check connections and stream: `python recording/lsl-viewer.py`
- Record data (replace "name" with your name, and "movie" with "sintel" or "bunny"):
  `python recording/lsl-record.py -f data/data_1.csv`
- Press enter on movie to really start movie
- Stop recording data by pressing Control-C in the `lsl-record.py` script

### Analysis

- Open `analysis/cross_brain_correlation.ipynb`
- Replace the filenames at the beginning with your filenames
- Run it and see the correlations!

(If you couldn't successfully collect data, I have put in some example files that I collected that you can try analyzing as well, inside data)
