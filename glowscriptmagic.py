from IPython.display import display, display_html, display_javascript
from IPython.display import Javascript
from IPython.display import HTML

def glowscript(line, cell):
    lst = line.lower().split()
    if (len(lst) == 0) or (lst[-1] in ['vpython','rapydscript','coffeescript','javascript']) :
        display(HTML("""<div id="glowscript" class="glowscript"></div>"""))
        lang = lst[-1] if len(lst) > 0 else ''
        display(Javascript("""
        require(['http://www.glowscript.org/lib/jquery/1.1/jquery-ui.custom.min.js','http://www.glowscript.org/package/compiler.1.1.min.js','http://www.glowscript.org/package/symbols.1.1.min.js','http://www.glowscript.org/package/RSrun.1.1.min.js','http://www.glowscript.org/package/RScompiler.1.1.min.js','http://www.glowscript.org/package/glow.1.1.min.js'], function() {
        var cell_content = '"""+cell.replace("\n","\\n")+"""';
        console.log(cell_content);
        var embedScript = window.glowscript_compile(cell_content, {lang:'"""+lang+"""'}); 
        embedScript = "require(['http://www.glowscript.org/lib/jquery/1.1/jquery-ui.custom.min.js','http://www.glowscript.org/package/glow.1.1.min.js'], function() {" + embedScript + ";$(function(){ window.__context = { glowscript_container: $('#glowscript').removeAttr('id') }; main() });})";
        embedScript = embedScript.replace("</", "<\\/"); // escape anything that could be a close script tag... hopefully this sequence only occurs in strings!
        console.log(embedScript);
        eval(embedScript);

        })
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