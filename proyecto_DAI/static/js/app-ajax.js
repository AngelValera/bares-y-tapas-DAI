$(function(){

  $.ajax({
    url: "/reclama_datos/",
    type: 'get',
    success: function(datos) {
      Visualiza_datos (datos);
    },
    failure: function(datos) {
      alert('esto no vá');
    }
  });

	function Visualiza_datos (datos) {
    var bares=[];
		var vis=[];

		bares =  datos['bares'];
		visitas = datos['visitas'];

    $('#container').highcharts({
      chart: {
        type: 'bar'
      },
      title: {
        text: 'Visitas bares'
      },
      xAxis: {
        categories: bares
      },
      yAxis: {
        title: {
          text: 'numero de visitas'
        }
      },
      series: [
        {
          name: 'Visitas',
          data: visitas
        },
      ],
    });

	};

});
