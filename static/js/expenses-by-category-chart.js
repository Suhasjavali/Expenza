document.addEventListener('DOMContentLoaded', function() {
    const categoryCtx = document.getElementById('categoryChart').getContext('2d');
    const categoryData = {
        labels: [
            {% for category in expenses_by_category %}
                '{{ category.category__name }}',
            {% endfor %}
        ],
        datasets: [{
            data: [
                {% for category in expenses_by_category %}
                    {{ category.total }},
                {% endfor %}
            ],
            backgroundColor: [
                '#4e73df', '#1cc88a', '#36b9cc', '#f6c23e', '#e74a3b',
                '#5a5c69', '#858796', '#5a5c69', '#858796', '#5a5c69'
            ],
            hoverBackgroundColor: [
                '#2e59d9', '#17a673', '#2c9faf', '#dda20a', '#be2617',
                '#373840', '#60616f', '#373840', '#60616f', '#373840'
            ],
            hoverBorderColor: "rgba(234, 236, 244, 1)",
        }],
    };

    new Chart(categoryCtx, {
        type: 'doughnut',
        data: categoryData,
        options: {
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom'
                }
            },
            cutout: '70%',
        },
    });
}); 