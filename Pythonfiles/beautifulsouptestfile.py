import requests
# so youll need to pip3 install bs4
from bs4 import BeautifulSoup
#youll need to make a request and recieve a response and set that response as the variable
variable="""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewpoint" content="width =device-width, initial-scale=1.0">
<title>MY Webpage</title>
<head>
<body>
<div id="section-1">
<h3 data-hello="hi">Hello</h3>
<img src="https://source.unsplash.com/200x200/?nature,water" />
<p> lorem ipsum dolor, sit amet consectetur random working i dont wrealkeae i dont wanna type a whole lot but im gonna</p>
</div>
<div id="section-2">
<ul class="items">
<li class="items"><a href="#">Item 1</a></li>
<li class="items"><a href="#">Item 2</a></li>
<li class="items"><a href="#">Item 3</a></li>
<li class="items"><a href="#">Item 4</a></li>
</ul>
</div>
</body>
</html>
"""

#first paramater is what to scrape and idk what second variable is.
soup = BeautifulSoup(variable,'html.parser')

#Direct should grab the body
#print(soup.body)
#shoud grab the head
#print(soup.head)
