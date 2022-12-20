# Initialization Script

Scripting is the coolest and the `initialize` script performs the following actions:

1. Ensures that a file named `.env` exists.
2. User selects whether they would like to override the default username, email, and password.
3. Shuts down and deletes existing Watch Party Docker containers (if any exist).
4. Removes the Docker volume for Watch Party (if it exists).
5. Creates a new Docker volume for Watch Party.
6. Checks to see if the computer is running on Apple Silicon and runs the appropriate `docker compose` command based on the result.
7. Runs the newly built docker containers. The Django movies container automatically populates its database with movie genres.
8. Runs a helper script `./test` that performs all existing linting and unit tests.
9. Creates a superuser with the default credentials: username: `admin` && password: `password` && email: `admin@watchparty.com` unless they were overridden at the beginning of the script.
10. Launches `http://localhost:3000/testhome/` in the default browser.

**Developers**: Do not push a changed version of this file to the `main` branch without talking to Josiah first. :)
