## Introduction to Shell Scripting
---
```
The shell is a program that provides the user with an interface to use the 
operating system’s functions through some commands. A shell script is a 
program that is used to perform specific tasks
```
```
Shell scripts are mostly used to avoid repetitive work. You can write 
a script to automate a set of instructions to be executed one after the other,
 instead of typing in the commands one after the other n number of time
```
### A typical script might look like this:
```
#!/bin/bash
echo "Welcome!! Please Enter Your Name"
read name
echo "Hello $name"
```
### Executing the file
```
Now that we have seen what a typical shell script looks like, 
let’s look at how to execute the file
1 . Save the file with a .sh extension
1 . To execute the file, first we need to give it execute permissions.
	* chmod +x filepath/filename.sh
1 . To execute the file, we can do it in the following ways
*If you are using a GUI file navigation system, right-click on the file and click on run or execute.
*If you are using the terminal, ./filename.sh will execute the script. 
(Make sure you are in the correct directory!) 
```
## Task list
---
* [x] Shell Basics
* [x] Shell Permissions
* [x] Shell Redirections
* [x] Shell Variables and Expansions
