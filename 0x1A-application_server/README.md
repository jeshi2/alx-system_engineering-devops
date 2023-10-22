# Application Server

## Description

This project focuses on setting up an application server for an AirBnB clone project and configuring Nginx to serve dynamic content. It also involves the graceful reloading of Gunicorn, adding routes with query parameters, and making the system run seamlessly without service interruption.

## Table of Contents

- [Concepts](#concepts)
- [Background Context](#background-context)
- [Resources](#resources)
- [Requirements](#requirements)
- [Tasks](#tasks)
    - [Task 0: Set up development with Python](#task-0-set-up-development-with-python)
    - [Task 1: Set up production with Gunicorn](#task-1-set-up-production-with-gunicorn)
    - [Task 2: Serve a page with Nginx](#task-2-serve-a-page-with-nginx)
    - [Task 3: Add a route with query parameters](#task-3-add-a-route-with-query-parameters)
    - [Task 4: Let's do this for your API](#task-4-lets-do-this-for-your-api)
    - [Task 5: Serve your AirBnB clone](#task-5-serve-your-airbnb-clone)
    - [Task 6: Deploy it!](#task-6-deploy-it)
    - [Task 7: No service interruption](#task-7-no-service-interruption)

## Concepts

- **Web Server**: A web server is software that serves web pages to users' web browsers. It processes requests, delivers web content, and can handle various web technologies.

- **Server**: A server is a computer or system that provides services or resources to other computers (clients) over a network. It can serve various purposes, including web hosting, application hosting, and data storage.

- **Web Stack Debugging**: Web stack debugging involves identifying and resolving issues within a web application's technology stack. It often includes debugging code, configurations, and server-related problems.

## Background Context

Your web infrastructure is already serving web pages via Nginx installed in your first web stack project. While a web server can serve static content, this project involves adding an application server to your infrastructure. The goal is to connect it to Nginx and make it serve your Airbnb clone project.

## Resources

Before proceeding with the tasks, you can read or watch the following resources for a better understanding:

- [Application Server vs. Web Server](https://www.nginx.com/resources/glossary/application-server-vs-web-server/)
- [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-20-04)
- [Running Gunicorn](https://docs.gunicorn.org/en/stable/run.html)
- [Be careful with the way Flask manages slash in route - strict_slashes](https://stackoverflow.com/questions/20552934/flask-url-rule-defaults-strict-slashes)
- [Upstart documentation](http://upstart.ubuntu.com/cookbook/)

## Requirements

- General:
  - A `README.md` file at the root of the project folder is mandatory.
  - Everything Python-related must be done using Python 3.
  - All configuration files must have comments.
  - All files should end with a new line.
  - All Bash script files must be executable.
  - Your Bash script must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any error.
  - The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`.
  - The second line of all your Bash scripts should be a comment explaining what the script is doing.

- Your servers:
  - You have three servers named:
    - `XXXXXX-web-01` with the username `ubuntu` and IP `VALID_IP`, in a running state.
    - `XXXXXX-web-02` with the username `ubuntu` and IP `VALID_IP`, in a running state.
    - `XXXXXX-lb-01` with the username `ubuntu` and IP `VALID_IP`, in a running state.

## Tasks

### Task 0: Set up development with Python

Let's serve what you built for AirBnB Clone v2 - Web framework on web-01. This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production.

Requirements:
- Make sure that task #3 of your SSH project is completed for `web-01`. The checker will connect to your servers.
- Install the `net-tools` package on your server: `sudo apt install -y net-tools`.
- Git clone your `AirBnB_clone_v2` on your `web-01` server.
- Configure the file `web_flask/0-hello_route.py` to serve its content from the route `/airbnb-onepage/` on port 5000.
- Your Flask application object must be named `app` (This will allow us to run and check your code).

Example:

```shell
Window 1:
ubuntu@229-web-01:~/AirBnB_clone_v2$ python3 -m web_flask.0-hello_route
 * Serving Flask app "0-hello_route" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
35.231.193.217 - - [02/May/2019 22:19:42] "GET /airbnb-onepage/ HTTP/1.1" 200 -
Window 2:
ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~/AirBnB_clone_v2$
```

### Task 1: Set up production with Gunicorn

Now that you have your development environment set up, let’s get

 your production environment ready. You will serve the same AirBnB clone project, but this time, it’ll be served with Gunicorn on web-01.

Requirements:
- Install Gunicorn 3.8.x
- Import your Gunicorn configuration from `web_flask/0-hello_route.py`
- Your application object should be named `app` (This will allow you to check if it's not named `app`, it won't pass the checker).
- You will start Gunicorn with the line `gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app`.
- For this task, please write a script that starts a Gunicorn instance to serve `web_flask.0-hello_route` on port 5000. You will put this script in the `/web_flask/` directory of your AirBnB Clone project. The script should be called `1-hbnb_route_gunicorn`.

### Task 2: Serve a page with Nginx

Building on your work in the previous task, configure Nginx to serve your page from the route `/airbnb-onepage/`.

Requirements:
- Nginx must serve this page both locally and on its public IP.
- Nginx should proxy requests to the process listening on port 5000.
- Ensure that your Gunicorn instance is listening on `0.0.0.0:5000`.
- Your solution should be the `web_flask/1-hbnb_route_gunicorn` script that you wrote before.

### Task 3: Add a route with query parameters

Building on what you did in the previous tasks, you'll implement a new route to handle query parameters. This route will accept a `?name= parameter` and display "Hello HBNB name" on the page.

Requirements:
- The name parameter is mandatory, but it is a string.
- The route will only accept GET requests.
- The name is part of the query string.
- You must use the option `strict_slashes=False` in your route definition.

Here is what my Gunicorn instance is doing for this route:

```shell
ubuntu@229-web-01:~/AirBnB_clone_v2$ python3 -m web_flask.3-python_route
 * Running on http://0.0.0.0:5000/airbnb-onepage/ ...
ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!
ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5000/airbnb-onepage/python/
Hello HBNB python!
```

### Task 4: Let's do this for your API

Let's serve what you built for AirBnB Clone v3 - RESTful API on web-01.

Requirements:

- Make sure that task #3 of your SSH project is completed for web-01. The checker will connect to your servers.
- Your API should be listening on `0.0.0.0` and port `5000`.
- You will use the `app` object from `web_flask/7-states_list.py`.
- You will use `gunicorn` to serve it on its public IP on port `5000`.
- Write a Bash script that starts a Gunicorn instance to serve `web_flask/7-states_list.py`. This script should be called `3-app_api` and should be placed in the `/web_flask/` directory.

### Task 5: Serve your AirBnB clone

Building on what you did in the previous tasks, let's serve your content.

Requirements:

- AirBnB clone v2 - Web framework: Make sure that task #3 of your AirBnB clone project is completed.
- AirBnB clone - RESTful API: Make sure that task #3 of your AirBnB clone project is completed.
- Your server should be listening on 0.0.0.0 and port 5000.
- The server must be serving the same content on the same route as the previous task.
- You can’t just serve your website via Gunicorn, and you have to serve the files via Nginx.
- Nginx should be listening on port 80.
- You might want to set up a route for `/redirect_me` with a `301` redirection to `http://example.com/`.

### Task 6: Deploy it!

Finally, you need to serve the web application. You have to serve Gunicorn (AirBnB clone v2), Gunicorn (AirBnB clone - RESTful API), and the static content via Nginx.

Requirements:

- For your web application to be fully deployed, you need to have a minimum of 2 servers (1 web server and 1 application server).
- For your web application to be fully deployed with a HAProxy load balancer, you need to have 3 servers (1 load balancer, 1 web server, and 1 application server).
- Write a Bash script that generates a self-signed SSL certificate and configures Nginx to use it.
- Nginx should be listening on port 443.
- Nginx should serve the static content from your AirBnB clone application.
- Nginx should reverse proxy requests to the Gunicorn application server.
- The `Nginx` and `Gunicorn` configuration files must be the same as the previous tasks.
- Nginx should be able to proxy HTTP requests to Gunicorn.
- Nginx should be able to proxy HTTP requests to Gunicorn for `/airbnb-onepage/`, `/airbnb-onepage/python`, and `hbnb_api`.
- You will need to use `location` in your Nginx configuration to be able to achieve this.
- For your certificate to be valid, you must have a `CN` set to your domain name and not an IP.
- For the moment, do not install a script that renews your SSL certificate automatically.
- Your web server should be running a process to monitor traffic and serve content.

### Task 7: No service interruption

The Web stack monitoring software is not installed on your web-01 server, so you have no visibility into the state of the server. Having no monitoring system, it's likely the server will go down.

Requirements:
- Write a Bash script that configures the server to monitor traffic (requests sent and requests received) on port 80.
- It should also alert you if the server goes down.

**Note**: This project involves multiple tasks that build upon each other, so it's important to complete the tasks sequentially. Before starting a task, make sure the previous ones are correctly implemented.

Once you've completed these tasks, your application server and Nginx should be configured to serve an AirBnB clone project with Gunicorn, and the whole system should be ready for deployment.

**Author:** Antony Evans
**Dated:** 10/21/2023

**License:** This project is open source and available under the MIT License.
