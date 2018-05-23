# Running a local copy

1. Fork the repository and clone it.

2. Install the requirements in a virtualenv using Python 3. For example, using `virtualenvwrapper`:

```
mkvirtualenv pybcn-web --python=/usr/bin/python3
source activate pybcn-web
pip install -r requirements.txt
```

3. Run the development server with:
```
lektor server
```
The site will be available at `http://localhost:5000/`.

You can edit the files in the folder `content` to change the content of the site. Alternatively, head to `http://localhost:5000/admin/` to edit the contents using the lektor web interface.

