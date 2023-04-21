const url="/api/RegEliteScorers"

// JSON and print to console to check data
d3.json(url).then(function(data) {
    players=data;
    console.log(players)
  for (x of data){
    let playername=x.player
    let playerpts=x.pts
    let playereff=(x.ts_per)
    // console.log(playername, playerpts, playereff)
  }
});

// Bar Chart Function
function plotBar(){
  // Get data
  d3.json(url).then(data => {
  
  let playerlist=[]
  let ptslist=[]
  let efflist=[]
  for (x of data.slice(0,10)){
    playerlist.push(x.player)
    ptslist.push(x.pts)
    efflist.push(x.ts_per)
    let playername=x.player
    let playerpts=x.pts
    let playereff=(x.ts_per)
    //Print to check
    //  console.log(playername, playerpts, playereff)
    }
  // Trace for Plotly
  let trace1={
    name: "Player PPG",
    x: playerlist,
    y: ptslist,
    type: "bar",
    marker:{
      color: '#0E63F5',
      opacity: .8
    }
  }
  // console.log(trace1)
  // Trace2 for Plotly
  let trace2={
    name: "Player TS%",
    x: playerlist,
    y: efflist,
    type: "bar",
    marker:{
      color: '#FA0606',
      opacity: .8
    }
  }
  console.log(trace2)
  // Layout for Plotly
  let layout={
    // xaxis:
    // yaxis:
    title: "Elite Scorers PPG & Efficiency",
    barmode: 'group',
    orientation: "h"
  }
  let bardata=[trace1, trace2]
  // Call Plotly
  Plotly.newPlot("bar", bardata, layout)
})}

const url2='/api/DefPlayers'
// Defensive Players Plot
function DefPlot()
{
  // Get data
  d3.json(url2).then(data2 => {
  
  let playerlist=[]
  let blklist=[]
  let stllist=[]
  for (x of data2.slice(0,10)){
    playerlist.push(x.player)
    blklist.push(x.BLK)
    stllist.push(x.STL)
    }
  // Trace for Plotly
  let trace1={
    name: "Player Blocks Per Game",
    x: blklist,
    y: playerlist,
    type: "bar",
    orientation: "h",
    marker:{
      color: '#0E63F5',
      opacity: .8
    }
  }
  // console.log(trace1)
  // Trace2 for Plotly
  let trace2={
    name: "Player Steals Per Game",
    x: stllist,
    y: playerlist,
    type: "bar",
    orientation: "h",
    marker:{
      color: '#FA0606',
      opacity: .8
    }
  }
  console.log(trace2)
  // Layout for Plotly
  let layout={
    // xaxis:
    // yaxis:
    title: "Top 10 Defensive Players",
    barmode: "group", 
  }
  let bardata=[trace1, trace2]
  // Call Plotly
  Plotly.newPlot("bar-2", bardata, layout)
})}

const url3='/api/Youngsters'
// Efficiency Across the NBA
function EffPlot()
{
  // Get data
  d3.json(url3).then(data3 => {
  
  let playerlist=[]
  let tslist=[]
  let ptslist=[]
  let astlist=[]
  let threeperlist=[]
  for (x of data3){
    playerlist.push(x.player)
    tslist.push(x.TS_per)
    astlist.push(x.AST)
    threeperlist.push(x.three_per)
    ptslist.push(x.PTS)
    }
  // Trace for Plotly
  let trace1={
    name: "True Shooting % per Player",
    x: playerlist,
    y: tslist,
    type: "bar",
    marker:{
      color: '#FA0606',
      opacity: .8,
      width: 7.0
    }
  }
  console.log(trace1)
  // Trace2 for Plotly
  let trace2={
    name: "Assists per Player",
    x: playerlist,
    y: astlist,
    type: "bar",
    marker:{
      color: '#8C17E3',
      opacity: .8,
      width: 7.0

    }
  }
    // Trace3 for Plotly
    let trace3={
      name: "Three % per Player",
      x: playerlist,
      y: threeperlist,
      type: "bar",
      marker:{
        color: '#2ACF0C',
        opacity: .8,
        width: 7.0
  
      }
    }
        // Trace4 for Plotly
    let trace4={
      name: "PTS per Player",
      x: playerlist,
      y: ptslist,
      type: "bar",
      marker:{
        color: '#0E63F5',
        opacity: .8,
        width: 7.0
  
      }
    }
  console.log(trace2)
  // Layout for Plotly
  let layout={
    xaxis:{'range': [0,100]},
    yaxis: {'range': [0,80]},
    title: "Offensive Metrics Across NBA Youngsters",
    barmode: "group" 
  }
  let bardata=[trace1, trace2, trace3, trace4]
  // Call Plotly
  Plotly.newPlot("bar-3", bardata, layout)
})}

// Call function
plotBar();
DefPlot();
EffPlot();     
       
