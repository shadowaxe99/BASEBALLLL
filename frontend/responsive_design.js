// Function to check device width and adjust layout accordingly
function checkDeviceWidth() {
    const deviceWidth = window.innerWidth;

    if (deviceWidth <= 600) {
        mobileLayout();
    } else if (deviceWidth <= 900) {
        tabletLayout();
    } else {
        desktopLayout();
    }
}

// Function to adjust layout for mobile devices
function mobileLayout() {
    // Adjust layout for mobile devices
    // This is just a placeholder, replace with actual layout adjustments
    console.log("Switched to mobile layout");
}

// Function to adjust layout for tablet devices
function tabletLayout() {
    // Adjust layout for tablet devices
    // This is just a placeholder, replace with actual layout adjustments
    console.log("Switched to tablet layout");
}

// Function to adjust layout for desktop devices
function desktopLayout() {
    // Adjust layout for desktop devices
    // This is just a placeholder, replace with actual layout adjustments
    console.log("Switched to desktop layout");
}

// Event listener for window resize
window.addEventListener('resize', checkDeviceWidth);

// Call function on page load
checkDeviceWidth();