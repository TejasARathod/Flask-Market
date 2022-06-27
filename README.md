
## Flask-Market  

An e-commerce website with its own authentication system created using flask that acts as a market. It serves basic functionalities such as Logging In , Registering New Account , Navigating through tabs, Validating each process ,Redirecting users accordingly and much more.
Key features include a budget for user to buy or sell products in the market. 
## WorkFlow
Step1: Setting up Flask and Running Basic Website ; playing with URLs (market.py)

*Note*: Turn Debugger ON for continous changes on website and OFF while final deployement  

Step2: Styling the website by creating html file (market.html) , using bootstrap ; setting up navigation bar and colors

*Note*: We will be using Jinja syntax to make changes in the html file

Step3: Creating tables and iterating through it for listing down items on our webpage

Step4: Template Inheritence; Creating a base template to avoid repetition . We want to create unique title/names while we traverse through our webpage: create blocks
We dont have functionality to traverse through buttons: {{ url_for('home_page') }}// dynamically , not hardcoded

Step5: Store Data in an organized way ; use databases: store data using tables. USE SQLite3 , usinf sqlalchmey create pyhton classes using database . We use Pyton Shell to create database

Step6: Restructing teh whole thing , having models in one file and same for routes. thus creating a new dir and moving our py files there. We will be using __init__ as it allows the file that is being called to execute first 

Step7: we have to deal about the user's , create a module to store their info in. we will be using the concept of model relationship for our database to know that user's can own certain items. Creating the table from scratch in database

    >>> from market.models import db
    >>> db.drop_all()
    >>> db.create_all()
    >>> from market.models import User,Item
    >>> u1 = User(username = 'tej', password_hash='98765',email_address='tej@tej.com')
    >>> db.session.add(u1)
    >>> db.session.commit()
    >>> User.query.all()
    [<User 1>]

    >>> i1 = Item(name='iPhone', description='desc',barcode='123456789123',price=95000)
    >>> db.session.add(i1)
    >>> db.session.commit()

    >>> Item.query.all()
    [Item iPhone, Item Laptop]
    >>> item1 = Item.query.filter_by(name='iPhone')
    >>> item1
        <flask_sqlalchemy.BaseQuery object at 0x000001D8274594E0>
    >>> item1 = Item.query.filter_by(name='iPhone').first()
    >>> item1
    Item iPhone
    >>> item1.owner
    >>>
    >>> item1.owner = User.query.filter_by(username='tej').first()
    >>> db.session.add(item1)
    To build a relationship between owner and product using the id is very important
    >>> db.session.rollback()
    >>> item1.owner = User.query.filter_by(username='tej').first().id
    >>> db.session.add(item1)
    >>> db.session.commit()
    >>> item1.owner
    1
    >>> i = Item.query.filter_by(name='iPhone').first()
    >>> i.owned_user
        <User 1>


Step8: Now we want to build a html form that allows the user to register. Flask has built in packages(flask-wtf, wtforms).When building a form we have to generate a security key more like a security layer for the form otherwise the html page wont show up

    >>> import os
    >>> os.urandom(12).hex()
    'd7ef8c8ac8577df15218d013'

Step9: We now have to configure the create account button by editing the route file and redirect the user to our desired page . we then have to create validations for the data we receive to create an account.

Step10: We use Flash to display error messages on the html page itself. we also then solve a specific problem if someone enters the same username

Step11: user's passwords are getting stored directly without any filters. thus we have to change the format of its looks(hash password) using Bcrypt ; next we will setup a login page like we did for register page ; next we want to properly configure the login page

step12: use flask_login to cutomize login page/system, create validations for login , create function to crosscheck password for login. In base.html make changes that adhere to standard websites after logging in . then create budget tab:

    >>> p=1000
    >>> str(p)
    '1000'
    >>> str(p)[-3]
    '0'
    >>> str(p)[-3:] 
    '000'
    >>> a = f',{str(p)[-3:]}'
    >>> a
    ',000'
    >>> a = f'{str(p)[:-3]},{str(p)[-3:]}' 
    >>> a
    '1,000'
    >>> p=100000
    >>> a = f'{str(p)[:-3]},{str(p)[-3:]}'
    >>> a
    '100,000'

Step13: Now time to configure Logout by creating new route. After we setup our home page we notice that market page is accessible without even logging in so we want our user to login/register first and then browse our webpage
Going back to our decorator concept:

        @app.route('/')  
        @app.route('/home')
        def home_page():
            return render_template('home2.html')
The decorator executes first before even executing the function , thus similar way we will use login required concept as a decorator.
After registering a new account we want to directly login rather than manually thus we have to fix that

Step14: We now want to customize our market page to diplay the items in a better way using bootstrap styling method: grid, modals  . We first enable the More Info buton to work properly but then call it in a for loop so that each item has its own unique description. Next we create a verification modal for 'Purchase this item'

Step15: We want a confirm purchase button on the window that appears for purchasing and for that we will have to create a form and a submit like button through it just like login and register but using a different request method. 
Whenever we refresh a page we get the confirm form resubmission and to fix that we have to differentiate the request methods that is get and post

Step16: Final setup for selling items.
## Tech Stack

**Language Used:** Python, HTML

**IDE Used:** VS Code


## Deployement

In the terminal:

    > FLASK_APP=market.py
    > set FLASK_DEBUG=1
    > python run.py 

Then follow the link where it says running on...
## Special thanks to

 - [freeCodeCamp.org](https://www.youtube.com/c/Freecodecamp)
 - [jimshapedcoding](http://jimshapedcoding.com/)
 
 


## Authors

- [@tejasrathod](https://www.linkedin.com/in/tejas-rathod-923187189/)



## License

[MIT](https://github.com/TejasARathod/Flask-Market/blob/387d2d5dacbe1d29422f9c0514933ddf815521c6/LICENSE)


## Website Preview

![](https://github.com/TejasARathod/Flask-Market/blob/21f98c0d4a4ec47683610e577f3c0a17c2092070/Screenshot%202022-06-27%20200528.png)



