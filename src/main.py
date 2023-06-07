import pyglet
import scenes.mainScene as mainScene


window = pyglet.window.Window(fullscreen=True)


#test github and vscode on windows

def update(dt):
    mainScene.update()

@window.event
def on_draw():
    window.clear()
    mainScene.draw()


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/1.0)

    mainScene = mainScene.MainScene(window)

    pyglet.app.run()

