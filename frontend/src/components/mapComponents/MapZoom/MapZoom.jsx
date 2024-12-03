import React from 'react'
import "./MapZoom.scss"

function MapZoom(props) {

    function handleZoom (value) {
        if (value === 'plus') props.setMapZoom(props.mapZoom + 1);
        if (value === 'minus') props.setMapZoom(props.mapZoom - 1);
    }

    return (
        <div id='mapZoom'>
            <div onClick={() => handleZoom('plus')}>+</div>
            <div onClick={() => handleZoom('minus')}>-</div>
        </div>
    )
}

export default MapZoom