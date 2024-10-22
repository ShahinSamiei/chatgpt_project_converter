<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>ChatGPT Project Converter</h1>

<p><strong>ChatGPT Project Converter</strong> is a Python-based tool that allows you to manage, document, and recreate the file structure and contents of a project directory. This tool can help you generate a text-based representation of a directory, save its structure and contents, and recreate the structure and files from a text file.</p>

<h2>Features</h2>
<ul>
    <li><strong>Save Directory Structure:</strong> The tool generates a tree-like structure of the directory and saves it into a text file.</li>
    <li><strong>Save File Contents:</strong> In addition to the structure, the tool captures the contents of all files within the directory and saves them in a structured format.</li>
    <li><strong>Recreate Project Structure:</strong> You can recreate the entire directory structure, along with files and their contents, from a text file.</li>
</ul>

<h2>Special Use Cases</h2>

<h3>1. Sending Project as a Text Document to ChatGPT</h3>
<p>One of the most useful scenarios for this tool is when you want to send a project to ChatGPT for assistance or analysis. Instead of compressing the project into a ZIP file and sending it (which can often lead to issues with extraction), this tool allows you to convert the entire project structure and its contents into a single <strong>text (.txt) document</strong>. This makes it much easier for ChatGPT to read and understand your project without the common issues encountered with ZIP files.</p>
<p>Since ChatGPT processes text files much more smoothly than extracting ZIP files, using this tool helps you avoid technical problems during file extraction, ensuring seamless communication with the AI.</p>

<h3>2. Printing a Project in a Readable Format</h3>
<p>Another great use of this tool is when you need to print a project in a readable format. Instead of printing each file individually, you can use this tool to convert the entire project, including the directory structure and file contents, into a single text document. This makes it easy to print everything in one go, providing a clear and organized overview of the entire project.</p>

<h2>File Overview</h2>
<ul>
    <li><strong>main.py:</strong> This script saves both the directory structure and file contents into a text file. The output includes the folder structure and the content of files.</li>
    <li><strong>doc.py:</strong> This script captures the contents of all files in a folder and saves them to a single text file, with relative paths indicating where each file is located.</li>
    <li><strong>tree.py:</strong> This script generates and saves the tree-like structure of a directory without file contents, focusing on the folder and file hierarchy.</li>
    <li><strong>project.py:</strong> This script allows the reconstruction of a directory structure and its files from a provided text file.</li>
</ul>

<h2>Requirements</h2>
<p>Ensure you have Python 3.x installed on your system.</p>

<pre><code>pip install os</code></pre>

<h2>How to Use</h2>

<h3>1. Saving Directory Structure and File Contents (main.py)</h3>
<p>This will generate a text file containing both the directory structure and the contents of each file.</p>
<pre><code>python main.py</code></pre>
<p>Provide the directory path when prompted, and the output file will be created with both the folder tree and file content.</p>

<h3>2. Saving File Contents Only (doc.py)</h3>
<p>This will capture the contents of all files in a directory and save them to a single text file, including the relative paths.</p>
<pre><code>python doc.py</code></pre>

<h3>3. Generating Directory Tree (tree.py)</h3>
<p>Generate and save the structure of a folder as a tree, excluding the file contents.</p>
<pre><code>python tree.py</code></pre>

<h3>4. Recreating Project Structure and Files (project.py)</h3>
<p>This will recreate the entire directory structure, along with file contents, from the text file previously generated.</p>
<pre><code>python project.py</code></pre>

<h2>Example Workflow</h2>
<ol>
    <li>Run <code>main.py</code> to save the project structure and contents of a folder into a text file.</li>
    <li>Use the output file for documentation, printing, or backup purposes.</li>
    <li>Later, use <code>project.py</code> to recreate the same structure from the saved text file.</li>
</ol>

<h2>Use Cases</h2>
<ul>
    <li><strong>Backup:</strong> Easily save the structure and content of important project folders.</li>
    <li><strong>Documentation:</strong> Use the tree and content output for project documentation purposes.</li>
    <li><strong>Project Reproduction:</strong> Recreate a complete project from a structured text file.</li>
    <li><strong>Sending Projects to ChatGPT:</strong> Use the text-based format to easily send projects to ChatGPT without the need for ZIP files, avoiding extraction errors.</li>
    <li><strong>Printing Projects:</strong> Convert the entire project into a single readable text file for easy printing of both the structure and contents.</li>
</ul>

<h2>Contributing</h2>
<p>Feel free to fork this repository, make improvements, and submit pull requests.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License.</p>

</body>
</html>
