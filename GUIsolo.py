#!/usr/bin/env python
import sys
import datetime
import time
import PySimpleGUI as sg
##
sg.theme('Default1')

# ------ Column Definition ------ #
column1 = [[sg.Text('Column 1', justification='center', size=(10, 1))],
           [sg.Spin(values=('Spin Box 1', '2', '3'),
                    initial_value='Spin Box 1')],
           [sg.Spin(values=('Spin Box 1', '2', '3'),
                    initial_value='Spin Box 2')],
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]

layout = [
    [sg.Frame(layout=[
        [sg.CBox('Motor 1', default= False,size=(8,1)),
         sg.CBox('Motor 2', default= False,size=(8,1)),
         sg.CBox('Motor 3', default= False,size=(8,1)),
         sg.CBox('Motor 4', default= False,size=(8,1)),
         sg.CBox('Motor 5', default= False,size=(8,1)),
         sg.CBox('Motor 6', default= False,size=(8,1)),
         sg.CBox('Motor 7', default= False,size=(8,1)),
         sg.CBox('Motor 8', default= False,size=(8,1)),
         sg.CBox('Motor 9', default= False,size=(8,1)),
         sg.CBox('Motor 10',default= False,size=(8,1)),
         sg.CBox('Motor 11',default= False,size=(8,1)),
         sg.CBox('Motor 12',default= False,size=(8,1)),
         sg.Button('Send',size=(10,1))]]
         ,title='ON/OFF Toggles', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
    [sg.Frame(layout = [
        [sg.Slider(range=(0, 100), orientation='v', size=(20, 60), default_value=0, tick_interval=25),
         sg.Slider(range=(0, 100), orientation='v', size=(20, 60), default_value=0, tick_interval=25),
         sg.Slider(range=(0, 100), orientation='v', size=(20, 60), default_value=0, tick_interval=25),
         sg.Slider(range=(0, 100), orientation='v', size=(20, 60), default_value=0, tick_interval=25),
         sg.Slider(range=(0, 100), orientation='v', size=(20, 60), default_value=0, tick_interval=25),
         sg.Slider(range=(0, 100), orientation='v', size=(20, 60), default_value=0, tick_interval=25),
         sg.Slider(range=(0, 100), orientation='v', size=(20, 60), default_value=0, tick_interval=25),
         sg.Slider(range=(0, 100), orientation='v', size=(20, 60), default_value=0, tick_interval=25),
         sg.Slider(range=(0, 100), orientation='v', size=(20, 60), default_value=0, tick_interval=25),
         sg.Slider(range=(0, 100), orientation='v', size=(20, 60), default_value=0, tick_interval=25),
         sg.Slider(range=(0, 100), orientation='v', size=(20, 60), default_value=0, tick_interval=25),
         sg.Slider(range=(0, 100), orientation='v', size=(20, 60), default_value=0, tick_interval=25)]]
         ,title='Max/Min Speed Control', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
    [sg.Frame(layout = [
        [sg.Text('M1: '),sg.InputText('',size=(7,1)),
        sg.Text('M2: '),sg.InputText('', size=(7,1)),
        sg.Text('M3: '),sg.InputText('', size=(7,1)),
        sg.Text('M4: '),sg.InputText('', size=(7,1)),
        sg.Text('M5: '),sg.InputText('', size=(7,1)),
        sg.Text('M6: '),sg.InputText('', size=(7,1)),
        sg.Text('M7: '),sg.InputText('', size=(7,1)),
        sg.Text('M8: '),sg.InputText('', size=(7,1)),
        sg.Text('M9: '),sg.InputText('', size=(7,1)),
        sg.Text('M10:'),sg.InputText('', size=(7,1)),
        sg.Text('M11:'),sg.InputText('', size=(7,1)),
        sg.Text('M12:'),sg.InputText('', size=(7,1))]]
        ,title='Postion Control', relief=sg.RELIEF_SUNKEN)]
]
#
window = sg.Window('ODRIVE Motor Control Board', layout,
    default_element_size=(100, 100), grab_anywhere=False)
#
motor_state = [0,0,0,0,0,0]
motor_speed = [0,0,0,0,0,0]
motor_rotation = [0,0,0,0,0,0]

while True:
    now = datetime.datetime.now()
    event, values = window.read()
    print(now.strftime("%H:%M:%S"), values)
   
    guiData = str(values)
    guiData = guiData.translate({ord('['): None})
    guiData = guiData.translate({ord(']'): None})
    guiData = guiData.translate({ord(','): None})
    
    data = guiData.split()
    motor_state[0:11] = data[0:11]
    motor_speed[0:11] = data[12:23]
    motor_rotation[0:11] = data[24:35] 
    
    if values == None:
        sys.exit()

