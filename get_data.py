import os
import requests
import argparse

def get_list(shortname):
    res = requests.get("https://cs7ns1.scss.tcd.ie", params={'shortname': shortname})
    raw = res.content
    file_list = raw.decode('utf-8').split(',\n')
    return file_list


def get_img(shortname, file_name):
    res = requests.get("https://cs7ns1.scss.tcd.ie", params={'shortname': shortname, 'myfilename': file_name})
    image_data = res.content
    with open(f"captchas/{file_name}.png", "wb") as file:
        file.write(image_data)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--shortname', help='Shortname of the user to grab the files for', type=str)
    args = parser.parse_args()

    if args.shortname is None:
        print("Please specify a shortname")
        exit(1)

    os.makedirs('captchas', exist_ok=True)
    file_listing = get_list(args.shortname)
    for file_name in file_listing:
        get_img(args.shortname, file_name)

if __name__ == '__main__':
    main()
