var rawData = [
    {living_well:75,hip_enthusiast:25,collector:0,label:'persona distribution'},
    
];

Plotly.newPlot('myDiv', [{
    type: 'scatterternary',
    mode: 'markers',
    a: rawData.map(function(d) { return d.living_well; }),
    b: rawData.map(function(d) { return d.hip_enthusiast; }),
    c: rawData.map(function(d) { return d.collector; }),
    text: rawData.map(function(d) { return d.label; }),
    marker: {
        symbol: 100,
        color: '#DB7365',
        size: 14,
        line: { width: 2 }
    },
}], {
    ternary: {
        sum: 100,
        aaxis: makeAxis('Living Well', 0),
        baxis: makeAxis('<br>Hip Enthusiast', 45),
        caxis: makeAxis('<br>Collector', -45),
        bgcolor: '#fff1e0'
    },
    annotations: [{
      showarrow: false,
      text: 'Replica of Tom Pearson\'s <a href="http://bl.ocks.org/tomgp/7674234">block</a>',
        x: 1.0,
        y: 1.3,
        font: { size: 15 }
    }],
    paper_bgcolor: '#fff1e0',
});

function makeAxis(title, tickangle) {
    return {
      title: title,
      titlefont: { size: 20 },
      tickangle: tickangle,
      tickfont: { size: 8 },
      tickcolor: 'rgba(0,0,0,0)',
      ticklen: 5,
      showline: true,
      showgrid: true
    };
}