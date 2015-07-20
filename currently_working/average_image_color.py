from PIL import Image

def average_image_color(filename):

    i = Image.open('filename.ext')
    h = i.histogram()

    # split into red, green, blue
    r = h[0:255]
    g = h[255:255*2]
    b = h[255*2: 255*3]

    # perform the weighted average of each channel:
    # the *index* is the channel value, and the *value* is its weight
    return (
        sum( i*w for i, w in enumerate(r) ) / sum(r),
        sum( i*w for i, w in enumerate(g) ) / sum(g),
        sum( i*w for i, w in enumerate(b) ) / sum(b)
    )

if __name__ == '__main__':

    import sys

    if len(sys.argv) > 1:
       print 'Prints the average color of the image'
       print average_image_color(sys.argv[1])
    else:
      print 'usage: average_image_color.py FILENAME'
      print 'prints the average color of the image as (R,G,B) where R,G,B are between 0 and 255.'

    print 'Now for gray scaled image the average value is:'
