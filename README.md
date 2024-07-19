
# Gemini-CLI

This is a simple python application that you can alias to pass your query to Gemini.



## Author

- [@veenoise](https://github.com/veenoise)


## Installation

Use pip to install all python dependencies

```python
  pip install -r requirements.txt
```
    
## Deployment

To deploy this application, get your API key from [Gemini](https://ai.google.dev/gemini-api/docs/api-key).

Place the api key in the `.env.sample` file replacing the placeholder string.

Rename the `.env.sample` to `.env` and run the application to test if it works.

```python
python gemini.py "Hello, Gemini!"
```

To alias the python application, open the `~/.bashrc` file and add the command at the bottom of the file.

```bash
alias gemini='python /path/to/gemini.py/gemini.py'
```

After saving changes, use the source command to reflect the changes.

```bash
source ~/.bashrc
```

## Usage/Examples

```bash
gemini "Hello, Gemini! Tell me about yourself."
```
