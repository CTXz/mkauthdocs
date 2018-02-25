# Copyright (c) 2018 Patrick Pedersen <ctx.xda@gmail.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import glob
import argparse
import pkg_resources

## Generate PHP Session Guard ##
def generate_session_guard(redirect):
    calibration = ''
    for directory in os.path.dirname(redirect).split('/'):
        if directory:
            calibration += '../'

    with open(pkg_resources.resource_filename('mkauthdocs', 'templates/session_guard_template.php'), 'r') as f:
        template = f.read()
        template = template.replace('{calibration}', calibration)
        return template.replace('{redirect}', redirect)

## Generate Login Page
def generate_login_page(heading, username, password):
    with open(pkg_resources.resource_filename('mkauthdocs', 'templates/login_template.php'), 'r') as f:
        template = f.read()
        template = template.replace('{heading}', heading)
        template = template.replace('{username}', username)

        return template.replace('{password}', password)

def main():

    ## Handle arguments ##

    parser = argparse.ArgumentParser()

    parser.add_argument('username',  help="Username used for authentication")                          # Username Argument (-u | --username)
    parser.add_argument('password',  help="Password used for authentication")                          # Password Argument (-p | --password)
    parser.add_argument('build_dir', help="Path to build output directory")                            # Docs Dir
    parser.add_argument('--heading', help="Heading on login page (default: 'Login')", default="Login") # Login page heading

    args = parser.parse_args();

    ## Modify Build Dir ##

    # Check if build_dir exists
    if not os.path.exists(args.build_dir):
        print("mkauthdocs: '" + args.build_dir + "' No such file or directory")
        exit(-1);

    # Check if build_dir is really a mkdocs build
    if not os.path.exists(args.build_dir + "/mkdocs"):
        print("mkauthdocs: '" + args.build_dir + "' does not appear to be a mkdocs build directory!")
        exit(-1);

    # Append php session guard to the beginning of every file
    for root, dirs, files in os.walk(args.build_dir):
        for file in files:
            if file.endswith(".html"):
                f_path = os.path.join(root, file)
                f_base = os.path.splitext(f_path)[0]

                with open(f_path, 'r+') as f:
                    f_content = f.read()
                    f.seek(0, 0)
                    f.write(generate_session_guard(os.path.relpath(f_base, args.build_dir) + ".php") + f_content)
                    f.close()

                os.rename(f_path, f_base + ".php") # Change extension from .html to .php

    # Generate Login Page
    with open(args.build_dir + '/login.php', 'w+') as f:
        f.write(generate_login_page(args.heading, args.username, args.password))
        f.close()
