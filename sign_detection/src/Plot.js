import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Plot() {
    const [plotUrl, setPlotUrl] = useState('');

    useEffect(() => {
        async function fetchPlot() {
            //HEREEEE: Flask API Endpoint
            const response = await axios.get('http://localhost:5000/plot');
            setPlotUrl(response.data);
        }
        fetchPlot();
    }, []);

    return (
        <div>
            {plotUrl ? (
            <img src={plotUrl} alt="Plot" />
            ) : (
                <p>Loading plot...</p>
            )}
        </div>
    );
}

export default Plot;