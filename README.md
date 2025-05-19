# 🔐 CAPTCHA Recognition with TensorFlow Lite

This project focuses on recognizing text from CAPTCHA images using lightweight TensorFlow Lite models. It includes preprocessing steps, grayscale conversion, and classification pipelines optimized for fast, resource-efficient inference ideal for deployment on mobile or embedded systems.

## 🎯 Objectives

- Convert and preprocess CAPTCHA images (e.g., grayscale, resizing)
- Classify individual characters using `.tflite` models
- Generate predictions and output decoded CAPTCHA text

## 🗂️ Project Structure

| File               | Description |
|--------------------|-------------|
| `classify.py`      | Main script for classifying individual CAPTCHA characters using a `.tflite` model. |
| `classify_lite.py` | Lightweight version for rapid testing or constrained environments. |
| `convert.py`       | Converts CAPTCHA images to grayscale and formats them for model input. |
| `generate.py`      | Combines model outputs to generate full CAPTCHA predictions. |
| `get_data.py`      | Handles loading and structuring of CAPTCHA image datasets. |
| `.tflite` models   | Pretrained TFLite models (`grayscale`, `proper2`, `proper3`, etc.) optimized for recognizing CAPTCHA characters. |

## 🧪 Example Usage

### 1. Classify a single CAPTCHA character

```bash
python classify.py --model proper2.tflite --image captcha_char.png
```
### 2. Convert full CAPTCHA image to grayscale
```bash
python convert.py --input raw_captcha.png --output grayscale_output.png  
```

### 3. Predict entire CAPTCHA string
```bash
python generate.py --model proper2.tflite --captcha path/to/captcha.png
```

## 🛠️ Dependencies

- Python
- TensorFlow Lite Runtime
- NumPy
- Pillow

### Install via pip:

```bash
pip install numpy pillow tflite-runtime
```
🔍 Model Info

## Multiple .tflite models are provided:

- grayscale.tflite: For grayscale image classification.
- proper2.tflite & proper3.tflite: Refined versions for better character recognition accuracy.

## 🚀 Future Improvements

- Add segmentation logic for multi-character CAPTCHA images
- Integrate with OCR pipelines or web scraping tools
- Deploy as a microservice (e.g., Flask or FastAPI backend)

## Author 

### Atharva Devne ###





