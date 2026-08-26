document.addEventListener("DOMContentLoaded", function () {


const themeToggle = document.getElementById("themeToggle");
const themeIcon = document.getElementById("themeIcon");
const themeText = document.getElementById("themeText");

const savedTheme = localStorage.getItem("sewlink-theme");

if (savedTheme === "light") {
    document.body.classList.add("light-mode");
    updateThemeButton(true);
} else {
    document.body.classList.remove("light-mode");
    updateThemeButton(false);
}

themeToggle.addEventListener("click", function () {

    document.body.classList.toggle("light-mode");

    const isLightMode = document.body.classList.contains("light-mode");

    if (isLightMode) {
        localStorage.setItem("sewlink-theme", "light");
        updateThemeButton(true);
    } else {
        localStorage.setItem("sewlink-theme", "dark");
        updateThemeButton(false);
    }

});

function updateThemeButton(isLightMode) {

    if (isLightMode) {
        themeIcon.textContent = "☾";
        themeText.textContent = "Dark Mode";
    } else {
        themeIcon.textContent = "☀";
        themeText.textContent = "Light Mode";
    }

}


});
