## List of usefull commands to run the app in Docker:

- Build and run the project:

      docker build -t myapp .
      docker run --rm -d -p 80:8000 myapp

- Run the project for development purpose (with shared codebase to the container for automatic reloading):

      docker build -t myapp .
      docker run --rm -it -p 80:8000 -v $(pwd):/app myapp bash

Open http://localhost/ to see the app
