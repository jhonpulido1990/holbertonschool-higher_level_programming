# 0x09. Python - Everything is object
## Details
      By Guillaume          Weight: 1              Project over - took place from 01-25-2022 to 01-26-2022          - you're done with 97% of tasks.                Manual QA review was done by Johanna Alfonso Moreno on 01-30-2022.              An auto review will be launched at the deadline      #### In a nutshell…
* Manual QA review:          70.0/72 mandatory      
* Auto QA review:          94.0/94 mandatory            &            0.0/59 optional      
* Altogether:         98.8%* Mandatory: 98.8%
* Optional: 0.0%
*               Calculation:                   98.8%                    + (98.8% * 0.0%)               == 98.8%

 ![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/252/r_208403_QPSN8.jpg) 

## Background Context
Now that we understand that everything is an object and have a little bit of knowledge, let’s pause and look a little bit closer at how Python works with different types of objects.
BTW, have you ever modified a variable without knowing it or wanting to? I mean:
 ` >>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>> 
 ` OK. But what about this?
 ` >>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>> 
 `  ![](https://media.giphy.com/media/wAjfQ9MLUfFjq/giphy.gif) 

This project is a little bit different than the usual projects. The first part is only questions about Python’s specificity like “What would be the result of…”. You should  read all documentation first (as usual :)) , then take the time to  think and brainstorm with your peers  about what you think and why.  Try to do this without coding anything for a few hours .
Trying examples in the Python interpreter will give you most of the answers without having to think about it.  Don’t go this route . First read, then think, then brainstorm together. Only then you can test in the interpreter.
It’s important that you truly understand the reasons behind the answers of all those tasks so that you can apply the same logic to other variables and other variable types.The biggest mandatory task is the blog post and it will count for 50% of the total score of the project.
Note that during interviews for Python positions,  you will most likely have to answer to these type of questions .
All your answers should be only one line in a file. No space before or after the answer.
## Resources
Read or watch :
* [9.10. Objects and values](https://intranet.hbtn.io/rltoken/n1x09X-KJSllpJkJorBw2A) 

* [9.11. Aliasing](https://intranet.hbtn.io/rltoken/3teQMNNfDeyGvCtZfjsf5g) 

* [Immutable vs mutable types](https://intranet.hbtn.io/rltoken/JuPVygeoG27Q_qKxB2lP8g) 

* [Mutation](https://intranet.hbtn.io/rltoken/UbL96sV3cIxewdQPW_zwRw) 
 (Only this chapter)
* [9.12. Cloning lists](https://intranet.hbtn.io/rltoken/-t_1VsmKlgWHszL5y1YiKA) 

* [Python tuples: immutable but potentially changing](https://intranet.hbtn.io/rltoken/IdBAdTYNLuS3YpRRQIam6Q) 

## Learning Objectives
At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/d0Wvl9mlCY4CQDJg1qzamQ) 
 ,  without the help of Google :
### General
* Why Python programming is awesome
* What is an object
* What is the difference between a class and an object or instance
* What is the difference between immutable object and mutable object
* What is a reference
* What is an assignment
* What is an alias
* How to know if two variables are identical
* How to know if two variables are linked to the same object
* How to display the variable identifier (which is the memory address in the CPython implementation)
* What is mutable and immutable
* What are the built-in mutable types
* What are the built-in immutable types
* How does Python pass variables to functions
## Requirements
### Python Scripts
* Allowed editors:  ` vi ` ,  ` vim ` ,  ` emacs ` 
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly  ` #!/usr/bin/python3 ` 
* A  ` README.md `  file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* The length of your files will be tested using  ` wc ` 
### .txt Answer Files
* Only one line
* No Shebang
* All your files should end with a new line
## More Info
### Manual QA Review
It is your responsibility to request a review for your blog from a peer before the project’s deadline. If no peers have been reviewed, you should request a review from a TA or staff member.
## Tasks
### 0. Who am I?
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body What function would you use to print the type of an object?
Write the name of the function in the file, without   ` () `  .
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x09-python-everything_is_object ` 
* File:  ` 0-answer.txt ` 
 Self-paced manual review  Panel footer - Controls 
### 1. Where are you?
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body How do you get the variable identifier (which is the memory address in the CPython implementation)?
Write the name of the function in the file, without   ` () `  .
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x09-python-everything_is_object ` 
* File:  ` 1-answer.txt ` 
 Self-paced manual review  Panel footer - Controls 
### 2. Right count
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body In the following code, do   ` a `   and   ` b `   point to the same object?Answer with   ` Yes `   or   ` No `  .
 ` >>> a = 89
>>> b = 100
 `  Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x09-python-everything_is_object ` 
* File:  ` 2-answer.txt ` 
 Self-paced manual review  Panel footer - Controls 
### 3. Right count =
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body In the following code, do   ` a `   and   ` b `   point to the same object?Answer with   ` Yes `   or   ` No `  .
 ` >>> a = 89
>>> b = 89
 `  Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x09-python-everything_is_object ` 
* File:  ` 3-answer.txt ` 
 Self-paced manual review  Panel footer - Controls 
### 4. Right count =
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body In the following code, do   ` a `   and   ` b `   point to the same object?Answer with   ` Yes `   or   ` No `  .
 ` >>> a = 89
>>> b = a
 `  Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x09-python-everything_is_object ` 
* File:  ` 4-answer.txt ` 
 Self-paced manual review  Panel footer - Controls 
### 5. Right count =+
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body In the following code, do   ` a `   and   ` b `   point to the same object?Answer with   ` Yes `   or   ` No `  .
 ` >>> a = 89
>>> b = a + 1
 `  Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x09-python-everything_is_object ` 
* File:  ` 5-answer.txt ` 
 Self-paced manual review  Panel footer - Controls 
### 6. Is equal
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body What do these 3 lines print?
 ` >>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
 `  Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x09-python-everything_is_object ` 
* File:  ` 6-answer.txt ` 
 Self-paced manual review  Panel footer - Controls 
### 7. Is the same
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body What do these 3 lines print?
 ` >>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
 `  Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x09-python-everything_is_object ` 
* File:  ` 7-answer.txt ` 
 Self-paced manual review  Panel footer - Controls 
### 8. Is really equal
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body What do these 3 lines print?
 ` >>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
 `  Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x09-python-everything_is_object ` 
* File:  ` 8-answer.txt ` 
 Self-paced manual review  Panel footer - Controls 
### 9. Is really the same
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body What do these 3 lines print?
 ` >>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
 `  Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x09-python-everything_is_object ` 
* File:  ` 9-answer.txt ` 
 Self-paced manual review  Panel footer - Controls 
### 10. And with a list, is it equal
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body What do these 3 lines print?
 ` >>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
 `  Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x09-python-everything_is_object ` 
* File:  ` 10-answer.txt ` 
 Self-paced manual review  Panel footer - Controls 
### 11. And with a list, is it the same
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body What do these 3 lines print?
 ` >>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
 `  Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x09-python-everything_is_object ` 
* File:  ` 11-answer.txt ` 
 Self-paced manual review  Panel footer - Controls 
### 12. And with a list, is it really equal
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body What do these 3 lines print?
 ` >>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
 `  Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x09-python-everything_is_object ` 
* File:  ` 12-answer.txt ` 
 Self-paced manual review  Panel footer - Controls 
### 13. And with a list, is it really the same
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body What do these 3 lines print?
 ` >>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
 `  Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x09-python-everything_is_object ` 
* File:  ` 13-answer.txt ` 
 Self-paced manual review  Panel footer - Controls 
### 14. List append
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body What does this script print?
 ` l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
 `  Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x09-python-everything_is_object ` 
* File:  ` 14-answer.txt ` 
 Self-paced manual review  Panel footer - Controls 
### 15. List add
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body What does this script print?
 ` l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
 `  Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x09-python-everything_is_object ` 
* File:  ` 15-answer.txt ` 
 Self-paced manual review  Panel footer - Controls 
### 16. Integer incrementation
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body What does this script print?
 ` def increment(n):
    n += 1

a = 1
increment(a)
print(a)
 `  Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x09-python-everything_is_object ` 
* File:  ` 16-answer.txt ` 
 Self-paced manual review  Panel footer - Controls 
### 17. List incrementation
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body What does this script print?
 ` def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
 `  Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x09-python-everything_is_object ` 
* File:  ` 17-answer.txt ` 
 Self-paced manual review  Panel footer - Controls 
### 18. List assignation
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body What does this script print?
 ` def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
 `  Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x09-python-everything_is_object ` 
* File:  ` 18-answer.txt ` 
 Self-paced manual review  Panel footer - Controls 
### 19. Copy a list object
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body Write a function   ` def copy_list(l): `   that returns a  copy  of a list.
* The input list can contain any type of objects
* Your file should be maximum 3-line long (no documentation needed)
* You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x09$ cat 19-main.py
#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)

guillaume@ubuntu:~/0x09$ ./19-main.py
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
True
False
guillaume@ubuntu:~/0x09$ wc -l 19-copy_list.py 
3 19-copy_list.py
guillaume@ubuntu:~/0x09$ 

```
No test cases needed
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x09-python-everything_is_object ` 
* File:  ` 19-copy_list.py ` 
 Self-paced manual review  Panel footer - Controls 
### 20. Tuple or not?
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body  ` a = ()
 ` Is   ` a `   a tuple? Answer with   ` Yes `   or   ` No `  .
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x09-python-everything_is_object ` 
* File:  ` 20-answer.txt ` 
 Self-paced manual review  Panel footer - Controls 
### 21. Tuple or not?
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body  ` a = (1, 2)
 ` Is   ` a `   a tuple? Answer with   ` Yes `   or   ` No `  .
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x09-python-everything_is_object ` 
* File:  ` 21-answer.txt ` 
 Self-paced manual review  Panel footer - Controls 
### 22. Tuple or not?
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body  ` a = (1)
 ` Is   ` a `   a tuple? Answer with   ` Yes `   or   ` No `  .
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x09-python-everything_is_object ` 
* File:  ` 22-answer.txt ` 
 Self-paced manual review  Panel footer - Controls 
### 23. Tuple or not?
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body  ` a = (1, )
 ` Is   ` a `   a tuple? Answer with   ` Yes `   or   ` No `  .
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x09-python-everything_is_object ` 
* File:  ` 23-answer.txt ` 
 Self-paced manual review  Panel footer - Controls 
### 24. Who I am?
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body What does this script print?
 ` a = (1)
b = (1)
a is b
 `  Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x09-python-everything_is_object ` 
* File:  ` 24-answer.txt ` 
 Self-paced manual review  Panel footer - Controls 
### 25. Tuple or not
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body What does this script print?
 ` a = (1, 2)
b = (1, 2)
a is b
 `  Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x09-python-everything_is_object ` 
* File:  ` 25-answer.txt ` 
 Self-paced manual review  Panel footer - Controls 
### 26. Empty is not empty
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body What does this script print?
 ` a = ()
b = ()
a is b
 `  Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x09-python-everything_is_object ` 
* File:  ` 26-answer.txt ` 
 Self-paced manual review  Panel footer - Controls 
### 27. Still the same?
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body  ` >>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
 ` Will the last line of this script print   ` 139926795932424 `  ? Answer with   ` Yes `   or   ` No `  .
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x09-python-everything_is_object ` 
* File:  ` 27-answer.txt ` 
 Self-paced manual review  Panel footer - Controls 
### 28. Same or not?
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body  ` >>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
 ` Will the last line of this script print   ` 139926795932424 `  ? Answer with   ` Yes `   or   ` No `  .
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x09-python-everything_is_object ` 
* File:  ` 28-answer.txt ` 
 Self-paced manual review  Panel footer - Controls 
### 29. Python3: Mutable, Immutable... everything is object!
          mandatory         Progress vs Score           Score: 97.22% (Checks completed: 100.00%)         Task Body Write a blog post about everything you just learned / this project is covering. Your blog post should be articulated this way (one paragraph per item):
* introduction
* id and type
* mutable objects
* immutable objects
* why does it matter and how differently does Python treat mutable and immutable objects
* how arguments are passed to functions and what does that imply for mutable and immutable objects
If you worked on advanced tasks, please also include what you did learn in those tasks in the blog post.
Your posts should have many code/output examples to illustrate what you are explaining, and at least one picture, at the top.Publish your blog post on Medium or LinkedIn, and share it at least on LinkedIn.
When done, please add all urls below (blog post, LinkedIn post, etc.)
Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.
 Task URLs #### Add URLs here:
                Save              [https://medium.com/@3825_30593/python-ab52a53f0121](https://medium.com/@3825_30593/python-ab52a53f0121) 
                  Remove                 Github information  Self-paced manual review  Panel footer - Controls 
[Done with the mandatory tasks? Unlock 6 advanced tasks now!](https://intranet.hbtn.io/projects/252/unlock_optionals) 

Ready for a manualsecond review×#### Recommended Sandbox
[Running only]() 
### 1 image(1/5 Sandboxes spawned)
### Ubuntu 20.04
Basic Ubuntu 20.04, with vim, emacs, curl, wget and all needed for Holberton Foundations
SSHSFTP[Webterm](https://intranet.hbtn.io/user_containers/17836/webterm) 
[Destroy]() 
#### Credentials
Host4aa76ec2605d.ba0aa7bd.hbtn-cod.ioUsername4aa76ec2605dPassword95896abd009a136e84ba#### Web access
[HTTPS](https://4aa76ec2605d.ba0aa7bd.hbtn-cod.io/) 
[HTTP](http://4aa76ec2605d.ba0aa7bd.hbtn-cod.io/) 
[3000](http://4aa76ec2605d.ba0aa7bd.hbtn-cod.io:3000/) 
[4000](http://4aa76ec2605d.ba0aa7bd.hbtn-cod.io:4000/) 
[5000](http://4aa76ec2605d.ba0aa7bd.hbtn-cod.io:5000/) 
[5001](http://4aa76ec2605d.ba0aa7bd.hbtn-cod.io:5001/) 
[8000](http://4aa76ec2605d.ba0aa7bd.hbtn-cod.io:8000/) 
[8080](http://4aa76ec2605d.ba0aa7bd.hbtn-cod.io:8080/) 
#### Port mapping
SSH49328HTTP49327HTTPS49326300049325MySQL49324400049323500049322500149321800049320808049319