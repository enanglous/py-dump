from PIL import Image, ImageFilter

# img = Image.open("./Pokedex/210 - pikachu.jpg")
# filtered_img = img.convert('RGB').filter(ImageFilter.SHARPEN)
# cropped = filtered_img.crop((100, 100, 400, 400))
# cropped.save("cropped.png", "png")


img = Image.open("212 - astro.jpg")
img.thumbnail((400, 400))
img.save("thumbnail.jpg")
