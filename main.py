from pyscript import document, display  # Import document and display from PyScript[cite: 16]


# Dictionary storing the creator's personal information[cite: 1, 19]
creator_profile = {
    "Name": "Firstname Lastname",
    "Grade & Section": "Grade 10 - Section",
    "Interests": "Web Design, Python Programming, Technology",
    "Hobbies": "Coding, Basketball, Reading, Gaming",
    "Dream": "To become a Full-Stack Software Developer",
    "Favorite Quote": "First, solve the problem. Then, write the code."
}

# List to store visitor messages dynamically[cite: 8]
visitor_messages = []


def display_creator(e):
    """Display the creator's profile details from the dictionary."""
    output_box = document.getElementById("creator_output")
    output_box.innerHTML = ""  # Clear previous output

    # Loop through dictionary keys and values[cite: 1]
    for category, detail in creator_profile.items():
        display(f"{category}: {detail}", target="creator_output")[cite: 16]


def add_visitor_message(e):
    """Retrieve visitor input, append to list, and display all messages."""
    name = document.getElementById("visitor_name").value.strip()[cite: 16]
    message = document.getElementById("visitor_message").value.strip()[cite: 16]
    wall_box = document.getElementById("wall_output")
    wall_box.innerHTML = ""

    # Validate that both input fields have text[cite: 18]
    if name == "" or message == "":
        display("Please fill out both your name and a message.", target="wall_output")[cite: 16]
        return

    # Append formatted entry to the list[cite: 10]
    entry = f"{name}: \"{message}\""
    visitor_messages.append(entry)[cite: 10]

    # Display total count and each entry[cite: 12]
    display(f"Total Messages ({len(visitor_messages)}):", target="wall_output")[cite: 12, 16]
    for item in visitor_messages:
        display(item, target="wall_output")[cite: 16]

    # Clear input boxes after submitting
    document.getElementById("visitor_name").value = ""
    document.getElementById("visitor_message").value = ""