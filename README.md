# Movie Party
A resource for film lovers and their friends to plan the next movie night.
<br /><br />
<img src="resources/stock-photos/couch-1.jpg" alt="watch party"/>

## Plan Your Next Movie Night

### Functionality
Movie Party provides responsive movie information for users to explore. Authenticated users may also rate, write reviews, create customized watchlists, and host watch parties.

A watch party is an event that can one or many users. One to three genres of interest are selected. An algorithm compares the attendees' watchlists and provides a movie suggestion from which they can read user reviews and a summary/watch a trailer. Users can either accept that suggestion or receive another.

### Getting started
Follow these instructions to spin up the server locally. Note: This project is designed so that the following steps apply to all operating systems. You only need to do this once. On future startups, you will run `docker compose up` from the root directory.
1. Clone the repo.
2. This is a containerized project. Install and open [Docker Desktop](https://www.docker.com/products/docker-desktop/).
3. Obtain a [TMDB API key](https://www.themoviedb.org/documentation/api). (Developers: check [Notes for Developers](#notes-for-developers) section for how to access this repo's existing key)
4. Navigate to the project root directory in the terminal and open in a code editor.
5. Create a copy of `.exampleenv` called  `.env`.
6. Copy your API Key (v3 auth) from your [TMDB account page](https://www.themoviedb.org/settings/api) and paste it into `.env` as the value of the `TMDB_API_KEY_V3` environment variable.
7. From the project root directory, initialize repo with the command that can take three optional arguments: `./initialize`. See the [initialization script documentation](docs/initialization-script.md) for how to override default username, email, and password.
8. The browser will automatically launch `http://localhost:3000/testhome/` when the `initialize` script finishes. It will take several minutes to complete so grab a cup of coffee!

### Design & Documentation

<img src="docs/wireframes/watch-party.png" alt="system design"/>

You can browse Watch Party's documentation here.
* [API design](docs/apis.md)
* [Data models](docs/data-model.md)
* [GHI](docs/ghi.md)
* [Integrations](docs/integrations.md)
* [Wireframes](docs/wireframes/)
* [Initialization script](docs/initialization-script.md)

## Why I decided to work on it

### Goals for developing this project
1. Get comfortable with new technologies by expanding beyond your usual tech stack
2. Enhance your teamwork skills by regular collaboration and pair programming
3. Test-driven development. Integrating this programming style into your regular routine is imperative to success on production code

### General notes for developers
* Grab a GitLab issue when you are looking for another task to work on. Reach out to Josiah for clarification or if there are none available.
* To access the existing TMDB API key, go to this repo's Settings / CI/CD and copy the value of the `TMDB_API_KEY_V3` key. For its protection, do **not** hard code this into any file except `.env`. It will be accessible via its variable name in the `os.environ` object.
* If you intend to push a branch to the Gitlab repo and want to run the CI tests you must include `development-` at the beginning of your branch name. This protects the branch and allows access to GitLab env variables to run the CI tests. Branches that are not protected can still be pushed to GitLab but will not be tested. Example testable branch name: `development-watchlists`
* Merge, push and test your changes on a `development-` branch before merging with `main` to ensure its protection.
* If you delete migration files or purge your database manually and the Genres are not loaded into the database you can reload them from the movies cli via command: `python manage.py loaddata genres.json`. You can also run `./initialize` from the root directory to repopulate the entire database.
* Use concise and descriptive commit messages. (Not only for our sanity but for any recruiters that might take a look at the repo)
* Please do not push to `main` without talking to Josiah.

### Testing
  TEST, TEST, TEST. Write unit tests early and often. Thankfully, testing is too easy in this environment. Just run `./test` from the root directory and all unit tests will run. (And the script will auto-lint your code as a little bonus)

### Tech Stack
* Python
* JavaScript
* SQL
* Docker
* React
* Redux
* Django
* Redis
* RabbitMQ
* Flask
* GitLab CI/CD
* GitLab Pages
* AWS EC2

### Movie data provided by TMDB
<img src="docs/wireframes/tmdb-logo/tmdb.svg" alt="tmdb logo" width="150"/>
