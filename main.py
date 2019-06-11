import sys
import random
from PIL import Image, ImageTk
from tkinter import Canvas, Frame, NW, Tk, ALL
from config import Config


class WonszCode(Canvas):
    def __init__(self, config):
        self.dimensions = config.get_window_size()
        print(self.dimensions["HEIGHT"])
        super().__init__(width=self.dimensions["WIDTH"], height=self.dimensions["HEIGHT"], background='black')

        self.config = config

        self.in_game = True
        self.snake_size = 2
        self.score = 0

        self.move_x = config.get_unit_size()
        self.move_y = 0

        self.items_list = [("item_" + str(x + 1) + ".png") for x in range(self.config.get_number_of_items())]
        self.items_images = []
        self.item_x = 150
        self.item_y = 150

        self.load_graphics()
        self.create_graphics()
        self.locate_item()
        self.bind_all("<Key>", self.on_key_pressed)
        self.after(config.get_game_speed(), self.on_timer)
        self.pack()

    def load_graphics(self):
        try:
            self.raw_image = Image.open("./static/head.png")
            self.head_up = ImageTk.PhotoImage(self.raw_image)
            self.head_left = ImageTk.PhotoImage(self.raw_image.rotate(90))
            self.head_down = ImageTk.PhotoImage(self.raw_image.rotate(180))
            self.head_right = ImageTk.PhotoImage(self.raw_image.rotate(270))

            self.raw_image = Image.open("./static/body.png")
            self.body = ImageTk.PhotoImage(self.raw_image)

            for item in self.items_list:
                self.raw_image = Image.open("./static/" + item)
                self.items_images.append(ImageTk.PhotoImage(self.raw_image))

        except IOError as e:
            print("Error: " + e)
            sys.exit(-1)

    def create_graphics(self):
        self.create_image(100, 100, image=self.head_up, anchor=NW, tag="head")
        self.create_image(100, 120, image=self.body, anchor=NW, tag="body")
        self.create_image(130, 100, image=self.items_images[0], anchor=NW, tag="item")
        # self.create_image(160, 100, image=self.items[1], anchor=NW, tag="head")
        # self.create_image(190, 100, image=self.items[2], anchor=NW, tag="head")

    def locate_item(self):
        item = self.find_withtag("item")
        self.delete(item[0])

        new_item = random.randint(0, self.config.get_number_of_items()-1)

        position = random.randint(0, self.dimensions["WIDTH"]/self.config.get_unit_size())
        self.item_x = position * self.config.get_unit_size()
        position = random.randint(0, self.dimensions["HEIGHT"]/self.config.get_unit_size())
        self.item_y = position * self.config.get_unit_size()

        self.create_image(self.item_x, self.item_x, anchor=NW, image=self.items_images[new_item], tag="item")

    def on_key_pressed(self):
        pass

    def on_timer(self):
        pass


class MegaWonsz(Frame):
    def __init__(self, config):
        super().__init__()
        self.master.title("MegaWonsz9")
        self.board = WonszCode(config)
        self.pack()


def main():
    config = Config()
    root = Tk()
    game = MegaWonsz(config)
    root.mainloop()

if __name__ == '__main__':
    main()