document.addEventListener('DOMContentLoaded', () => {
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeIcon = document.getElementById('theme-icon');
    const themeText = document.getElementById('theme-text');
    const htmlElement = document.documentElement;

    // Read stored preference or default to dark
    const savedTheme = localStorage.getItem('theme') || 'dark';
    setTheme(savedTheme);

    themeToggleBtn.addEventListener('click', () => {
        const currentTheme = htmlElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        setTheme(newTheme);
    });

    function setTheme(theme) {
        htmlElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);

        if (theme === 'dark') {
            themeIcon.textContent = '☼';
            themeText.textContent = 'Light';
            themeToggleBtn.setAttribute('aria-label', 'Switch to light mode');
        } else {
            themeIcon.textContent = '☾';
            themeText.textContent = 'Dark';
            themeToggleBtn.setAttribute('aria-label', 'Switch to dark mode');
        }
    }
});