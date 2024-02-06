# Convert ChatGPT Conversations to Markdown

## Overview

This Python script automates the extraction of ChatGPT conversations from a zip file exported from the OpenAI platform and formats them into readable Markdown (.md) files. It's designed to help users easily convert their ChatGPT interactions into a structured format that can be viewed, edited, or converted into other formats using popular Markdown editors such as Obsidian, Visual Studio Code, or Typora. Additionally, you can use tools like Pandoc to further convert these Markdown files into other formats including .docx, .HTML, or .PDF.

## Features

- **Automatic Extraction**: Unzips the ChatGPT conversation data file into a specified directory.
- **Markdown Formatting**: Converts conversations into Markdown format, indexing them in descending order based on creation time—newer conversations are assigned lower indices.
- **Clean & Organize**: Stores formatted conversations in a dedicated `conversations_md` folder for easy access and management.
- **User-Friendly**: Offers a simple command-line interface for specifying the input zip file.

## Prerequisites

Before running this script, ensure you have:

- Python installed on your machine.
- The exported ChatGPT conversation zip file, obtainable via ChatGPT -> Settings & Beta -> Data controls tab -> Export data.

## Usage

1. **Prepare Your Environment**: Place the script and the ChatGPT export zip file in the same directory.

2. **Run the Script**: Open your terminal or command prompt, navigate to the directory containing the script and zip file, and execute the script using Python. Specify the name of the zip file as an argument:

    ```bash
    python3 export.py 'your-exported-file.zip'
    ```

    Replace `'your-exported-file.zip'` with the actual name of your ChatGPT export zip file.

3. **View Conversations**: After execution, find your conversations formatted as Markdown files in the `conversations_md` folder. These files are named sequentially (e.g., `0. Title 0.md`, `1. Title 1.md`, ...) with newer conversations having lower indices.

4. **Edit or Convert (Optional)**: Use a Markdown editor like Obsidian, VS Code, or Typora to view or edit your conversations. If needed, convert the Markdown files to other formats like .docx, .HTML, or .pdf using Pandoc or a similar tool.

## Additional Information

- **Customization**: Advanced users can modify the script to adjust the Markdown formatting or the structure of the exported files to better suit their needs.
- **Troubleshooting**: If you encounter any issues with the script, first ensure that the zip file's path and name are correctly specified. 

## Contributing

Your contributions are welcome! If you have improvements or bug fixes, please feel free to fork the repository, make your changes, and submit a pull request.

## Author

**Penjan Antonio Eng Lim**
AI engineer. Researcher & Master's Student in Artificial Intelligence at Chungnam National University.

- **LinkedIn**: [penjan-antonio-eng-lim](https://www.linkedin.com/in/penjan-antonio-eng-lim-635080296/?originalSubdomain=kr) 
- **GitHub**: [@daehan-lim](https://github.com/daehan-lim)
## License

This project is open-sourced under the MIT License. See the LICENSE file for more details.
