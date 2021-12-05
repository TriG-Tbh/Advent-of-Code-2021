import sys
from colorama import Fore, Back, Style
import contextlib, io
import traceback
import difflib

from functools import wraps

renderall = []

global toggle_off
toggle_off = False

global success
global failure
global total
success = 0
failure = 0
total = 0

def toggle():
    global toggle_off
    toggle_off = not(toggle_off)

def test(stdin=None, stdout=None):
    
    if stdin is None:
        stdin = ""
    if stdout is None:
        raise TypeError("function test missing output data to compare to")
        return
    def decorate(function):
        @wraps(function)
        def inner(*args, **kwargs):
            global success, failure, total
            f = io.StringIO()

            #err = io.StringIO()
            raised = False
            error = ""
            with contextlib.redirect_stdout(f):
                try:
                    function(stdin)
                except Exception as e:    
                    exc_type, exc_value, exc_tb = sys.exc_info()
                    tb = traceback.TracebackException(exc_type, exc_value, exc_tb)
                    error = (''.join(tb.format_exception_only()))
                    raised = True
            output = f.getvalue()

            if output.endswith("\n"):
                output = "\n".join(output.split("\n")[:-1])

            if raised:
                
                print("[ " + Fore.RED + Style.BRIGHT + "X" + Style.RESET_ALL + " ] Test failed: " + Fore.RED + Style.BRIGHT + function.__name__ + Style.RESET_ALL)
                print("\t" + Fore.RED + Style.BRIGHT + "Exception raised\n\t" + Style.RESET_ALL + str(error))
                
                failure += 1
            elif stdout != output:
                print("[ " + Fore.RED + Style.BRIGHT + "X" + Style.RESET_ALL + " ] Test failed: " + Fore.RED + Style.BRIGHT + function.__name__ + Style.RESET_ALL)
                expectedlines = stdout.split("\n")
                print("\tExpected: ", end="")
                print(expectedlines[0])
                for line in expectedlines[1:]:
                    print("\t          " + line)

                chars = []
                
                difference = [c for c in difflib.ndiff(stdout, output)]
                out = False
                for c in difference:
                    mod = c[0]
                    char = c[-1]
                    if mod == "+" and not out:
                        chars.append(Back.RED)
                        chars.append(Style.BRIGHT)
                        out = True
                    if mod == " " and out:
                        chars.append(Style.RESET_ALL)
                        out = False
                    if mod != "-":
                        chars.append(char)
                chars.append(Style.RESET_ALL)

                returned = "".join(chars)
                rlines = returned.split("\n")
                print("\tReturned: ", end="")
                print(rlines[0])
                for line in rlines[1:]:
                    print("\t          " + line)
                failure += 1
            else:
                print("[ " + Fore.GREEN + Style.BRIGHT + "✓" + Style.RESET_ALL + " ] Test passed: " + Fore.GREEN + Style.BRIGHT + function.__name__ + Style.RESET_ALL)
                success += 1
            total += 1
        renderall.append(inner)
        return inner
    return decorate

def render():
    
    global success, failure, total, toggle_off
    if not toggle_off:
        print("[ " + Style.BRIGHT + "*" + Style.RESET_ALL + " ] Beginning tests\n---")
        for config in renderall:
            config()

        print("---\n[ " + Style.BRIGHT + "*" + Style.RESET_ALL + " ] " + "All tests complete.")
        color = ""
        if total == 0:
            color = Fore.GREEN
        elif int(success / total) == 1:
            color = Fore.GREEN
        elif success == 0:
            color = Fore.RED
        
        print(color + Style.BRIGHT + "[ * ] " + str(success) + "/" + str(total) + " tests passed." + Style.RESET_ALL)