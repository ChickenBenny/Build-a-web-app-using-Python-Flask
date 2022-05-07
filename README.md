# Web app with taking note function
This project is my first web app project.I try to build a web app with two funtions, which are taking note and asking question anonymously.

And this web app is make for our lab, since we need to have a meeting on Wednesday and make the weekly report.Sometimes, teacher and classmates will have an amazing question, but will forgot quickly.Therefore I make this project try to solve the problem.


* ### Project Structure
```
├── main.py
├── website
│  ├── static
│  │  └── index.js
│  ├── templates
│  │  ├── base.html
│  │  ├── home.html
│  │  ├── login.html
│  │  ├── meeting.html
│  │  └── sign.html
│  ├── __init__.py
│  ├── auth.py
│  ├── models.py
│  ├── views.py
│  └── database.db
```

* ### Database
In this app we build three table with sqlite.
1. User information
2. User note
3. Meeting question


* ### Screenshot
#### Sign up
![](https://i.imgur.com/Mj8B0TT.png)

#### Login
![](https://i.imgur.com/DJL7nG2.png)

#### Add or Delete Note and Question
![](https://i.imgur.com/BGHuRwa.png)

* ### Running The App
```
python main.py
```

* ### Viewing The App
```
Go to http://127.0.0.1:5000
```
