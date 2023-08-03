document.addEventListener('DOMContentLoaded', (event) => {
    const ctx = document.getElementById('chart').getContext('2d');
    let chart;

    const form = document.getElementById('count-form');
    const userField = document.getElementById('user');

    const createChart = (data) => {
        const labels = data.map(x => x.user);
        const counts = data.map(x => x.count);

        chart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Count',
                    data: counts,
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    };

    const updateChart = (data) => {
        chart.data.labels = data.map(x => x.user);
        chart.data.datasets[0].data = data.map(x => x.count);
        chart.update();
    };

    const fetchData = () => {
        fetch('/data')
            .then(response => response.json())
            .then(data => updateChart(data));
    };

    form.addEventListener('submit', (e) => {
        e.preventDefault();

        const user = userField.value;
        userField.value = '';

        fetch('/count', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user: user })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            fetchData();
        })
        .catch((error) => {
            console.error('There has been a problem with your fetch operation:', error);
        });
    });

    fetchData();
});
