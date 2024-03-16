from PIL import Image


def resize_image(input_path, output_path, size):
    with Image.open(input_path) as image:
        resized_image = image.resize(size, Image.Resampling.LANCZOS)
        resized_image.save(output_path)


# Example usage
resize_image(
    r"C:\Users\97252\Documents\בוטקאמפ\botP\screenshots\Screenshot 2023-11-13 174608.png",
    r"C:\Users\97252\Documents\בוטקאמפ\botP\screenshots\end_game.png",
    (640, 450),
)
