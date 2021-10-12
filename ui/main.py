import time
import threading

import buttons
import hardware
import screen
import components.buttons as compButton
import components.menu as menu
import components.command as compCommand
import config as configReader
import logic.menuNavigator as navigator
import logic.renderChain as renderChain

dirtyEvent = threading.Event()
dirtyLock = threading.Lock()

chanButtonMap = {
        27: buttons.left,
        18: buttons.center,
        17: buttons.right
        }


def setDirty():
    with dirtyLock:
        dirtyEvent.set()


def main():
    config = configReader.Config.instance().getConfig()
    me = menu.Menu(setDirty)
    navi = navigator.MenuNavigator(config)
    me.setItems(navi.getOptions())
    button = buttons.Buttons()
    cb = compButton.Buttons(setDirty)
    chain = renderChain.RenderChain.instance()
    
    hardware.Hardware(lambda c: button.callButton(chanButtonMap[c]), lambda c: None)


    def setupScreen(screen):
        chain = renderChain.RenderChain.instance()
        chain.set(screen['pipeline'])

        buttonConfig = screen['buttons']
        for id in buttonConfig:
            button.setButton(id, buttonConfig[id][0], buttonConfig[id][1])

        cb.updateLabelsViaButton(button)
        setDirty()
    
    def functionCalled(item):
        if(item['_type'] == 'command'):
            setupScreen(screenConfig['command'])
            cc = compCommand.Command(setDirty)
            chain.add(cc)
            cc.run(item['command'])
    
    okButton = lambda: me.setItems(navi.goDown(me.getSelected()).getOptions()) if navi.getChildType(me.getSelected()) == 'item' else functionCalled(navi.getChild(me.getSelected()))

    screenConfig = {
            "main": {
                "buttons": {
                    buttons.left: ("prev", me.selectPrev),
                    buttons.center: ("next", me.selectNext),
                    buttons.right: ("OK", okButton)
                    },
                "pipeline": [cb, me]
                },
            "command": {
                "buttons": {
                    buttons.left: ("", lambda: None),
                    buttons.center: ("", lambda: None),
                    buttons.right: ("exit", lambda: setupScreen(screenConfig['main']))
                    },
                "pipeline": [cb]
                }
            }

    setupScreen(screenConfig['main'])

    disp = screen.Screen.instance()
    while True:
        if dirtyEvent.wait(timeout=10):
            with dirtyLock:
                disp.clear()
                chain.render()
                disp.render()
                dirtyEvent.clear()

if (__name__ == "__main__"):
    main()
