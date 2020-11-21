
from flask import render_template, url_for, request
from App.Api.CodeRunner import runcode
from App.Websockets.base import websockets, ws_login_required


from .base import dashboard



default_c_code = """#include <stdio.h>

int main(int argc, char **argv)
{
    printf("Hello C World!!\\n");
    return 0;
}    
"""

default_cpp_code = """#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    cout << "Hello C++ World" << endl;
    return 0;
}
"""

default_py_code = """import sys
import os

if __name__ == "__main__":
    print("Hello Python World!!")
"""

default_rows = "15"
default_cols = "60"


#@websockets.on("codeReview")
#    returns that tuple


@websockets.on('code-review')
@ws_login_required
def handle_code_review(message):
    code = message['code']
    lang = message['lang']
    if lang == 'C':
        run = runcode.RunCCode(code)
        rescompil, resrun = run.run_c_code()
    elif lang == 'py':
        run = runcode.RunPyCode(code)
        rescompil, resrun = run.run_py_code()
    elif lang == 'cpp':
        run = runcode.RunCppCode(code)
        rescompil, resrun = run.run_cpp_code()
    if resrun == 'No run done':
        resrun = rescompil
    websockets.emit('code-review-complete', resrun)


@websockets.on('lang-changed')
@ws_login_required
def handle_lang_changed(message):
    lang = message
    # print(lang)
    if lang == 'C':
        websockets.emit('lang-changed-returned', default_c_code)
    elif lang == 'py':
        websockets.emit('lang-changed-returned', default_py_code)
    elif lang == 'cpp':
        websockets.emit('lang-changed-returned', default_cpp_code)
    else:
        websockets.emit('lang-changed-returned', default_c_code)


@dashboard.route('/room', methods=['POST', 'GET'])
def handle_room():
    if request.method == 'POST':
        code = request.form['code']
        run = runcode.RunCCode(code)
        rescompil, resrun = run.run_c_code()
        if not resrun:
            resrun = 'No result!'
    else:
        code = default_c_code
        resrun = 'No result!'
        rescompil = ''
    return render_template("gameRoom.html",
                           code=code,
                           target="runc",
                           resrun=resrun,
                           rescomp=rescompil,
                           rows=default_rows,
                           cols=default_cols)
    #return render_template('gameRoom.html', title = 'Game Room')



