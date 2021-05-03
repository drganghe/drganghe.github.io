# Build a simple academic Github Page using jemdoc

I had hoped to create a simple static page hosted on Github, and here is my experiences after a few tryouts.

First get to know main versions of jemdoc:

* [jemdoc](http://jemdoc.jaboc.net/)
* [jemdoc+MathJax](https://github.com/wsshin/jemdoc_mathjax)

The following new design could also be useful if you like the design. It is also responsive to devices. However, I like the orgrinal jemdoc layout and color more.

* [jemdoc+new design](https://github.com/szl2/jemdoc-new-design)

In the end, I found this version of jemdoc to research group ready very useful.

* [jemdoc-ready](https://github.com/mkhaled87/jemdoc-ready)

It was adapted from original jemdoc but created new css files and news and rss functionality. It only works in Python 2.

I use jemdoc-ready as the template, and replace the jemdoc.py file with that of the jemdoc+MathJax so it could be used in Python 3 and open exteranl links in a new tab.

1. Creat a new repository named yourgithubusername.github.io
2. Down load [jemdoc-ready](https://github.com/mkhaled87/jemdoc-ready)
2. Replace the jemdoc.py file with the jemdoc.py file from [jemdoc+MathJax](https://github.com/wsshin/jemdoc_mathjax)
3. Edit MENU (add a \ before your external link so it will be opened in a new tab), website.conf, and files in the jemdoc folder.
4. If you just need a single page, then use the members.jemdoc and rename it to index.jemdoc.
5. Run $make in the command line
6. The html files are compiled from jemdoc files.
7. I only have one page so I copy the index.html and css files to the root folder, but you can [Deploying a subfolder to GitHub Pages](https://gist.github.com/cobyism/4730490)
7. Check if like your page in local browser and commit the changes to the username.github.io repository.

Your Github page should be active once your commit is completed.

[https://drganghe.github.io](https://drganghe.github.io)