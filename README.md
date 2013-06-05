Analysis-StackExchange
======================

This is all the python code you would need to mine the complete StackExchange dump. The data used is  all the stackexchange data till September, 2011, released under a creative-commons license. I used this for a course project that is not even remotely commercial. 

You can download the data over Http, which is what I did, or you can use torrents. The data is quite large in size, I am uploading the smallest XML files for you to get started while your data gets downloaded ;) 

StackExchange Story
==================

The data is in the form of big XML files. Some questions you can answer

1. how many users
2. badges distribution
3. how many producers/consumers
4. popular tags

and so on. 

There was a slightly higher purpose of doing this project. I wanted to find out the kind of patterns that are visible in contributions. But, those details can be found in the blog posts  here : http://www.rohitdholakia.com/blog/categories/stackoverflow/

Getting Started
===============

I have added data about Bicycles StackExchange in the folder. Lets find out how many users . 

<pre>
Rohits-MacBook-Pro:Scripts rohitdholakia$ python CountingUsers.py ../Bicycles/users.xml 
2002
</pre>

The script is very simple. But, it has a couple of things which will be seen throughout. Note that we are doing this work on a 4gb macbook pro with a modest processor. nothing fancy. Hence, dealing with this gigantic xml files keeping them all in memory in not an option. That is where the iterparse and clearElem() play a role. we parse it line-by-line and when we are done, we remove  the element and all its parents. The parents part becomes important if you are dealing with highly nested XML files.  


