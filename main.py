from pyglet.window import mouse
from pyglet.window import key
from life import Life
import itertools
import pyglet

IMG_SIZE = 8
SIZE = 800//IMG_SIZE
game = Life(SIZE)

window = pyglet.window.Window(height=800, width=800)


@window.event
def on_draw():
    window.clear()
    batch = pyglet.graphics.Batch()
    batch_sprites = []
    for i, j in itertools.product(range(SIZE), repeat=2):
        if game.grid[i][j]:
            x, y = j*IMG_SIZE, 784-i*IMG_SIZE
            batch_sprites.append(pyglet.sprite.Sprite(pyglet.image.load(f'life{IMG_SIZE}.png'), x, y, batch=batch))
    batch.draw()


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        game.change_life(x // IMG_SIZE, SIZE - 1 - y // IMG_SIZE)


@window.event
def on_key_press(symbol, modifiers):
    global game
    if symbol == key.N:
        game = Life(800//IMG_SIZE)


@window.event
def on_text(text):
    if text == ' ':
        game.iterate()


def main():
    pyglet.app.run()


if __name__ == '__main__':
    main()
