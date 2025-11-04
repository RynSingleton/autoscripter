import click


class InteractivePrompt:
    SUPPORTED_OPERATIONS = [
        'mkdir',
        'touch',
        'ls',
        'cd',
        'rm',
        'mv'
    ]
    
    def __init__(self):
        self.config = {}
        
    def run(self):
        #get script language
        script_type = click.prompt("Script language (Python or Bash, defualts to Python): ",
                     type=click.Choice(['python', 'bash'], case_sensitive=False), default='python')
        self.config['script_type'] = script_type.lower()
        
        #get filename
        default_ext = '.py' if script_type == 'python' else '.sh'
        filename = click.prompt('Output filename', default=f'generated_script{default_ext}')
        self.config['filename'] = filename
        
        #get operations
        click.echo("\nPlease select an operation")
        click.echo("\nOperations include:")
        for index, item in enumerate(self.SUPPORTED_OPERATIONS):
            click.echo(f"  {index + 1}. {item}")
        click.echo("\nEnter operation numbers separated by spaces (e.g., '1 2 5')")
        
        #list ops
        ops = click.prompt('Operations to include').split()

        try:
            selected_indices = [int(x) for x in ops]
            
            operations = [self.SUPPORTED_OPERATIONS[i-1] for i in selected_indices 
                    if 0 < i <= len(self.SUPPORTED_OPERATIONS)]
            
            if not operations:
                click.echo("No valid operations selected. Exiting.")
                return None
            
            self.config['operations'] = operations
            
        except(ValueError, IndexError):
            click.echo("Invalid input. Exiting.")
            return None

        self.config['operation_params'] = {}
        
        #get params
        for op in operations:
            click.echo(f"\n=== Config for '{op}' ===")
            params = self._get_operation_params(op)
            self.config['operation_params'][op] = params
            
        #error handling
        add_error_handling = click.confirm('\nAdd error handling?', default=True)
        self.config['error_handling'] = add_error_handling

        return self.config

    def _get_operation_params(self, operation):
        params = {}
        
        if operation == 'mkdir':
            params['path'] = click.prompt("  Directory path to create")
            params['parents'] = click.confirm("  Create parent directories if needed?", default=True)
        
        elif operation == 'touch':
            params['path'] = click.prompt("  File path to create")
        
        elif operation == 'ls':
            params['path'] = click.prompt("  Directory to list", default='.')
            params['recursive'] = click.confirm("  Recursive listing?", default=False)
        
        elif operation == 'cd':
            params['path'] = click.prompt("  Directory to change to")
        
        elif operation == 'rm':
            params['path'] = click.prompt("  Path to remove")
            params['recursive'] = click.confirm("  Remove recursively?", default=False)
            params['force'] = click.confirm("  Force removal (no prompts)?", default=False)
        
        elif operation == 'mv':
            params['source'] = click.prompt("  Source path")
            params['destination'] = click.prompt("  Destination path")
        
        return params
