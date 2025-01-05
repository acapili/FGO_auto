from PIL import Image

class color_sensing:

    def get_max_rgb(self, image_path, box):
        with Image.open(image_path) as img:
            cropped_img = img.crop(box)
            pixels = list(cropped_img.getdata())

            # # Display the cropped image for verification
            # cropped_img.show(title="Cropped Image")

            total_r, total_g, total_b = 0,0,0
            for pixel in pixels:
                r,g,b = pixel[:3]
                total_r += r
                total_g += g
                total_b += b

            my_list = [total_r, total_g, total_b]

            if my_list[0] > my_list[1] and my_list[0] > my_list[2]:
                return 0
            if my_list[1] > my_list[2] and my_list[1] > my_list[0]:
                return 1
            if my_list[2] > my_list[1] and my_list[2] > my_list[0]:
                return 2
            else:
                print("Card typing is unknown")

    