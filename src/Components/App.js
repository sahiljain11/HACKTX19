import React from 'react';
import '../styles/home.css';
import Home from "./Home";
import Data from "./DataDisplay";

class App extends React.Component {

    state = {
        uploading: false,
        received: false,
        image: null,
        classification: [
            true, true, false, false, true,
            true, false, false, false, false,
            true, false, false, false, false,
            false, false, true, true, false,
            true, false, false, true, false
        ]
    }

    onChange = e => {
        const files = Array.from(e.target.files)
        this.setState({uploading: true})

        const formData = new FormData()
        //
        // formData.append("0", files[0])
        // console.log(files[0])
        // fetch(`${"https://image-classification.cognitiveservices.azure.com/customvision/v3.0/Prediction/2744fc95-61ce-4f3a-a4d6-e0fad1647c9c/classify/iterations/Iteration3/url"}`, {
        //     method: 'POST',
        //     body: {"Url": "https://cbsnews1.cbsistatic.com/hub/i/2018/09/12/96f981d8-2b5f-4bde-a092-8ea3aa621af9/florence3.jpg"},
        //     'Prediction-Key': 'ba8e403c3f904d85adf408928b13fa90',
        //     'Content-Type': 'application/json'


        // fetch(`${"http://finddamaged-env.jvxwipk8ke.us-east-2.elasticbeanstalk.com/find"}`, {
        //     method: 'POST',
        //     body: files[0],
        // })
        //     .then(res => res.json())
        //     .then(data => {
        //         console.log(data)
        //         this.setState({
        //             received: true
        //         })
        //     })

        fetch('http://localhost:5000/upload', {
            method: 'POST',
            body: formData
        }).then(data => {
            console.log(data)
        })

        this.setState({
            uploading: false,
            received: true,
            image: files[0]
        })
    }

    falsifyUploadReceive() {
        this.setState({
            uploading: false,
            receiving: false
        })
    }

    render() {
        const {uploading, received, image, classification} = this.state;

        const content = () => {
            switch (true) {
                case uploading:
                    return <div>hol up</div>;
                case received:
                    return <Data data={classification} image={image}/>;
                default:
                    return (<Home onChange={this.onChange}/>);
            }
        };

        return (
            <div>
                {content()}
            </div>
        )
    }
}

export default App;
