# Open edx to Static HTML Pages
## Project Goal
This project intends to provide a means to render an open edx course archive file to static HTML pages that include all of the static content included in the course. Note that only the code features of an open edx course archive are supported. 

## Motivation
The project makes it possible to go through static elements of a course preserving static course content, page hierarchy and navigation. This allows the static content of the course to be viewed or served from a simple web server that only needs the ability to serve static pages. If all of the static course content is included in the course archive (nothing is linked form external sources) it is possible to save the static HTML to a local file system and view the content completely offline.

## How it Works
The tool is capable of reading the files used to represent the course structure from the course archive and reconstruct the page hierarchy and navigation. This is done by wrapping the HTML snippets, images and videos from the archive in very basic HTML.

The HTML is purposely left very plain so that the project can be customized without having unnecessary and possibly unwanted style choices made in advance.

## Introductory Video
I apologize for talking so slow:
https://www.youtube.com/watch?v=as7k0_7q3mc&t=41s
