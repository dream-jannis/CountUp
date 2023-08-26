const labels = Object.keys(rawData);
const counts = Object.values(rawData);

const ctx = document.getElementById('myChart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'bar',  // Ändern Sie dies zu 'horizontalBar'
    data: {
        labels: labels,
        datasets: [{
            label: 'Anzahl Striche',
            data: counts,
            backgroundColor: 'rgba(54, 162, 235, 0.5)',
            borderRadius: 50,
        }]
    },
    options: {
        indexAxis: 'y',
        scales: {
            x: {
                beginAtZero: true
            }
        },
        plugins: {
            legend: {
                display: false
            }
        },
        scales: {
            x: {
                ticks: {
                    color: "white",
                },
                grid: {
                display: false
                }
            },
            y: {
                ticks: {
                    color: "white",
                    font: {
                        size: 16,
                    },
                },
                grid: {
                display: false
                }
            }
        }
    }
});