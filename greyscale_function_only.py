def greyscale(img, height, width):
    resized_img = cv2.resize(img,(height,width),interpolation=cv2.INTER_CUBIC)
    return cv2.cvtColor(resized_img,cv2.COLOR_RGB2GRAY)