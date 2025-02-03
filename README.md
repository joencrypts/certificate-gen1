# Certificate Gen v1
# Flask-Based Application

## Overview
This is a **Flask-based web application** that allows users to generate and download files. The project is designed to be minimalistic, with a simple UI and backend handling for file generation and downloading.

## Features
- **Flask Backend**: Handles user requests and file generation.
- **Jinja2 Templates**: Used for rendering HTML pages dynamically.
- **Download Functionality**: Users can generate files and download them easily.
- **Mobile & Laptop Optimization**: The UI is responsive for better usability.

## Prerequisites
Ensure you have the following installed on your system:
- Python (>=3.8)
- Flask (latest version)

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/your-repo.git](https://github.com/joencrypts/certificate-gen1.git
   cd certificate-gen1
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Application
Start the Flask server:
```sh
python app.py
```
Then, open **http://127.0.0.1:5000/** in your browser.

## Project Structure
```
/
├── app.py                # Main Flask application
├── templates/            # HTML templates
│   ├── index.html        # Main UI page
│   ├── download.html     # Download page
├── static/               # Static assets (CSS, images, fonts, etc.)
│   ├── styles.css        # Styling for the project
├── requirements.txt      # Project dependencies
├── README.md             # Documentation
```

## Deployment
To deploy the project on **Render** or another hosting platform:
1. Ensure all dependencies are installed.
2. Set up a **requirements.txt** file.
3. Configure a **Procfile** if required.
4. Push the code to a repository and deploy it.

## Troubleshooting
- **Template Not Found Error**: Ensure templates are inside the `templates/` folder.
- **Font Not Loaded on Render**: Check if the font files are in the correct `static/` directory.
- **Flask Not Found**: Run `pip install flask` to ensure it's installed.

## License
This project is open-source and available under the [MIT License].

## Author
Developed by **Joencrypts**. Reach out for any queries! 🚀

