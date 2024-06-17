document.addEventListener("DOMContentLoaded", function() {
    // Get the JSON data string from the script tag
    const jsonDataString = document.getElementById('totals-data').textContent.trim();
    const result = jsonDataString.slice(49);
    
    // Parse the JSON data
    const totalsData = JSON.parse(result);

    // Extract labels and data for the chart
    const labels = totalsData.map(item => item.date);
    const data = totalsData.map(item => item.total);

    // Create the chart
    const ctx = document.getElementById('totalsChart').getContext('2d');
    const chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Valor Total dos Serviços',
                data: data,
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
});
document.addEventListener("DOMContentLoaded", function() {
  // Get the JSON data string from the script tag
  const jsonDataString = document.getElementById('service-counts-data').textContent.trim();
  const result = jsonDataString.slice(57);

  try {
      // Parse the JSON data
      const serviceCountsData = JSON.parse(result);

      // Extract labels and data for the chart
      const labels = serviceCountsData.map(item => item.date);
      const data = serviceCountsData.map(item => item.count);

      // Create the chart
      const ctx = document.getElementById('serviceCountsChart').getContext('2d');
      const chart = new Chart(ctx, {
          type: 'bar',
          data: {
              labels: labels,
              datasets: [{
                  label: 'Quantidade Total de Serviços',
                  data: data,
                  backgroundColor: 'rgba(75, 192, 192, 0.2)',
                  borderColor: 'rgba(75, 192, 192, 1)',
                  borderWidth: 1
              }]
          },
          options: {
              scales: {
                  y: {
                      beginAtZero: true,
                      precision: 0, // Ensure y-axis labels are integers
                      stepSize: 1 // Ensure steps are in integers
                  }
              }
          }
      });
  } catch (error) {
      console.error('Error parsing JSON:', error);
  }
});