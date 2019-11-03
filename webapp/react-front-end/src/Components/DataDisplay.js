import React from 'react'
import "../styles/results.css"

class Data extends React.Component {

    render() {
        return (
            <div className={"App-Secondary"}>
                <img src={process.env.PUBLIC_URL + "/images/wassup.png"} alt={"dataset"} className="overlay-image"/>
            </div>
        )
    }
}

export default Data