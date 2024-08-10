# Folder Zipper Python

A Flask webapp that allows users to upload a folder, compress and then download it in zip.

## Features

1. Upload a folder (including its contents).
2. Compress the folder into a ZIP file.
3. Download the ZIP file.

## Live Demo

You can access the live application [here](https://folderzipper-9e27836748c4.herokuapp.com/).

 
## How to run?

1. __Clone the Repo__
    ```
     git clone https://github.com/apoorvpathak/python-folder-compression-webapp
    ```
2. __Navigate to the Repo directory__
    ```
    cd python-folder-compression-webapp
    ``` 
3. __Create a Virtual Env__
    ```
    python -m venv projectenv
    ```
4. __Active the Virtual Env__
    On Windows: ```projectenv\Scripts\activate```
    On mac or Linux: ```source projectenv/bin/activate```

5. __Install Dependencies__
    ```
    pip install -r requirements.txt
    ```
6. __Run at Local Muchine__
    Once you are in python-folder-compression-webapp/ run
    ```
    python app.py
    ``` 
    The application will be available at http://127.0.0.1:5000/

## Troubleshooting

### TemplateNotFound Error
Ensure that your `index.html` file is located in the `templates` directory. The directory structure should look like this:
```
your-project/
├── app.py
├── Procfile
├── requirements.txt
├── templates/
│ └── index.html
└── uploads/
```


## Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

