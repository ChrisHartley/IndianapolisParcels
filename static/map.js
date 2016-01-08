var lon = -9590863.695045754313469;
var lat = 4835547.198063937388361;
var zoom = 12;
var map, OSMlayer, gmap, gypb, statemLayer, stamenTerrainLayer, drawControls, polyfeature, polygonLayer, searchResultsLayer, searchResults, surplusLayer;
var selectControl, selectedFeature, selectedFill, selectedLayer;
var lbStyle, lbStyleMap;
var searchArea = new Array();

var geojson_format = new OpenLayers.Format.GeoJSON({
                    'internalProjection': new OpenLayers.Projection("EPSG:900913"),
                    'externalProjection': new OpenLayers.Projection("EPSG:4326")
});

var table = $('#example').DataTable({
					dom: 'T<"clear">lrtip',
					tableTools: {
						"sSwfPath": "https://cdn.datatables.net/tabletools/2.2.4/swf/copy_csv_xls.swf",
						"aButtons": [
                            "copy",
                            {
                                "sExtends":    "collection",
                                "sButtonText": "Save",
                                "aButtons":    [ "csv", "xls", "pdf" ]
                            },
                            "print"
						]
					},

					"columns": [
						{"data": "properties.parcel"},
						{"data": "properties.streetAddress"},
						{"data": "properties.zipcode"},
						{"data": "properties.structureType"},
						{"data": "properties.nsp"},
						{"data": "properties.sidelot_eligible"},
						{"data": "properties.homestead_only"},
						{"data": "properties.status"},
						{"data": "properties.price"}

					]
	});

var stamenAttribution = 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://creativecommons.org/licenses/by-sa/3.0">CC BY SA</a>.';




function toggleDraw(element) {
	if(element.value == "polygon" && element.checked) {
   		polyfeature.activate();
		alert("Click on the map to draw a corner, double click to finish");
    } else {
                polyfeature.deactivate();
            }
}

function clearDrawn() {
	polygonLayer.destroyFeatures();
}


function onPopupClose(evt) {
    selectControl.unselect(selectedFeature);
}

function onFeatureSelect(feature) {
    selectedFeature = feature;
	selectedLayer = feature.layer;
	selectedLayer.drawFeature(feature, {fillColor: "#ffff00", strokeColor: "black"});
	popup = new OpenLayers.Popup.FramedCloud("chicken",
                         feature.geometry.getBounds().getCenterLonLat(),
                         null,
						 $.ajax({ type: "GET", url: '/propertyPopup/', data: {parcel: feature.attributes.parcel}, async: false}).responseText,
                         null, true, onPopupClose);
    feature.popup = popup;
    map.addPopup(popup);

}

function onFeatureUnselect(feature) {
    map.removePopup(feature.popup);
    feature.popup.destroy();
    feature.popup = null;
}

function getSearchArea(){
	try{
		$('input[name=property-searchArea]').val(polygonLayer.features[0].geometry.toString());
	}
	catch(err){ return; }
}

function zoomChanged(){ // not working yet - how do we change opacity? it is a complete mystery of non-working.
/*	if (map.getZoom() > 16){
		console.log(map.getZoom())
		searchResultsLayer.setOpacity(0.1);
		lbLayer.setOpacity(0.1);
		searchResultsLayer.redraw();
		lbLayer.redraw();
	} */
}



$(function() {

	map = new OpenLayers.Map( 'map', {controls: [
		new OpenLayers.Control.PanZoomBar(),
		new OpenLayers.Control.KeyboardDefaults(),
		new OpenLayers.Control.Navigation(),
		new OpenLayers.Control.Attribution()
	]});


	var extent = new OpenLayers.Bounds(-86.328121, 39.632177, -85.937379, 39.997392);	// (left, bottom, right, top)
	var proj = new OpenLayers.Projection("EPSG:4326");
	var intProj = new OpenLayers.Projection("EPSG:900913");
	extent.transform(proj, intProj);
	map.setOptions({restrictedExtent: extent});

	var ls = new OpenLayers.Control.LayerSwitcher({});
	map.addControl(ls);
	ls.maximizeControl();

	// set up basemaps
	stamenLayer = new OpenLayers.Layer.Stamen("toner", {attribution: stamenAttribution});
	stamenLayer.setName('Stamen Toner');
	ghyb = new OpenLayers.Layer.Google("Google Hybrid",	{type: google.maps.MapTypeId.HYBRID, numZoomLevels: 20});


		// define style maps


	lbStyle = new OpenLayers.Style({
		fillColor: '#33A02C',
		strokeWidth: '.05',
		strokeColor: 'black',
		pointRadius: '8',
		fontColor: "#ffffff",
        fontOpacity: 0.8,
		fillOpacity: 1,
        fontSize: "12px"
	},
    {
    rules: [
        new OpenLayers.Rule({
          filter: new OpenLayers.Filter.Comparison(
              {
                  type: OpenLayers.Filter.Comparison.LIKE,
                  property: "status",
                  value: 'Sold'
               }),
               symbolizer: {
                   fillColor: "gray"
               },

        }),
        new OpenLayers.Rule({
                // apply this rule if no others apply
                elseFilter: true,
                symbolizer: {
                    fillColor: "#33A02C"
                }
        })
     ]
 });


	var surplusStyleMap = new OpenLayers.StyleMap({fillColor: '#A6CEE3', strokeWidth: '.05', strokeColor: 'black'});
	lbStyleMap = new OpenLayers.StyleMap(lbStyle);
	var searchResultStyleMap = new OpenLayers.StyleMap({fillColor: '#1F78B4', strokeWidth: '.05', strokeColor: 'black', opacity: '0.9'});

	// define vector layers
	polygonLayer = new OpenLayers.Layer.Vector("Drawn Search Area"); // search by polygon layer
	searchResultsLayer = new OpenLayers.Layer.Vector("Search Results", {styleMap: searchResultStyleMap, rendererOptions: { zIndexing: true }});

	lbLayer = new OpenLayers.Layer.Vector("Landbank Properties", {
		protocol: new OpenLayers.Protocol.HTTP({
			url: "/search_property/?returnType=geojson",
			format: new OpenLayers.Format.GeoJSON()
		}),
		strategies: [
			new OpenLayers.Strategy.Fixed()
    	],
		styleMap: lbStyleMap,
		rendererOptions: { zIndexing: true }
	});

	map.addLayer(lbLayer);
	map.setLayerIndex(lbLayer, 1);

	map.addLayer(stamenLayer);
	map.addLayer(ghyb);
	map.addLayer(polygonLayer);

	map.addLayer(searchResultsLayer);
	map.setLayerIndex(searchResultsLayer, 2);

	map.setCenter(new OpenLayers.LonLat(lon, lat), zoom);
    ghyb.mapObject.setTilt(0);
	// draw polygon to define search area
	polyfeature = new OpenLayers.Control.DrawFeature(polygonLayer, OpenLayers.Handler.Polygon);
	map.addControl(polyfeature);


	selectControl = new OpenLayers.Control.SelectFeature([lbLayer, searchResultsLayer],
		{onSelect: onFeatureSelect, onUnselect: onFeatureUnselect});
	map.addControl(selectControl);
	selectControl.activate();

	map.events.register("zoomend", map, zoomChanged); // on close zoom increase layer transparency

});


function getCSV(){
	var tmp = $("#myForm").serialize();
	document.location.href = "?property-report-propertysearchtable=csv" + tmp;
}

function getSearchResults(data)  {
	jsonData = JSON.parse(data);
	table.clear();
	searchResultsLayer.destroyFeatures();
	table.rows.add(jsonData.features);
	table.draw();
	if (data.length > 60){ // aprox length of geojson string with no features
		searchResultsLayer.addFeatures(geojson_format.read(data));
		console.log("Post search extent: " + searchResultsLayer.getDataExtent());
		map.zoomToExtent(searchResultsLayer.getDataExtent());
	}
}


function toggleSearchOptions(){
    console.log("Toggle search)");
	if ( $('#searchToggle').is(':contains("Show more search options >>>")') ){
		$('#moreSearchOptions').show();
		$('#searchToggle').html('Show fewer search options <<<');
		return;
	}else{
		$('#moreSearchOptions').hide();
		$('#searchToggle').html('Show more search options >>>');
	}

}


//jquery ajax form
$(function(){
    $("#intro").dialog({
        autoOpen: true
    });
	var options = {
		beforeSerialize: function(){
			getSearchArea();
			console.log("Pre search extent: " + searchResultsLayer.getDataExtent());
		},
		data: { returnType: 'geojson' },
		dataType: 'html', // because it makes it a json javascript object if you chose json
		success: getSearchResults
	};


	$("#PropertySearchForm").validate({
		rules: {
			maxsize: {
				number: true
			},
			minsize: {
				number: true
			}
		},
		submitHandler: function(form) {
			//$(form).ajaxSubmit(optionsTable);
			$(form).ajaxSubmit(options);
			return false;
		},
		debug: false
	});
});

$(function() {
	$('#help-hints').click(function () {
		$("#intro").dialog('open');
        return false;
    });
	$('#searchToggle').click(function() { toggleSearchOptions(); });
	$('#downloadButton').click(function() { getCSV(); } );



 });
