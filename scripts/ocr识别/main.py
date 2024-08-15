import easyocr


if __name__ == "__main__":

    reader = easyocr.Reader(['en', 'ch_sim'])
    result = reader.readtext("cropped_image_mJiMWOx.png")
    for (text, bbox, confidence) in result:
        # print(text, bbox, confidence)
        print(bbox)
