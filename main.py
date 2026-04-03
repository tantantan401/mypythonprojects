"""
Copyright© for Hu ShuWen(Internet Name: sche)
2026/4/3 16:33
"""

import tkinter as tk
from tkinter import ttk
from datetime import datetime
import inspect
import functools

class df:
    """
    A class saved variables for class 'autoTk' to use.
    """
    tcbtext = "\033[1;31m[TRACEBACK]\033[0m"
    errtext = "\033[1;31m[ERROR]\033[0m"
    inftext = "\033[1;33m[INFO]\033[0m"
    def getTime():
        return f"\033[1;34m{datetime.now().strftime('%Y-%m-%d/%H:%M')}\033[0m"
    class winds:
        bws = f"\033[1;32mBuilt Window Successed\033[0m"
        bwsinftext = f"\033[1;32m[INFO]\033[0m"

class autoTk:
    """
    A class it implements auto call tk.Tk() objects' function mainloop()
    And added some new auto function.
    >>> with autoTk(True) as window:
    >>>     window.title("Test Window")
    >>> # There will call mainloop()
    
    **The Example of function logf:**
    
    >>> @auto.logf
    >>>     def swhenClicked():
    >>>         print("Button Clicked!")
    >>> # This decorator will print to the terminal "{df.winds.bwsinftext} {df.getTime()} {df.fustext}" when function whenClicked ended.
    >>> btn = ttk.Button(window, text="Click Me!", command=whenClicked)
    >>> btn.pack()
    """
    def __init__(self, isLog: bool):
        self.isLog = isLog
        self.mw = tk.Tk()
        
    def __enter__(self):
        return self.mw
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.isLog:
            if traceback is not None:
                print(f"{df.tcbtext} {df.getTime()} {traceback}")
            else:
                print(f"{df.winds.bwsinftext} {df.getTime()} {df.winds.bws}")
                self.mw.mainloop()
        
    times = 1
    maxt = 15
        
    @staticmethod
    def logf(func):
        """
        A log function for autoTk objects'.\n
        **This decorator will label the function a callback function!**\n
        **The output will like this:**\n
        *(Call This Function)*\n
        **Output**: Callback Function *{functioname}* Ran Successed.
        """
        sig = inspect.signature(func)
        hva = False
        hvk = False
        for p in sig.parameters.values():
            if p.kind == p.VAR_POSITIONAL:
                hva = True
            if p.kind == p.VAR_KEYWORD:
                hvk = True
        @functools.wraps(func)
        def inner(*args, **kwargs):
            try:
                if hva or hvk:
                    func(*args, **kwargs)
                else:
                    bound = sig.bind(*args, **kwargs)
                    bound.apply_defaults()
                    func(*bound.args, **bound.kwargs)
            except Exception as err:
                print(f"{df.errtext} {df.getTime()} {str(err)}")
                return 1
            else:
                autoTk.times += 1
                if "when" in func.__name__.lower():
                    global iscf
                    iscf = True
                else:
                    iscf = False
                fustext = f"\033[1;32m{'' if iscf == False else "Callback "}Function '{func.__name__}' Ran Successed\033[0m"
                if not autoTk.times > autoTk.maxt:
                    print(f"{df.winds.bwsinftext} {df.getTime()} {fustext}")
                else:
                    import os
                    os.system("cls")
                    print(f"{df.winds.bwsinftext} {df.getTime()} {fustext}")
                    autoTk.times = 1
        return inner
            
with autoTk(True) as window:
    autoTk.maxt = 3
    window.title("Test Window")
    window.geometry("800x600")
    @autoTk.logf
    def whenClicked():
        ...
    btn = ttk.Button(window, text="Click Me!", command=whenClicked)
    btn.pack()