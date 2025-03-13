# JSAnalyzer

## Description
**JSAnalyzer** is a tool for analyzing and extracting links from JavaScript files. It uses `tornado` to serve a web interface and `jsbeautifier` to format JavaScript code, allowing for better content inspection.

---

## Features
- Automatic extraction of paths and links within JavaScript files.
- Use of `tornado` to handle web requests and present results.
- JavaScript formatting and beautification with `jsbeautifier`.
- Integration with `BeautifulSoup` for handling HTML.
- Handling HTTP requests with `pycurl`.
- Allows setting custom headers for requests.
---

## Installation
### Pre-requisites

Make sure you have **Python 3.0** or higher installed on your system.

### Installing Dependencies

Clone the repository
```
git clone https://github.com/Zuk4r1/JSAnalyzer.git
```
go to the folder

```
cd JSAnalyzer
```
create the virtual environment and install the library
```
python3 -m venv venv
source venv/bin/activate
pip install jsbeautifier
```
Then install the dependencies with:
```sh
pip install -r requirements.txt
```

If you prefer to install it as a package:
```sh
python setup.py install
```

---

## Usage
Run the script and provide a port:
```sh
python handler.py
```
The script will prompt you for a port. You can enter it manually or press **Enter** to use the default port **8008**.

The server will be available at:
```
http://localhost:8008/
```

### Endpoint Options
| Endpoint | Method | Description |
|---------------|--------|-------------|
| `/` | GET | Home |
| `/about` | GET | Tooltip |
| `/parse/ajax` | POST | Parse links in JS files |

To parse a JavaScript file, send a `POST` request to `/parse/ajax` with a JSON like this:
```json
{
"url": "https://example.com/script.js",
"headers": ["User-Agent: custom-agent"]
}
```
## License
This project is licensed under the **AGPL-3.0** license. See the `LICENSE` file for details.

---

## Author
Created with ❤️ by [@Zuk4r1](https://github.com/Zuk4r1).
