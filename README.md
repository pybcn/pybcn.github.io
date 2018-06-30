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


# Compile .less files into .css

We use [LessJS](http://lesscss.org/usage/) to ease the management of CSS assets.

1. Install LessJS:
```
npm install less -g
```
2. Get to the static assets folder and compile:
```
cd assets/static/
lessc pybcn_style.less pybcn_style.css
```

# Send tweets about events

1. Go to the `scripts` folder and install/activate the last NodeJS version:
```
cd scripts/
nvm use
```

2. Install all required node packages:
```
npm install
```

3. Set the environment variables `TWITTER_CONSUMER_KEY`, `TWITTER_CONSUMER_SECRET`,
`TWITTER_ACCESS_TOKEN` and  `TWITTER_ACCESS_TOKEN_SECRET` (e.g. using a
`.env` file) and run:
```
npm run main
```