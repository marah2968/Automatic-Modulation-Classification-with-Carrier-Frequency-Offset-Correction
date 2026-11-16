# Automatic Modulation Classification with Carrier Frequency Offset Correction

This repository contains the code, data and material for a project on automatic
modulation classification (AMC) using deep learning, with estimation and
correction of the carrier frequency offset (CFO) before classification. The work
covers simulation in Python, dataset generation in MATLAB, and a practical
implementation with GNU Radio and an SDR board.

## Repository structure

```
.
├── GNU/
├── dataset/
│   ├── data/
│   └── mydataset/
├── readmydatset/
├── python model/
├── RML/
└── Presentation/
```

### `GNU/`

The practical implementation. It contains three folders:

1. **Captured signal files** – files captured from the dataset signals that are
   used in the practical part.
2. **GNU Radio simulation** – the practical modelling of the system using
   GNU Radio.
3. **SDR transmitter and receiver** – the transmitter and receiver flowgraphs
   used with the SDR board.

### `dataset/`

Contains two folders:

- **`data/`** – the dataset used in this work.
- **`mydataset/`** – MATLAB 2018 code that generates the dataset. The code
  includes the modulation types, and it allows other channels to be added.

### `readmydatset/`

Python code that reads the data generated in MATLAB.

### `python model/`

The deep learning models, in two folders:

- **Integrated models** – end-to-end models in which CFO prediction, signal
  correction and modulation classification are layers of a single network.
- **Separate models** – one model that predicts the CFO, and a second model
  that classifies the modulation type of the corrected signal.

### `RML/`

The RadioML dataset used in this work (RML2016.10a).

### `Presentation/`

The presentation of the project.

## Environments

| Part | Environment |
|---|---|
| Dataset generation | MATLAB 2018 |
| Python models | Google Colab with a T4 GPU runtime, and the institute server `notebook-Gpu` |
| Practical implementation | GNU Radio 3.10.10 |

## How to use

1. Generate the dataset by running the MATLAB code in `dataset/mydataset/`.
2. Read the generated data with the Python code in `readmydatset/`.
3. Train and evaluate the models in `python model/`, using the data in
   `dataset/data/` and `RML/`.
4. Run the GNU Radio simulation and the SDR transmitter and receiver in `GNU/`.
