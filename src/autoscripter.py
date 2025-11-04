#!/usr/bin/env python3

import click
import os
from pathlib import Path

# Import our modules (we'll create these next)
from generator import ScriptGenerator
from prompts import InteractivePrompt


@click.command()
@click.option('--output-dir', default='output', help='Directory to save generated scripts')
def main(output_dir):
    """Interactive script generator for common filesystem operations."""
    
    # Display welcome message
    click.echo("=" * 50)
    click.echo("Welcome to Autoscripter!")
    click.echo("Generate Python or Bash scripts interactively")
    click.echo("=" * 50)
    click.echo()
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Start interactive prompt
    prompt = InteractivePrompt()
    config = prompt.run()
    
    # If user cancelled, exit
    if not config:
        click.echo("Script generation cancelled.")
        return
    
    # Generate the script
    generator = ScriptGenerator(config)
    script_content = generator.generate()
    
    # Save to file
    output_path = Path(output_dir) / config['filename']
    with open(output_path, 'w') as f:
        f.write(script_content)
    
    # Make executable
    os.chmod(output_path, 0o755)
    
    click.echo()
    click.echo(f"Script generated: {output_path}")
    click.echo(f"Run with: ./{output_path}")
    

if __name__ == "__main__":
    main()