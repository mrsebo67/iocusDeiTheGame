import pyglet
import scenes.mainScene as mainScene

window = pyglet.window.Window(fullscreen=True)
fps_display = pyglet.window.FPSDisplay(window=window)



#test github and vscode on windows

def update(dt):
    mainScene.update()

@window.event
def on_draw():
    window.clear()
    mainScene.draw()
    label.draw()
    fps_display.draw()

    


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/60.0)

    mainScene = mainScene.MainScene(window)
    label = pyglet.text.Label("Bok Decki", font_size=35, y = 900)
    label.x = (window.width // 2) - (label.content_width // 2)

    pyglet.app.run()

