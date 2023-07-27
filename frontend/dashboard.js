```javascript
document.addEventListener('DOMContentLoaded', (event) => {
    loadTasks();
    loadUpcomingMeetings();
    loadPlayerPerformance();
});

function loadTasks() {
    // Fetch tasks from backend
    fetch('/backend/main.py/get_tasks')
    .then(response => response.json())
    .then(data => {
        const taskList = document.querySelector('#task-list');
        data.forEach(task => {
            const taskCard = document.createElement('div');
            taskCard.className = 'task-card';
            taskCard.textContent = task;
            taskList.appendChild(taskCard);
        });
    });
}

function loadUpcomingMeetings() {
    // Fetch upcoming meetings from Google Calendar API
    fetch('/api/google_calendar.py/get_upcoming_meetings')
    .then(response => response.json())
    .then(data => {
        const meetingList = document.querySelector('#upcoming-meetings');
        data.forEach(meeting => {
            const meetingCard = document.createElement('div');
            meetingCard.className = 'meeting-card';
            meetingCard.textContent = meeting;
            meetingList.appendChild(meetingCard);
        });
    });
}

function loadPlayerPerformance() {
    // Fetch player performance from backend
    fetch('/backend/player_management.py/get_player_performance')
    .then(response => response.json())
    .then(data => {
        const performanceList = document.querySelector('#player-performance');
        data.forEach(performance => {
            const performanceCard = document.createElement('div');
            performanceCard.className = 'performance-card';
            performanceCard.textContent = performance;
            performanceList.appendChild(performanceCard);
        });
    });
}
```