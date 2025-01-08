Toolbox Program

This Python program manages a collection of tools, allowing users to list, borrow, return, and utilize various tools.
Features

    Load Tools: Reads tool information from a CSV file and initializes the toolbox.
    Save Toolbox State: Saves the current state of the toolbox to a CSV file.
    List Tools: Displays all tools in the toolbox with their details.
    Borrow Tool: Allows a user to borrow a tool, updating its status and recording the borrower's information.
    Return Tool: Enables the return of a borrowed tool, updating its status accordingly.
    Use Tool: Simulates the usage of a borrowed tool, with specific actions based on the tool type.

#Requirements

    Python 3.x
    CSV file named toolbox.csv containing tool data.

CSV File Format

The toolbox.csv file should have the following columns:

    Type: The type of tool (e.g., Tournevis, Marteau).
    sous-type: The subtype of the tool, if applicable.
    taille: The size of the tool.
    Etat: The current state of the tool (e.g., disponible, emprunté).
    Emprunt: The name of the person who borrowed the tool.
    date emprunt: The date and time when the tool was borrowed.
    usage: The number of times the tool has been used.

#Usage

    Initialize the Toolbox: Ensure the toolbox.csv file is in the same directory as the script.
    Run the Program: Execute the script using Python.
    Main Menu: Follow the on-screen prompts to list tools, borrow a tool, return a tool, use a tool, save the toolbox state, or exit the program.

Tool Classes

The program defines the following tool classes, each with specific attributes and methods:

    Tournevis (Screwdriver): Methods include visser() and devisser().
    Marteau (Hammer): Method includes planter_clou().
    Clé Plate (Wrench): Specific methods can be added as needed.
    Perceuse (Drill): Method includes percer().
    Foret (Drill Bit): Specific methods can be added as needed.

Adding New Tools

To add a new tool to the toolbox:

    Update the CSV File: Add a new row with the tool's details.
    Define a New Class (if necessary): Create a new Python class for the tool type with appropriate methods.
    Modify the charger_boite Function: Include logic to handle the new tool type during initialization.

#Notes

    Ensure that the CSV file uses a semicolon (;) as the delimiter.
    The program assumes that the CSV file is encoded in latin-1. Adjust the encoding parameter in the open function if your file uses a different encoding.
    Date and time are recorded in the format YYYY-MM-DD HH:MM:SS.


Acknowledgments

This program was developed to manage a toolbox inventory efficiently using Python classes and CSV file handling.
