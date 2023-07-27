```javascript
// Theme switcher functionality for the Baseball Agent Assistant application

// Define the theme names
const lightTheme = 'light-theme';
const darkTheme = 'dark-theme';

// Get the theme switcher element
const themeSwitcher = document.getElementById('theme-switcher');

// Function to switch the theme
function switchTheme() {
    if (document.body.classList.contains(lightTheme)) {
        document.body.classList.remove(lightTheme);
        document.body.classList.add(darkTheme);
        localStorage.setItem('theme', darkTheme);
    } else {
        document.body.classList.remove(darkTheme);
        document.body.classList.add(lightTheme);
        localStorage.setItem('theme', lightTheme);
    }
}

// Event listener for the theme switcher
themeSwitcher.addEventListener('click', switchTheme);

// Check the saved theme on page load
document.addEventListener('DOMContentLoaded', (event) => {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        document.body.classList.add(savedTheme);
    } else {
        document.body.classList.add(lightTheme);
    }
});
```