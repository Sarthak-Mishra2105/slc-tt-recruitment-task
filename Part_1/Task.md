# Part 1

## Question 1
Try finding atleast 5 technical/UI-UX issues you feel in the clubs or life website. (Not to give things like "I don't like the color of the website" or "I don't like the font of the website" as they are subjective and not technical/UI-UX issues). Write how can you solve them/potential solutions.

## Answer

1. **List of Events**: In the list of events page, I noticed that all the past events are tried to be shown in a single page. This is not a good practice as it will make the page very long and the user will have to scroll a lot to reach the bottom of the page. This can be solved by adding pagination to the list of events page. This way, only a few events will be shown on a single page and the user can navigate to other pages to see more events.

2. **Gallery**: In the gallery page, I noticed that the images are not optimized. This can make the page load very slow. This can be solved by optimizing the images. The images can be compressed and resized to reduce the size of the images. This will make the page load faster. Also, the images can be lazy loaded. This way, the images will be loaded only when the user scrolls to them.

3. **Account System**: After visiting the page many times since college begun, I finally noticed that there actually is an account system. This can be solved by making the account system more prominent. The login button can be placed in a more prominent location on the page. 

4. **Utility of Account System**: The account system is not very useful for a normal user. This can be solved by adding more features to the account system. For example, the user can save their favorite events, get notifications for upcoming events, apply for different clubs and events, etc.

5. **Reporting Issues**: There is no way to directly report issues with the website. Currently the website links to external platforms for reporting issues. This can be solved by adding a form on the website where the user can report issues directly. This way, the user does not have to leave the website to report issues, and would be more likely to report issues.

6. **Life Page Gallery**: The same issue with the clubs page gallery is also present in the life page gallery. The images are not optimized and paginated. This can be solved by optimizing the images and adding pagination to the gallery.

## Question 2
Go through the codebase of Clubs Council Website, and try to explain that how, in your opinion, the whole structure works. How there are dierent components, how they interact with each other, etc. (In a very basic way, you don't need to go into the details of the codebase)

## Answer
The codebase of the Clubs Council Website is structured in a way that makes it easy to understand and maintain. The codebase is divided into different components, and microservices. Each component is responsible for a specific part of the website, such as the frontend, backend, database, etc. The components interact with each other through APIs. For example, the frontend component interacts with the backend component through APIs to get data from the database.

The frontend component is responsible for the user interface of the website. It is built using React and Next.js. The frontend component interacts with the backend component to get data from the database and display it on the website.

The backend consists of several microservices repositories. Each microservice is responsible for a specific part of the website, such as events, clubs, etc. The microservices interact with each other through APIs to get data from the database and send it to the frontend. It is using FastAPI and Strawberry and MongoDB in Python, although it may differ since some of the code is not accessible.