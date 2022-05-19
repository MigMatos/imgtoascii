import cv2
import os
import time
import io
from matplotlib.pyplot import title
from convertimg import unicode_img
import asyncio

#this convert video to img

def ascii_frame(filename,start,limited=False):
    filename = filename
    vidcap = cv2.VideoCapture(f'ytd/{filename}')
    framerate = vidcap.get(cv2.CAP_PROP_FPS)
    success,image = vidcap.read()
    count = 0
    frames = 0
    cache_txt = ""
    framepass = framerate/2
    while success:
        #cv2.imwrite("frames/frame%d.jpg" % count, image)     # save frame (optional)
        is_success, buffer = cv2.imencode(".jpg", image)
        w,h,c = image.shape
        #print(w,h) 
        io_buf = io.BytesIO(buffer)
        timenow = time.time() - start
        timesleeped = (60 / framerate) * 0.001
        frames = count/framerate
        converted_unicode = unicode_img(io_buf,w,h)
        txt_pt = f"\n{converted_unicode}\n"
        extrainfo = f"[FPS:{framerate/2} | TimeLapsed: {round(float(timenow),2)} | Frame: {round(float(frames),2)}]"
        #print(txt_pt,extrainfo)
        if int(framepass) == int(count+1) or count == 0:
            if cache_txt != txt_pt:
                finaltxt = txt_pt + extrainfo
                print(txt_pt) #frame print (opcionally)
            cache_txt = txt_pt
        success,image = vidcap.read()
        if frames <= timesleeped:
            try:
                time.sleep(timenow - frames)
            except:
                pass
        elif (timenow - frames) < 0:
            time.sleep(frames - timenow)
        #print(frames, " --- ", timenow, " // ", timenow - frames, " FPS: ",framerate)
        count += 1
        if limited == True:
            if int(framepass) == count:
                framepass = framepass + (framerate/2)
        else:
            framepass = count
        
