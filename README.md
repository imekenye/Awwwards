## AWWWARDS
Web application built in django that allows users to review/view projects from other users and also post their own.
### Author
Isaiah Mekenye
### Live link
Click on this link https://im-awwwards.herokuapp.com/
### Api Links
use the following API links to get access to the apps JSON files using the endpoints
<code>/api/all_posts</code>
&
<code>/api/all_profile</code>at the end of the link
### Project Description
This application allows users to share their website projects and let users rate/review
### Technologies used
Python 3.6<br>
Django 2.2.1
## Application requirements

1. Ensure you have Python3.6 installed in your computer. you can download it by running this command.

`$ sudo apt-get update sudo apt-get install python3.6.`

2. Ensure you have PiP installed in your computer, you can download it by running this command:

`$ python get-pip.py`

3. set up a virtual environment using the following command;

`$ python3.6 -m venv --without-pip virtual`

4. Run the following command to install all your dependencies in your local computer;

`$ pip install -r requirements.txt`

## Project setup instruction/ installations


1. From the repository, click + in the global sidebar and select Clone this repository .

2.  Copy the clone command.

3.  From a terminal window, change to the local directory where you want to clone your repository.

or just use this

`$ git clone https://github.com/watibini/awward.git`

4. Run this command to open the app

`$ python3.6 manage.py runserver`


## BDD

| Behavior        | Result |
| ------------- |:----:|
| user loads the page | all available projects that have been posted are displayed |
| user clicks on an image of choice | user is taken to the image details |
| user clicks on make review | User is redirected to a page where he/she can make a review|
| User clicks on profile at the navbar  | Profile details of the current user is loaded |
| User clicks on update  | Profile forms are displayed |
| user searches for a project category  | user is re-directed to the searched term with relevant projects displayed |




## Contact Information

Email:ismekenye@gmail.com



## License

MIT License

Copyright (c) [2019] [Isaiah Mekenye]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.