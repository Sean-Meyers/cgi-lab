#!/usr/bin/env python3

import cgi
import os
import json

print("Content-Type: application/json")
print()
os.environ["QUERY_STRING"] = "query=hello&world"
print(json.dumps(dict(os.environ), indent=2))
print(f"<p>QUERY_STRING = {os.environ['QUERY_STRING']}</p>")
print(f"<p>HTTP_USER_AGENT = {os.environ['HTTP_USER_AGENT']}</p>")


#form = cgi.FieldStorage()


# 1 How do you inspect all environment variables in Python?: os.environ gives a container that contains all the current environment vars
# 2 What environment variable contains the query parameter data?: QUERY_STRING
# 3 What environment variable contains information about the user’s browser?: HTTP_USER_AGENT
# 4 How does the POSTed data come to the CGI script?: cgi field storage
# 5 What is the HTTP header syntax to set a cookie from the server?: 'Set-Cookie: THECOOKIE'
# 6 What is the HTTP header syntax the browser uses to send the cookie back?: HTTP_COOKIE
# 7 In your own words, what are cookies used for?: cookies are used to store user data, ~~and steal it~~
# 8 What is the link to your code on GitHub?: https://github.com/Sean-Meyers/cgi-lab

