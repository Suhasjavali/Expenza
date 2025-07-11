document.addEventListener('DOMContentLoaded', function() {
    const monthlyCtx = document.getElementById('monthlyChart').getContext('2d');
    const monthlyData = {
        labels: [
            {% for month in monthly_expenses %}
                '{{ month.date|date:"M Y" }}',
            {% endfor %}
        ],
        datasets: [{
            label: 'Monthly Expenses',
            data: [
                {% for month in monthly_expenses %}
                    {{ month.total }},
                {% endfor %}
            ],
            backgroundColor: 'rgba(78, 115, 223, 0.5)',
            borderColor: 'rgba(78, 115, 223, 1)',
            borderWidth: 1,
            pointBackgroundColor: 'rgba(78, 115, 223, 1)',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: 'rgba(78, 115, 223, 1)'
        }]
    };

    new Chart(monthlyCtx, {
        type: 'line',
        data: monthlyData,
        options: {
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        callback: function(value) {
                            return '$' + value;
                        }
                    }
                }
            },
            plugins: {
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return '$' + context.parsed.y;
                        }
                    }
                }
            }
        }
    });
}); 