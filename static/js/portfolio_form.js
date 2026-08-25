const themeToggle = document.getElementById('themeToggle');

const savedTheme = localStorage.getItem('sewlink-theme');

if (savedTheme === 'dark') {
    document.body.classList.add('dark');
}

function updateThemeButton() {
    if (document.body.classList.contains('dark')) {
        themeToggle.textContent = 'Light Mode';
    } else {
        themeToggle.textContent = 'Dark Mode';
    }
}

updateThemeButton();

themeToggle.addEventListener('click', function () {
    document.body.classList.toggle('dark');

    if (document.body.classList.contains('dark')) {
        localStorage.setItem('sewlink-theme', 'dark');
    } else {
        localStorage.setItem('sewlink-theme', 'light');
    }

    updateThemeButton();
});