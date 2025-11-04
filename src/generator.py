from jinja2 import Environment, FileSystemLoader
import os

class ScriptGenerator:
    
    def __init__(self, config):
        self.config = config
        self.script_type = config["script_type"]
        
        #grab template
        template_dir = os.path.join(os.path.dirname(__file__), 'templates')
        self.env = Environment(loader=FileSystemLoader(template_dir), trim_blocks=True, lstrip_blocks=True)
        self.env.filters['repr'] = repr

    def generate(self):
        if self.script_type == 'python':
            return self._generate_python()
        elif self.script_type == 'bash':
            return self._generate_bash()
        else:
            raise ValueError(f"Unsupported script type: {self.script_type}")
        
    def _generate_bash(self):
        template = self.env.get_template('bshscript.j2')
        return template.render(self.config)
    
    def _generate_python(self):
        template = self.env.get_template('pyscript.j2')
        return template.render(self.config)