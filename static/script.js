document.addEventListener("DOMContentLoaded", function() {
    const canvas = document.getElementById('channelChart');

    // Get values from result.html
    const channelWidth = parseFloat(canvas.getAttribute('data-channel-width'));
    const waterDepth = parseFloat(canvas.getAttribute('data-water-depth'));
    const channelDepth = parseFloat(canvas.getAttribute('data-channel-depth'));
    const bankSlope = parseFloat(canvas.getAttribute('data-bank-slope'));

    const ctx = canvas.getContext('2d');
    const overflowWarning = document.getElementById('overflow-warning');

    // Check for overflow
    const isOverflow = waterDepth > channelDepth;

    // Show warning if overflow
    if (isOverflow) {
        overflowWarning.style.display = 'block';
    }

    // Calculating trapezoidal shape and points for graphing
    const leftBase = channelWidth / 2 + channelDepth * bankSlope;
    const rightBase = channelWidth / 2 + channelDepth * bankSlope;
    const trapezoidPoints = [
        {x: -leftBase, y: channelDepth},
        {x: -channelWidth / 2, y: 0},
        {x: channelWidth / 2, y: 0},
        {x: rightBase, y: channelDepth}
    ];

    // Calculating water line points for graphing
    const waterLinePoints = [
        {x: (-channelWidth / 2 ) - (waterDepth * bankSlope), y: waterDepth}, // Extend the water level till it reaches the banks in -x
        {x: (channelWidth / 2) + (waterDepth * bankSlope), y: waterDepth} // Extend the water level till it reaches the banks in +x
    ];

    const data = {
        datasets: [{
            label: 'Channel Shape',
            data: trapezoidPoints,
            borderColor: 'black',
            borderWidth: 2,
            fill: false,
            lineTension: 0,
            showLine: true,
            pointRadius: 0
        }, {
            label: 'Water Level',
            data: waterLinePoints,
            borderColor: 'blue',
            borderWidth: 2,
            fill: '-1',
            lineTension: 0,
            showLine: true,
            pointRadius: 0
        }]
    };

    const config = {
        type: 'scatter',
        data: data,
        options: {
            responsive: true,
            scales: {
                x: {
                    type: 'linear',
                    position: 'bottom',
                    title: {
                        display: true,
                        text: 'Width (m)'
                    }
                },
                y: {
                    reverse: false,
                    title: {
                        display: true,
                        text: 'Depth (m)'
                    }
                }
            }
        }
    };

    const channelChart = new Chart(ctx, config);
});
