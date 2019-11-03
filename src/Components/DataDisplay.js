import React from 'react'
import Overlay from "./Overlay";
import "../styles/results.css"
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
} from "react-router-dom";

class Data extends React.Component {

    state = {
        imgSrc: "",
        update: true,
        rects: null
    }

    loadFile() {

        console.log(this.state)
        if (this.state.update) {
            // const image = document.getElementById('output');
            // image.srcObject = this.props.image;
            console.log(this.props.image);

            const file = this.props.image;
            const reader = new FileReader();
            const url = reader.readAsDataURL(file);

            reader.onloadend = function (e) {
                this.setState({
                    imgSrc: [reader.result],
                    update: false,
                    // rects: this.fillRects()
                });

                // this.setState({rects: this.fillRects()})
            }.bind(this);

        }

        console.log(this.state.imgSrc)
    }

    fillRects() {

        // if (!this.state.refresh) {
        const data = this.props.data;
        let out = [];

        for (let i = 0; i < data.length; i++) {
            console.log(data[i]);
            out.push(<Overlay key={i} classification={("" + data[i])}/>);
        }

        return <div>{out}</div>;
        // }
    }

    render() {
        return (

            <div className={"App-Secondary"}>
                {this.loadFile()}
                <div className={"overlay-wrapper"}>
                    <img src={this.state.imgSrc} className={"overlay-image"} alt={"dataset"}/>
                    {/*<div className={"mini-overlays"} id={"wrapper"}>*/}
                    {/*    /!*{this.state.rects}*!/*/}
                    {/*</div>*/}
                </div>
            </div>
        )
    }
}

export default Data