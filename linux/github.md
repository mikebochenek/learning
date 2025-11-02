# Create a new repository on the command line
~~~
touch README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/mikebochenek/html5.git
git push -u origin master
~~~

# Push an existing repository from the command line

~~~
git remote add origin https://github.com/mikebochenek/html5.git
git push -u origin master

git reset --hard HEAD~1
git rm --cached myfile
~~~