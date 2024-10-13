# Part 2

## Part A
Create a `Python` function that scrapes all links from the Intranet website, based on a file extension provided as input (e.g., `.pdf`). The function should ensure that only links within the intranet domain are collected, and not any other external links outside of intranet. Also, save the list of URLs in a text file (`urls.txt`).

## Answer
The required function is implemented in the `script.py` file. The function `get_intranet_links` takes the required file extension as input and scrapes all the links with that file extension from the Intranet website. The function ensures that only links within the intranet domain are collected and not any other external links outside of the intranet. The function saves the list of URLs in a text file `urls.txt`.

## Part B
We want to implement a feature in the Intranet website, where we store the version history
and changes of the documents uploaded on the website. Think of how you would implement this
feature. Try to go in the details of issues which can occur considering the current Intranet, and your
experience with college linked to documents (like Timetable, etc)

## Answer
To implement the feature of storing the version history and changes of the documents uploaded on the Intranet website, we can follow the following steps:

1. **Version Control System**: We can implement a version control system like Git to store the version history and changes of the documents. This will allow us to track the changes made to the documents over time and revert to previous versions if needed.

2. **Database**: We can store the version history and changes of the documents in a database. The database can store the metadata of the documents, such as the author, date of creation, date of modification, etc. This will allow us to keep track of who made the changes and when.

3. **User Permissions**: We can implement user permissions to control who can view, edit, and delete the documents. This will ensure that only authorized users can make changes to the documents.

Since the Intranet website currently being used is very basic and outdated, there are several issues that can occur while implementing this feature:

1. **Data Loss**: The current Intranet website probably does not have a backup system in place. If the data is lost due to a server crash or other issues, we may lose all the version history and changes of the documents.

2. **Security**: The current Intranet website may not have proper security measures in place to protect the documents and their version history. This can lead to data breaches and unauthorized access to sensitive information.

3. **User Experience**: The current Intranet website may not be user-friendly and may not have the features required to implement a version control system because of a lack of modern technologies and practices. This can make it difficult for users to navigate and use the website effectively.

It was pretty difficult to use resources like timetable, etc. because of the lack of accessibility and user-friendliness of the current Intranet website. Because of that, I ended up making a quick timetable for myself to keep track of my classes and assignments, which can be found [here](https://cgd-timetable.netlify.app/) (not official). This shows the need for a better Intranet website that can provide the necessary features and functionalities to the students and faculty.

## Part C
Go through the codebase of the events submdoule and try to make a flowchart of the event flow from the codebase - from event creation to getting completed. You can use any tool you are comfortable with (like draw.io, Lucidchart, etc.)

## Answer

The flowchart of the event flow from the codebase of the events submodule is created using draw.io and can be found [here](https://drive.google.com/file/d/1YwJaHbBvRLaI5T6eFrOmIXDf8PkFuyya/view?usp=sharing).
