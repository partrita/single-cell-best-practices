import os
import jupytext
from translate import Translator
import shutil

def translate_text(text, target_language='ko'):
    """Translates text into the target language."""
    if not text.strip():
        return text
    try:
        translator = Translator(to_lang=target_language)
        return translator.translate(text)
    except Exception as e:
        print(f"    Could not translate text: {e}")
        return text

def translate_notebook(notebook_path, output_path):
    """Translates a Jupyter notebook file and saves it to a new location."""
    print(f"Translating {notebook_path} to {output_path}...")
    try:
        notebook = jupytext.read(notebook_path)
        for cell in notebook.cells:
            if cell.cell_type in ['markdown', 'raw']:
                cell.source = translate_text(cell.source)

        # Create the output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        jupytext.write(notebook, output_path)
        print(f"  Successfully translated and saved {output_path}")

    except Exception as e:
        print(f"  Could not process {notebook_path}: {e}")

if __name__ == "__main__":
    source_dir = 'jupyter-book'
    output_dir = 'korean-jupyter-book'

    # Recreate the output directory to ensure it's clean
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.ipynb'):
                source_path = os.path.join(root, file)
                relative_path = os.path.relpath(source_path, source_dir)
                output_path = os.path.join(output_dir, relative_path)
                translate_notebook(source_path, output_path)
            else:
                # Copy non-notebook files to the new directory
                source_path = os.path.join(root, file)
                relative_path = os.path.relpath(source_path, source_dir)
                output_path = os.path.join(output_dir, relative_path)
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                shutil.copy2(source_path, output_path)

    print("Translation complete.")