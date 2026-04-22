# CAPTCHA Recognition with TensorFlow Lite

This project trains a CNN to recognize text from CAPTCHA images and exports it as a TensorFlow Lite model for fast, lightweight inference on CPU, mobile, or embedded devices.

## Project Structure

| File | Description |
|------|-------------|
| `generate.py` | Generates synthetic CAPTCHA images for training/validation datasets |
| `train.py` | Trains a CNN model on generated CAPTCHA images (supports GPU and CPU) |
| `convert.py` | Converts a trained Keras `.h5` model to TensorFlow Lite `.tflite` format |
| `classify.py` | Classifies CAPTCHAs using a full Keras model (`.json` + `.h5`) |
| `classify_lite.py` | Classifies CAPTCHAs using a TFLite model (faster, no full TF required) |
| `get_data.py` | Downloads CAPTCHA images from a remote server |
| `symbols.txt` | Character set used for CAPTCHA generation and recognition |
| `*.tflite` | Pretrained TFLite models ready for inference |

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### 1. Generate training data

```bash
python generate.py \
  --width 128 --height 64 \
  --upper-length 6 --lower-length 4 \
  --count 10000 \
  --output-dir train_data/ \
  --symbols symbols.txt \
  --dict-name train_dict.txt
```

### 2. Train the model

```bash
python train.py \
  --width 128 --height 64 --length 6 \
  --batch-size 32 --epochs 20 \
  --train-dataset train_data/ \
  --validate-dataset validate_data/ \
  --output-model-name my_model \
  --symbols symbols.txt \
  --train-dict train_dict.txt \
  --validate-dict validate_dict.txt
```

> Automatically uses GPU if available, falls back to CPU otherwise.

### 3. Convert to TFLite

```bash
python convert.py --model-name my_model --output my_model_lite
```

### 4. Classify CAPTCHAs with TFLite model

```bash
python classify_lite.py \
  --model-name my_model_lite \
  --captcha-dir captchas/ \
  --output results.txt \
  --symbols symbols.txt \
  --shortname myname
```

### 5. Classify CAPTCHAs with full Keras model

```bash
python classify.py \
  --model-name my_model \
  --captcha-dir captchas/ \
  --output results.txt \
  --symbols symbols.txt
```

## Pretrained Models

Four `.tflite` models are included for immediate use:

- `grayscale.tflite` / `greyscale2.tflite` — trained on grayscale-preprocessed CAPTCHAs
- `proper2.tflite` / `proper3.tflite` — refined versions with improved accuracy

## Author

Atharva Devne
