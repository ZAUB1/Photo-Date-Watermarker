from PIL import Image;
from PIL import ImageDraw;
from PIL import ImageFont;
import glob;
import os;

IMAGE_EXTENSIONS = ["jpg", "png"];

def waterImage(incoming):
    photo = Image.open(incoming);
    draw = ImageDraw.Draw(photo);
    exifs = photo._getexif()[36867]

    blk = (224, 159, 54);
    font = ImageFont.truetype("arial.ttf", 140);

    draw.text((30, 0), exifs, fill = blk, font = font);
    photo.save("./rendered/" + incoming);
    print("-> Rendered: " + incoming)

def main():
    os.chdir("./");
    os.mkdir("rendered");

    for ext in IMAGE_EXTENSIONS:
        for file in glob.glob("*." + ext):
            print("-> Marking: " + file);
            waterImage(file);

    print("Jobs done.");

main();
