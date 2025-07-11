document.addEventListener('DOMContentLoaded', function() {
    const budgetCtx = document.getElementById('budgetChart').getContext('2d');
    const budgetData = {
        labels: [
            {% for budget in budgets %}
                '{{ budget.category.name }}',
            {% endfor %}
        ],
        datasets: [{
            label: 'Budget Progress',
            data: [
                {% for budget in budgets %}
                    {{ budget.progress_percentage }},
                {% endfor %}
            ],
            backgroundColor: [
                'rgba(78, 115, 223, 0.5)',
                'rgba(28, 200, 138, 0.5)',
                'rgba(54, 185, 204, 0.5)',
                'rgba(246, 194, 62, 0.5)',
                'rgba(231, 74, 59, 0.5)'
            ],
            borderColor: [
                'rgba(78, 115, 223, 1)',
                'rgba(28, 200, 138, 1)',
                'rgba(54, 185, 204, 1)',
                'rgba(246, 194, 62, 1)',
                'rgba(231, 74, 59, 1)'
            ],
            borderWidth: 1
        }]
    };

    new Chart(budgetCtx, {
        type: 'bar',
        data: budgetData,
        options: {
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100,
                    ticks: {
                        callback: function(value) {
                            return value + '%';
                        }
                    }
                }
            },
            plugins: {
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return context.parsed.y + '%';
                        }
                    }
                }
            }
        }
    });
}); 