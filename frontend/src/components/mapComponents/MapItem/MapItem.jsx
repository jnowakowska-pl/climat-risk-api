import React, { useEffect, useRef } from "react";
import Map from "@arcgis/core/Map";
import MapView from "@arcgis/core/views/MapView";
import "./MapItem.scss"

function MapItem(props) {
    const mapDiv = useRef(null);
    const mapView = useRef(null);

    useEffect(() => {
      if (mapDiv.current) {
        const mapItem = new Map({
          basemap: "topo-vector", 
        });

        mapView.current= new MapView({
          container: mapDiv.current, 
          map: mapItem, 
          center: [-118.805, 34.027], 
          zoom: props.mapZoom, 
        });
  
        return () => {
          if (mapView.current) {
            mapView.current.destroy();
          }
        };
      }
    }, []);

    useEffect(() => {
      mapView.current.zoom = props.mapZoom;
    }, [props.mapZoom])
    
  
    return (
      <div
        ref={mapDiv}
        id="mapItem"
      ></div>
    );
}

export default MapItem