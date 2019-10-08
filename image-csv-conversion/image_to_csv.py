import numpy as np
import sys

from skimage import filters, io

def image_to_csv(image_array: np.ndarray, output_filename: str):
    with open(output_filename, "w") as f:
        for row in image_array:
            output_string = ''
            for pixel in row:
                output_string += str(pixel) + ','

            output_string = output_string[:-2]
            output_string += '\n'
            f.write(output_string)

def load_and_convert(filename):
    image = io.imread(filename + '.jpg')
    image_to_csv(image, filename + '.csv')
    # note: filters.sobel_v uses the following kernel:
    # 1   0  -1
    # 2   0  -2
    # 1   0  -1
    # source: https://scikit-image.org/docs/dev/api/skimage.filters.html#skimage.filters.sobel_v
    edges = filters.sobel_v(image)
    io.imsave(filename + '-expected-sobel-v.jpg', edges)
                
def main():
    if len(sys.argv) < 2:
        print("usage:", sys.argv[0], "file-to-convert.jpg")
        sys.exit(1)
    load_and_convert(''.join(sys.argv[1].split('.')[0]))

if __name__ == "__main__":
    main()