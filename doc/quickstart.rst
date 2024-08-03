QuickStart
==========

Here, you will learn how to quickly launch the project on your local computer using docker.

Launch the project using Docker
-------------------------------

Follow those steps
    * Create a `DockerHub <https://hub.docker.com/signup/>`__ Account
    * Install Docker Desktop on your computer *follow docker tutorial, depending on your OS*
    * Open your terminal

Now, enter this command::

    docker pull antini83/oc_lettings_site:latest

.. warning::
    Before launching the following command make sure that localhost:8000 is free to use

Simply build it with::

    docker run -it -p 8000:8000 antini83/oc_lettings_site:latest

You can now visit the website at: **http://localhost:8000/** 

Launch the project using Github
-------------------------------

Go to the :doc:`/installation` content.