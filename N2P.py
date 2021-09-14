import argparse
import os
import subprocess

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description='This tool converts your ipynb notebooks to a clean static HTML page '
                                             'with an option to show/hide code if needed.' + os.linesep +
                                             'Make sure to unhide all input cells if you want to include them',
                                 epilog='Made by @CorvusAI , source code available in Github. Thanks to @Chris Said for the button idea',
                                 usage='%(prog)s notebook_location [-h] [-nb] [-v]'
                                 )

parser.add_argument('notebook_location',
                    action='store',
                    type=str,
                    help='Filepath of the notebook to be converted')

parser.add_argument('-nb', '--no-button',
                    action='store_true',
                    dest='no_button',
                    help='Specify this to remove the Show/Hide code button')

parser.add_argument('-o', '--output',
                    action='store_true',
                    dest='no_input',
                    help='Specify this to exclude input cells and output prompts')

parser.add_argument('-s', '--silent',
                    action='store_true',
                    dest='silent',
                    help='Specify this for silent execution')

inputargs = parser.parse_args()


def process(input_file):
    if not inputargs.silent:
        print("Filepath of the ipynb being converted is : ", inputargs.notebook_location)
        if inputargs.no_button:
            print("Show/Hide code button disabled")
        else:
            if inputargs.no_input:
                print("Converting to HTML using nbconvert")
                subprocess.run(["jupyter", "nbconvert", inputargs.notebook_location, "--to=html", "--log-level=ERROR",
                                "--no-input"])
            else:
                print("Unable to add Button : Feature is still in development")
                # TODO the following cell in the notebook if no_button is false
                button_code = '''{
                                      "cell_type": "raw",
                                      "metadata": {},
                                      "source": [
                                          "<script>\n",
                                          "  function code_toggle() {\n",
                                          "    if (code_shown){\n",
                                          "      $('div.input').hide('500');\n",
                                          "      $('#toggleButton').val('Show Code')\n",
                                          "    } else {\n",
                                          "      $('div.input').show('500');\n",
                                          "      $('#toggleButton').val('Hide Code')\n",
                                          "    }\n",
                                          "    code_shown = !code_shown\n",
                                          "  }\n",
                                          "\n",
                                          "  $( document ).ready(function(){\n",
                                          "    code_shown=false;\n",
                                          "    $('div.input').hide()\n",
                                          "  });\n",
                                          "</script>\n",
                                          "<form action=\"javascript:code_toggle()\"><input type=\"submit\" id=\"toggleButton\" value=\"Show Code\"></form>"
                                      ]
                                  }, '''
                print("Converting to HTML using nbconvert")
                # TODO jupyter nbconvert "name" --to='html' --log-level='ERROR'
                subprocess.run(["jupyter", "nbconvert", inputargs.notebook_location, "--to=html", "--log-level=ERROR"])

        print("Converted successfully")
    pass


process(inputargs.notebook_location)

# TODO download rendered file from nbviewer itself
# javascript:date = new Date();
# url_root = 'http://nbviewer.jupyter.org/';
# url = null;
# gist_re = /^https?:\/\/gist\.github\.com\/(?:\w+\/)?([a-f0-9]+)$/;
# github_re = /^https:\/\/(github\.com\/.*\/)blob\/(.*\.ipynb)$/;
# https_re = /^https:\/\/(.*\.ipynb)$/;
# http_re = /^http:\/\/(.*\.ipynb)$/;
# loc = location.href;
# if (gist_re.test(loc)) {
#     gist = gist_re.exec(loc);
#     url = url_root + gist[1];
# } else if (github_re.test(loc)) {
#     path = github_re.exec(loc);
#     url = url_root + 'urls/raw.' + path[1] + path[2];
# } else if (https_re.test(loc)) {
#     path = https_re.exec(loc);
#     url = url_root + 'urls/' + path[1];
# } else if (http_re.test(loc)) {
#     path = http_re.exec(loc);
#     url = url_root + 'url/' + path[1];}
# if (url) {void(window.open(url, 'nbviewer' + date.getTime()));}
# TODO and then process it to remove certain divs and replace mathjax script URL
