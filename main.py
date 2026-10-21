from pyscript import document   # access to the page (DOM)
from html import escape         # makes user text safe to show as HTML

# ---------------------------------------------------------------
# Predefined sets: one per grade level (sets ignore duplicates)
# ---------------------------------------------------------------
grade_7  = {"Ava Reyes", "Liam Cruz", "Noah Tan"}
grade_8  = {"Mia Garcia", "Ethan Lim", "Zoe Ramos"}
grade_9  = {"Olivia Chen", "Lucas Dela Cruz", "Emma Bautista"}
grade_10 = {"Sophia Mendoza", "Jacob Uy", "Isabella Flores"}

# Members added through the form are collected in their own set
added_members = set()


def render():
    """Combine all sets with the union operator (|) and show the results."""
    # Union operator merges every grade set plus the newly added members
    master = grade_7 | grade_8 | grade_9 | grade_10 | added_members

    # Build one list item per member (sorted) without a loop:
    # map() applies the lambda to every member in the set
    items = "".join(map(
        lambda m: f'<li class="list-group-item">👤 {escape(m)}</li>',
        sorted(master)
    ))

    # Output the full member list and the total count as HTML with an f-string
    document.querySelector("#output").innerHTML = f"""
        <h5>Total members:
            <span class="badge bg-primary">{len(master)}</span>
        </h5>
        <h5 class="mt-3">All members</h5>
        <ul class="list-group">{items}</ul>
    """


def result_checker(event):
    """Runs when the Submit button is clicked: adds the member and updates results."""
    global added_members

    first = document.querySelector("#first_name").value.strip().title()
    last  = document.querySelector("#last_name").value.strip().title()

    # One-item set for the new member. Set difference (-) removes the empty
    # string, so a blank entry is ignored without needing an if statement.
    new_member = {f"{first} {last}".strip()} - {""}

    # Union operator adds the new member (duplicates are ignored automatically)
    added_members = added_members | new_member

    # Clear the text boxes
    document.querySelector("#first_name").value = ""
    document.querySelector("#last_name").value = ""

    # Refresh the displayed results
    render()


# Show the starting roster when the page first loads
render()
