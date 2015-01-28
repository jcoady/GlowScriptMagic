from IPython.display import display, Javascript, HTML
import json

def glowscript(line, cell):
    lst = line.lower().split()
    if (len(lst) == 0) or (lst[-1] in ['vpython','rapydscript','coffeescript','javascript']) :
        display(HTML("""<div id="glowscript" class="glowscript"></div>"""))
        lang = lst[-1] if len(lst) > 0 else ''
        display(Javascript("""
        if (window.location.protocol === 'https:') {
            require(['https://dl.dropboxusercontent.com/u/5095342/glowscript/lib/jquery/1.1/jquery-ui.custom.min.js','https://dl.dropboxusercontent.com/u/5095342/glowscript/package/compiler.1.1.min.js','https://dl.dropboxusercontent.com/u/5095342/glowscript/package/symbols.1.1.min.js','https://dl.dropboxusercontent.com/u/5095342/glowscript/package/RSrun.1.1.min.js','https://dl.dropboxusercontent.com/u/5095342/glowscript/package/RScompiler.1.1.min.js','https://dl.dropboxusercontent.com/u/5095342/glowscript/package/glow.1.1.min.js'], function() {
            var cell_content = """+json.dumps(cell)+""";
            var embedScript = window.glowscript_compile(cell_content, {lang:'"""+lang+"""'}); 
            embedScript = "require(['https://dl.dropboxusercontent.com/u/5095342/glowscript/lib/jquery/1.1/jquery-ui.custom.min.js','https://dl.dropboxusercontent.com/u/5095342/glowscript/package/glow.1.1.min.js'], function() {" + embedScript + ";$(function(){ window.__context = { glowscript_container: $('#glowscript').removeAttr('id') }; main() });})";
            embedScript = embedScript.replace("</", "<\\/"); // escape anything that could be a close script tag... hopefully this sequence only occurs in strings!
            eval(embedScript);
            })
        } else if (window.location.host === 'nbviewer.ipython.org') {
            require(['http://www.glowscript.org/lib/jquery/1.1/jquery.min.js','http://www.glowscript.org/lib/jquery/1.1/jquery-ui.custom.min.js','http://www.glowscript.org/package/compiler.1.1.min.js','http://www.glowscript.org/package/symbols.1.1.min.js','http://www.glowscript.org/package/RSrun.1.1.min.js','http://www.glowscript.org/package/RScompiler.1.1.min.js','http://www.glowscript.org/package/glow.1.1.min.js'], function() {
            var cell_content = """+json.dumps(cell)+""";
            var embedScript = window.glowscript_compile(cell_content, {lang:'"""+lang+"""'}); 
            embedScript = "require(['http://www.glowscript.org/lib/jquery/1.1/jquery-ui.custom.min.js','http://www.glowscript.org/package/glow.1.1.min.js'], function() {" + embedScript + ";$(function(){ window.__context = { glowscript_container: $('#glowscript').removeAttr('id') }; main() });})";
            embedScript = embedScript.replace("</", "<\\/"); // escape anything that could be a close script tag... hopefully this sequence only occurs in strings!
            eval(embedScript);
            })
        } else {
            require(['http://www.glowscript.org/lib/jquery/1.1/jquery-ui.custom.min.js','http://www.glowscript.org/package/compiler.1.1.min.js','http://www.glowscript.org/package/symbols.1.1.min.js','http://www.glowscript.org/package/RSrun.1.1.min.js','http://www.glowscript.org/package/RScompiler.1.1.min.js','http://www.glowscript.org/package/glow.1.1.min.js'], function() {
            var cell_content = """+json.dumps(cell)+""";
            var embedScript = window.glowscript_compile(cell_content, {lang:'"""+lang+"""'}); 
            embedScript = "require(['http://www.glowscript.org/lib/jquery/1.1/jquery-ui.custom.min.js','http://www.glowscript.org/package/glow.1.1.min.js'], function() {" + embedScript + ";$(function(){ window.__context = { glowscript_container: $('#glowscript').removeAttr('id') }; main() });})";
            embedScript = embedScript.replace("</", "<\\/"); // escape anything that could be a close script tag... hopefully this sequence only occurs in strings!
            eval(embedScript);
            })
        }
        """ ))
        
def GlowScript(line, cell):
    glowscript(line, cell)
    

def vpython(line, cell):
    glowscript("vpython", cell)

def VPython(line, cell):
    glowscript("vpython", cell)

def rapydscript(line, cell):
    glowscript("rapydscript", cell)

def RapydScript(line, cell):
    glowscript("rapydscript", cell)

def coffeescript(line, cell):
    glowscript("coffeescript", cell)

def CoffeeScript(line, cell):
    glowscript("coffeescript", cell)

def load_ipython_extension(ipython):
    """This function is called when the extension is loaded.
    It accepts an IPython InteractiveShell instance.
    We can register the magic with the `register_magic_function`
    method of the shell instance."""
    ipython.register_magic_function(glowscript, 'cell')
    ipython.register_magic_function(vpython, 'cell')
    ipython.register_magic_function(rapydscript, 'cell')
    ipython.register_magic_function(coffeescript, 'cell')
    ipython.register_magic_function(GlowScript, 'cell')
    ipython.register_magic_function(VPython, 'cell')
    ipython.register_magic_function(RapydScript, 'cell')
    ipython.register_magic_function(CoffeeScript, 'cell')