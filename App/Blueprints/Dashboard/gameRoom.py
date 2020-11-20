from flask import render_template, url_for, request
from App.Api.CodeRunner import runcode

from .base import gameRoom


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
    print "Hello Python World!!"
"""

default_rows = "15"
default_cols = "60"


@gameRoom.route('/room', methods=['POST', 'GET'])
def handle_index():
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
                           rows=default_rows, cols=default_cols)
    #return render_template('gameRoom.html', title = 'Game Room')
    


