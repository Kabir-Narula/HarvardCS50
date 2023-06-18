# Surge Web App
#### Video Demo:  https://youtu.be/YjrYyn9bU3M
#### Description:

This project is a web application which can be used by its users to search any book in the world using the search bar and to add it to their reading list. The main motive behind this application is to promote the habit of reading amongst people by letting them keep a track of their progress in terms of the number of books they have read.

#### Technologies/Frameworks/Languages/APIs used:

Flask 
HTML
CSS
Bootstrap 5
Sqlite3
JavaScript
Google Books API
Other small libraries or packages required in order to run the code

#### Working of the web app

The users start at the homepage where they can explore the main motive behind the website and why it was created. They can also read about why reading is beneficial and one should develop this habit.

Users can also search for any book they want using the search bar provided at the homepage. The books will be displayed to them in an orderly format (in the form of bootstrap cards) using the google books API to serve the books.

The users can also create a list of books they have read. However, they will be required to log in before they do so. If they are not registered, users have the option to register by using their full name, username and password. The password should have at least 5 characters in it.

Furthermore, the we app is fully responsive and is therefore capable of running smoothly on both large and small screen devices.

#### Reading List

The users can enter the name of the book as well as the Author (optional) in order to add it to their reading list. The list also gives the users the ability to delete their list and start fresh.

#### Sessions

The webpage uses sessions to confirm that user is logged in. Once the user logs in, her credentials are checked. Once everything passes a session is created (serialized and deserialized) and stored in the cookies. This allows the user to access her reading list whenever she logs in.

#### Database

There are two tables that have been used in this application, namely, registrants and userBookList. These keep track of the users’ details and the books they have read respectively.

#### Possible improvements

Users can remove an element individually from the reading list instead of having to delete all the list altogether.
Users should have the ability to add books to their reading list directly from the search results instead of having to manually enter the details.
Users should be able to update whatever they have entered in the reading list.