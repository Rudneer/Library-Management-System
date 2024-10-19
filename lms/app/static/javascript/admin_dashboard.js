function toggleSettings() {
    var settingsDiv = document.getElementById("settings-div");
    if (settingsDiv.style.display === "none" || settingsDiv.style.display === "") {
        settingsDiv.style.display = "flex";
    } else {
        settingsDiv.style.display = "none";
    }
}
