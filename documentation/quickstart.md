# Preliminaries

## Background Reading

* Read the ECA Paper - this is the best explanation of our motivation right now
* Fundamentals of Critical Argumentation - A good introduction to practical argumentation theory and some introduction to argument analysis, diagrams and schemes:
* The Araucaria paper - we use the Araucaria software tool to analsyse textual argument resources. This paper introduces the motivations for the development of the tool:
    * https://www.dropbox.com/s/42ksaxshqnz3x2n/reed2001araucaria.pdf?dl=1
* The Araucaria Manual - has practical information about using the tool:
    * https://www.dropbox.com/s/wkxkd54vs6i46wm/araucaria.3-1.manual.pdf?dl=1
* Handbook of Argumentation Theory - For deeper background and historical perspectives on the field:


# Software

For software you will need to install the following:

* Git - a software source code repository manager that we use to store and track the STCD. How you install it depends upon your operating system.
* Python - a programming language and interpreter that runs the scripts & tools used in the STCD to add and analyse resources. Python version 2.7+ & 3+ should work fine. If you discover bugs, raise an issue in the github page.
* Araucaria - the argument analysis tool available from here:
    * https://dl.dropboxusercontent.com/u/12095473/software/araucaria.zip


# STCD
The dataset exploits the functionality of the "Git" source code management tool. This provides an automatic history of changes made to any resources that are committed to it. However, Git can be complicated to get started with. I recommend using an online tutorial to get started in understanding general Git use. You also have a choice of using a terminal or GUI program. Terminal is best if you are comfortable with it, but a GUI is simpler for beginners (I haven't personally used a GUI for Git so cannot recommend one). To keep track of resources, such as our transport communication resoruces, we have to follow a process that ensures that well formed resources are properly saved. This process is best summed up as follows:


* Find resource: note the URL. Make a plain text (resource.txt) copy of the resource. Print to PDF, or screen capture the resource in its original location (resource.pdf or resource.jpg). Use the python script from the STCD repository to create a unique ID (a UUID) for the resource. The script sets up a folder using the UUID and a metadata file (metadata.txt) - I encourage you to explore the contents of the STCD dataset folder.
* Make initial capture of data and format correctly on disk using the resources.py python script
* Add resources to our STCD Git repo (the 'git add' process)
* Commit the resources into the repo (the 'git commit' process) with a commit message. Commit messages form our history of changes for the repository so we must aim to get not make commits of changes to large or fine grained. This is a skill that we'll develop.


Until now the above process will create local changes in your repo. You do not have to share these, and your local repo is just as good as any othe copy. However no-one else can see your changes so you need to move your changes to a remote copy of the repository that is public. There is a public copy of the repo that is owned by Simon Wells (which is currently the canonical version mentioned in the STCD paper):
    https://github.com/siwells/STCD


However, a good workflow might be to use a GitHub or Bitbucket account to host your own remote backup copy. Once your changes are in your remote repository then you can contact other owners to 'pull' a copy of your changes. This ensures that there is a controlled process of updating the canonical public master copy.


    When you are ready to move your changes to your public repository then you do a 'git push' to a "remote" repository









