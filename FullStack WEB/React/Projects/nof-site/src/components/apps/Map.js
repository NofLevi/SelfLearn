import react, { useState } from 'react';
import ReactMapGL, {Marker} from 'react-map-gl';
import classes from './Map.module.css';


function Map(){
    const [viewport, setViewport] = useState({
        latitude: 32.3381976,
        longitude: 34.8546063,
        width: '99vw',
        height: "99vh",
        zoom: 10
    
    });
    
    // Provide your access token

// Create a map in the div #map


    return(
        <div className = {classes.container}>
            <div className = {classes.map}> 
                <ReactMapGL {...viewport} mapboxApiAccessToken={process.env.REACT_APP_MAPBOX_TOKEN} mapStyle = "mapbox://styles/noflevi/ckt78ul4y25vk17ofaywuidxi" onViewportChange={(viewport) => {setViewport(viewport)}}>
                    <Marker className={classes.redmarker} latitude={22.00} longitude={86.20}>

                    </Marker>

                    <Marker className={classes.greenmarker} latitude={22.00} longitude={96.20}>

                    </Marker>
                </ReactMapGL>
            </div>
        </div>


    );
}


export default Map;