# -*- coding:utf-8 -*- 
# Author R. Bryan Sanchez M. 
#  by :> RTkw0rk3r
import sys
import os


# import colorama
# import operative system 
# 

import time
from termcolor import colored

# term color 
#import movie.convert as mov
import moviepy.editor as mvc

# from moviepy.editor import * as mvc

# lib compresor de imagenes y editor de videos una libreria que trabaja a nivel de control de ffmpg ademas del control que este mantine 
# con el control de sistema 
# esclareciendo asi otro tipo de segmento de a nivel de construccion  de este tipo de ideas



def makeconverter(example):
    # "___name__function _is sample text to file document"
    #if os.system(dir('example')):

    if  os.path.exists(example):
        print("\033[1;30;46m file \033[0m :> {}".format(example))
        print("processing to file") 
        time.sleep(0.5)
        make = os.path.basename(example)

        # if make == '.mp4':
        
        # m_video = mvc.VideoFileClip(sys.argv[1])
        m_video = mvc.VideoFileClip(example)
        m_video.audio.write_audiofile(make.replace('.mp4','.mp3'))
        print("\033[1;30;10m video convert...\033[0;m")
        sys.exit(0)
    # else:
    #    print('files movie not compress, or other extencion type movie')
    #    sys.exit(1)

    else:
        print("\033[1;43;31m file not found -->  {} example  :>\033[0m /u/v/file.ext".format(example) ,end ="...\n")
        sys.exit(1)

#worm segment not  create transform collective  


if __name__ == "__main__":
    makeconverter(str(sys.argv[1]))
    
