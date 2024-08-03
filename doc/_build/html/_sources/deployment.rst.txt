Deployment
===========

Step 1: set up Gitlab CI/CD for Compilation, Testing, Linting, and Coverage Checking
------------------------------------------------------------------------------------

The deployment is automated using Gitlab and Render.
The gitlab-ci.yml file contains all the steps of the deployment.

To be able to deploy the website you'll need a Gitlab account, a Docker account and a Render account.

Explanation

Stages:

    * test: Compiles, tests, lints, and checks coverage greater than 80%.
    * build: Builds the Docker image and pushes it to the Docker Hub.
    * deploy: Placeholder for deployment, handled by Render's GitHub/GitLab integration.

Environment variables:

SECRET_KEY, SENTRY_DSN, DOCKER_USERNAME and DOCKER_PASSWORD are defined as environment variables.
Set the following environment variables and secrets in your GitLab CI/CD settings for your project:

    * SECRET_KEY: Your Django secret key.
    * SENTRY_DSN: Your Sentry DSN.
    * DOCKER_USERNAME: Your Docker Hub username.
    * DOCKER_PASSWORD: Your Docker Hub password. (you can use a personnal token)

Services:

    * postgres: A PostgreSQL service for running tests.

Jobs:

    * test: Installs dependencies, runs linting, tests, and coverage checks.
    * build: Logs in to Docker Hub, builds the Docker image, and pushes it to the GitLab Container Registry.
    * deploy: Placeholder job to indicate deployment to Render.

Step 2: Dockerfile for Building Docker Images
---------------------------------------------

Ensure you have a Dockerfile in your project's root directory.
This step will build a Docker image and push it to the Docker Hub.

DOCKER_IMAGE: $DOCKER_USERNAME/oc_lettings_site:$CI_COMMIT_SHA

The name of the Docker image will be the docker username, followed by oc_lettings_site and tagged with the commit SHA.

Step 3: Configure Render for Continuous Deployment
--------------------------------------------------

Create a New Web Service on Render:

    * Log in to your Render account.
    * Click "New" and select "Web Service".
    * Connect your GitLab repository to Render.
    * Configure the build and runtime settings, such as environment variables (SECRET_KEY, SENTRY_DSN), and specify the start command (e.g., gunicorn oc_lettings_site.wsgi:application).

Set Up Environment Variables on Render:

    * In the Render dashboard, go to the "Environment" tab for your web service.
    * Add environment variables such as SECRET_KEY, SENTRY_DSN, and any other variables required by your Django application.

Configure Automatic Deployments:

You can enable automatic deployments from your GitLab repository to Render.
This will trigger a deployment on Render whenever changes are pushed to the master branch.