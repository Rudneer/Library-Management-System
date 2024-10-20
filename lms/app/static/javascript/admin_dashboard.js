// Update password Credentials
function toggleSettings() {
    var settingsDiv = document.getElementById("settings-div");
    if (settingsDiv.style.display === "none" || settingsDiv.style.display === "") {
        settingsDiv.style.display = "flex";
    } else {
        settingsDiv.style.display = "none";
    }
}


// Display/Hide Add Book form
function add_book_toggle() {
    var settingsDiv = document.getElementById("addBookModal");
    if (settingsDiv.style.display === "none" || settingsDiv.style.display === "") {
        settingsDiv.style.display = "block";
    } else {
        settingsDiv.style.display = "none";
    }
}

// Update/Edit Book form
function update_book_toggle(){
    var settingsDiv = document.getElementById("updateBookModal");
    if (settingsDiv.style.display === "none" || settingsDiv.style.display === "") {
        settingsDiv.style.display = "block";
    } else {
        settingsDiv.style.display = "none";
    }
}

// Delete Book
function delete_book_toggle(){
    var settingsDiv = document.getElementById("deleteBookModal");
    if (settingsDiv.style.display === "none" || settingsDiv.style.display === "") {
        settingsDiv.style.display = "block";
    } else {
        settingsDiv.style.display = "none";
    }
}


// View Book
function view_book_toggle(){
    var settingsDiv = document.getElementById("viewBookModal");
    if (settingsDiv.style.display === "none" || settingsDiv.style.display === "") {
        settingsDiv.style.display = "block";
    } else {
        settingsDiv.style.display = "none";
    }
}

//switching button between borrowed books and overdue borrowers
function toggleActive(button) {
    // Remove the 'active' class from both buttons
    const buttons = document.querySelectorAll('.tab-button');
    buttons.forEach(btn => btn.classList.remove('active'));

    // Add 'active' class to the clicked button
    button.classList.add('active');
}


// Button for switching tables between borrowed books and overdue borrowers
function showTable(tableId) {
    // Hide all tables
    var tables = document.querySelectorAll('.table-content');
    tables.forEach(function(table) {
        table.classList.add('hidden');
    });

    // Show the selected table
    document.getElementById(tableId).classList.remove('hidden');

    // Update active tab button
    var buttons = document.querySelectorAll('.tab-button');
    buttons.forEach(function(button) {
        button.classList.remove('active');
    });

    // Set the active button
    event.target.classList.add('active');
}


