import React from 'react'
import Overlay from "./Overlay";
import "../styles/results.css"

class Data extends React.Component {

    state = {
        imgSrc: null
    }

    loadFile() {
        const image = document.getElementById('output');
        // image.srcObject = this.props.image;
        // console.log(this.props.image)

        const file = this.props.image;
        const reader = new FileReader();
        const url = reader.readAsDataURL(file);

        reader.onloadend = function (e) {
            this.setState({
                imgSrc: [reader.result]
            })
        }.bind(this);
    }

    render() {
        return (
            <div className={"App-Secondary"}>
                <img src={this.state.imgSrc} alt={"dataset"}/>
                <div className={"overlay-wrapper"}>
                    {
                        // absolutely positioned stuff using props.data
                    }
                </div>
                {this.loadFile()}
            </div>
        )
    }
}

export default Data