from pyscript import document, display  # Import document and display from PyScript


# Dictionary storing the creator's personal information
creator_profile = {
    "Name": "Firstname Lastname",
    "Grade & Section": "Grade 10 - Section",
    "Interests": "Web Design, Python Programming, Technology",
    "Hobbies": "Coding, Basketball, Reading, Gaming",
    "Dream": "To become a Full-Stack Software Developer",
    "Favorite Quote": "First, solve the problem. Then, write the code."
}

# List to store visitor messages dynamically
visitor_messages = []


def display_creator(_event):
    """Display the creator's profile details from the dictionary."""
    output_box = document.getElementById("creator_output")
    output_box.innerHTML = ""  # Clear previous output

    # Loop through dictionary keys and values
    for category, detail in creator_profile.items():
        display(f"{category}: {detail}", target="creator_output")


def add_visitor_message(_event):
    """Retrieve visitor input, append to list, and display all messages."""
    name = document.getElementById("visitor_name").value.strip()
    message = document.getElementById("visitor_message").value.strip()
    wall_box = document.getElementById("wall_output")
    wall_box.innerHTML = ""

    # Validate that both input fields have text
    if name == "" or message == "":
        display("Please fill out both your name and a message.", target="wall_output")
        return

    # Append formatted entry to the list
    entry = f'{name}: "{message}"'
    visitor_messages.append(entry)

    # Display total count and each entry
    display(f"Total Messages ({len(visitor_messages)}):", target="wall_output")
    for item in visitor_messages:
        display(item, target="wall_output")

    # Clear input boxes after submitting
    document.getElementById("visitor_name").value = ""
    document.getElementById("visitor_message").value = ""