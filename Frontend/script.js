document.addEventListener('DOMContentLoaded', function() {
    // Fetch the hello world message when the page loads
    fetch('/hello')
        .then(response => response.json())
        .then(data => {
            alert(data.message); // Show the message in a popup window
        })
        .catch(error => {
            console.error('Failed to fetch the greeting:', error);
        });
});

// Existing functions and event listeners remain unchanged
