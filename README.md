## Team Information

**Suchitra M**
- Backend setup and database schema definition, built monshop & meal log page, developed logic for logging meals, assisted in prompt engineering, chose design theme for the website, ideated and brainstormed solutions, worked on presentation and was responsible solely for video editing

**Tasneem I**
- Backend setup and database schema definition, built distractions page, developed logic for gaining meal log analytics, points increase and purchase of Eatimons, developed chatbot and its UI and deployed it, worked on prompt engineering, worked on data collection, ideated and brainstormed solutions, cleaning and preprocessing for short screening model, developed and compared different models and chose the most accurate for short screening classification, worked on script writing and presentation

**Thejuswini R**
- Frontend ideation and flow, pair programmed with Trisheta to build landing, awareness - anorexia nervosa, bulimia nervosa, binge eating disorder and Avoidant/Restrictive Food Intake Disorder, signup, login and home page, worked on data collection, preprocessing and encoding, ideated and brainstormed solutions, worked on presentation.

**Trisheta S**
- Frontend ideation and flow, pair programmed with Thejuswini to build landing, awareness - anorexia nervosa, bulimia nervosa, binge eating disorder and Avoidant/Restrictive Food Intake Disorder, signup, login and home page, worked on data collection, consulted and collected science backed EDE-Q questions with a psychologist, organized and developed logic for questionnaires, ideated and brainstormed solutions, worked on presentation.

## Inspiration

For this hackathon, we aimed to address an issue that is often overlooked and focused on problems related to sustainable development goals. That's when we came across the topic of eating disorders. As we researched various eating disorders and their impact on society, we were shocked to discover some alarming facts:

1. People with eating disorders often suffer from major mental health conditions like PTSD, depression, and OCD.
2. Close to 20% of people with anorexia die within 20 years.
3. 95% of people reported to suffer from eating disorders are in the 18-25 age group.
4. There are almost 8 million people with eating disorders in America alone.
5. Only 10% of people with eating disorders receive treatment.

We were further surprised to find that some symptoms of eating disorders were exhibited by people in our social circles. This motivated us to dive deeper into the available software solutions. We found a blog on Healthline about the top software solutions for eating disorders. While the top-rated app had interesting research-backed solutions, it also had some drawbacks:

1. It lacked an interactive and well-designed UI.
2. Some features, though good, lacked clarity and guidance.

We also explored projects on Devpost but couldn't find a good solution for eating disorders. This made us realize that eating disorders don't get the attention they deserve. So, we decided to build a solution to help people with eating disorders develop a better relationship with food.

Eat-o-Mate is our effort to create a supportive, user-friendly platform that not only provides real-time assistance and resources but also fosters a sense of community. We believe that with the right tools and support, individuals can overcome their challenges and lead healthier, happier lives.

## What it does

Eat-o-Mate is a user-friendly web app designed to help manage and understand eating disorders through these key features:

- **EDE-Q Questionnaire**: A simple, science-backed questionnaire to help identify the type and intensity of an eating disorder, providing personalized insights and understanding.

- **Meal Log**: Track your meals and reflect on your eating habits, feelings, and behaviors. Earn Nurture Stars for each log, which can be exchanged for fun EatMons characters, encouraging regular tracking and self-awareness. It also keeps track of normal meals where the user did'nt overeat or restrict and also displays with whom they ate most normal meals with to give users some insights.

- **Distraction Tab**: When facing triggers, access engaging exercises with a timer to help shift focus from intrusive thoughts, promoting healthier choices and well-being.

Additional features include:

- **Chatbot**: Tailored responses to your emotional needs, offering comforting suggestions using advanced AI.

- **Monshop Page**: A reward system where you can trade Nurture Stars for cute EatiMons characters, motivating frequent use of the app's features.

- **Awareness Page**: Comprehensive information about eating disorders, helping you understand your eating patterns and use the app’s tools effectively.

Eat-o-Mate is designed to support and empower users in building a healthier relationship with food.

## How we built it

We developed the main website using Flask, SQLite, HTML, CSS, and JavaScript. Additionally, we utilized the Requests library for HTTP requests. 

For the chatbot, we integrated the Gemini Pro model via its API and employed Prompt Engineering techniques to provide emotional support. The chatbot's user interface was created with Streamlit.

To build the classification model for the EDE-Q questionnaire, we used Pandas, Scikit-Learn, and Joblib. We tested various models, including decision trees, KNN, and Random Forests, using five-fold cross-validation with GridSearchCV to find the best parameters. After comparing the accuracy, we chose decision trees due to the minimal difference in performance between decision trees and random forests.

## Challenges we ran into

1. We had so many features in mind that it was challenging to decide which ones to include in our prototype.
2. Our limited experience with JavaScript meant it took us some time to get things up and running.
3. We had never worked with the Gemini API or prompt engineering before, so implementing the chatbot was a learning curve.
4. Deploying with Streamlit presented some unexpected issues that we had to resolve.
5. Developing the ML model for the questionnaire results took longer than expected, so we ended up using a less efficient conditional classification since integration was challenging.
6. Creating our dataset and gathering accurate information about eating disorders was time-consuming, as we wanted to avoid spreading misinformation.
7. We attempted to use computer vision to check exercise posture but couldn't get it to work accurately, so we had to set that feature aside.

## Accomplishments that we're proud of

This project got us some valuable knowledge and satisfaction. We got the hang of JavaScript, which we believed to be a huge setback as we are all primarily python-ers.
Using Gemini's API was easier than what we believed, and it was interesting to learn about how APIs and LLMs work, particularly how they can be tuned to provide better answers with prompt engineering techniques.
We were also very invested in maximizing our model accuracy and comparing different models which helped us understand how to work with data better and some glimpses into how optimizing works.

Implementing the camera and distract session functionalities while considered easy was a huge milestone for us, so was the case for meal logging. 
We are extremely happy to have implemented a way for users to gain insights about their logged meals where they ate right and with whom they had most normal meals with which could help them in their meal planning. 
We also spent quite some time holding conversations with a relative of our teammate- a psychologist, to understand about eating disorders in a better way since online resources may not be the most accurate.
 Overall, the biggest accomplishment is our belief that this solution, while still in its infancy will be useful and helpful for people with eating disorders.



## What's next for Eat-O-Mate

We brainstormed and came up with a lot more ideas than what we could implement during this hackathon, which we believe can be implemented in the future. 
1. The first one would be to find ways to provide more deeper visualizations and analytics to the user, specifically discussing over what data we could potentially collect.
2. Next, we want to provide a guided way for users to identify their triggers and keep track of them and brainstorm ways to handle them.
3. We also plan to find a way to provide an optional way for users to connect with clinical experts to curate better treatment plans and a way to implement an anonymous conversation feature for users to discuss about their problems in a safer environment with people in similar position.
4. A computer vision based posture checker for exercising would be an interesting feature to add, which can increase the gamification process.
5. Most importantly, we also want to find ways to extend our awareness details on eating disorders to be more gamified, and increase our database on eating disorders like orthorexia, which is a rising type where a person is so heath conscious that they eliminate a certain category of food due to fear, resulting in malnutrition.
