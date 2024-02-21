function fetchData() {
    var xhr = new XMLHttpRequest();
    var url = '../data/registrations.json';
    xhr.open('GET', url, true);
    xhr.onload = function() {
        if (xhr.status === 200) {
            try {
                var data = JSON.parse(xhr.responseText);
                handleData(data);
            } catch (error) {
                console.error('Error parsing JSON:', error);
            }
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
fetchData();
