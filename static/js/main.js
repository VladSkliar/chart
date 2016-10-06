$.ajax({
  	method: "GET",
	dataType: "json",
	url: window.location.origin+'/api/groups/',
	success: function(result){
	    buildDropBox(result)
    }
	});
  $.ajax({
  	method: "GET",
	dataType: "json",
	url: window.location.origin+'/api/groups/1/',
	success: function(result){
	    buildChart(result['parameters_values'])
    }
	});
  function buildDropBox(data){
  	$('#dropName').html(data[0]['title'] +'<span class="caret"></span></button>')
  	for(var i=0; i<data.length;i++){
  		$('.dropdown-menu').append('<li><a class="dropClick" href="#" data-name="'+ data[i]['title'] +'" data-id="'+ data[i]['id'] +'">'+ data[i]['title']+'</a></li>')
  	}
  }
  $(document).on('click', '.dropClick', function () {
    $('#dropName').html($(this).attr('data-name') +'<span class="caret"></span></button>')
    getData($(this).attr('data-id'))
	});
  function getData(id){
  	$.ajax({
	  	method: "GET",
		dataType: "json",
		url: window.location.origin+'/api/groups/'+id +'/',
		success: function(result){
		    buildChart(result['parameters_values'])
	    }
	});
  }
  function buildChart(data){
	  var chart = AmCharts.makeChart("chartdiv", {
  "type": "serial",
  "theme": "light",
  "marginRight": 70,
  "dataProvider": data,
  "startDuration": 1,
  "graphs": [{
    "balloonText": "<b>[[category]]: [[value]]</b>",
    "fillColorsField": "color",
    "fillAlphas": 0.9,
    "lineAlpha": 0.2,
    "type": "column",
    "valueField": "value"
  }],
  "chartCursor": {
    "categoryBalloonEnabled": false,
    "cursorAlpha": 0,
    "zoomable": false
  },
  "categoryField": "parameters",
  "categoryAxis": {
    "gridPosition": "start",
    "labelRotation": 45
  },
  "export": {
    "enabled": true
  }

})}