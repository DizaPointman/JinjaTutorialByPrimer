#!/usr/bin/python

import jinja2

environment =jinja2.Environment()
template = environment.from_string("Hello, {{name}}!")
result = template.render(name="Oh Greatest Motherfucker")
    
print(result)