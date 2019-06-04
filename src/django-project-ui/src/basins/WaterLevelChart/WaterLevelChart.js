import React, { Component } from 'react';
import * as d3 from "d3";
import 'whatwg-fetch'
import cookie from 'react-cookies'

class WaterLevelChart extends Component {
  render() {
    const {data} = this.props
    const {parameter} = this.props
    const {color} = this.props
    const margin = {top: 10, right:5 , bottom: 40, left: 10};
    const width = 300 - margin.left - margin.right;
    const height = 150 - margin.top - margin.bottom;

    function toTitle(field) {
          if (field == 'water_level'){
            return 'Profundidad';
          } else if (field == 'radar_rain') {
            return 'Intensidad de lluvia promedio en la cuenca';
          } else {
            return 'Velocidad superficial';
          }
    }

    function isEmpty(obj) {
        for(var key in obj) {
            if(obj.hasOwnProperty(key))
                return false;
        }
        return true;
    }

    if (isEmpty(data)){
    } else {
    data.forEach(function(d){
        //console.log(typeof(d.date)); //check the type before it changes
        var orgDate = new Date(d.date); // changes the string date into origional date type
        d.date = orgDate;
    }); //

    var minDate = data[0]["date"]
    var maxDate = data[30]["date"]
    var maxValue = Math.max.apply(Math, data.map(function(o) { return o[parameter]; }))
    var xScale = d3.scaleTime().domain([new Date(minDate),new Date(maxDate)]).range([0,width-10]);
    var yScale = d3.scaleLinear().domain([0,maxValue*1.5]).range([height,0]);
    var lineGenerator = d3.line()
    	.x(function(d, i) {
          return xScale(d.date);
        })
    	.y(function(d) {
          return yScale(d[parameter]);
        })
      .defined(function(d) {
          return (typeof d[parameter] != 'undefined' && d[parameter]);
        });

    var line = lineGenerator(data);
    var x_axis = d3.axisBottom().scale(xScale);
    var y_axis = d3.axisLeft().scale(yScale);

    d3.select("#"+parameter).selectAll("*").remove();
    var svg = d3.select("#"+parameter)
      .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom);

    svg.append("path")
      .attr("d",line)
      .attr("transform", "translate("+margin.left*3.0 + "," + margin.top + ")")
      .style("stroke", color)
      .style("stroke-width","2px")
      .style("fill","none");

    var areaGenerator = d3.area()
      .x(function(d) { return xScale(d.date); })
      .y0(height)
      .y1(function(d) { return yScale(d[parameter]); });

    var areaGenerator = d3.area()
      .x(function(d, i) {
          return xScale(d.date);
        })
      .y0(height)
      .y1(function(d) {
          return yScale(d[parameter]);
        })
      .defined(function(d) {
          return (typeof d[parameter] != 'undefined' && d[parameter]);
        });

    var area = areaGenerator(data);
    console.log(data)

    svg.append("path")
       .attr("class", "area")
       .attr("d", area)
       .attr("transform", "translate("+margin.left*3.0 + "," + margin.top + ")")
       .style("fill",color)
       .style("opacity","0.5");
    var ypos = height+margin.top;

    var div = d3.select("#"+parameter).append("div")
        .attr("class", "tooltip")
        .style("opacity", "1.0");

    console.log(div)

    svg.selectAll("#"+parameter)
        .data(data)
    .enter().append("circle")
        .attr("r", 5)
        .attr("cx", function(d) { return xScale(d.date); })
        .attr("cy", function(d) { return yScale(d[parameter]); })
        .attr("transform", "translate("+margin.left*3.0 + "," + margin.top + ")")
        .style("fill",color)
        .style("opacity","0.0")
        .on("mouseover", function(d) {
            var string = "<p>"+d.hour+" - "+d[parameter]+" cm <p>";
            console.log("y = "+d3.event.pageY)
            div.html(string)
                .style("left", (200) + "px")
                .style("top", (0) + "px")
                ;
            })
        .on("mouseout", function(d) {
            div.transition()
                .duration(100)
                .style("opacity", 0.9);
        });

    var axG = svg.append("g")
         .attr("class", "x axis")
         .attr("transform", "translate("+margin.left*3.0 + "," + ypos + ")")
         .call(x_axis)
         .selectAll("text")
           .attr("transform", "rotate(-30)");

    svg.append("g")
      .attr("class", "y axis")
      .attr("transform", "translate("+margin.left*2.5 + "," + margin.top + ")")
      .call(y_axis);
    }

  return (
    <div>
      <div className="chart-wrapper">
        <div className="chart-title">
          {"Profundidad (cm)"}
        </div>
        <div className="chart-stage">
          <div id={parameter}></div>
        </div>
      </div>
    </div>
    );
  }
}

export default WaterLevelChart;
