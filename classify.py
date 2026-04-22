#!/usr/bin/env python3

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

import os
import cv2
import numpy
import argparse
import tensorflow as tf
import tensorflow.keras as keras

def decode(characters, y):
    y = numpy.argmax(numpy.array(y), axis=2)[:,0]
    return ''.join([characters[x] for x in y])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model-name', help='Model name to use for classification', type=str)
    parser.add_argument('--captcha-dir', help='Where to read the captchas to break', type=str)
    parser.add_argument('--output', help='File where the classifications should be saved', type=str)
    parser.add_argument('--symbols', help='File with the symbols to use in captchas', type=str)
    args = parser.parse_args()

    if args.model_name is None:
        print("Please specify the CNN model to use")
        exit(1)

    if args.captcha_dir is None:
        print("Please specify the directory with captchas to break")
        exit(1)

    if args.output is None:
        print("Please specify the path to the output file")
        exit(1)

    if args.symbols is None:
        print("Please specify the captcha symbols file")
        exit(1)

    symbols_file = open(args.symbols, 'r')
    captcha_symbols = symbols_file.readline().strip()
    captcha_symbols = captcha_symbols + '&'
    symbols_file.close()

    print("Classifying captchas with symbol set {" + captcha_symbols + "}")

    with tf.device('/cpu:0'):
        with open(args.output, 'w') as output_file:
            json_file = open(args.model_name+'.json', 'r')
            loaded_model_json = json_file.read()
            json_file.close()
            model = keras.models.model_from_json(loaded_model_json)
            model.load_weights(args.model_name+'.h5')
            model.compile(loss='categorical_crossentropy',
                          optimizer=keras.optimizers.Adam(1e-3, amsgrad=True),
                          metrics=['accuracy'])

            for x in os.listdir(args.captcha_dir):
                # load image and preprocess it (grayscale + Otsu threshold, matching train.py)
                raw_data = cv2.imread(os.path.join(args.captcha_dir, x))
                grey_data = cv2.cvtColor(raw_data, cv2.COLOR_BGR2GRAY)
                _, thresh = cv2.threshold(grey_data, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
                image = numpy.array(thresh, dtype=numpy.float32) / 255.0
                (h, w) = image.shape
                image = image.reshape([-1, h, w, 1])
                prediction = model.predict(image)
                output_file.write(x + ", " + (decode(captcha_symbols, prediction).replace('&', '')) + "\n")

                print('Classified ' + x)

if __name__ == '__main__':
    main()
