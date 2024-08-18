from fastapi import APIRouter, FastAPI
import sharp_aquos_rc
from dotenv import load_dotenv

import os

load_dotenv()
IP = os.getenv('IP')
PORT = int(os.getenv('PORT'))
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

app = FastAPI()
router = APIRouter(prefix='/aquos')
aquos = sharp_aquos_rc.TV(IP, PORT, USERNAME, PASSWORD, command_map='jp')

success_response = {"success": True}
fail_response = {"success": False}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@router.get('/toggle_power')
async def toggle_power():
    try:
        print(aquos.power())
        res = aquos.power(1)
        if res == False:
            res2 = aquos.power(0)
            if res2 == False:
                return fail_response
            return {
                "success": True,
                "power": "Off"
            }
        else:
            return {
                "success": True,
                "power": "On"
            }
    except:
        return fail_response
    
@router.get('/arrow')
async def arrow(direction: str = 'up'):
    try:
        if direction == 'up':
            aquos.remote_button('up')
            return success_response
        elif direction == 'down':
            aquos.remote_button('down')
            return success_response
        elif direction == 'left':
            aquos.remote_button('left')
            return success_response
        elif direction == 'right':
            aquos.remote_button('right')
            return success_response
        return fail_response
    except:
        return fail_response
    
@router.get('/enter')
async def enter():
    try:
        aquos.remote_button('enter')
        return success_response
    except:
        return fail_response
    
@router.get('/back')
async def back():
    try:
        aquos.remote_button('return')
        return success_response
    except:
        return fail_response
    
@router.get('/exit')
async def exit():
    try:
        aquos.remote_button('exit')
        return success_response
    except:
        return fail_response
    
@router.get('/volume')
async def volume(direction: str = 'up'):
    try:
        if direction == 'up':
            aquos.volume_up()
            return success_response
        elif direction == 'down':
            aquos.volume_down()
            return success_response
        return fail_response
    except:
        return fail_response

@router.get('/toggle_mute')    
async def toggle_mute():
    try:
        aquos.mute('0')
        return success_response
    except:
        return fail_response
    
@router.get('/channel')
async def channel(input: str = ''):
    channel_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    try:
        if input == 'up':
            aquos.remote_button('channel_up')
            return success_response
        elif input == 'down':
            aquos.remote_button('channel_down')
            return success_response
        elif input == 'list':
            aquos.remote_button('channels')
            return success_response
        elif input in channel_list:
            aquos.remote_button('ch_' + input)
            return success_response
        else:
            return fail_response
    except:
        return fail_response
    
@router.get('/cc')
async def cc():
    try:
        aquos.remote_button('cc')
        return success_response
    except:
        return fail_response
    
@router.get('/menu')
async def menu():
    try:
        aquos.remote_button('menu')
        return success_response
    except:
        return fail_response
        
@router.get('/color')
async def color(col: str = ''):
    color_list = ['red', 'green', 'blue', 'yellow']
    try:
        if col in color_list:
            aquos.remote_button(col)
            return success_response
        return fail_response
    except:
        return fail_response
    
@router.get('/third-party')
async def third_party(service: str = ''):
    service_list = ['netflix', 'youtube', 'u-next', 'prime']
    try:
        if service in service_list:
            aquos.remote_button(service)
            return success_response
        return fail_response
    except:
        return fail_response

@router.get('/d-button')
async def d_button():
    try:
        aquos.remote_button('d-button')
        return success_response
    except:
        return fail_response
    
@router.get('/tv-mode')
async def tv_mode(mode: str = ''):
    tv_modes = ['t-d', 'bs', 'cs', 'bs4k']
    try:
        if mode in tv_modes:
            aquos.remote_button(mode)
            return success_response
        return fail_response
    except:
        return fail_response
    
@router.get('/sleep')
async def sleep(time: str = ''):
    time_list = ['off', '30', '60', '90', '120']
    try:
        if time in time_list:
            i = time_list.index(time)
            aquos.sleep(i)
            return success_response
        return fail_response
    except:
        return fail_response

app.include_router(router)