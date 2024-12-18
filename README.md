# Speech-Recognition-And-Voice-Assistant-System
A Python-based voice assistant that uses speech recognition to process commands and text-to-speech to respond. It retrieves stock prices from a MySQL database, reads content from text files, and executes actions based on voice input.

1.Overview:

This project demonstrates how to create a simple voice assistant using Python, integrating speech recognition for user input and text-to-speech for responses. The system can provide real-time stock price updates, read content from text files, and execute specific tasks based on voice commands.

2.Features:

Speech Recognition: Uses the speech_recognition library to recognize user commands via microphone input.

Text-to-Speech: Utilizes the pyttsx3 library to convert text responses into speech.

Stock Price Retrieval: Fetches stock prices from a database using MySQL and displays them based on user requests.

File Reading: Reads content from pre-defined text files (e.g., politics.txt, metal.txt, movies.txt).

Continuous Listening: The assistant keeps listening for commands until "stop" is said.

3.Prerequisites:

MySQL database with a table (stockprices) containing stock prices (or any equivalent setup).

Required libraries: speech_recognition, pyttsx3, and pymysql.

4.Setup

Configure MySQL Database:

Create a MySQL database named keke.
Create a table stockprices with columns such as company and price.
Insert stock prices (e.g., Infosys stock price) into the database.

Ensure Audio Input:

Make sure your microphone is connected and properly set up.

Text Files:

Add text files such as politics.txt, metal.txt, and movies.txt to your project directory for the assistant to read.

5.Commands:

"price": Fetches and announces the stock price of Infosys.

"politics": Reads the contents of politics.txt.

"jewels": Reads the contents of metal.txt.

"movies": Reads the contents of movies.txt.

"stop": Ends the program and stops listening for commands.

The assistant will respond audibly with the requested information.

6.Code Explanation:

Speech Recognition: Uses the speech_recognition library to capture the audio command from the user and convert it into text using Google's speech recognition API.

Text-to-Speech: pyttsx3 converts the recognized text into speech output.

MySQL Integration: The goldprice() function connects to the MySQL database and fetches the stock price for a specific company, in this case, Infosys.

Looping & Error Handling: The assistant continuously listens for commands and handles errors (e.g., network issues, unrecognized commands).

7.Example Command Flow:

"Price": The assistant will respond with the current stock price of Infosys.

"Politics": The assistant will read the contents of the politics.txt file aloud.

"Stop": The assistant will stop and exit.

