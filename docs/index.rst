Welcome to Jinja
================

Jinja is a modern and designer-friendly templating language for Python.
It is fast, widely used, and secure with the optional sandboxed template
execution environment:

.. sourcecode:: html+jinja

   <title>{% block title %}{% endblock %}</title>
   <ul>
   {% for user in users %}
     <li><a href="{{ user.url }}">{{ user.username }}</a></li>
   {% endfor %}
   </ul>

**Features:**

-   sandboxed execution
-   powerful automatic HTML escaping system for XSS prevention
-   template inheritance
-   compiles down to the optimal python code just in time
-   optional ahead-of-time template compilation
-   easy to debug.  Line numbers of exceptions directly point to
    the correct line in the template.
-   configurable syntax

.. include:: contents.rst.inc
