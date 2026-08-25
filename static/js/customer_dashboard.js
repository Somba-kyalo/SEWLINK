const themeToggle = document.getElementById('theme-toggle');

const savedTheme = localStorage.getItem('theme');

if (savedTheme === 'dark') {
    document.body.classList.add('dark-mode');
    themeToggle.textContent = 'Light Mode';
}

themeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');

    const isDarkMode = document.body.classList.contains('dark-mode');

    localStorage.setItem('theme', isDarkMode ? 'dark' : 'light');

    themeToggle.textContent = isDarkMode ? 'Light Mode' : 'Dark Mode';
});