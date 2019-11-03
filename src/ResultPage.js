import React from 'react';
import './App.css';

export default props =>
    props.images.map((image, i) =>
        <div key={i} className='fadein'>
            <img src={image.secure_url} alt=''/>
        </div>
    )