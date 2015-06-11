var lon = -9590863.695045754313469;
var lat = 4835547.198063937388361;
var zoom = 12;
var map, OSMlayer, gmap, gypb, statemLayer, stamenTerrainLayer, drawControls, polyfeature, polygonLayer, searchResultsLayer, searchResults, surplusLayer;
var selectControl, selectedFeature, selectedFill, selectedLayer;
var lbStyle, lbStyleMap;
var searchArea = new Array();
var clusterStrategy = new OpenLayers.Strategy.Cluster({distance: 15, threshold: 4});

var stamenAttribution = 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://creativecommons.org/licenses/by-sa/3.0">CC BY SA</a>.';


var geojson_format = new OpenLayers.Format.GeoJSON({
                    'internalProjection': new OpenLayers.Projection("EPSG:900913"),
                    'externalProjection': new OpenLayers.Projection("EPSG:4326")
});   

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
	// for regular features we show a nice popup with additional information
	if (!feature.cluster) {
		selectedLayer.drawFeature(feature, {fillColor: "#ffff00", strokeColor: "black"});
    	popup = new OpenLayers.Popup.FramedCloud("chicken", 
                             feature.geometry.getBounds().getCenterLonLat(),
                             null,
                             "<div style='font-size:.8em'>Parcel: " + feature.attributes.parcel +"<br>Address: " + feature.attributes.streetAddress+"<br>Status: " +feature.attributes.status + "<br>Structure Type: "+ feature.attributes.structureType + "<br>Side lot Eligible: "+ feature.attributes.sidelot_eligible + "<br>Homestead only: " + feature.attributes.homestead_only + "</div>",
                             null, true, onPopupClose);
	} else { // for feature clusters we show a popup listing the properties contained within.
		var addresses ="";
		for (var i=0; i < feature.cluster.length; i++){
			addresses += feature.cluster[i].attributes.streetAddress + ", " + feature.cluster[i].attributes.parcel +"<br/>"; 

		}

		popup = new OpenLayers.Popup.FramedCloud("chicken", 
                             feature.geometry.getBounds().getCenterLonLat(),
                             null,
                             "<div style='font-size:.8em'>Properties: " + addresses +"</div>",
                             null, true, onPopupClose);
	}
		
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
		$('input[name=searchArea]').val(polygonLayer.features[0].geometry.toString());		
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



function init(){
	

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
	stamenTerrainLayer = new OpenLayers.Layer.Stamen('terrain', {attribution: stamenAttribution});
	stamenTerrainLayer.setName('Stamen Terrain');
    OSMlayer = new OpenLayers.Layer.OSM();
	gmap = new OpenLayers.Layer.Google(
		"Google Streets", 
		{numZoomLevels: 20}
	);
	ghyb = new OpenLayers.Layer.Google(
		"Google Hybrid",
		{type: google.maps.MapTypeId.HYBRID, numZoomLevels: 20}
	);

	
	// define style maps
	
	lbStyle = new OpenLayers.Style({
		fillColor: '#33A02C', 
		strokeWidth: '.05', 
		strokeColor: 'black', 
		pointRadius: '8', 
		label:"${label}",
		fontColor: "#ffffff",
        fontOpacity: 0.8,
		fillOpacity: 1,
        fontSize: "12px" 
	}, {
		context: {
			label: function(feature) {
				// clustered features count or blank if feature is not a cluster
				return feature.cluster ? feature.cluster.length : "";  
      		}	
		}
	}); 

	var surplusStyleMap = new OpenLayers.StyleMap({fillColor: '#A6CEE3', strokeWidth: '.05', strokeColor: 'black'});
	lbStyleMap = new OpenLayers.StyleMap(lbStyle);
	var searchResultStyleMap = new OpenLayers.StyleMap({fillColor: '#1F78B4', strokeWidth: '.05', strokeColor: 'black', opacity: '0.9'});

	// define vector layers
	polygonLayer = new OpenLayers.Layer.Vector("Drawn Search Area"); // search by polygon layer
	searchResultsLayer = new OpenLayers.Layer.Vector("Search Results", {styleMap: searchResultStyleMap, rendererOptions: { zIndexing: true }});

//	surplusLayer = new OpenLayers.Layer.Vector("Surplus Properties", {
//		strategies: [new OpenLayers.Strategy.Fixed()],
//		styleMap: surplusStyleMap,
//		protocol: new OpenLayers.Protocol.HTTP({
//			url: "/map/search/?searchType=sp",
//			format: new OpenLayers.Format.GeoJSON()
//		})
//	});
	
	lbLayer = new OpenLayers.Layer.Vector("Landbank Properties", {
		protocol: new OpenLayers.Protocol.HTTP({
			url: "/map/search/?searchType=lb",
			format: new OpenLayers.Format.GeoJSON()
		}),
		strategies: [
			new OpenLayers.Strategy.Fixed()
    	],
		styleMap: lbStyleMap,
		rendererOptions: { zIndexing: true }
	});
	map.addLayer(lbLayer);
//	map.addLayer(surplusLayer);
	map.setLayerIndex(lbLayer, 1);
//	map.setLayerIndex(surplusLayer, 3);

	map.addLayer(stamenLayer);	
	map.addLayer(OSMlayer);
	map.addLayer(gmap);
	map.addLayer(ghyb);
	map.addLayer(polygonLayer);
    map.addLayer(stamenTerrainLayer);

	map.addLayer(searchResultsLayer);
	map.setLayerIndex(searchResultsLayer, 2);

	map.setCenter(new OpenLayers.LonLat(lon, lat), zoom);

	// draw polygon to define search area   
	polyfeature = new OpenLayers.Control.DrawFeature(polygonLayer, OpenLayers.Handler.Polygon);
	map.addControl(polyfeature);
	

	selectControl = new OpenLayers.Control.SelectFeature([lbLayer, searchResultsLayer],
		{onSelect: onFeatureSelect, onUnselect: onFeatureUnselect});
	map.addControl(selectControl);
	selectControl.activate(); 

	map.events.register("zoomend", map, zoomChanged); // on close zoom increase layer transparency

}


function getCSV(){
	var tmp = $("#myForm").serialize(); 
	document.location.href = "/map/search/?returnType=csv&" + tmp;
}

function getSearchResults(data)  {
	if (data.length > 60){ // aprox length of geojson string with no features
		searchResultsLayer.addFeatures(geojson_format.read(data));
		console.log("Post search extent: " + searchResultsLayer.getDataExtent());
		map.zoomToExtent(searchResultsLayer.getDataExtent());
	}
}

function clearSearchResults(){
	searchResultsLayer.destroyFeatures();
	$('#myTable').empty();
	$('input[name=searchArea]').val("");
	//clearDrawn();
}

;
function toggleSearchOptions(){
	if ( $('#searchToggle').is(':contains("Show more search options >>>")') ){
		$('#moreSearchOptions').show();
		$('#searchToggle').html('Show fewer search options <<<');
		return;
	}else{
		$('#moreSearchOptions').hide();
		$('#searchToggle').html('Show more search options >>>');
	}
	
}

function toggleClustering(){

	selectControl.deactivate();
	map.removeControl(selectControl);
	map.removeLayer(lbLayer);

	var strategies = [];

	if ( document.getElementById("toggleClustersCheckbox").checked ) {
		strategies.push(new OpenLayers.Strategy.Fixed());
		strategies.push(clusterStrategy);
	}else {
		strategies.push(new OpenLayers.Strategy.Fixed());
	}

	lbLayer = new OpenLayers.Layer.Vector("Landbank Properties", {
		protocol: new OpenLayers.Protocol.HTTP({
			url: "/map/search/?searchType=lb",
			format: new OpenLayers.Format.GeoJSON()
		}),
		strategies: strategies,
		styleMap: lbStyleMap,
		rendererOptions: { zIndexing: true }
	});
	
	map.addLayer(lbLayer);
	map.setLayerIndex(lbLayer, 1);

	selectControl = new OpenLayers.Control.SelectFeature([lbLayer, searchResultsLayer],
		{onSelect: onFeatureSelect, onUnselect: onFeatureUnselect});
	map.addControl(selectControl);
	selectControl.activate(); 

}

//jquery ajax form
$(function(){
	var options = {		
		beforeSerialize: function(){
			getSearchArea();
			console.log("Pre search extent: " + searchResultsLayer.getDataExtent());
		},		
		dataType: 'html', // because it makes it a json javascript object if you chose json
		success: getSearchResults
	};

	var optionsTable = {
		beforeSerialize: function(){
			getSearchArea();
		},
		data: { returnType: 'html'},				
		dataType: 'html', // because it makes it a json javascript object if you chose json
		success: function(data) { 
		    $('#myTable')
				.empty()
				.append(data)
				.endlessPaginate(); 
		} 
	};


	$("#myForm").validate({
		rules: {
			maxsize: {
				number: true
			},
			minsize: {
				number: true
			}
		},
		submitHandler: function(form) {
			$(form).ajaxSubmit(optionsTable);
			$(form).ajaxSubmit(options);
			return false;
		},
		debug: false
	});
});

$(function() {
	$( "#intro" ).dialog();

	$('#help-hints').click(function () {
		$("#intro").dialog('open');
        return false;
    });
	$('#searchToggle').click(function() { toggleSearchOptions(); });
	$('#downloadButton').click(function() { getCSV(); } );
	$('#toggleClustersCheckbox').change(function() { toggleClustering(); } );

 });


