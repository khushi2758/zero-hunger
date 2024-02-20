function fetchData() {
    var xhr = new XMLHttpRequest();
    var url = '../data/registrations.json';
    xhr.open('GET', url, true);
    xhr.onload = function() {
        if (xhr.status === 200) {
            var data = JSON.parse(xhr.responseText);

            handleData(data);
        } else {
            console.error('Error fetching data:', xhr.statusText);
        }
    };
    xhr.onerror = function() {
        console.error('Network error while fetching data');
    };
    xhr.send();
}
function handleData(data) {
    var container = document.getElementById('notification-container');
    container.innerHTML = '';
    data.forEach(function(notification) {
        var div = document.createElement('div');
        div.className = 'notification';

        div.innerHTML = `
            <p class="notification-content">
                <strong>Name:</strong> ${notification.name}<br>
                <strong>Email:</strong> ${notification.email}<br>
                <strong>Phone:</strong> ${notification.phone}<br>
                <strong>Address:</strong> ${notification.address}<br>
                <strong>Quantity:</strong> ${notification.quantity}
            </p>
        `;
        container.appendChild(div);
    });
}
function deleteNotification(button) {
    var notification = button.parentElement.parentElement;
    notification.remove();
}
function markAsRead(button) {
    var notification = button.parentElement.parentElement;
    notification.classList.add('read');
}
document.querySelectorAll('.complete-button').forEach(button => {
    button.addEventListener('click', () => {
        const notificationId = button.dataset.id;
        const notificationElement = document.getElementById('notification-' + notificationId);
        notificationElement.classList.add('completed-icon');
        button.disabled = true;
        const tickIcon = document.createElement('img');
        tickIcon.src = 'https://img.icons8.com/material-rounded/24/000000/checkmark--v1.png';
        tickIcon.classList.add('tick-icon');
        notificationElement.prepend(tickIcon);
    });
});
fetchData();